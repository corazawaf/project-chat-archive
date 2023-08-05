### Wed, Apr 26th, 2023

**JC** <span style="color: grey; font-size: 90%;">12:00:53 UTC</span>

<span style="font-size: 90%;">Hi everyone, thanks for joining our monthly meeting :coraza-party:</span>

**Matteo Pace** <span style="color: grey; font-size: 90%;">12:01:51 UTC</span>

<span style="font-size: 90%;">Hello :coraza-party: :wave:</span>

**dune73** <span style="color: grey; font-size: 90%;">12:02:07 UTC</span>

<span style="font-size: 90%;">Hi there. _@JC_ invited me to join you.</span>

**JC** <span style="color: grey; font-size: 90%;">12:03:10 UTC</span>

<span style="font-size: 90%;">Updates:
</span>

**JC** <span style="color: grey; font-size: 90%;">12:04:54 UTC</span>

<span style="font-size: 90%;">Any comments on the above?</span>

**dune73** <span style="color: grey; font-size: 90%;">12:05:51 UTC</span>

<span style="font-size: 90%;">Nothing outside of congratulations on the 1K stars and RC2.</span>

**JC** <span style="color: grey; font-size: 90%;">12:06:11 UTC</span>

<span style="font-size: 90%;">Thanks! It’s been a journey but we are closer to v3.</span>

**JC** <span style="color: grey; font-size: 90%;">12:06:19 UTC</span>

<span style="font-size: 90%;">Let’s follow with the agenda</span>

**JC** <span style="color: grey; font-size: 90%;">12:06:22 UTC</span>

<span style="font-size: 90%;">Agenda:
</span>

**dune73** <span style="color: grey; font-size: 90%;">12:07:02 UTC</span>

<span style="font-size: 90%;">So I get to go first? (thanks)</span>

**JC** <span style="color: grey; font-size: 90%;">12:08:28 UTC</span>

<span style="font-size: 90%;">Yes, be our guest.</span>

↳ **JC** <span style="color: grey; font-size: 90%;">12:08:52 UTC</span>

<span style="font-size: 90%;">We don’t want to waste your time too much time. You already been very careful to be here _@dune73_</span>

**dune73** <span style="color: grey; font-size: 90%;">12:08:33 UTC</span>

<span style="font-size: 90%;">Thank you</span>

**dune73** <span style="color: grey; font-size: 90%;">12:08:55 UTC</span>

<span style="font-size: 90%;">So we are getting closer to CRSv4 too. We are still working on keyword lists and that's the last big task.</span>

**dune73** <span style="color: grey; font-size: 90%;">12:09:54 UTC</span>

<span style="font-size: 90%;">Keyword lists means we no longer want to maintain outdated lists by hand. Instead we want to have sources and then we automate the retrieval and transformation of the keyword lists from these sources into our format, being regex or text-based data files.</span>

**dune73** <span style="color: grey; font-size: 90%;">12:10:13 UTC</span>

<span style="font-size: 90%;">I'm working on the new user-agent list which is now based on 3 github sources and very, very long.</span>

**dune73** <span style="color: grey; font-size: 90%;">12:10:26 UTC</span>

<span style="font-size: 90%;">Another big item which is open is PHP functions and keywords.</span>

**dune73** <span style="color: grey; font-size: 90%;">12:10:36 UTC</span>

<span style="font-size: 90%;">Other than that it looks mostly clear for v4.</span>

**dune73** <span style="color: grey; font-size: 90%;">12:11:39 UTC</span>

<span style="font-size: 90%;">Development had died down somewhat after we closed the remaining bug bounty issues back in February, but I feel things are taking up speed again.</span>

**JC** <span style="color: grey; font-size: 90%;">12:12:20 UTC</span>

<span style="font-size: 90%;">Great to hear</span>

**dune73** <span style="color: grey; font-size: 90%;">12:12:26 UTC</span>

<span style="font-size: 90%;">Not giving out any release dates just yet, but it's going forward.</span>

**JC** <span style="color: grey; font-size: 90%;">12:12:44 UTC</span>

<span style="font-size: 90%;">Dates are not needed. It is great to know we are getting closer.</span>

**dune73** <span style="color: grey; font-size: 90%;">12:12:50 UTC</span>

<span style="font-size: 90%;">+1</span>

**JC** <span style="color: grey; font-size: 90%;">12:13:31 UTC</span>

<span style="font-size: 90%;">Awesome.</span>

**JC** <span style="color: grey; font-size: 90%;">12:13:35 UTC</span>

<span style="font-size: 90%;">I can go next about v3.</span>

**JC** <span style="color: grey; font-size: 90%;">12:13:46 UTC</span>

<span style="font-size: 90%;">unless you want to give the updates _@Matteo Pace_?</span>

**dune73** <span style="color: grey; font-size: 90%;">12:13:52 UTC</span>

<span style="font-size: 90%;">Looking fwd to hear that.</span>

**JC** <span style="color: grey; font-size: 90%;">12:14:40 UTC</span>

<span style="font-size: 90%;">So we are close to v3 too. We have two tickets on triage and waiting for feedback. There is also a PR from _@Matteo Pace_ about the scoring model we need to get in.</span>

**JC** <span style="color: grey; font-size: 90%;">12:15:05 UTC</span>

<span style="font-size: 90%;">In general the API is stable and we are just cutting final details but of course bug reports that come in the process need to be addressed ASAP.</span>

**Matteo Pace** <span style="color: grey; font-size: 90%;">12:15:45 UTC</span>

