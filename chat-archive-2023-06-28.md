### Wed, Jun 28th, 2023

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:00:25 UTC</span>

<span style="font-size: 90%;">Hello everyone, and welcome to our monthly meeting!
Let’s wait a few minutes to see who else is joining :slightly_smiling_face:</span>

**Matteo Pace** <span style="color: grey; font-size: 90%;">12:02:29 UTC</span>

<span style="font-size: 90%;">Hey hey :wave:</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:03:16 UTC</span>

<span style="font-size: 90%;">_@JC_ _@fzipitria_</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:04:29 UTC</span>

<span style="font-size: 90%;">Meeting link: [https://github.com/corazawaf/coraza/issues/814](https://github.com/corazawaf/coraza/issues/814)</span>

**JC** <span style="color: grey; font-size: 90%;">12:04:54 UTC</span>

<span style="font-size: 90%;">Aloha</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:05:43 UTC</span>

<span style="font-size: 90%;">This month has been full of releases, we released v3, v3.0.1, and v3.0.2.
As most of you Know we are super proud of v3 as it is a major update with tons of performance and API improvements</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:06:48 UTC</span>

<span style="font-size: 90%;">v3.0.1 is a super important update as it implements a few bug fixes, performance improvements and most important it fixes this security advisory [https://github.com/corazawaf/coraza/security/advisories/GHSA-c2pj-v37r-2p6h](https://github.com/corazawaf/coraza/security/advisories/GHSA-c2pj-v37r-2p6h)
This bug allows an attacker to DDOS coraza by using a malicious content-type header</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:07:57 UTC</span>

<span style="font-size: 90%;">and v3.0.2 fixes a super important bug that was affecting our connectors by sometimes breaking the body buffers</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:08:17 UTC</span>

<span style="font-size: 90%;">This month 6 PRs were created and merged:
[https://github.com/corazawaf/coraza/pull/807](https://github.com/corazawaf/coraza/pull/807)
[https://github.com/corazawaf/coraza/pull/808](https://github.com/corazawaf/coraza/pull/808)
[https://github.com/corazawaf/coraza/pull/811](https://github.com/corazawaf/coraza/pull/811)
[https://github.com/corazawaf/coraza/pull/812](https://github.com/corazawaf/coraza/pull/812)
[https://github.com/corazawaf/coraza/pull/824](https://github.com/corazawaf/coraza/pull/824)
[https://github.com/corazawaf/coraza/pull/825](https://github.com/corazawaf/coraza/pull/825)</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:09:09 UTC</span>

<span style="font-size: 90%;">After v3 release, we have seen a considerable increase in the number of issues and contributions, so I would like to thank the team for the diffusion and the rest of the community for trusting us with our security :slightly_smiling_face: it has been an awesome month</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:10:01 UTC</span>

<span style="font-size: 90%;">We are receiving a lot of activity for most of our connectors, there is a lot of interest in the SPOA and we have received a lot of feedbacks so we hope at some point it can become stable</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:10:23 UTC</span>

<span style="font-size: 90%;">Caddy connector has received lots of issues but it means there is interest in the community :slightly_smiling_face: development is quite active here</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:10:41 UTC</span>

<span style="font-size: 90%;">We are finally receiving a lot of interest and participation in libcoraza, which will become the heart of the Nginx connector</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:12:02 UTC</span>

<span style="font-size: 90%;">and of course, our proxy-wasm team has finally released v0.1.0 and v0.1.1 :slightly_smiling_face: [https://github.com/corazawaf/coraza-proxy-wasm/releases/tag/0.1.0](https://github.com/corazawaf/coraza-proxy-wasm/releases/tag/0.1.0)</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:12:24 UTC</span>

<span style="font-size: 90%;">so enough of project status, any questions ?</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:13:38 UTC</span>

<span style="font-size: 90%;">Ok so the first topic is HTTP audit log writer</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:15:32 UTC</span>

<span style="font-size: 90%;">We have to do a few definitions
</span>

**JC** <span style="color: grey; font-size: 90%;">12:17:09 UTC</span>

<span style="font-size: 90%;"> right now coraza is not aware of its own version so we cannot add it to the user-agentnice to have, not toooo important tho.

 Are we keeping compatibility for mlogc?is this what people does use? What are the alternatives?

Are we adding any extra headers to the log upload?Shall we support auth?

 How much is the timeout value?whatever we come up will be wrong but maybe a best guess e.g. 1s?

Should we use content-type? the problem is we are not aware of the formatter’s content-typeGood one, we must make the formatter aware of it

I guess like every other format

nope, it creates a barrier for local development and PoC</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:17:56 UTC</span>

<span style="font-size: 90%;">I’m not aware if anyone uses mlogc, its part of the modsec toolkit, _@airween_ what do you think?</span>

↳ **airween** <span style="color: grey; font-size: 90%;">12:24:33 UTC</span>

<span style="font-size: 90%;">Uhm, sorry, I don't use mlogc. (Actually I use autit.log very rarely...)</span>

↳ **Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:24:50 UTC</span>

<span style="font-size: 90%;">but what do you think about the community?</span>

↳ **airween** <span style="color: grey; font-size: 90%;">12:26:14 UTC</span>

<span style="font-size: 90%;">Sorry, I don't understand this now :slightly_smiling_face: - what do you mean about "the community"?</span>

↳ **Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:26:35 UTC</span>

<span style="font-size: 90%;">I mean, do you see people asking about mlogc? Is it a thing?</span>

↳ **Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:26:41 UTC</span>

<span style="font-size: 90%;">or nobody really uses it</span>

↳ **airween** <span style="color: grey; font-size: 90%;">12:28:36 UTC</span>

<span style="font-size: 90%;">oh, I got it - once I saw an issue under ModSecurity GH page that they want to finish the developing of that tool, because none of them use that</span>

↳ **Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:29:13 UTC</span>

<span style="font-size: 90%;">great! thank you very much :slightly_smiling_face:</span>

↳ **airween** <span style="color: grey; font-size: 90%;">12:29:26 UTC</span>

<span style="font-size: 90%;">but now I can't find that issue :disappointed:</span>

↳ **airween** <span style="color: grey; font-size: 90%;">12:32:28 UTC</span>

<span style="font-size: 90%;">oh, sorry - here is the post what I remember:

[https://github.com/SpiderLabs/ModSecurity/issues/2275#issuecomment-594551793](https://github.com/SpiderLabs/ModSecurity/issues/2275#issuecomment-594551793)

he just mentions there that mlogc is not available in libmodsecurity3.

Hope this helps :heart:</span>

↳ **Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:33:02 UTC</span>

<span style="font-size: 90%;">thank you very much! This is a great reference. It makes sense to ignore mlogc support</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:18:26 UTC</span>

<span style="font-size: 90%;">Auth is supported by using basic auth, just set the URL as [http://username:passsword@url.com](http://username:passsword@url.com)</span>

↳ **JC** <span style="color: grey; font-size: 90%;">12:18:45 UTC</span>

<span style="font-size: 90%;">This isn’t ZeroTrust friendly</span>

↳ **Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:18:56 UTC</span>

<span style="font-size: 90%;">nothing is zerotrust friendly</span>

↳ **Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:20:19 UTC</span>

<span style="font-size: 90%;">In that case we would have to extend AuditLogConfig with a username and a password</span>

↳ **JC** <span style="color: grey; font-size: 90%;">12:21:07 UTC</span>

<span style="font-size: 90%;">Probably support for headers is desirable.</span>

↳ **Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:22:17 UTC</span>

<span style="font-size: 90%;">we could add something like
SecAuditLogHttpsHeader X-Api-Key %{API_KEY}
To get API keys from ENV?</span>

↳ **JC** <span style="color: grey; font-size: 90%;">12:26:08 UTC</span>

<span style="font-size: 90%;">Since we are talking about adding a new directive it is better to defer this until someone request it.</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:21:14 UTC</span>

<span style="font-size: 90%;">what happens if the binary formatter uses null bytes ?</span>

↳ **JC** <span style="color: grey; font-size: 90%;">12:21:41 UTC</span>

<span style="font-size: 90%;">What is the problem? We let the receiver to deal with it.</span>

↳ **JC** <span style="color: grey; font-size: 90%;">12:21:56 UTC</span>

<span style="font-size: 90%;">I mean in https we can't do much more than sending the payload.</span>

↳ **JC** <span style="color: grey; font-size: 90%;">12:22:13 UTC</span>

<span style="font-size: 90%;">If we want something more sofisticated maybe people use other stuff</span>

↳ **Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:23:27 UTC</span>

<span style="font-size: 90%;">what I mean if we would have to handle CRLFs inside the binary payloads</span>

↳ **Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:23:45 UTC</span>

<span style="font-size: 90%;">but I agree</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:24:28 UTC</span>

<span style="font-size: 90%;">ok so for log formatters lets update the map to store both, the content-type and the formatter. Then we propagate it using the options</span>

**airween** <span style="color: grey; font-size: 90%;">12:24:33 UTC</span>

<span style="font-size: 90%;">Uhm, sorry, I don't use mlogc. (Actually I use autit.log very rarely...)</span>

↳ **airween** <span style="color: grey; font-size: 90%;">12:24:33 UTC</span>

<span style="font-size: 90%;">Uhm, sorry, I don't use mlogc. (Actually I use autit.log very rarely...)</span>

↳ **Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:24:50 UTC</span>

<span style="font-size: 90%;">but what do you think about the community?</span>

↳ **airween** <span style="color: grey; font-size: 90%;">12:26:14 UTC</span>

<span style="font-size: 90%;">Sorry, I don't understand this now :slightly_smiling_face: - what do you mean about "the community"?</span>

↳ **Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:26:35 UTC</span>

<span style="font-size: 90%;">I mean, do you see people asking about mlogc? Is it a thing?</span>

↳ **Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:26:41 UTC</span>

<span style="font-size: 90%;">or nobody really uses it</span>

↳ **airween** <span style="color: grey; font-size: 90%;">12:28:36 UTC</span>

<span style="font-size: 90%;">oh, I got it - once I saw an issue under ModSecurity GH page that they want to finish the developing of that tool, because none of them use that</span>

↳ **Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:29:13 UTC</span>

<span style="font-size: 90%;">great! thank you very much :slightly_smiling_face:</span>

↳ **airween** <span style="color: grey; font-size: 90%;">12:29:26 UTC</span>

<span style="font-size: 90%;">but now I can't find that issue :disappointed:</span>

↳ **airween** <span style="color: grey; font-size: 90%;">12:32:28 UTC</span>

<span style="font-size: 90%;">oh, sorry - here is the post what I remember:

[https://github.com/SpiderLabs/ModSecurity/issues/2275#issuecomment-594551793](https://github.com/SpiderLabs/ModSecurity/issues/2275#issuecomment-594551793)

he just mentions there that mlogc is not available in libmodsecurity3.

Hope this helps :heart:</span>

↳ **Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:33:02 UTC</span>

<span style="font-size: 90%;">thank you very much! This is a great reference. It makes sense to ignore mlogc support</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:24:50 UTC</span>

<span style="font-size: 90%;">but what do you think about the community?</span>

↳ **airween** <span style="color: grey; font-size: 90%;">12:24:33 UTC</span>

<span style="font-size: 90%;">Uhm, sorry, I don't use mlogc. (Actually I use autit.log very rarely...)</span>

↳ **Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:24:50 UTC</span>

<span style="font-size: 90%;">but what do you think about the community?</span>

↳ **airween** <span style="color: grey; font-size: 90%;">12:26:14 UTC</span>

<span style="font-size: 90%;">Sorry, I don't understand this now :slightly_smiling_face: - what do you mean about "the community"?</span>

↳ **Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:26:35 UTC</span>

<span style="font-size: 90%;">I mean, do you see people asking about mlogc? Is it a thing?</span>

↳ **Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:26:41 UTC</span>

<span style="font-size: 90%;">or nobody really uses it</span>

↳ **airween** <span style="color: grey; font-size: 90%;">12:28:36 UTC</span>

<span style="font-size: 90%;">oh, I got it - once I saw an issue under ModSecurity GH page that they want to finish the developing of that tool, because none of them use that</span>

↳ **Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:29:13 UTC</span>

<span style="font-size: 90%;">great! thank you very much :slightly_smiling_face:</span>

↳ **airween** <span style="color: grey; font-size: 90%;">12:29:26 UTC</span>

<span style="font-size: 90%;">but now I can't find that issue :disappointed:</span>

↳ **airween** <span style="color: grey; font-size: 90%;">12:32:28 UTC</span>

<span style="font-size: 90%;">oh, sorry - here is the post what I remember:

[https://github.com/SpiderLabs/ModSecurity/issues/2275#issuecomment-594551793](https://github.com/SpiderLabs/ModSecurity/issues/2275#issuecomment-594551793)

he just mentions there that mlogc is not available in libmodsecurity3.

Hope this helps :heart:</span>

↳ **Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:33:02 UTC</span>

<span style="font-size: 90%;">thank you very much! This is a great reference. It makes sense to ignore mlogc support</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:29:22 UTC</span>

<span style="font-size: 90%;">The rest of the points looks good to me:
</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:29:42 UTC</span>

<span style="font-size: 90%;">let’s consider headers for the future, I think it requires more feedbacks</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:30:43 UTC</span>

<span style="font-size: 90%;">if everyone is ok we could proceed to the next topic</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:31:04 UTC</span>

<span style="font-size: 90%;">I believe it’s not a thing anymore as we already released v3.0.1 and v3.0.2</span>

↳ **JC** <span style="color: grey; font-size: 90%;">12:31:56 UTC</span>

<span style="font-size: 90%;">Following semver</span>

↳ **Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:32:27 UTC</span>

<span style="font-size: 90%;">exactly we should always use semantic versioning as it is the go standard for go mod</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:31:22 UTC</span>

<span style="font-size: 90%;">Sponsorship perks !</span>

**JC** <span style="color: grey; font-size: 90%;">12:31:56 UTC</span>

<span style="font-size: 90%;">Following semver</span>

↳ **JC** <span style="color: grey; font-size: 90%;">12:31:56 UTC</span>

<span style="font-size: 90%;">Following semver</span>

↳ **Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:32:27 UTC</span>

<span style="font-size: 90%;">exactly we should always use semantic versioning as it is the go standard for go mod</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:33:02 UTC</span>

<span style="font-size: 90%;">thank you very much! This is a great reference. It makes sense to ignore mlogc support</span>

↳ **airween** <span style="color: grey; font-size: 90%;">12:24:33 UTC</span>

<span style="font-size: 90%;">Uhm, sorry, I don't use mlogc. (Actually I use autit.log very rarely...)</span>

↳ **Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:24:50 UTC</span>

<span style="font-size: 90%;">but what do you think about the community?</span>

↳ **airween** <span style="color: grey; font-size: 90%;">12:26:14 UTC</span>

<span style="font-size: 90%;">Sorry, I don't understand this now :slightly_smiling_face: - what do you mean about "the community"?</span>

↳ **Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:26:35 UTC</span>

<span style="font-size: 90%;">I mean, do you see people asking about mlogc? Is it a thing?</span>

↳ **Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:26:41 UTC</span>

<span style="font-size: 90%;">or nobody really uses it</span>

↳ **airween** <span style="color: grey; font-size: 90%;">12:28:36 UTC</span>

<span style="font-size: 90%;">oh, I got it - once I saw an issue under ModSecurity GH page that they want to finish the developing of that tool, because none of them use that</span>

↳ **Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:29:13 UTC</span>

<span style="font-size: 90%;">great! thank you very much :slightly_smiling_face:</span>

↳ **airween** <span style="color: grey; font-size: 90%;">12:29:26 UTC</span>

<span style="font-size: 90%;">but now I can't find that issue :disappointed:</span>

↳ **airween** <span style="color: grey; font-size: 90%;">12:32:28 UTC</span>

<span style="font-size: 90%;">oh, sorry - here is the post what I remember:

[https://github.com/SpiderLabs/ModSecurity/issues/2275#issuecomment-594551793](https://github.com/SpiderLabs/ModSecurity/issues/2275#issuecomment-594551793)

he just mentions there that mlogc is not available in libmodsecurity3.

Hope this helps :heart:</span>

↳ **Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:33:02 UTC</span>

<span style="font-size: 90%;">thank you very much! This is a great reference. It makes sense to ignore mlogc support</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:33:20 UTC</span>

<span style="font-size: 90%;">I want to use as examples:
</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:34:07 UTC</span>

<span style="font-size: 90%;">Also I would like to mention that although we don’t have any financial requirement as a project, we would be able to do some interesting things, like issues with bounties, a dev on duty program, and a coraza live event somewhere in the world</span>

↳ **JC** <span style="color: grey; font-size: 90%;">12:35:42 UTC</span>

<span style="font-size: 90%;">The ConRaza cc _@fzipitria_</span>

↳ **Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:36:09 UTC</span>

<span style="font-size: 90%;">corazacon</span>

↳ **Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:36:27 UTC</span>

<span style="font-size: 90%;">corazapalooza</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:36:03 UTC</span>

<span style="font-size: 90%;">There is also another kind of support that we appreciate a lot, for example, Tetrate provides helps in the development, and Traceable formally supports my work in coraza. Among other companies like Intel.
Should we also have a perk for them?</span>

↳ **JC** <span style="color: grey; font-size: 90%;">12:36:59 UTC</span>

<span style="font-size: 90%;">Interesting idea</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:38:05 UTC</span>

<span style="font-size: 90%;">Zap has the following criteria for platinum sponsorship:
Perks:
</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:39:39 UTC</span>

<span style="font-size: 90%;">I don’t think there is anyone working 80% on coraza so maybe we should adjust it to a lower sponsorship level</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:44:10 UTC</span>

<span style="font-size: 90%;">Let’s copy Zap’s criterias wit ha few changes:
</span>

**JC** <span style="color: grey; font-size: 90%;">12:46:32 UTC</span>

<span style="font-size: 90%;">I would create an issue on this and see if there are companies interested</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:46:49 UTC</span>

<span style="font-size: 90%;">Ok lgtm</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:47:00 UTC</span>

<span style="font-size: 90%;">so we will continue this topic inside the issue</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:47:31 UTC</span>

<span style="font-size: 90%;">Finally, JC’s philosophical topic, to Dependabot or not to dependabot</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:47:55 UTC</span>

<span style="font-size: 90%;">I personally love dependabot, it doesnt hurt</span>

**JC** <span style="color: grey; font-size: 90%;">12:48:12 UTC</span>

<span style="font-size: 90%;">So I should have create an issue for this, it's being in my head for a while</span>

**JC** <span style="color: grey; font-size: 90%;">12:48:31 UTC</span>

<span style="font-size: 90%;">Whenever we release a new stable version in coraza, updating all the connectors is a pain.</span>

**JC** <span style="color: grey; font-size: 90%;">12:48:47 UTC</span>

<span style="font-size: 90%;">So I think that should be automated.</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:49:38 UTC</span>

<span style="font-size: 90%;">mmh I think dependabot should take care of that, but I don’t know how</span>

**JC** <span style="color: grey; font-size: 90%;">12:50:08 UTC</span>

<span style="font-size: 90%;">I saw this working in other orgs.</span>

**JC** <span style="color: grey; font-size: 90%;">12:50:31 UTC</span>

<span style="font-size: 90%;">So we just need to implement a flow for dependabot to fot he updated whenever coraza is out. Now that coraza is stable we can do that easily.</span>

**JC** <span style="color: grey; font-size: 90%;">12:50:54 UTC</span>

<span style="font-size: 90%;">Like we don't have to deal with breaking changes.</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:55:13 UTC</span>

<span style="font-size: 90%;">let’s create an issue to do the configs</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:55:24 UTC</span>

<span style="font-size: 90%;">but I agree with you, we use dependabot everywhere and it just makes sense</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:56:05 UTC</span>

<span style="font-size: 90%;">any other thing you would like to discuss team? As _@JC_ calls us, corazones :rolling_on_the_floor_laughing: which means hearts in spanish</span>

**JC** <span style="color: grey; font-size: 90%;">12:56:55 UTC</span>

<span style="font-size: 90%;">I wonder if we should look at supply chain checks on CI like using snyk or things like that.</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:57:36 UTC</span>

<span style="font-size: 90%;">it is interesting but we should also keep in mind that most of our dependencies are for development and building, not for runtime</span>

**JC** <span style="color: grey; font-size: 90%;">12:58:19 UTC</span>

<span style="font-size: 90%;">But my real big concern is who is taking ownership of the actions we just talked about in this meeting. When people wakes up it would be cool for us to check the meeting and see if any of us can own some work _@Matteo Pace_ _@Roshan Piyush_ _@fzipitria_ _@Anuraag Agrawal_</span>

**JC** <span style="color: grey; font-size: 90%;">12:59:55 UTC</span>

<span style="font-size: 90%;">I can own dependabot check</span>

**JC** <span style="color: grey; font-size: 90%;">13:00:12 UTC</span>

<span style="font-size: 90%;">Since _@Juan Pablo Tosso_ is owning the https reporter</span>

**Matteo Pace** <span style="color: grey; font-size: 90%;">13:01:36 UTC</span>

<span style="font-size: 90%;">I think would be great to create all the issues that you just talk about and wait for some assignments/self assignments</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">13:03:12 UTC</span>

<span style="font-size: 90%;">I agree with Matteo, lets create proper issues</span>

**Matteo Pace** <span style="color: grey; font-size: 90%;">13:03:14 UTC</span>

<span style="font-size: 90%;">About dependabot, I don’t know if it is feasible, but some issues required to manually run go mod tidy</span>

↳ **Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">13:03:39 UTC</span>

<span style="font-size: 90%;">[https://docs.github.com/en/code-security/dependabot/working-with-dependabot/configuring-access-to-private-registries-for-dependabot](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/configuring-access-to-private-registries-for-dependabot) there are a lot of options for dependabot</span>

↳ **Matteo Pace** <span style="color: grey; font-size: 90%;">13:05:24 UTC</span>

<span style="font-size: 90%;">I will be careful if it happens again, and see if it is doable to make it run automatically</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">13:03:16 UTC</span>

<span style="font-size: 90%;">and each one of us take ownership</span>

**Liang Zhibang** <span style="color: grey; font-size: 90%;">13:07:00 UTC</span>

<span style="font-size: 90%;">please review my PR :saluting_face: [https://github.com/corazawaf/libcoraza/pull/30](https://github.com/corazawaf/libcoraza/pull/30)</span>

↳ **Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">13:08:41 UTC</span>

<span style="font-size: 90%;">nice catch, I will take a look and approve it, thank you</span>

↳ **Liang Zhibang** <span style="color: grey; font-size: 90%;">13:09:48 UTC</span>

<span style="font-size: 90%;">:saluting_face:</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">13:08:47 UTC</span>

<span style="font-size: 90%;">Ok so we close our monthly meetings</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">13:08:56 UTC</span>

<span style="font-size: 90%;">Please team help me creating issues</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">13:08:58 UTC</span>

<span style="font-size: 90%;">Thank you everyone!</span>

**Liang Zhibang** <span style="color: grey; font-size: 90%;">13:14:04 UTC</span>

<span style="font-size: 90%;">I’ve ported coraza to openresty successfully. But my libcoraza-nginx not compatible with libcoraza. I think of create a repo named libcoraza-nginx</span>

↳ **Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">13:14:57 UTC</span>

<span style="font-size: 90%;">lets try to keep it as generic as possible but we can do that in the meantime</span>

↳ **Liang Zhibang** <span style="color: grey; font-size: 90%;">13:16:25 UTC</span>

<span style="font-size: 90%;">you are right.</span>

**Liang Zhibang** <span style="color: grey; font-size: 90%;">13:14:19 UTC</span>

<span style="font-size: 90%;">[https://github.com/potats0/lua-resty-coraza](https://github.com/potats0/lua-resty-coraza)</span>

**Liang Zhibang** <span style="color: grey; font-size: 90%;">13:15:07 UTC</span>

<span style="font-size: 90%;">load full coreruleset spend 50M in arm ubuntu</span>

**Liang Zhibang** <span style="color: grey; font-size: 90%;">13:16:49 UTC</span>

<span style="font-size: 90%;">worker process 4,</span>

↳ **Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">13:17:51 UTC</span>

<span style="font-size: 90%;">terrific work, thank you very much Liang, we will keep a close eye</span>

**Liang Zhibang** <span style="color: grey; font-size: 90%;">13:23:31 UTC</span>

<span style="font-size: 90%;">qps with  coraza</span>

**Liang Zhibang** <span style="color: grey; font-size: 90%;">13:23:51 UTC</span>

<span style="font-size: 90%;">qps without coraza</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">13:28:35 UTC</span>

<span style="font-size: 90%;">and have you tested blocking?</span>

**Liang Zhibang** <span style="color: grey; font-size: 90%;">13:29:47 UTC</span>

<span style="font-size: 90%;">sure</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">13:29:51 UTC</span>

<span style="font-size: 90%;">_@fzipitria_ / _@JC_ what should be a decent test plan to test there are no memory leaks?</span>

**Liang Zhibang** <span style="color: grey; font-size: 90%;">13:30:04 UTC</span>

<span style="font-size: 90%;">I tested</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">13:30:28 UTC</span>

<span style="font-size: 90%;">it is hard to test memory leaks using cgo because of the garbage collector</span>

**Liang Zhibang** <span style="color: grey; font-size: 90%;">13:31:03 UTC</span>

<span style="font-size: 90%;">if memory was leaked the nginx  will  oom  when
 10000 requests</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">13:31:14 UTC</span>

<span style="font-size: 90%;">I see</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">13:31:53 UTC</span>

<span style="font-size: 90%;">I’m impressed, I will take a deeper look and get back to you. We really appreciate your contribution</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">13:32:29 UTC</span>

<span style="font-size: 90%;">We have to solve the log callbacks issue too</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">13:32:39 UTC</span>

<span style="font-size: 90%;">where are you pointing the error logs?</span>

**Liang Zhibang** <span style="color: grey; font-size: 90%;">13:33:50 UTC</span>

<span style="font-size: 90%;">i didn't  point the  error log  .I am wondering about  log  callback</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">13:34:15 UTC</span>

<span style="font-size: 90%;">there is a function but it is not working. I will take some time to fix it and get back to you</span>

**Liang Zhibang** <span style="color: grey; font-size: 90%;">13:35:31 UTC</span>

<span style="font-size: 90%;">sure, i'm waiting for you, and thank  you for contributing</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">13:36:02 UTC</span>

<span style="font-size: 90%;">but we should send coraza a pointer to a function that handles the log

void
ngx_http_modsecurity_log(void *log, const void* data)
{
    const char *msg;
    if (log == NULL) {
        return;
    }
    msg = (const char *) data;

    ngx_log_error(NGX_LOG_INFO, (ngx_log_t *)log, 0, "%s", msg);
}
msc_set_log_cb(conf->modsec, ngx_http_modsecurity_log);</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">13:36:07 UTC</span>

<span style="font-size: 90%;">this is how modsec - nginx handles it</span>

**Liang Zhibang** <span style="color: grey; font-size: 90%;">13:39:56 UTC</span>

<span style="font-size: 90%;">cgo is hard to invoke pointer of function</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">13:40:08 UTC</span>

<span style="font-size: 90%;">yes but there is a hack</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">13:40:19 UTC</span>

<span style="font-size: 90%;">you create a C function inside go, then you do it from there</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">13:40:34 UTC</span>

<span style="font-size: 90%;">so instead of calling the C function, you call the CGO C function that calls the C function</span>

**Liang Zhibang** <span style="color: grey; font-size: 90%;">13:44:05 UTC</span>

<span style="font-size: 90%;">you mean that log callback for printing  error log of coraza?</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">13:44:13 UTC</span>

<span style="font-size: 90%;">yes</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">13:44:29 UTC</span>

<span style="font-size: 90%;">_@airween_ would be happy if it is fixed lol</span>

**Liang Zhibang** <span style="color: grey; font-size: 90%;">13:45:42 UTC</span>

<span style="font-size: 90%;">libcoraza exposed a few api for calling.maybe  use go reflect  to  solve the problem</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">13:46:20 UTC</span>

<span style="font-size: 90%;">[https://github.com/corazawaf/libcoraza/blob/master/libcoraza/log.go](https://github.com/corazawaf/libcoraza/blob/master/libcoraza/log.go)</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">13:46:36 UTC</span>

<span style="font-size: 90%;">[https://github.com/corazawaf/libcoraza/blob/3fb9f6c3928e8fc141eb5fd9cea3d74a268204e1/libcoraza/coraza.go#L280](https://github.com/corazawaf/libcoraza/blob/3fb9f6c3928e8fc141eb5fd9cea3d74a268204e1/libcoraza/coraza.go#L280)</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">13:46:57 UTC</span>

<span style="font-size: 90%;">coraza_set_log_cb should call C.send_log_to_cb</span>

**Liang Zhibang** <span style="color: grey; font-size: 90%;">13:48:12 UTC</span>

<span style="font-size: 90%;">get it</span>

