### Wed, Jan 25th, 2023

**Matteo Pace** <span style="color: grey; font-size: 90%;">12:55:41 UTC</span>

<span style="font-size: 90%;">Are there some ways to make it more an automatic experience (or at least more coupled with the PRs)?</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:56:27 UTC</span>

<span style="font-size: 90%;">yes we could do more automation, for example, we could create documentation right from the comments</span>

↳ **unknown user** <span style="color: grey; font-size: 90%;">13:35:01 UTC</span>

<span style="font-size: 90%;">Yeah I think this is what we should do, otherwise maintaining the docs will be a nightmare.</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:56:46 UTC</span>

<span style="font-size: 90%;">that would be a nice project</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:57:57 UTC</span>

<span style="font-size: 90%;">Ok no more comments around this I think?</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:57:59 UTC</span>

<span style="font-size: 90%;">[https://github.com/corazawaf/coraza/pull/519](https://github.com/corazawaf/coraza/pull/519)</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:58:21 UTC</span>

<span style="font-size: 90%;">Added by _@Matteo Pace_</span>

**Matteo Pace** <span style="color: grey; font-size: 90%;">12:59:29 UTC</span>

<span style="font-size: 90%;">About this, just wanted to agree on the log levels before updating the PR. Right now The v3 implementation, documentation and coraza recommended.conf are not aligned</span>

**Matteo Pace** <span style="color: grey; font-size: 90%;">13:00:10 UTC</span>

<span style="font-size: 90%;">The PR proposes to reorder the levels to:  trace -> debug -> info -> warning -> error</span>

**Matteo Pace** <span style="color: grey; font-size: 90%;">13:01:29 UTC</span>

<span style="font-size: 90%;">The main question is, do we want to keep compatibility with ModSecurity? Adding some levels that we are currently not using (no log  and fatal if I am not wrong) and sticking with the number correspondence (even if it is weird because it skips some numbers?)</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">13:02:17 UTC</span>

<span style="font-size: 90%;">it looks good to me</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">13:02:20 UTC</span>

<span style="font-size: 90%;">we should update docs</span>

**fzipitria** <span style="color: grey; font-size: 90%;">13:02:31 UTC</span>

<span style="font-size: 90%;">Updating the docs is a reasonable path</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">13:02:45 UTC</span>

<span style="font-size: 90%;">yes we should avoid fatal as we should not os.Exit(..) nor panic from coraza</span>

**fzipitria** <span style="color: grey; font-size: 90%;">13:02:57 UTC</span>

<span style="font-size: 90%;">Definitely</span>

**Matteo Pace** <span style="color: grey; font-size: 90%;">13:04:09 UTC</span>

<span style="font-size: 90%;">Good! I can take another look, but I think that the PR is pretty aligned to what you are saying</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">13:04:42 UTC</span>

<span style="font-size: 90%;">maybe maintain modsec standard for regression ?</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">13:04:45 UTC</span>

<span style="font-size: 90%;">0: Fatal
1: Panic
2: Error
3: Warning
4: details of how transactions are handled
5: log everything</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">13:04:53 UTC</span>

<span style="font-size: 90%;">we point fatal and panic to Error</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">13:05:16 UTC</span>

<span style="font-size: 90%;">0-3: Error, 3 warning, …</span>

↳ **Matteo Pace** <span style="color: grey; font-size: 90%;">13:07:35 UTC</span>

<span style="font-size: 90%;">Ok, makes sense!</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">13:06:47 UTC</span>

<span style="font-size: 90%;">Ok I have to fix my summer time event :sweat_smile: sorry for the delay</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">13:07:03 UTC</span>

<span style="font-size: 90%;">If you have any additional topic to discuss, all discussions are still open here! feel free to contribute</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">13:07:05 UTC</span>

<span style="font-size: 90%;">Thank you everyone</span>

**Matteo Pace** <span style="color: grey; font-size: 90%;">13:09:41 UTC</span>

<span style="font-size: 90%;">About [https://github.com/corazawaf/coraza/pull/572](https://github.com/corazawaf/coraza/pull/572), are we happy with at least a fallback that takes the server name from the headers? Or could you elaborate a little about the additional helper? _@Juan Pablo Tosso_</span>

**Matteo Pace** <span style="color: grey; font-size: 90%;">13:10:36 UTC</span>

<span style="font-size: 90%;">I wish to provide an initial fix to it considering that SERVER_NAME is currently never working right now</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">13:32:10 UTC</span>

<span style="font-size: 90%;">That’s a big one… modsecurity relies on the headers </span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">13:32:43 UTC</span>

<span style="font-size: 90%;">Maybe we could add a SetServerName helper to transactions, it would make sense as reverse proxies hides the host name </span>

↳ **unknown user** <span style="color: grey; font-size: 90%;">13:35:54 UTC</span>

<span style="font-size: 90%;">Sounds good to me.</span>

↳ **Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">13:39:34 UTC</span>

<span style="font-size: 90%;">Maybe it would make more sense processServerName? To follow naming convention _@Matteo Pace_ </span>

↳ **Matteo Pace** <span style="color: grey; font-size: 90%;">13:41:46 UTC</span>

<span style="font-size: 90%;">Yep, got the point :)</span>

↳ **unknown user** <span style="color: grey; font-size: 90%;">14:09:30 UTC</span>

<span style="font-size: 90%;">Quick question: is this the name of the own server? Or the client? If so, maybe instead of letting the customer setting the server we want to pass a function to extract the server from headers on the waf itself.</span>

↳ **unknown user** <span style="color: grey; font-size: 90%;">14:09:48 UTC</span>

<span style="font-size: 90%;">My main concern is the mutability</span>

↳ **Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">14:09:58 UTC</span>

<span style="font-size: 90%;">That’s the problem, you can’t use the server name </span>

↳ **Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">14:10:03 UTC</span>

<span style="font-size: 90%;">It could be a virtual host </span>

↳ **unknown user** <span style="color: grey; font-size: 90%;">14:10:21 UTC</span>

<span style="font-size: 90%;">Like we pass that function when building the waf and then on every transaction before we process phase 1 we set the server name from headers.</span>

↳ **Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">14:10:24 UTC</span>

<span style="font-size: 90%;">And golang http reverse proxy library removes the host header </span>

↳ **Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">14:10:38 UTC</span>

<span style="font-size: 90%;">Also caddy </span>

↳ **unknown user** <span style="color: grey; font-size: 90%;">14:10:58 UTC</span>

<span style="font-size: 90%;">Ok, so my question would be, can we do this at waf level instead of transaction level?</span>

↳ **Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">14:12:05 UTC</span>

<span style="font-size: 90%;">Wouldn’t work for cases like spoa </span>

↳ **Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">14:12:13 UTC</span>

<span style="font-size: 90%;">A single waf instance might feed multiple apps</span>

↳ **Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">14:12:36 UTC</span>

<span style="font-size: 90%;">It’s a transaction thing </span>

↳ **unknown user** <span style="color: grey; font-size: 90%;">14:23:32 UTC</span>

<span style="font-size: 90%;">But you can set on all wags.</span>

↳ **unknown user** <span style="color: grey; font-size: 90%;">14:23:35 UTC</span>

<span style="font-size: 90%;">*wafs</span>

↳ **unknown user** <span style="color: grey; font-size: 90%;">14:24:05 UTC</span>

<span style="font-size: 90%;">My main point is that lets not make the transaction mutablr.</span>

↳ **unknown user** <span style="color: grey; font-size: 90%;">14:24:36 UTC</span>

<span style="font-size: 90%;">If we set a callback on the waf that will be applied "when logging" then we have the info and still don't mutate the transaction.</span>

↳ **unknown user** <span style="color: grey; font-size: 90%;">14:24:43 UTC</span>

<span style="font-size: 90%;">Let me scratch a Pr</span>

↳ **unknown user** <span style="color: grey; font-size: 90%;">14:25:13 UTC</span>

<span style="font-size: 90%;">Because this is about logging right?</span>

↳ **Matteo Pace** <span style="color: grey; font-size: 90%;">14:26:06 UTC</span>

<span style="font-size: 90%;">It just not only about logging, rules may try to match the SERVER_NAME variable, that currently is never populated</span>

↳ **unknown user** <span style="color: grey; font-size: 90%;">14:26:55 UTC</span>

<span style="font-size: 90%;">Ok, still that can happen after adding the headers.</span>

↳ **Matteo Pace** <span style="color: grey; font-size: 90%;">14:27:03 UTC</span>

<span style="font-size: 90%;">So it is something that should be populated at phase 1</span>

↳ **unknown user** <span style="color: grey; font-size: 90%;">14:27:34 UTC</span>

<span style="font-size: 90%;">If we do wafconfig.WithServerExtractor(func(headers) string)</span>

↳ **Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">14:28:07 UTC</span>

<span style="font-size: 90%;">but that should be the default behavior</span>

↳ **Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">14:28:17 UTC</span>

<span style="font-size: 90%;">unless we process the server name</span>

↳ **Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">14:29:23 UTC</span>

<span style="font-size: 90%;">AddRequestHeaders looks for the host</span>

↳ **unknown user** <span style="color: grey; font-size: 90%;">14:36:46 UTC</span>

<span style="font-size: 90%;">Forget about my concerns. Tx is mutable already. Let's just add the method.</span>

**Matteo Pace** <span style="color: grey; font-size: 90%;">13:38:17 UTC</span>

<span style="font-size: 90%;">Great, thanks. I will update the PR following this approach. Retrieving the server name from the headers can be something delegated to the connectors before calling the setter</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">14:38:56 UTC</span>

<span style="font-size: 90%;">should we start tagging nightlies for the unstable v3/dev branch? There are a lot of people using v3, and it would be easier to handle breaking changes (We only tag if there was a merged PR)</span>