<span style="font-size: 90%;">Yep, would be nice to also squeeze it in v3 ([https://github.com/corazawaf/coraza/pull/778](https://github.com/corazawaf/coraza/pull/778))</span>

↳ **Matteo Pace** <span style="color: grey; font-size: 90%;">12:16:04 UTC</span>

<span style="font-size: 90%;">I will try to address the review by today</span>

↳ **JC** <span style="color: grey; font-size: 90%;">12:16:17 UTC</span>

<span style="font-size: 90%;">Right. Tagged as v3 too.</span>

**JC** <span style="color: grey; font-size: 90%;">12:16:02 UTC</span>

<span style="font-size: 90%;">I expected we can close the tickets by the end of next week and we can release rc.3 which will be probably the final version.</span>

**dune73** <span style="color: grey; font-size: 90%;">12:16:24 UTC</span>

<span style="font-size: 90%;">You are not expecting any bug showing up in RC2?</span>

**JC** <span style="color: grey; font-size: 90%;">12:17:42 UTC</span>

<span style="font-size: 90%;">Well we didn’t have any report yet, not even in the work we are doing with the connectors.</span>

**dune73** <span style="color: grey; font-size: 90%;">12:17:54 UTC</span>

<span style="font-size: 90%;">ok</span>

**JC** <span style="color: grey; font-size: 90%;">12:18:08 UTC</span>

<span style="font-size: 90%;">Maybe _@Matteo Pace_ wants to give an update on the work we are doing for connectors.</span>

**Matteo Pace** <span style="color: grey; font-size: 90%;">12:21:22 UTC</span>

<span style="font-size: 90%;">the main work has been around Caddy, aligning the middleware to the one that we are already using in the Coraza main repo and with [https://github.com/corazawaf/coraza-caddy/pull/56](https://github.com/corazawaf/coraza-caddy/pull/56).
The mage commands now mimic what we have in the proxy-wasm connector. It makes easier to jump from one connector to the other for just sone tests and provides an example reference easy to spin up.
This PR introduces also FTW tests, Overall we have about 60 failing tests. Would be great to add it to the CI, but currently I’m experiencing some inconsistency across runs, with random tests failing :disappointed:</span>

**Matteo Pace** <span style="color: grey; font-size: 90%;">12:22:42 UTC</span>

<span style="font-size: 90%;">Still, about the Caddy connector would be great to have a dedicated maintainer with some expertise on Caddy itself</span>

**JC** <span style="color: grey; font-size: 90%;">12:24:30 UTC</span>

<span style="font-size: 90%;">Yeah, that would be truly great. We are trying to make caddy be production ready but it would be cool to have someone who can give some more love and care.</span>

**JC** <span style="color: grey; font-size: 90%;">12:25:39 UTC</span>

<span style="font-size: 90%;">Does anyone have anything else to add?</span>

**Matteo Pace** <span style="color: grey; font-size: 90%;">12:28:16 UTC</span>

<span style="font-size: 90%;">Ups, sorry, let me update also about multiphase</span>

**JC** <span style="color: grey; font-size: 90%;">12:28:48 UTC</span>

<span style="font-size: 90%;">Sure, go ahead.</span>

**Matteo Pace** <span style="color: grey; font-size: 90%;">12:31:06 UTC</span>

<span style="font-size: 90%;">Multiphase rule evaluation is tricky, the main focus has been making it compatible with the CRS rules. All the CRS tests are passing, and most of the Coraza tests are now also running against Coraza with Multiphase evaluation enabled. Exceptions comes from corner cases of flow actions, that still have to be properly documented (raw documentation here: [https://gist.github.com/M4tteoP/57001a5066f2f76c9f99c6dc3e9bf4af](https://gist.github.com/M4tteoP/57001a5066f2f76c9f99c6dc3e9bf4af)). There is quite a complex logic that avoids multiple matches for chained rules, but it has been mostly split in dedicated functions and file, so I’m confident it is not going to affect any Coraza “plain behavior” (When Multiphase evaluation is off)</span>

**Matteo Pace** <span style="color: grey; font-size: 90%;">12:31:33 UTC</span>

<span style="font-size: 90%;">Any further reviews would be really appreciated: [https://github.com/corazawaf/coraza/pull/719](https://github.com/corazawaf/coraza/pull/719)</span>

**Matteo Pace** <span style="color: grey; font-size: 90%;">12:34:40 UTC</span>

<span style="font-size: 90%;">The PR includes also the split of ARGS and ARGS_NAMES into *_GET and *_POST variables at parsing time</span>

**Matteo Pace** <span style="color: grey; font-size: 90%;">12:35:52 UTC</span>

<span style="font-size: 90%;">Overall I would consider it still an experimental feature, but proxy-wasm users are experiencing the issue that this feature is going to handle (E.g. [https://github.com/corazawaf/coraza-proxy-wasm/issues/1719](https://github.com/corazawaf/coraza-proxy-wasm/issues/1719)), so we might also have some early adopters and feedbacks :slightly_smiling_face:</span>

↳ **JC** <span style="color: grey; font-size: 90%;">12:38:34 UTC</span>

<span style="font-size: 90%;">Thanks _@Matteo Pace_</span>

**JC** <span style="color: grey; font-size: 90%;">12:44:36 UTC</span>

<span style="font-size: 90%;">Thank you. Anyone else wants to add something? Otherwise thank you and see you in the other side.</span>

↳ **unknown user** <span style="color: grey; font-size: 90%;">12:45:25 UTC</span>

<span style="font-size: 90%;">... I hope is not that other side</span>

↳ **JC** <span style="color: grey; font-size: 90%;">12:46:33 UTC</span>

<span style="font-size: 90%;">You never know</span>

**Matteo Pace** <span style="color: grey; font-size: 90%;">12:48:31 UTC</span>

<span style="font-size: 90%;">Thanks, see you around!</span>

