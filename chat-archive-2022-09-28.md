### Wed, Sep 28th, 2022

**JC** <span style="color: grey; font-size: 90%;">12:02:32 UTC</span>

<span style="font-size: 90%;">Aloha, are we having the montly meeting?</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:08:51 UTC</span>

<span style="font-size: 90%;">hello everyone ! Sorry for the delay :sweat_smile:</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:09:10 UTC</span>

<span style="font-size: 90%;">Welcome to the monthly meeting agenda [https://github.com/corazawaf/coraza/issues/388](https://github.com/corazawaf/coraza/issues/388)</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:09:21 UTC</span>

<span style="font-size: 90%;">There are not many topics to discuss today, but we can go deep into them</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:10:16 UTC</span>

<span style="font-size: 90%;">First of all I want to greet again _@Anuraag Agrawal_ and _@JC_ who are now part of. the core team</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:11:16 UTC</span>

<span style="font-size: 90%;">Also I would like to specially notice _@Anuraag Agrawal_ great work on the immutability pattern implementation [https://github.com/corazawaf/coraza/pull/397](https://github.com/corazawaf/coraza/pull/397)</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:12:07 UTC</span>

<span style="font-size: 90%;">In the past month, we have merged more than 30 PRs, mostly enhancing performance and fixing bugs</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:12:41 UTC</span>

<span style="font-size: 90%;">Great performances for libinjection-go too!</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:13:38 UTC</span>

<span style="font-size: 90%;">Regarding libcoraza (C exports), we have had issues with the log callback, it’s working better now, but we still have to update some headers in order to make it work</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:14:07 UTC</span>

<span style="font-size: 90%;">Coraza for nginx is compiling, but we have to write a function to “clone” waf instances in order to make it execute rules</span>

↳ **JC** <span style="color: grey; font-size: 90%;">12:15:26 UTC</span>

<span style="font-size: 90%;">This can be done with the new immutable API</span>

↳ **Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:15:50 UTC</span>

<span style="font-size: 90%;">Yes, we should document the specific path though</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:14:54 UTC</span>

<span style="font-size: 90%;">that’s because in nginx a location coraza instance should inherit rules from the server coraza instance</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:15:22 UTC</span>

<span style="font-size: 90%;">Our first topic for this meeting is: [https://github.com/corazawaf/community/issues/1](https://github.com/corazawaf/community/issues/1)</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:16:38 UTC</span>

<span style="font-size: 90%;">Thanks _@JC_ for the draft, this is a great opportunity to discus what you expect on the community guidelines</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:17:33 UTC</span>

<span style="font-size: 90%;">Personally I think we should keep some level of flexibility in order to avoid entering complex company bureaucracies for our contributors and users</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:18:10 UTC</span>

<span style="font-size: 90%;">But I also think we must keep a zero trust approach on how we handle our resources as a cybersecurity project</span>

**JC** <span style="color: grey; font-size: 90%;">12:19:12 UTC</span>

<span style="font-size: 90%;">Agree. Notice this document documents practices that are already in place tacitly. The main change is the introduction of github issues for certain decisions but that is mainly because we make decisions over slack and as a free plan we have no retention.</span>

**Anuraag Agrawal** <span style="color: grey; font-size: 90%;">12:20:08 UTC</span>

<span style="font-size: 90%;">Don’t think it’s free plan :smile:</span>

**JC** <span style="color: grey; font-size: 90%;">12:20:36 UTC</span>

<span style="font-size: 90%;">Nice finding _@Anuraag Agrawal_ I somehow assumed it was free because OSS org.</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:21:12 UTC</span>

<span style="font-size: 90%;">I think slack can be used to maintain important decisions but we would have to implement some good practices like pinning and creating bookmarks</span>

↳ **Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:27:03 UTC</span>

<span style="font-size: 90%;">Btw I prefer github discussions, but nobody uses them</span>

**JC** <span style="color: grey; font-size: 90%;">12:21:17 UTC</span>

<span style="font-size: 90%;">Still no way to point to specific decision made in the slack channel. Probably we need to make that visible somewhere.</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:22:09 UTC</span>

<span style="font-size: 90%;">Usually what we do during meetings is we wait for a few votes in a message. We don’t wait for enough votes, we just wait for counter-arguments</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:22:58 UTC</span>

<span style="font-size: 90%;">Decisions can be taking during meetings because everyone was notified that there is an ongoing meeting, but what about decisions outside meetings</span>

**JC** <span style="color: grey; font-size: 90%;">12:23:29 UTC</span>

<span style="font-size: 90%;">Yep, also what about counter-arguments post meeting? maybe a github issue istn’t a terrible idea?</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:23:57 UTC</span>

<span style="font-size: 90%;">Of course, all proposals should have a github issue</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:24:37 UTC</span>

<span style="font-size: 90%;">The thing is how do we make decisions fast enough</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:24:51 UTC</span>

<span style="font-size: 90%;">during v3 development decisions has to be made fast until we reach a stable point</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:25:42 UTC</span>

<span style="font-size: 90%;">That’s why I think we should have a decision making protocol for stable and for development</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:27:03 UTC</span>

<span style="font-size: 90%;">Btw I prefer github discussions, but nobody uses them</span>

↳ **Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:27:03 UTC</span>

<span style="font-size: 90%;">Btw I prefer github discussions, but nobody uses them</span>

**JC** <span style="color: grey; font-size: 90%;">12:29:24 UTC</span>

<span style="font-size: 90%;">I think it should be linked to our values. For me there are only two important decisiones: those which can be resolved by 2-3 team members and can be easily reverted if general concern (e.g. PRs) and those which has to be decided by majority (which usually take time to digest) and reverting them would be harmful for the project: e.g. membership</span>

**JC** <span style="color: grey; font-size: 90%;">12:30:15 UTC</span>

<span style="font-size: 90%;">For the former one trust is the key word, I trust you guys will make a good decision in simple changes and you would ping the right people and wait for feedback for those complex ones.</span>

**JC** <span style="color: grey; font-size: 90%;">12:30:31 UTC</span>

<span style="font-size: 90%;">Without trust, a community is hard to build.</span>

**JC** <span style="color: grey; font-size: 90%;">12:31:08 UTC</span>

<span style="font-size: 90%;">The other ones should be decoupled from trust and more stuck to rules. 2 people can decide a new membership, we need rules for that.</span>

**JC** <span style="color: grey; font-size: 90%;">12:31:51 UTC</span>

<span style="font-size: 90%;">So for trust based decisions, we don’t have formal process more than common sense. For rule base decisions we have formal process and rules.</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:32:41 UTC</span>

<span style="font-size: 90%;">Yes, and we are our own moderators, that’s why the approvals system</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:33:15 UTC</span>

<span style="font-size: 90%;">Regarding membership, I think we should have unanimous consensus from the core team</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:33:45 UTC</span>

<span style="font-size: 90%;">Not explicit approvals from everyone, but also no rejections</span>

**JC** <span style="color: grey; font-size: 90%;">12:34:07 UTC</span>

<span style="font-size: 90%;">That is good but then we need a deadline because we can’t wait for too long.</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:34:23 UTC</span>

<span style="font-size: 90%;">50% team + 1 votes</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:34:39 UTC</span>

<span style="font-size: 90%;">We are already 6, we can easily get 4 votes</span>

**JC** <span style="color: grey; font-size: 90%;">12:35:17 UTC</span>

<span style="font-size: 90%;">Yeah, that is good.</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:37:01 UTC</span>

<span style="font-size: 90%;">Any other comments on the community doc? I think we will be discussing it for a few weeks in its repository</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:37:16 UTC</span>

<span style="font-size: 90%;">Feel free to comment [https://github.com/corazawaf/community/pull/2](https://github.com/corazawaf/community/pull/2)</span>

**JC** <span style="color: grey; font-size: 90%;">12:37:45 UTC</span>

<span style="font-size: 90%;">Yeah please, let’s have an active discussion for this. It’s going to be the first version and hopefully the first of many.</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:38:42 UTC</span>

<span style="font-size: 90%;">Ok! So _@Anuraag Agrawal_ after thousands of changes has managed to merge immutability</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:39:11 UTC</span>

<span style="font-size: 90%;">My first impressions after running tests and benchmarking is “its working”</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:39:34 UTC</span>

<span style="font-size: 90%;">now we have to validate that plugins can still be added for actions, operators, transformations and directives</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:40:02 UTC</span>

<span style="font-size: 90%;">Also we have to review important use-cases like libcoraza, coraza-caddy and coraza-nginx</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:40:22 UTC</span>

<span style="font-size: 90%;">I think this minimal api exposure is brilliant, and it will make development much easier</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:40:52 UTC</span>

<span style="font-size: 90%;">We will also have to update [coraza.io](http://coraza.io) :stuck_out_tongue_winking_eye: I will upload my previous v3 branch</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:41:34 UTC</span>

<span style="font-size: 90%;">Other thing we have to handle is quality control, we are currently not running pre-commit so we need to make sure we add validations for the old controls</span>

↳ **JC** <span style="color: grey; font-size: 90%;">12:42:13 UTC</span>

<span style="font-size: 90%;">Where?</span>

↳ **Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:52:32 UTC</span>

<span style="font-size: 90%;">Github actions, I think our current lint validations are not working fine. I will write an issue</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:41:57 UTC</span>

<span style="font-size: 90%;">- id: go-fmt
    - id: go-vet
    - id: go-lint
    - id: go-imports
    - id: golangci-lint
    - id: go-critic
    - id: go-unit-tests
    - id: go-mod-tidy</span>

**Anuraag Agrawal** <span style="color: grey; font-size: 90%;">12:42:28 UTC</span>

<span style="font-size: 90%;">These should all be checked by go run mage.go check now</span>

↳ **Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:43:01 UTC</span>

<span style="font-size: 90%;">is it part of CI?</span>

↳ **Anuraag Agrawal** <span style="color: grey; font-size: 90%;">12:43:06 UTC</span>

<span style="font-size: 90%;">Yeah</span>

↳ **Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:43:21 UTC</span>

<span style="font-size: 90%;">I will take a look, I think we are missing some validations</span>

↳ **Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:43:32 UTC</span>

<span style="font-size: 90%;">we should have a lot of errors from some declarations</span>

↳ **Anuraag Agrawal** <span style="color: grey; font-size: 90%;">12:44:01 UTC</span>

<span style="font-size: 90%;">We might need to check the lint config, it doesn’t include cyclo right now

[https://github.com/corazawaf/coraza/blob/v3/dev/.golangci.yml](https://github.com/corazawaf/coraza/blob/v3/dev/.golangci.yml)</span>

↳ **Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:44:18 UTC</span>

<span style="font-size: 90%;">Cyclo is problematic because of the modsecurity C ports</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:42:37 UTC</span>

<span style="font-size: 90%;">Also we need [https://goreportcard.com/report/github.com/corazawaf/coraza/v3](https://goreportcard.com/report/github.com/corazawaf/coraza/v3) A+ 100% in everything</span>

↳ **JC** <span style="color: grey; font-size: 90%;">12:43:25 UTC</span>

<span style="font-size: 90%;">Mind filling an issue?</span>

↳ **Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:43:43 UTC</span>

<span style="font-size: 90%;">Of course</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:45:00 UTC</span>

<span style="font-size: 90%;">Ok, we might have enough time to review everything</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:45:08 UTC</span>

<span style="font-size: 90%;">any other comments or questions on immutability?</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:45:37 UTC</span>

<span style="font-size: 90%;">Ok moving forward</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:45:43 UTC</span>

<span style="font-size: 90%;">What about GraphQL support?</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:45:48 UTC</span>

<span style="font-size: 90%;">Should it be part of the core?</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:46:12 UTC</span>

<span style="font-size: 90%;">[https://graphql.org/users/](https://graphql.org/users/)</span>

**JC** <span style="color: grey; font-size: 90%;">12:46:28 UTC</span>

<span style="font-size: 90%;">By core you mean coraza repo?</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:46:31 UTC</span>

<span style="font-size: 90%;">yes</span>

**JC** <span style="color: grey; font-size: 90%;">12:47:18 UTC</span>

<span style="font-size: 90%;">I think not. library should not take into account specifics IMHO. We can always write a connector/adapter.</span>

**JC** <span style="color: grey; font-size: 90%;">12:47:59 UTC</span>

<span style="font-size: 90%;">Also, and most importantly, who requested this? I see it is mainly listed in monthly meeting agenda.</span>

**Roshan Piyush** <span style="color: grey; font-size: 90%;">12:48:24 UTC</span>

<span style="font-size: 90%;">Yeah. Even corerulset tried to move all specifics to plugins.</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:48:36 UTC</span>

<span style="font-size: 90%;">I personally think we should add some features just to differentiate from modsecurity, nothing specific</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:48:42 UTC</span>

<span style="font-size: 90%;">But it can be implemented as a plugin</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:49:15 UTC</span>

<span style="font-size: 90%;">cool</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:49:18 UTC</span>

<span style="font-size: 90%;">Regarding persistence</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:49:30 UTC</span>

<span style="font-size: 90%;">we have had this discussion with _@fzipitria_ for more than a year</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:49:44 UTC</span>

<span style="font-size: 90%;">modsecurity persistence doesn’t work, it’s a walking race condition</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:50:00 UTC</span>

<span style="font-size: 90%;">we still get a lot of questions regarding DDOS though</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:50:37 UTC</span>

<span style="font-size: 90%;">should we consider persistence as part of the project? or should we directly implement plugins to perform actions like ddos protection</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:50:57 UTC</span>

<span style="font-size: 90%;">the other persistence feature is user tracking, you can assign risk scores to users based on their IP or session ID</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:51:38 UTC</span>

<span style="font-size: 90%;">it seems like there is not much interest in the community, people just want to run CRS :sweat_smile:</span>

**JC** <span style="color: grey; font-size: 90%;">12:53:12 UTC</span>

<span style="font-size: 90%;">I think DDoS is important but given the current capacity and focus it might be part of 3.1 maybe?</span>

**JC** <span style="color: grey; font-size: 90%;">12:53:51 UTC</span>

<span style="font-size: 90%;">For example, when it comes to wasm filter there is very likely some approaches and work additional to support whatever persistance we design.</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:54:01 UTC</span>

<span style="font-size: 90%;">lgtm, we must make sure to keep the persistent variables (like User, Session) open so we don’t have to make breaking changes</span>

**Roshan Piyush** <span style="color: grey; font-size: 90%;">12:54:20 UTC</span>

<span style="font-size: 90%;">You need the give users the taste before they demand for such features</span>

**JC** <span style="color: grey; font-size: 90%;">12:54:53 UTC</span>

<span style="font-size: 90%;">I mean, we are interested on it (tetrate is a contributor and also a user) but no time to look into that now.</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:55:23 UTC</span>

<span style="font-size: 90%;">cool, let’s keep the feature waiting</span>

**JC** <span style="color: grey; font-size: 90%;">12:55:23 UTC</span>

<span style="font-size: 90%;">and definitively no time to look at the implicances of it in WASM</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:55:48 UTC</span>

<span style="font-size: 90%;">Yes, we also need a default persistence engine, that could be redis or something like that. And it might break tinygo compatibility</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:56:17 UTC</span>

<span style="font-size: 90%;">Ok last topic and a specific request from _@Anuraag Agrawal_</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:56:37 UTC</span>

<span style="font-size: 90%;">Let’s switch to only squash commits</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:57:13 UTC</span>

<span style="font-size: 90%;">It seems like otherwise, it breaks history for some PRs?</span>

**Anuraag Agrawal** <span style="color: grey; font-size: 90%;">12:57:36 UTC</span>

<span style="font-size: 90%;">It makes cherrypicking or picking a point in time in the repo’s history difficult mostly</span>

**JC** <span style="color: grey; font-size: 90%;">12:58:14 UTC</span>

<span style="font-size: 90%;">Also polutes the history with: wip update file xxxx wip 2 chore: lint etc etc</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:58:40 UTC</span>

<span style="font-size: 90%;">great, lgtm, lets enforce squash commits</span>

**Anuraag Agrawal** <span style="color: grey; font-size: 90%;">12:58:45 UTC</span>

<span style="font-size: 90%;">Unfortunately I’m not sure there is an org-wide setting for it so we would need to tweak it in each repo IIUC</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:58:55 UTC</span>

<span style="font-size: 90%;">we will take a look at the repo configuration</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:59:11 UTC</span>

<span style="font-size: 90%;">Ok so we are done</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:59:14 UTC</span>

<span style="font-size: 90%;">any other thing to discuss?</span>

**Matteo Pace** <span style="color: grey; font-size: 90%;">12:59:41 UTC</span>

<span style="font-size: 90%;">If you guys have still some minutes, could we elaborate a little the default behaviour of request body processing ([https://github.com/corazawaf/coraza/issues/438](https://github.com/corazawaf/coraza/issues/438))?</span>

↳ **Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">13:00:02 UTC</span>

<span style="font-size: 90%;">sure, so this is a behavior inherited from modsecurity</span>

↳ **Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">13:00:12 UTC</span>

<span style="font-size: 90%;">It’s based on performance</span>

↳ **Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">13:00:40 UTC</span>

<span style="font-size: 90%;">We only explicitly evaluate request bodies if the configuration matches</span>

↳ **Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">13:01:03 UTC</span>

<span style="font-size: 90%;">also some body processors might fill REQUEST_BODY and others won’t</span>

↳ **Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">13:01:22 UTC</span>

<span style="font-size: 90%;">you can enforce REQUEST_BODY in JSON by using the force request body ctl</span>

↳ **Matteo Pace** <span style="color: grey; font-size: 90%;">13:01:58 UTC</span>

<span style="font-size: 90%;">What sounds odds to me is that the same payload with text/plain or any other manipulated content-type will just bypass the waf</span>

↳ **Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">13:02:19 UTC</span>

<span style="font-size: 90%;">you might force processing on text/plain</span>

↳ **Matteo Pace** <span style="color: grey; font-size: 90%;">13:02:29 UTC</span>

<span style="font-size: 90%;">This is basically the difference between what ModSec v2 and v3 (REQUEST_BODY is always populated) do</span>

↳ **Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">13:03:11 UTC</span>

<span style="font-size: 90%;">SecRule REQUEST_HEADERS:content-type “!\@rx ……” “…ctl:forceRequestBodyVariable=On,ctl:setReqBodyProcessor=urlencoded”</span>

↳ **JC** <span style="color: grey; font-size: 90%;">13:03:21 UTC</span>

<span style="font-size: 90%;">Jus tone thing here: in [https://github.com/corazawaf/coraza/pull/441/files#diff-63ab601287b8b9c040760fe0bdd288f55b73f37cd7e4f1e519bea2bd43a18bbaL568](https://github.com/corazawaf/coraza/pull/441/files#diff-63ab601287b8b9c040760fe0bdd288f55b73f37cd7e4f1e519bea2bd43a18bbaL568) we say // We force URLENCODED if mime is x-www... or we have an empty RBP and ForceRequestBodyVariable but that is not what code does.</span>

↳ **Matteo Pace** <span style="color: grey; font-size: 90%;">13:03:32 UTC</span>

<span style="font-size: 90%;">From a user perspective I would expect that by enabling SecRequestBodyAccess the bodies are indeed accessed and analysed.
Just as a second step I would fine tune my waf in order to improve performance, reduce dos problems and so on</span>

↳ **Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">13:04:04 UTC</span>

<span style="font-size: 90%;">lgtm, we can make that change. We must just try to maintain regression with CRS</span>

↳ **Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">13:04:37 UTC</span>

<span style="font-size: 90%;">but this is a huge problem for most wafs, look at AWS</span>

↳ **Matteo Pace** <span style="color: grey; font-size: 90%;">13:04:48 UTC</span>

<span style="font-size: 90%;">SecRule REQUEST_HEADERS:content-type “!\@rx ……” “…ctl:forceRequestBodyVariable=On,ctl:setReqBodyProcessor=urlencoded”Yep, I see, thanks. It was more about what, as a user, I would expect as the default behaviour. Besides that we can actually enfroce it with your example</span>

↳ **Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">13:04:48 UTC</span>

<span style="font-size: 90%;">[https://kloudle.com/blog/the-infamous-8kb-aws-waf-request-body-inspection-limitation](https://kloudle.com/blog/the-infamous-8kb-aws-waf-request-body-inspection-limitation)</span>

↳ **Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">13:06:00 UTC</span>

<span style="font-size: 90%;">Ok lets evaluate in your issue if we can implement this without breaking default CRS compatibility</span>

↳ **Matteo Pace** <span style="color: grey; font-size: 90%;">13:06:06 UTC</span>

<span style="font-size: 90%;">It’s a spiky problem :sweat_smile:</span>

↳ **Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">13:06:26 UTC</span>

<span style="font-size: 90%;">but it does make sense</span>

↳ **Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">13:06:56 UTC</span>

<span style="font-size: 90%;">btw in modsecurity 2 it always populates the body because it’s attached to the apache buffer, in libmodsecurity it’s not</span>

↳ **Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">13:07:20 UTC</span>

<span style="font-size: 90%;">body is a copy of the buffer</span>

↳ **Matteo Pace** <span style="color: grey; font-size: 90%;">13:09:45 UTC</span>

<span style="font-size: 90%;">Just tested yesterday against libmodsec and in the scenario both text/plain and malformed content types have been analyzed :thinking_face:</span>

↳ **Matteo Pace** <span style="color: grey; font-size: 90%;">13:11:12 UTC</span>

<span style="font-size: 90%;">[https://github.com/SpiderLabs/ModSecurity/wiki/Reference-Manual-(v3.x)#ctl:~:text=REQUEST_BODY%20is%20always%20populated%20in%20v3](https://github.com/SpiderLabs/ModSecurity/wiki/Reference-Manual-(v3.x)#ctl:~:text=REQUEST_BODY%20is%20always%20populated%20in%20v3)
(but well, no surprise if the doc is outdated)</span>

↳ **Matteo Pace** <span style="color: grey; font-size: 90%;">13:13:29 UTC</span>

<span style="font-size: 90%;">The point is, the only way I see to do not give a false sense of security is by default parsing all the bodies. But the solution ends up to be not okay for other reasons</span>

↳ **Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">13:16:56 UTC</span>

<span style="font-size: 90%;">I remember the documentation was outdated and I based my results in my labs and crs integration</span>

↳ **Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">13:17:05 UTC</span>

<span style="font-size: 90%;">But let’s make your changes and see what happens</span>

↳ **Matteo Pace** <span style="color: grey; font-size: 90%;">13:19:55 UTC</span>

<span style="font-size: 90%;">Let’s see! Thanks for you time _@Juan Pablo Tosso_, see you on Github!</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">13:01:55 UTC</span>

<span style="font-size: 90%;">Ok thank you everyone for joining !</span>

