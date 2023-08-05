#!/usr/bin/python3

import requests
import json
import sys
import argparse
import datetime
import re

def send_request(req):
    return requests.post(req['url'], data = req['data'])

USERS_URL = {
    'scheme':    "https",
    'host':      "owasp.slack.com",
    'resource':  "/api/users.list"
}

USERINFO_URL = {
    'scheme':    "https",
    'host':      "owasp.slack.com",
    'resource':  "/api/users.info"
}

CHANNEL = "C02BXH135AT"

def get_user_info(user, token):
    req = {
        'url': "%s://%s%s" % (USERINFO_URL['scheme'], USERINFO_URL['host'], USERINFO_URL['resource']),
        'data': {
            'token':   token,
            'channel': CHANNEL,
            'user':    user
        },
    }
    resp = send_request(req)
    return resp.json()

CONV_URL = {
    'scheme':    "https",
    'host':      "owasp.slack.com",
    'resource':  "/api/conversations.history"
}

DATA = {
    'token':   None,
    'channel': CHANNEL
}

conv_req = {
    'url': "%s://%s%s" % (CONV_URL['scheme'], CONV_URL['host'], CONV_URL['resource']),
    'data': DATA,
}

users = {}

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Tool to fetch conversations from Slack channel")
    parser.add_argument("-f", "--from", dest="fromtime", metavar='"%s"' % (datetime.datetime.now().strftime("%Y-%m-%d %H:%I:%S")),
                        type=str, help='From date and time', required=False)
    parser.add_argument("-t", "--to", dest="totime", metavar='"%s"' % (datetime.datetime.now().strftime("%Y-%m-%d %H:%I:%S")),
                        type=str, help='From date and time', required=False)
    parser.add_argument("-m", "--max", dest="maxout", metavar='N',
                        type=int, help='Max number of pieces of output', required=False)
    parser.add_argument("-T", "--token", dest="token", metavar='STR',
                        type=str, help='Slack API token', required=False)
    args = parser.parse_args()

    if args.fromtime is None and args.totime is None and args.maxout is None:
        print("You must pass at least -f (from) and -t (to) OR -m (max) argument")
        sys.exit()

    if args.token is None:
        print("You must pass the Slack API tokenn via -T / --token")
        sys.exit()

    if args.fromtime is not None:
        fromtime = datetime.datetime.timestamp(datetime.datetime.strptime(args.fromtime,"%Y-%m-%d %H:%M:%S"))

    if args.totime is not None:
        totime = datetime.datetime.timestamp(datetime.datetime.strptime(args.totime,"%Y-%m-%d %H:%M:%S"))

    conv_req['data']['oldest'] = fromtime
    conv_req['data']['latest'] = totime
    conv_req['data']['token'] = args.token

    outcnt = 0
    while True:
        resp = send_request(conv_req)
        if resp.json().get("ok", False) is not True:
            print("Error in Slack connection: %s" % (resp.json().get("error", "Unknown error")))
            sys.exit()
        resp = resp.json()
        outcnt += 1
        with open("out_%03d.json" % (outcnt), "w+") as fp:
            midx = 0

            for m in resp['messages']:
                if 'user' in m and m['user'] not in users:
                    users[m['user']] = get_user_info(m['user'], args.token)
                if 'users' in m:
                    for u in m['users']:
                        if u not in users:
                            users[u] = get_user_info(u, args.token)
                grp = re.findall("<@[A-Z0-9]+>", m['text'])
                for p in grp:
                    u = p.replace("<@", "").replace(">", "")
                    if u not in users:
                        users[u] = get_user_info(u, args.token)
                if 'thread_ts' in m:
                    replies = {
                        'url': "%s://%s%s" % (CONV_URL['scheme'], CONV_URL['host'], "/api/conversations.replies"),
                        'data': DATA,
                    }
                    replies['data']['ts'] = m['thread_ts']
                    repls = send_request(replies).json()
                    resp['messages'][midx]['replies'] = repls
                    for rp in repls['messages']:
                        grp = re.findall("<@[A-Z0-9]+>", rp['text'])
                        for p in grp:
                            u = p.replace("<@", "").replace(">", "")
                            if u not in users:
                                users[u] = get_user_info(u, args.token)
                midx += 1
            print("Writing data to out_%03d.json with number of %d items..." % (outcnt, len(resp['messages'])))
            fp.write(json.dumps(resp, indent=4, sort_keys=True))
            fp.close()

        if 'response_metadata' in resp and 'next_cursor' in resp['response_metadata']:
            conv_req['data']['cursor'] = resp['response_metadata']['next_cursor']
        else:
            print("No more next_cursor, exiting")
            break

        if args.maxout is not None and args.maxout == outcnt:
            break

    fp = open("users.json", "w+")
    fp.write(json.dumps(users, indent=4, sort_keys=True))
    fp.close()
