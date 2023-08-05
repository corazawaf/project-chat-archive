### Wed, Aug 31st, 2022

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:02:03 UTC</span>

<span style="font-size: 90%;">Hello and welcome to our monthly meeting
[https://github.com/corazawaf/coraza/issues/351](https://github.com/corazawaf/coraza/issues/351)</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:04:09 UTC</span>

<span style="font-size: 90%;">Let’s begin.
It’s been a crazy month, a lot has happened
</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:05:13 UTC</span>

<span style="font-size: 90%;">we have implemented a new feature, SecDatasets: [https://github.com/corazawaf/coraza/pull/361](https://github.com/corazawaf/coraza/pull/361) (</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:05:36 UTC</span>

<span style="font-size: 90%;">There is a new debug interface for custom debug [https://github.com/corazawaf/coraza/pull/337](https://github.com/corazawaf/coraza/pull/337)</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:05:49 UTC</span>

<span style="font-size: 90%;">The golang URL processor was replaced [https://github.com/corazawaf/coraza/pull/326](https://github.com/corazawaf/coraza/pull/326)</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:05:59 UTC</span>

<span style="font-size: 90%;">We are back at Core ruleset 100% compatibility</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:06:14 UTC</span>

<span style="font-size: 90%;">And now Coraza can be compiled using tinygo</span>

**JC** <span style="color: grey; font-size: 90%;">12:06:25 UTC</span>

<span style="font-size: 90%;">Yay</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:08:12 UTC</span>

<span style="font-size: 90%;">Current benchmark results, I will share the link of the repo at the end of the meeting so you can review the methodology and we can publish it</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:09:52 UTC</span>

<span style="font-size: 90%;">Great, any questions or comments?</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:10:07 UTC</span>

<span style="font-size: 90%;">Btw congratulations to everyone who has helped to make this happen</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:10:18 UTC</span>

<span style="font-size: 90%;">specially our newest contributor, _@Anuraag Agrawal_</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:11:33 UTC</span>

<span style="font-size: 90%;">ok to keep up with the agenda</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:12:02 UTC</span>

<span style="font-size: 90%;">_@Anuraag Agrawal_ or _@JC_, could you give us some insight into how tinygo compatibility was achieved and what the benefits are?</span>

**Anuraag Agrawal** <span style="color: grey; font-size: 90%;">12:12:26 UTC</span>

<span style="font-size: 90%;">Sure</span>

**JC** <span style="color: grey; font-size: 90%;">12:14:37 UTC</span>

<span style="font-size: 90%;">You go Rag</span>

**Anuraag Agrawal** <span style="color: grey; font-size: 90%;">12:16:18 UTC</span>

<span style="font-size: 90%;">For context, TinyGo is a compiler of Go code originally to create lighter weight binaries for microcontrollers. A target for WebAssembly was added because it also benefits from lightweight implementations.

Unfortunately, that means it is for a large part a reimplementation of the standard Go compiler, and features that are specific to compilation continue to get implemented over time. One significant gap vs normal Go is support for the reflect package. And lacking that, encoding/json doesn’t work for most cases.

Being able to compile Coraza with TinyGo would be great though because by compiling to WebAssembly, it can be loaded with Envoy, which supports extensions in wasm. So we went for it :slightly_smiling_face:

We replaced some implementations with non-reflection, e.g. JSON parsing uses a library called gjson in TinyGo, but XML is currently unsupported with TinyGo and we’ve flagged the implementation and tests off for TinyGo. Also file system access isn’t supported by Envoy so we flagged it too to be noop when compiling with TinyGo.

It isn’t a perfect reproduction of coraza’s features, but thanks to this, we have been able to load Coraza in Envoy and have a WAF there</span>

**Anuraag Agrawal** <span style="color: grey; font-size: 90%;">12:16:53 UTC</span>

<span style="font-size: 90%;">reflect will get better support over time for sure, and we can expect gaps to close over time</span>

**Anuraag Agrawal** <span style="color: grey; font-size: 90%;">12:18:11 UTC</span>

<span style="font-size: 90%;">One thing I am anxious about is if people submit changes to coraza but run into one of TinyGo’s unimplemented features - we are now running CI with TinyGo enabled. If something mysterious comes up, just ping me asap so we can work together as it can get quite tricky</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:18:48 UTC</span>

<span style="font-size: 90%;">thank you for the update Anuraag, btw gjson might become our official replacement for encoding/json, seems to be way faster and it fits all of our use cases</span>

**Anuraag Agrawal** <span style="color: grey; font-size: 90%;">12:18:49 UTC</span>

<span style="font-size: 90%;">EOF - happy to answer questions :slightly_smiling_face:</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:20:07 UTC</span>

<span style="font-size: 90%;">Regarding future regression, I think we should be clear on our contributors.md about tinygo.
We can always mark new features as “experimental” using build constrains so everything can be tested. Please open discussion for this</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:20:46 UTC</span>

<span style="font-size: 90%;">Ok so now we are done with the past, and lets discuss the future</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:21:30 UTC</span>

<span style="font-size: 90%;">If we have a limitation to read files, then we cannot use pmFromFile or other important operators used by CRS</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:21:38 UTC</span>

<span style="font-size: 90%;">That’s why we came with SecDataset: [https://github.com/corazawaf/coraza/pull/361](https://github.com/corazawaf/coraza/pull/361)</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:22:04 UTC</span>

<span style="font-size: 90%;">SecDatasets allows us to create inline datasets without having to create .data files. it’s compatible with all file consuming operators</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:23:15 UTC</span>

<span style="font-size: 90%;">It might be a great feature and I would like to read if there are any comments. Could we make this better?</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:25:16 UTC</span>

<span style="font-size: 90%;">The other issue regarding pmfromfile is Snort suricata syntax support</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:25:27 UTC</span>

<span style="font-size: 90%;">It is an interesting modsecurity feature but we haven’t had any request to implement it</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:25:45 UTC</span>

<span style="font-size: 90%;">maybe it’s not that important? Maybe we should implement it in other operator?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">12:25:53 UTC</span>

<span style="font-size: 90%;">Files are shared in a common memory area, right?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">12:26:03 UTC</span>

<span style="font-size: 90%;">Data I meant</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:26:23 UTC</span>

<span style="font-size: 90%;">data is stored into a map of slices in the bootstrap configuration</span>

**fzipitria** <span style="color: grey; font-size: 90%;">12:26:41 UTC</span>

<span style="font-size: 90%;">About the suricata syntax, I don’t know if adds too much in our case</span>

**fzipitria** <span style="color: grey; font-size: 90%;">12:26:55 UTC</span>

<span style="font-size: 90%;">It is a plus, but the CRS doesn’t use it per se</span>

**fzipitria** <span style="color: grey; font-size: 90%;">12:27:45 UTC</span>

<span style="font-size: 90%;">Unless there is a clear win from implementing it, we can push it to the backlog</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:28:01 UTC</span>

<span style="font-size: 90%;">great, we will keep avoiding suricata syntax, feel free to create an issue or comment here if you think there are reasons to implement it</span>

**Anuraag Agrawal** <span style="color: grey; font-size: 90%;">12:28:41 UTC</span>

<span style="font-size: 90%;"> We are back at Core ruleset 100% compatibilityI think this tends to be an important feature when evaluating a change in tech. If suricata isn’t important for it, then it’s probably not a big deal</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:29:03 UTC</span>

<span style="font-size: 90%;">It’s your time _@fzipitria_: Rate limiting: new operator, new action, or new specific rule?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">12:29:16 UTC</span>

<span style="font-size: 90%;">Yes</span>

**fzipitria** <span style="color: grey; font-size: 90%;">12:29:31 UTC</span>

<span style="font-size: 90%;">All the discussion in the ticket has been regarding the implementation details</span>

**fzipitria** <span style="color: grey; font-size: 90%;">12:29:44 UTC</span>

<span style="font-size: 90%;">Which honestly, I don’t is relevant yet</span>

**fzipitria** <span style="color: grey; font-size: 90%;">12:30:05 UTC</span>

<span style="font-size: 90%;">This is what we have as requirements in the issue:

    the url to protect
    the rate limit per second/minute/etc.
    the action when the limit is reached:
        return http code 429
        send it to a tarpit
    also, when to clear the rate limit

I’m rethinking if we want to have:
</span>

**fzipitria** <span style="color: grey; font-size: 90%;">12:30:39 UTC</span>

<span style="font-size: 90%;">Also, there is some advanced rate limiting that can make our life easier in the future</span>

**fzipitria** <span style="color: grey; font-size: 90%;">12:30:53 UTC</span>

<span style="font-size: 90%;">For distributed attacks, for example</span>

**fzipitria** <span style="color: grey; font-size: 90%;">12:31:13 UTC</span>

<span style="font-size: 90%;">So, the classic base RL is about IPs</span>

**fzipitria** <span style="color: grey; font-size: 90%;">12:31:32 UTC</span>

<span style="font-size: 90%;">Whatever URL some IP is hitting, we do the RL in that IP</span>

**fzipitria** <span style="color: grey; font-size: 90%;">12:31:54 UTC</span>

<span style="font-size: 90%;">But for distributed brute forcing, for example, that technique doesn’t apply well</span>

**fzipitria** <span style="color: grey; font-size: 90%;">12:32:29 UTC</span>

<span style="font-size: 90%;">So we might want to have something different as counting expression for tracking what to block</span>

**fzipitria** <span style="color: grey; font-size: 90%;">12:33:20 UTC</span>

<span style="font-size: 90%;">Could be a parameter (e.g. login?username=<user>, or some header (Authorization: Bearer ...)</span>

**fzipitria** <span style="color: grey; font-size: 90%;">12:33:56 UTC</span>

<span style="font-size: 90%;">So the question. is if the design using a SecRule is enough</span>

**fzipitria** <span style="color: grey; font-size: 90%;">12:34:27 UTC</span>

<span style="font-size: 90%;">Or we leverage the new SecRateLimit with extended options, that can give us more freedom afterwards</span>

**fzipitria** <span style="color: grey; font-size: 90%;">12:34:40 UTC</span>

<span style="font-size: 90%;">I see both working good</span>

**fzipitria** <span style="color: grey; font-size: 90%;">12:34:57 UTC</span>

<span style="font-size: 90%;">But for growing, probably the second option with a new directive is better</span>

**fzipitria** <span style="color: grey; font-size: 90%;">12:35:29 UTC</span>

<span style="font-size: 90%;">Or we start simply with a ratelimit action for SecRule</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:36:04 UTC</span>

<span style="font-size: 90%;">I think there is no problem with Directives being SecRule aliases, so maybe we can cover both</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:37:10 UTC</span>

<span style="font-size: 90%;">But ratelimit as a disruptive action looks interesting</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:37:26 UTC</span>

<span style="font-size: 90%;">in the future we might integrate it with the persistence engine to create variables</span>

**fzipitria** <span style="color: grey; font-size: 90%;">12:37:41 UTC</span>

<span style="font-size: 90%;">Definitely it should be integrated with persistence</span>

**fzipitria** <span style="color: grey; font-size: 90%;">12:37:53 UTC</span>

<span style="font-size: 90%;">If we want complex cases to be covered</span>

**fzipitria** <span style="color: grey; font-size: 90%;">12:38:21 UTC</span>

<span style="font-size: 90%;">But also because we might end up with a distributed coraza deployment</span>

**fzipitria** <span style="color: grey; font-size: 90%;">12:38:45 UTC</span>

<span style="font-size: 90%;">And we want to rate limit horizontally across the cluster</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:39:07 UTC</span>

<span style="font-size: 90%;">exactly</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:39:18 UTC</span>

<span style="font-size: 90%;">in the meantime single node blocking should work</span>

**Anuraag Agrawal** <span style="color: grey; font-size: 90%;">12:40:33 UTC</span>

<span style="font-size: 90%;">Just for context, more parameters does make it tough. e.g., if accepting username then I would expect that all requests to that username are handled by the same rule. This might not be commonly achievable</span>

**Anuraag Agrawal** <span style="color: grey; font-size: 90%;">12:41:06 UTC</span>

<span style="font-size: 90%;">But more general global rate limits without state would be easy</span>

**fzipitria** <span style="color: grey; font-size: 90%;">12:41:43 UTC</span>

<span style="font-size: 90%;">You need state for RL</span>

**fzipitria** <span style="color: grey; font-size: 90%;">12:41:58 UTC</span>

<span style="font-size: 90%;">I mean, it can be in memory</span>

**fzipitria** <span style="color: grey; font-size: 90%;">12:42:18 UTC</span>

<span style="font-size: 90%;">You cannot RL stateless</span>

**Anuraag Agrawal** <span style="color: grey; font-size: 90%;">12:43:17 UTC</span>

<span style="font-size: 90%;">Ah sorry I meant global state. Rate limiting without global/shared state is important, but single-node can still have some limitations, e.g. it can’t implement a SAS API rate limit usually</span>

**Anuraag Agrawal** <span style="color: grey; font-size: 90%;">12:43:25 UTC</span>

<span style="font-size: 90%;">So just need to be clear about that</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:44:13 UTC</span>

<span style="font-size: 90%;">great, I think this is great progress on the discussion
Felipe could we move this to a github discussion?</span>

**JC** <span style="color: grey; font-size: 90%;">12:45:26 UTC</span>

<span style="font-size: 90%;">I would like to propose Rag (anuraaga) to be a core team member due to his great contributions in v3 and also as one who is devoted to take coraza wasm to reality.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">12:47:05 UTC</span>

<span style="font-size: 90%;">I think is it a good idea, and he is very welcomed as core team member!</span>

**fzipitria** <span style="color: grey; font-size: 90%;">12:48:03 UTC</span>

<span style="font-size: 90%;">Just to be transparent with all members on this channel, we welcome all of you to be part of the core team.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">12:49:09 UTC</span>

<span style="font-size: 90%;">We did setup our rules in our first meeting :slightly_smiling_face:</span>

**fzipitria** <span style="color: grey; font-size: 90%;">12:50:17 UTC</span>

<span style="font-size: 90%;">The only thing we ask our contributors is to ask for additional reviews when there is people working in the same company, or working together in PRs.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">12:50:47 UTC</span>

<span style="font-size: 90%;">The more eyes we have, the stronger our project is going to be</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:51:18 UTC</span>

<span style="font-size: 90%;">Thank you _@fzipitria_ for the explanation</span>

**fzipitria** <span style="color: grey; font-size: 90%;">12:51:24 UTC</span>

<span style="font-size: 90%;">:bow:</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:51:40 UTC</span>

<span style="font-size: 90%;">_@JC_, we should wait for _@Roshan Piyush_ or _@bxlxx.wu_ for the final vote</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:51:46 UTC</span>

<span style="font-size: 90%;">but you have my vote and _@fzipitria_</span>

**Anuraag Agrawal** <span style="color: grey; font-size: 90%;">12:52:43 UTC</span>

<span style="font-size: 90%;"> We did setup our rules in our first meeting :slightly_smiling_face:Are these written on GitHub anywhere? Would be great to refer to, for example at these times. If not, yet we could possibly create corazawaf/community repo for collecting community guidelines</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:53:18 UTC</span>

<span style="font-size: 90%;">[https://github.com/corazawaf/coraza/issues/162](https://github.com/corazawaf/coraza/issues/162)</span>

**Anuraag Agrawal** <span style="color: grey; font-size: 90%;">12:53:48 UTC</span>

<span style="font-size: 90%;">Thanks for the reference!</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:54:29 UTC</span>

<span style="font-size: 90%;">Ok so we are moving to the next topics</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:54:51 UTC</span>

<span style="font-size: 90%;">we will go fast as I only have a few minutes</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:54:57 UTC</span>

<span style="font-size: 90%;"></span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:55:52 UTC</span>

<span style="font-size: 90%;">Although I think it would make life of many people easier, I think users should still download the package and setup it up by themselves. Otherwise they would miss a lot of documentation and requirements. Also it will be hard to maintain. This is my humble opinion</span>

**Anuraag Agrawal** <span style="color: grey; font-size: 90%;">12:57:23 UTC</span>

<span style="font-size: 90%;">I think we would decide by what we expect users to fall into


If 1., we would generally expect them to get very familiar to coraza / modsec. If 2., a simpler experience will help them I think</span>

**Anuraag Agrawal** <span style="color: grey; font-size: 90%;">12:58:23 UTC</span>

<span style="font-size: 90%;">If we decide to focus on 1., then I agree that it’s good to absorb the concept of rules, etc. But I have also heard that WAF is becoming more important for compliance reasons, i.e. in US some standards will require it. So if we expect apps to add it for compliance reason, an easy entry could help them</span>

**fzipitria** <span style="color: grey; font-size: 90%;">12:58:26 UTC</span>

<span style="font-size: 90%;">I think this might be a part of coraza + caddy, if anything</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:58:33 UTC</span>

<span style="font-size: 90%;">Complex features like this could be easily implemented using plugins. We can merge plugins into the core if they are ok</span>

**Anuraag Agrawal** <span style="color: grey; font-size: 90%;">12:58:52 UTC</span>

<span style="font-size: 90%;">But I do tend to agree that embedding not in coraza, but in the proxy integration layers, should satisfy almost if not all users</span>

**fzipitria** <span style="color: grey; font-size: 90%;">12:59:20 UTC</span>

<span style="font-size: 90%;">Basic users just want caddy + coraza</span>

**fzipitria** <span style="color: grey; font-size: 90%;">12:59:28 UTC</span>

<span style="font-size: 90%;">Enterprise users want a strong API</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:59:44 UTC</span>

<span style="font-size: 90%;">exactly</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">13:00:04 UTC</span>

<span style="font-size: 90%;">Let’s move this discussion to the issue</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">13:00:50 UTC</span>

<span style="font-size: 90%;">[https://github.com/corazawaf/coraza/issues/373](https://github.com/corazawaf/coraza/issues/373)</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">13:01:11 UTC</span>

<span style="font-size: 90%;">it is a major change, it will break some code but I think v3 is the moment to do it</span>

**Anuraag Agrawal** <span style="color: grey; font-size: 90%;">13:02:14 UTC</span>

<span style="font-size: 90%;">For context, I think my recent [https://github.com/corazawaf/coraza/pull/375](https://github.com/corazawaf/coraza/pull/375) breaks everyone anyways so collating them will not be a huge delta, probably</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">13:02:28 UTC</span>

<span style="font-size: 90%;">yes, but it had to happen at some point</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">13:02:56 UTC</span>

<span style="font-size: 90%;">Ok, next issue is [https://github.com/corazawaf/coraza/issues/374](https://github.com/corazawaf/coraza/issues/374)</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">13:03:12 UTC</span>

<span style="font-size: 90%;">I agree with this, we should start moving all types to specific packages inside the types/ directory</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">13:03:29 UTC</span>

<span style="font-size: 90%;">but not just from types</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">13:03:41 UTC</span>

<span style="font-size: 90%;">we should try to remove most dmetadata from the core package and move it to a type</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">13:03:47 UTC</span>

<span style="font-size: 90%;">to avoid circular dependencies</span>

↳ **fzipitria** <span style="color: grey; font-size: 90%;">13:04:02 UTC</span>

<span style="font-size: 90%;">:pray:</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">13:04:16 UTC</span>

<span style="font-size: 90%;">[https://github.com/corazawaf/coraza/issues/371](https://github.com/corazawaf/coraza/issues/371)</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">13:04:22 UTC</span>

<span style="font-size: 90%;">this one should become a long discussion</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">13:04:32 UTC</span>

<span style="font-size: 90%;">although I like it, I think it breaks A LOT and it requires a major refactor</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">13:06:07 UTC</span>

<span style="font-size: 90%;">Ok everyone, thank you very much for joining</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">13:06:17 UTC</span>

<span style="font-size: 90%;">please help me write comments in the monthly meeting issue to keep track</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">13:06:30 UTC</span>

<span style="font-size: 90%;">Also please have a look at [https://github.com/corazawaf/coraza/issues/336](https://github.com/corazawaf/coraza/issues/336)</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">13:06:58 UTC</span>

<span style="font-size: 90%;">Also _@fzipitria_ created a calendar event: [https://calendar.google.com/calendar/ical/c_s1vf6auene1ehionfslv010tk8%40group.calendar.google.com/public/basic.ics](https://calendar.google.com/calendar/ical/c_s1vf6auene1ehionfslv010tk8%40group.calendar.google.com/public/basic.ics)</span>

**Anuraag Agrawal** <span style="color: grey; font-size: 90%;">13:09:21 UTC</span>

<span style="font-size: 90%;">Thanks _@Juan Pablo Tosso_ - if going with [https://github.com/corazawaf/coraza/issues/371](https://github.com/corazawaf/coraza/issues/371) I think the schedule on [https://github.com/corazawaf/coraza/issues/336](https://github.com/corazawaf/coraza/issues/336) is impossible, so we would probably need a go or no go for that. Should we set a deadline on a decision while debating on [https://github.com/corazawaf/coraza/issues/371](https://github.com/corazawaf/coraza/issues/371)?</span>

**Anuraag Agrawal** <span style="color: grey; font-size: 90%;">13:09:41 UTC</span>

<span style="font-size: 90%;">(impossible=should require one extra month IMO)</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">13:11:39 UTC</span>

<span style="font-size: 90%;">I agree, feel free to propose new dates</span>

**Anuraag Agrawal** <span style="color: grey; font-size: 90%;">13:12:22 UTC</span>

<span style="font-size: 90%;">Thanks everyone, see you on GitHub :slightly_smiling_face:</span>

**fzipitria** <span style="color: grey; font-size: 90%;">13:18:27 UTC</span>

<span style="font-size: 90%;">:wave: See you next one!</span>

