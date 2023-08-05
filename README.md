## Protocols of the project chats

We are running a general project chat the first Monday of a month 20:30 CET and a chat about open issues the 3rd Monday of a month on the OWASP Slack, channel #coraza.

The Agenda for the chat is announced as a github issue in advance with the tag `Meeting Agenda`. In the Agenda you will also find general news for the project like links to 3rd party news articles etc. Also look through the "other topics" in the agenda for infos about the project.

| *Period* | *Project Chat* | *Issue Chat* |
| -------- | -------------- | ------------ |
| 2022, February | [chat-archive-2022-02-07.md](chat-archive-2022-02-07.md) | [chat-archive-2022-02-21.md](chat-archive-2022-02-21.md) |
| 2022, March | [chat-archive-2022-03-07.md](chat-archive-2022-03-07.md) | [chat-archive-2022-03-21.md](chat-archive-2022-03-21.md) |
| 2022, April | [chat-archive-2022-04-04.md](chat-archive-2022-04-04.md) | [chat-archive-2022-04-18.md](chat-archive-2022-04-18.md) |
| 2022, May | [chat-archive-2022-05-02.md](chat-archive-2022-05-02.md) | [chat-archive-2022-05-16.md](chat-archive-2022-05-16.md) |
| 2022, June | [chat-archive-2022-06-06.md](chat-archive-2022-06-06.md) | [chat-archive-2022-06-20.md](chat-archive-2022-06-20.md) |
| 2022, July | [chat-archive-2022-07-04.md](chat-archive-2022-07-04.md) | [chat-archive-2022-07-18.md](chat-archive-2022-07-18.md) |
| 2022, August | [chat-archive-2022-08-01.md](chat-archive-2022-08-01.md) | [chat-archive-2022-08-15.md](chat-archive-2022-08-15.md) |
| 2022, September | [chat-archive-2022-09-05.md](chat-archive-2022-09-05.md) | [chat-archive-2022-09-19.md](chat-archive-2022-09-19.md) |
| 2022, October | [chat-archive-2022-10-03.md](chat-archive-2022-10-03.md) | [chat-archive-2022-10-17.md](chat-archive-2022-10-17.md) |
| 2022, November | [chat-archive-2022-11-07.md](chat-archive-2022-11-07.md) | [chat-archive-2022-11-21.md](chat-archive-2022-11-21.md) |
| 2022, December | [chat-archive-2022-12-05.md](chat-archive-2022-12-05.md) | [chat-archive-2022-12-19.md](chat-archive-2022-12-19.md) |
| 2023, January | [chat-archive-2023-01-02.md](chat-archive-2023-01-02.md) | [chat-archive-2023-01-16.md](chat-archive-2023-01-16.md) |
| 2023, February | [chat-archive-2023-02-06.md](chat-archive-2023-02-06.md) | [chat-archive-2023-02-20.md](chat-archive-2023-02-20.md) |
| 2023, March | [chat-archive-2023-03-06.md](chat-archive-2023-03-06.md) | [chat-archive-2023-03-20.md](chat-archive-2023-03-20.md) |
| 2023, April | [chat-archive-2023-04-03.md](chat-archive-2023-04-03.md) | n.n. |
| 2023, Mai | [chat-archive-2023-05-01.md](chat-archive-2023-05-01.md) |  [chat-archive-2023-05-15.md](chat-archive-2023-05-15.md) |
| 2023, June | [chat-archive-2023-06-05.md](chat-archive-2023-06-05.md) |  [chat-archive-2023-06-19.md](chat-archive-2023-06-19.md) |
| 2023, July | [chat-archive-2023-07-03.md](chat-archive-2023-07-03.md) |  []() ([Agenda]()) / [Decisions]() |
| 2023, August | []() ([Agenda]()) / [Decisions]() |  []() ([Agenda]()) / [Decisions]() |
| 2023, September | []() ([Agenda]()) / [Decisions]() |  []() ([Agenda]()) / [Decisions]() |
| 2023, October | []() ([Agenda]()) / [Decisions]() |  []() ([Agenda]()) / [Decisions]() |
| 2023, November | []() ([Agenda]()) / [Decisions]() |  []() ([Agenda]()) / [Decisions]() |
| 2023, December | []() ([Agenda]()) / [Decisions]() |  []() ([Agenda]()) / [Decisions]() |

## How to generate the chat logs

### 3 Scripts

* generate-all.sh : master script that fetches and formats all the chats based on `chat-dates.txt`. Slack API token is expected in env variable `$TOKEN`. @dune73 has the token.
* get-chat.py : script called by `generate-all.sh`; it fetches the chats from slack.
* chat2md.py : script called by `generate-all.sh`; it reformats the chats JSON files into mardown (`.md`)

### File chat-dates.txt

Edit the file `chat-dates.txt` and add chat dates.

### Generate

```bash
$ export TOKEN="******"
$ ./bin/generate-all.sh
```

Add links new files, agenda, decisions etc to table in README.md.
