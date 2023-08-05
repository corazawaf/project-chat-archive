### Wed, Oct 26th, 2022

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:01:45 UTC</span>

<span style="font-size: 90%;">Hello and welcome to our monthly meeting ! </span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:04:10 UTC</span>

<span style="font-size: 90%;">[https://github.com/corazawaf/coraza/issues/474](https://github.com/corazawaf/coraza/issues/474)</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:07:27 UTC</span>

<span style="font-size: 90%;">So for the project status:
</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:07:46 UTC</span>

<span style="font-size: 90%;">We must set some milestones for the release, but it seems we are stable enough to make it work</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:08:18 UTC</span>

<span style="font-size: 90%;">There have been many issues regarding Coreruleset, CRS V3 branch is not compatible with Coraza and V4 is not versioned yet so we cannot guarantee regression compatibility</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:10:58 UTC</span>

<span style="font-size: 90%;">A lot of bugfixes and performance issues had been fixed, more than 30 PRs merged in the last 30 days with great enhancements</span>

**JC** <span style="color: grey; font-size: 90%;">12:11:41 UTC</span>

<span style="font-size: 90%;">There are two main focus on those PRs: 1. performance and 2. compatibility with CRS</span>

↳ **JC** <span style="color: grey; font-size: 90%;">12:20:17 UTC</span>

<span style="font-size: 90%;">Coraza is a library that should not impact critically in the performance of the application itself despite the intensive work. More so when we talk about envoy environments where the latency added is critical.</span>

↳ **JC** <span style="color: grey; font-size: 90%;">12:20:37 UTC</span>

<span style="font-size: 90%;">On the other hand, CRS is our main goal in proxy-wasm as it goes in the line of zero-trust.</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:13:26 UTC</span>

<span style="font-size: 90%;">That’s an important topic, as CRS are fixing a lot of vulnerabilities and bypasses, it’s been a race to keep track of the changes and maintain compatibility. We are doing our best effort and we expect we should reach a stable compatibility soon</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:14:45 UTC</span>

<span style="font-size: 90%;">Also an important announcement, Tetrate has donated [https://github.com/corazawaf/coraza-proxy-wasm](https://github.com/corazawaf/coraza-proxy-wasm) to Coraza. Special thanks to the tetrate team, _@Anuraag Agrawal_, _@Matteo Pace_ and _@JC_
This greatly enhances our coverage, as now we support Envoy proxy :smile: and well, any WASM-proxy compatible system</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:15:58 UTC</span>

<span style="font-size: 90%;">congratulations on the great work</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:16:38 UTC</span>

<span style="font-size: 90%;"> has led an incredible bug bounty program in the past months and a lot of vulnerabilities were discovered</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:17:28 UTC</span>

<span style="font-size: 90%;">Most of them were patched by CRS rules but there were two vulnerabilities that required engine changes</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:18:09 UTC</span>

<span style="font-size: 90%;">This PR [https://github.com/corazawaf/coraza/pull/470](https://github.com/corazawaf/coraza/pull/470) changes the default regex for the JSON request body processor mime type</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:18:37 UTC</span>

<span style="font-size: 90%;">And this PR [https://github.com/corazawaf/coraza/pull/452](https://github.com/corazawaf/coraza/pull/452) adds support for the MULTIPART_PART_HEADERS variable, extending Coraza capabilities to handle multipart bodies</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:20:40 UTC</span>

<span style="font-size: 90%;">We have migrated to an immutable pattern, special thanks to _@Anuraag Agrawal_. It provides a simple and safe mechanism to invoke coraza and handle transactions. It also helps us to write major changes without updating the public API and maintaining compatibility</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:23:29 UTC</span>

<span style="font-size: 90%;">And finally, from my part, the latest V3 topics to solve:
</span>

**JC** <span style="color: grey; font-size: 90%;">12:29:03 UTC</span>

<span style="font-size: 90%;">From coraza-proxy-wasm side: we are focused on CRS now as we reach stability in terms of performance with latest changes in GC done by _@Anuraag Agrawal_</span>

**JC** <span style="color: grey; font-size: 90%;">12:29:38 UTC</span>

<span style="font-size: 90%;">And CRS includes a set of things, notably response body processing.</span>

**JC** <span style="color: grey; font-size: 90%;">12:30:10 UTC</span>

<span style="font-size: 90%;">Other than tat the API is stable enough and we don’t expect that much of changes in coraza v3</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:31:01 UTC</span>

<span style="font-size: 90%;">thanks JC for the update, we are really excited about coraza-proxy-wasm</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:31:39 UTC</span>

<span style="font-size: 90%;">The only topic I would like to review is controlling headers from coraza directives</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:32:09 UTC</span>

<span style="font-size: 90%;">If we add a function like tx.AddRequestHeaders(headers http.Header), we could actually control headers</span>

↳ **JC** <span style="color: grey; font-size: 90%;">12:53:07 UTC</span>

<span style="font-size: 90%;">Please create an issue for htis.</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:32:17 UTC</span>

<span style="font-size: 90%;">but it would only apply to implementations using http.Requests</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:32:45 UTC</span>

<span style="font-size: 90%;">Would that generate confusion?</span>

**JC** <span style="color: grey; font-size: 90%;">12:34:05 UTC</span>

<span style="font-size: 90%;">I’d rather not add a function just for http package. Can we use a map[string][]string which is kind of the standard? e.g. grpc uses that</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:34:24 UTC</span>

<span style="font-size: 90%;">we can cast http.Header into that, right?</span>

**JC** <span style="color: grey; font-size: 90%;">12:34:47 UTC</span>

<span style="font-size: 90%;">Yes.</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:35:13 UTC</span>

<span style="font-size: 90%;">sure, I mean, having a type defined makes it easier, but we can also do that</span>

**JC** <span style="color: grey; font-size: 90%;">12:35:24 UTC</span>

<span style="font-size: 90%;">[https://pkg.go.dev/net/http#Header](https://pkg.go.dev/net/http#Header)</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:36:43 UTC</span>

<span style="font-size: 90%;">also, that would only affect coraza implementations assuming coraza is a proxy. If coraza doesn’t run in the edge, then users should be aware it won’t work</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:37:01 UTC</span>

<span style="font-size: 90%;">that’s a separation we haven’t made so far</span>

**JC** <span style="color: grey; font-size: 90%;">12:37:41 UTC</span>

<span style="font-size: 90%;">uhmm</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:38:18 UTC</span>

<span style="font-size: 90%;">maybe we should add a function to make connectors announce themself, like modsecurity does</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:38:32 UTC</span>

<span style="font-size: 90%;">and the connector should declare if it supports some features</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:39:04 UTC</span>

<span style="font-size: 90%;">like coraza.RegisterConnector(“coraza-caddy”, “v1.0", FEATURES_FLAGS)</span>

**JC** <span style="color: grey; font-size: 90%;">12:39:11 UTC</span>

<span style="font-size: 90%;">Well the library won’t do that ifself. I guess if we add such method then we will need to expose a way to retrieve those headers isn’t and apply the changes in [https://github.com/corazawaf/coraza/blob/v3/dev/http/interceptor.go#L26](https://github.com/corazawaf/coraza/blob/v3/dev/http/interceptor.go#L26)</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:40:13 UTC</span>

<span style="font-size: 90%;">exactly</span>

**JC** <span style="color: grey; font-size: 90%;">12:40:27 UTC</span>

<span style="font-size: 90%;">So it is fine, we don’t need to do any separation.</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:40:50 UTC</span>

<span style="font-size: 90%;">cool, so I don’t have any more topics, anything else to discuss?</span>

**JC** <span style="color: grey; font-size: 90%;">12:41:57 UTC</span>

<span style="font-size: 90%;">not from my side.</span>

**Matteo Pace** <span style="color: grey; font-size: 90%;">12:44:11 UTC</span>

<span style="font-size: 90%;">Nothing important, but just to do not keep things pending: can I close [https://github.com/corazawaf/coraza/issues/438#issuecomment-1276335416](https://github.com/corazawaf/coraza/issues/438#issuecomment-1276335416) after the summary I wrote? Are we all on the same page about this behaviour? (Maybe I was the only one that he was not ahah)</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:54:37 UTC</span>

<span style="font-size: 90%;">Can we keep an internal discussion on this? _@fzipitria_ opinion is very important</span>

**fzipitria** <span style="color: grey; font-size: 90%;">12:54:55 UTC</span>

<span style="font-size: 90%;">Hey! :wave:</span>

**fzipitria** <span style="color: grey; font-size: 90%;">12:55:25 UTC</span>

<span style="font-size: 90%;">Sorry, too many things happening at the same time :slightly_smiling_face:</span>

**Matteo Pace** <span style="color: grey; font-size: 90%;">12:56:05 UTC</span>

<span style="font-size: 90%;">Can we keep an internal discussion on this?Of course, no rush!</span>

**fzipitria** <span style="color: grey; font-size: 90%;">12:56:25 UTC</span>

<span style="font-size: 90%;">ModSecurity v3 is broken, so we should choose what is best for us.</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:57:01 UTC</span>

<span style="font-size: 90%;">Exactly, and we should also know that changing the behavior will break crs tests </span>

**fzipitria** <span style="color: grey; font-size: 90%;">12:57:41 UTC</span>

<span style="font-size: 90%;">Will it?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">12:58:35 UTC</span>

<span style="font-size: 90%;">The only problem I recall was with text/plain</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:59:05 UTC</span>

<span style="font-size: 90%;">So we should look for the safest and more effective approach, not modsecurity’s</span>

↳ **fzipitria** <span style="color: grey; font-size: 90%;">13:00:05 UTC</span>

<span style="font-size: 90%;">This could be the law for us.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">12:59:19 UTC</span>

<span style="font-size: 90%;">This :point_up:</span>

**fzipitria** <span style="color: grey; font-size: 90%;">12:59:42 UTC</span>

<span style="font-size: 90%;">Honestly, ModSecurity’s implementation is a guidance, not a law.</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">13:00:35 UTC</span>

<span style="font-size: 90%;">Great, so we have an agreement on that ? </span>

**fzipitria** <span style="color: grey; font-size: 90%;">13:01:43 UTC</span>

<span style="font-size: 90%;">BTW, the CRS team is going to work hard on getting the v4 out next week. So the versioning problem might dissapear.</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">13:02:10 UTC</span>

<span style="font-size: 90%;">That would be awesome, we should also add some info to the readme</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">13:02:34 UTC</span>

<span style="font-size: 90%;">_@fzipitria_ is it possible to release a minor crs 3.3 version with re2 compatibility ? </span>

**fzipitria** <span style="color: grey; font-size: 90%;">13:04:06 UTC</span>

<span style="font-size: 90%;">No, sorry.</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">13:04:55 UTC</span>

<span style="font-size: 90%;">:( ok so we should disclose that we are only compatible with crs 4+</span>

**fzipitria** <span style="color: grey; font-size: 90%;">13:05:07 UTC</span>

<span style="font-size: 90%;">Yes.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">13:05:27 UTC</span>

<span style="font-size: 90%;">re2 compatibility in v3 would need to backport a lot, and is not worth it</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">13:05:37 UTC</span>

<span style="font-size: 90%;">Good to know </span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">13:05:46 UTC</span>

<span style="font-size: 90%;">Great, any other topic ? </span>

**fzipitria** <span style="color: grey; font-size: 90%;">13:07:15 UTC</span>

<span style="font-size: 90%;">Not from my side. Expect additional news on CRS by next meeting! :smile:</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">13:07:48 UTC</span>

<span style="font-size: 90%;">Ok thank you everyone for participating ! See you on GitHub </span>

**Matteo Pace** <span style="color: grey; font-size: 90%;">13:08:24 UTC</span>

<span style="font-size: 90%;">Thanks, see you!</span>

**fzipitria** <span style="color: grey; font-size: 90%;">13:08:49 UTC</span>

<span style="font-size: 90%;">:wave:</span>

