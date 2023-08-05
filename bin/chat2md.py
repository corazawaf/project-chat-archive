#!/usr/bin/python3

import sys
import argparse
import datetime
import os
import json
import re
import html

users = {}

def ord(n):
    return str(n)+("th" if 4 <= (n%100) <=20 else {1:"st",2:"nd",3:"rd"}.get(n%10, "th"))

def dtStylish(dt, f):
    return dt.strftime(f).replace("{th}", ord(dt.day))

def transform(t, users):
    # set the #NNNN format as link
    grp = re.findall("#\d{3,}", t)
    for p in grp:
        t = t.replace(p, "[%s](https://github.com/corazawaf/coraza/issues/%s)" % (p, p))

    #t = re.sub("^#", "\#", text)

    # Replace the <@USER_ID> by @Username
    # format it as _italic_
    grp = re.findall("<@[A-Z0-9]+>", t)
    for p in grp:
        p = p.replace("<@", "").replace(">", "")
        t = t.replace("<@" + p + ">", "_@%s_" % (users[p]))

    # keep shrug as is :)
    t = re.sub("¯\\\_\(ツ\)_/¯", "¯\\\\\\\\\_(ツ)\_/¯", t)

    # unescape HTML entities
    t = html.unescape(t)

    return t

def get_text(d, indent):
    if 'blocks' in d:
        text = ""
        for b in d['blocks']:
            subtext = ""
            if (b.__contains__('elements')):
                for ee in b['elements']:
                    if (ee.__contains__('elements')):
                        for e in ee['elements']:
                            if e['type'] == "text":
                                subtext += "%s" % (transform(e['text'], users))
                            elif e['type'] == "link":
                                if 'text' in e:
                                    subtext += "[%s](%s)" % (e['text'], e['url'])
                                else:
                                    subtext += "[%s](%s)" % (e['url'], e['url'])
                            elif e['type'] == "emoji":
                                subtext += ":%s:" % (e['name'])
                            elif e['type'] == "user":
                                subtext += "_@%s_" % (users[e['user_id']])
                            elif e['type'] == 'rich_text_section':
                                for element in e['elements']:
                                    if element['type'] == "text":
                                        print(e)
                            else:
                                print("Error: Unknown type %s" % (e['type']))
                    else:
                        print("Error: no item 'elements' in ee")
            else:
                print("Error: no item 'elements' in b")
            text += "%s" % (subtext)
    else:
        text = "%s" % (transform(d['text'], users))
    return text

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="MD formatted chat creation tool")
    parser.add_argument("-d", "--directory", dest="directory", metavar="/path/to/directory", help="Input directory", required=True)
    parser.add_argument("-o", "--output", dest="output", metavar='file to content', type=str,
                            help='Output file', required=True)
    args = parser.parse_args()
    files = []
    try:
        for f in os.listdir():
            if f[-5:] == ".json":
                if f == "users.json":
                    try:
                        with(open(f, "r")) as fp:
                            _users = json.load(fp)
                        for u in _users:
                            users[u] = _users[u]['user']['profile']['display_name']
                            if users[u] == "":
                                users[u] = _users[u]['user']['profile']['real_name']
                    except:
                        print(sys.exc_info()[0])
                        sys.exit(1)
                else:
                    files.append(f)
    except:
        print("Can't open directory: %s" % (args.directory))
    files.sort(reverse=True)
    lastdate = ""
    try:
        fpo = open(args.output, "w")
    except:
        print("Can't open output file: %s" % (args.output))
        sys.exit(1)
    for f in files:
        with(open(f, "r")) as fp:
            data = json.load(fp)
        for d in reversed(data['messages']):
            ts = datetime.datetime.fromtimestamp(float(d['ts']), tz=datetime.timezone.utc)
            tsdate = ts.strftime("%Y-%m-%d")
            tstime = ts.strftime("%H:%M:%S %Z")
            if lastdate != tsdate:
                fpo.write("### %s\n\n" % dtStylish(ts, "%a, %b {th}, %Y"))
                lastdate = tsdate
            if (d.__contains__('user')):
                if (d['user'] in users):
                    fpo.write("**%s** <span style=\"color: grey; font-size: 90%%;\">%s</span>\n\n" % (users[d['user']], tstime))
                else:
                    print("User " + d['user'] + " not in user table.")
                    fpo.write("**%s** <span style=\"color: grey; font-size: 90%%;\">%s</span>\n\n" % ("unknown user", tstime))
            else:
                fpo.write("**%s** <span style=\"color: grey; font-size: 90%%;\">%s</span>\n\n" % ("unknown user", tstime))
            text = get_text(d, 2)
            fpo.write("<span style=\"font-size: 90%%;\">%s</span>\n\n" % (text))
            if 'replies' in d:
                for r in d['replies']['messages'][1:]:
                    ts = datetime.datetime.fromtimestamp(float(r['ts']), tz=datetime.timezone.utc)
                    tsdate = ts.strftime("%Y-%m-%d")
                    tstime = ts.strftime("%H:%M:%S %Z")
                    if lastdate != tsdate:
                        fpo.write("##### %s\n\n" % dtStylish(ts, "%a, %b {th}, %Y"))
                        lastdate = tsdate
                    if (r.__contains__('user')):
                        if (r['user'] in users):
                            fpo.write("↳ **%s** <span style=\"color: grey; font-size: 90%%;\">%s</span>\n\n" % (users[r['user']], tstime))
                        else:
                            print("User " + r['user'] + " not in user table.")
                            fpo.write("↳ **%s** <span style=\"color: grey; font-size: 90%%;\">%s</span>\n\n" % ("unknown user", tstime))
                    else:
                        fpo.write("↳ **%s** <span style=\"color: grey; font-size: 90%%;\">%s</span>\n\n" % ("unknown user", tstime))
                    #text = transform(r['text'], users)
                    text = get_text(r, 4)
                    #fpo.write("&nbsp;&nbsp;&nbsp;&nbsp;%s\n\n" % (text))
                    fpo.write("<span style=\"font-size: 90%%;\">%s</span>\n\n" % (text))
    fpo.close()
