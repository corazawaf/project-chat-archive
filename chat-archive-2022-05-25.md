### Wed, May 25th, 2022

**fzipitria** <span style="color: grey; font-size: 90%;">12:01:56 UTC</span>

<span style="font-size: 90%;">:wave:</span>

**airween** <span style="color: grey; font-size: 90%;">12:03:20 UTC</span>

<span style="font-size: 90%;">hey, I'm here with an half eye, but unfortunately I'm very busy...</span>

**Roshan Piyush** <span style="color: grey; font-size: 90%;">12:18:13 UTC</span>

<span style="font-size: 90%;">:wave:</span>

**c z** <span style="color: grey; font-size: 90%;">12:19:02 UTC</span>

<span style="font-size: 90%;">:wave:</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:19:23 UTC</span>

<span style="font-size: 90%;">Hey!  Sorry for the delay, the timezone changes in my country are messy</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:20:02 UTC</span>

<span style="font-size: 90%;">Well this haven’t been a very interesting month regarding changes to the project, but there has been a lot of unfinished activity that is important</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:20:15 UTC</span>

<span style="font-size: 90%;">Project Status

</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:22:27 UTC</span>

<span style="font-size: 90%;">The same for CRS compatibility, we have figured some compatibility issues but we haven’t been able to fix them all.</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:23:16 UTC</span>

<span style="font-size: 90%;">For the C connector, we have been struggling with CGO, we need some help for this project, as CGO is hard and some experience would be appreciated. We currently have problems moving a C function callback into golang</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:23:37 UTC</span>

<span style="font-size: 90%;">Are there any comments or questions until now?</span>

**Roshan Piyush** <span style="color: grey; font-size: 90%;">12:25:55 UTC</span>

<span style="font-size: 90%;">I can take PR [https://github.com/corazawaf/coraza/pull/235](https://github.com/corazawaf/coraza/pull/235) forward. IMO this would be a priority as it would lead to good bypasses.</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:26:57 UTC</span>

<span style="font-size: 90%;">Thank you Roshan, that would be awesome</span>

**airween** <span style="color: grey; font-size: 90%;">12:28:20 UTC</span>

<span style="font-size: 90%;">we could move forward in C connector, if the logger function would work... then we can make some test applications which embed the libcoraza, and start to measure the memory leaks - may be those are not real problems</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:28:59 UTC</span>

<span style="font-size: 90%;">That is another issue, how do we measure memory leaks</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:29:28 UTC</span>

<span style="font-size: 90%;">the problem with the C wrapper is that we must abandon the GO garbage collector to allow C to handle the memory</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:29:47 UTC</span>

<span style="font-size: 90%;">But once we want to clean the memory we must connect the objects back into golangs garbage collector</span>

**c z** <span style="color: grey; font-size: 90%;">12:29:52 UTC</span>

<span style="font-size: 90%;">This PR [https://github.com/corazawaf/coraza/pull/245](https://github.com/corazawaf/coraza/pull/245)
Is there any other design idea for logger, after discussion I think I can go ahead and finish it</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:30:23 UTC</span>

<span style="font-size: 90%;">Your design is fine but it is a breaking change</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:30:32 UTC</span>

<span style="font-size: 90%;">we cannot update waf.Logger as it would break the api</span>

**fzipitria** <span style="color: grey; font-size: 90%;">12:30:53 UTC</span>

<span style="font-size: 90%;">We were planning on a redesign for v3</span>

**fzipitria** <span style="color: grey; font-size: 90%;">12:31:29 UTC</span>

<span style="font-size: 90%;">that PR won’t be left out, we just need to make adjustments</span>

**fzipitria** <span style="color: grey; font-size: 90%;">12:31:41 UTC</span>

<span style="font-size: 90%;">IMHO, we should have one logger factory or similar</span>

**fzipitria** <span style="color: grey; font-size: 90%;">12:32:16 UTC</span>

<span style="font-size: 90%;">That can create audit, legacy, serial, concurrent, etc.</span>

**Roshan Piyush** <span style="color: grey; font-size: 90%;">12:32:36 UTC</span>

<span style="font-size: 90%;">For memory leaks. All I could think of was post cleanup force runtime.GC() and measure the allocated memory.</span>

↳ **Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:33:04 UTC</span>

<span style="font-size: 90%;">Thank you Roshan, that would be helpful</span>

**fzipitria** <span style="color: grey; font-size: 90%;">12:32:41 UTC</span>

<span style="font-size: 90%;">Then anyone implementing that can move to logrus or others</span>

**fzipitria** <span style="color: grey; font-size: 90%;">12:32:59 UTC</span>

<span style="font-size: 90%;">Hmmm. We are overstepping each other :smile:</span>

**fzipitria** <span style="color: grey; font-size: 90%;">12:33:31 UTC</span>

<span style="font-size: 90%;">Or we go for threads on a topic, or we keep discussing one each time :wink:</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:34:16 UTC</span>

<span style="font-size: 90%;">I agree. Thank you _@c z_ for your PR, and it will be merged once we start working on the v3 branch</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:34:47 UTC</span>

<span style="font-size: 90%;">Any other questions regarding the current PRs? and thank you _@fzipitria_ for the explanation</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:35:55 UTC</span>

<span style="font-size: 90%;">Ok so we move on</span>

**c z** <span style="color: grey; font-size: 90%;">12:37:03 UTC</span>

<span style="font-size: 90%;">Thanks, _@fzipitria_ and _@Juan Pablo Tosso_.
And when does the v3 plan start?</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:37:13 UTC</span>

<span style="font-size: 90%;">that’s what we are going to discuss in a few minutes</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:37:22 UTC</span>

<span style="font-size: 90%;">let me continue with a few points and we will get there</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:38:29 UTC</span>

<span style="font-size: 90%;">Regarding funding, we are generating a few donations, and we are working with sponsors to receive more. Two meetings ago we discussed about bounties likes shirts, mugs, etc, but we agreed that they were not good enough</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:39:55 UTC</span>

<span style="font-size: 90%;">I would like to be able to tell sponsors why their money would be helpful. That’s why I would like to propose issue bounties and dev on-duty program</span>

**fzipitria** <span style="color: grey; font-size: 90%;">12:40:37 UTC</span>

<span style="font-size: 90%;">We had (and still have) a good experience in our dev on-duty program</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:41:12 UTC</span>

<span style="font-size: 90%;">Exactly, coreruleset have a great design for their program and we can learn from it, _@fzipitria_ could you provide a short description?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">12:41:25 UTC</span>

<span style="font-size: 90%;">Sure</span>

**fzipitria** <span style="color: grey; font-size: 90%;">12:41:35 UTC</span>

<span style="font-size: 90%;">We basically divide efforts weekly</span>

**fzipitria** <span style="color: grey; font-size: 90%;">12:41:51 UTC</span>

<span style="font-size: 90%;">People self assign a weekly (can be bi-weekly) calendar</span>

**fzipitria** <span style="color: grey; font-size: 90%;">12:42:09 UTC</span>

<span style="font-size: 90%;">And takes the lead on answering issues, and evaluating PRs</span>

**fzipitria** <span style="color: grey; font-size: 90%;">12:42:24 UTC</span>

<span style="font-size: 90%;">Doesn’t need to solve everything, by the way</span>

**fzipitria** <span style="color: grey; font-size: 90%;">12:42:45 UTC</span>

<span style="font-size: 90%;">but it will be the first line of response</span>

**fzipitria** <span style="color: grey; font-size: 90%;">12:43:15 UTC</span>

<span style="font-size: 90%;">If there is the need for a patch, more discussions, etc, then you drive it in that week</span>

**fzipitria** <span style="color: grey; font-size: 90%;">12:44:06 UTC</span>

<span style="font-size: 90%;">It is not a full day job. You are “around” our github to take care</span>

**fzipitria** <span style="color: grey; font-size: 90%;">12:44:25 UTC</span>

<span style="font-size: 90%;">You can take a look daily, during that week</span>

**fzipitria** <span style="color: grey; font-size: 90%;">12:45:03 UTC</span>

<span style="font-size: 90%;">At the CRS we also handle discussions on stackoverflow</span>

**fzipitria** <span style="color: grey; font-size: 90%;">12:45:16 UTC</span>

<span style="font-size: 90%;">But it doesn’t make sense for Coraza now</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:46:16 UTC</span>

<span style="font-size: 90%;">Thank you Felipe. In our case it would make sense, as we had a problem last week keeping discussions alive</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:46:37 UTC</span>

<span style="font-size: 90%;">so having a dev on duty program would encourage users to participate and keep the discussion flowing</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:47:30 UTC</span>

<span style="font-size: 90%;">Regarding the issue bounty, there are feature requests that are part of our roadmap and require a lot of work. It would be great to have paid bounties on them.</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:47:58 UTC</span>

<span style="font-size: 90%;">Any questions about these plans?</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:49:21 UTC</span>

<span style="font-size: 90%;">Also, does everyone agree with these plans?</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:51:05 UTC</span>

<span style="font-size: 90%;">Ok next topic: We know we have many enterprise users</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:51:12 UTC</span>

<span style="font-size: 90%;">fortune 500s</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:51:27 UTC</span>

<span style="font-size: 90%;">and interesting companies</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:52:04 UTC</span>

<span style="font-size: 90%;">I would like our community to encourage enterprise users for reviews and permission to add them to our README</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:52:35 UTC</span>

<span style="font-size: 90%;">If any of you belongs to an enterprise using Coraza, it would be amazing to have feedback or at least the chance to link them into our readme or website</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:54:13 UTC</span>

<span style="font-size: 90%;">Regarding [coraza.io](http://coraza.io), our website is properly structured but it requires a major update</span>

**Roshan Piyush** <span style="color: grey; font-size: 90%;">12:55:16 UTC</span>

<span style="font-size: 90%;">And [playground](https://playground.coraza.io/) is down too.</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:55:37 UTC</span>

<span style="font-size: 90%;">That one is on me, I have asked Owasp for an AWS account but not success yet</span>

**fzipitria** <span style="color: grey; font-size: 90%;">12:55:50 UTC</span>

<span style="font-size: 90%;">I can help with that</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:56:05 UTC</span>

<span style="font-size: 90%;">that would be amazing, we will keep a parallel discussion for that one</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:57:02 UTC</span>

<span style="font-size: 90%;">I would like to take as reference this: [https://coreruleset.org/docs/rules/](https://coreruleset.org/docs/rules/)</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:58:22 UTC</span>

<span style="font-size: 90%;">We will keep a discussion during this week for [coraza.io](http://coraza.io), it is a long one</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:58:28 UTC</span>

<span style="font-size: 90%;">Finally coraza v3!</span>

**c z** <span style="color: grey; font-size: 90%;">12:58:35 UTC</span>

<span style="font-size: 90%;">We can find some templates, such as vuepress, gitbook and Hugo</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:58:49 UTC</span>

<span style="font-size: 90%;">we already use a hugo template, the problem is the content</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:59:11 UTC</span>

<span style="font-size: 90%;">I created the content almost two years ago, and there have been no updates</span>

**Roshan Piyush** <span style="color: grey; font-size: 90%;">13:00:06 UTC</span>

<span style="font-size: 90%;">Can we break this work into chunks. Would be easier to target.</span>

↳ **fzipitria** <span style="color: grey; font-size: 90%;">13:02:42 UTC</span>

<span style="font-size: 90%;">Good one. Let’s create issues on what needs to be documented</span>

↳ **Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">13:03:15 UTC</span>

<span style="font-size: 90%;">Great, there are many things that were removed from the original project, we should start with them</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">13:00:33 UTC</span>

<span style="font-size: 90%;">Yes, I will take some time to create issues here [https://github.com/corazawaf/coraza.io](https://github.com/corazawaf/coraza.io)</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">13:00:47 UTC</span>

<span style="font-size: 90%;">I will post them here so people could assign them to theirselves</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">13:01:28 UTC</span>

<span style="font-size: 90%;">Regarding v3</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">13:02:13 UTC</span>

<span style="font-size: 90%;">I would like to propose the v3 version not as a major change (like in the original roadmap), but as an API redesign</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">13:02:26 UTC</span>

<span style="font-size: 90%;">we should fix v2 design issues and enhance extensibility</span>

**fzipitria** <span style="color: grey; font-size: 90%;">13:03:08 UTC</span>

<span style="font-size: 90%;">Excellent! We need this to be even more extensible</span>

**fzipitria** <span style="color: grey; font-size: 90%;">13:03:33 UTC</span>

<span style="font-size: 90%;">One thing we need to keep track though is supported versions</span>

**fzipitria** <span style="color: grey; font-size: 90%;">13:04:20 UTC</span>

<span style="font-size: 90%;">Also, documentation for v2 and v3 is going to run in parallel?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">13:04:59 UTC</span>

<span style="font-size: 90%;">Probably for godoc we don’t have problems, but if we need to explain details further in the website docs, we need to be aware of that</span>

**fzipitria** <span style="color: grey; font-size: 90%;">13:05:17 UTC</span>

<span style="font-size: 90%;">That’s why having supported version would make our lives easier</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">13:05:50 UTC</span>

<span style="font-size: 90%;">So do you think we should version our documentation? for example [https://coraza.io/docs/seclang/directives/](https://coraza.io/docs/seclang/directives/) should migrate to [https://coraza.io/docs/v3/seclang/directives/](https://coraza.io/docs/v3/seclang/directives/)</span>

↳ **Roshan Piyush** <span style="color: grey; font-size: 90%;">13:07:13 UTC</span>

<span style="font-size: 90%;">Backporting docs would be painful though?</span>

↳ **Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">13:07:23 UTC</span>

<span style="font-size: 90%;">Exactly</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">13:07:02 UTC</span>

<span style="font-size: 90%;">I think it could be hard to maintain, as we can barely maintain the website</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">13:07:40 UTC</span>

<span style="font-size: 90%;">So we should just specify what changed on each page</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">13:08:05 UTC</span>

<span style="font-size: 90%;">like docker documentation does</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">13:08:24 UTC</span>

<span style="font-size: 90%;">We add disclaimers on breaking changes</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">13:09:13 UTC</span>

<span style="font-size: 90%;">Ok so if everyone agrees with the development of v3, I would like to start tagging issues as v3</span>

**fzipitria** <span style="color: grey; font-size: 90%;">13:09:33 UTC</span>

<span style="font-size: 90%;">Sure, let’s create a milestone also</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">13:09:39 UTC</span>

<span style="font-size: 90%;">great</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">13:10:05 UTC</span>

<span style="font-size: 90%;">What would be a great starting point? Do you think we should create the branch right now and start pushing things? Or we should wait for more issues?</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">13:10:31 UTC</span>

<span style="font-size: 90%;">Also, what is the criteria to accept v3 issues</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">13:11:00 UTC</span>

<span style="font-size: 90%;">Finally, regarding supported versions, I would create a final v2.1 tag and maintain both, v3 and v2.1</span>

**fzipitria** <span style="color: grey; font-size: 90%;">13:12:08 UTC</span>

<span style="font-size: 90%;">We need to publish that, and also the criteria we are going to use.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">13:12:51 UTC</span>

<span style="font-size: 90%;">Unless there are security issues, we should do that asap. Creating 2.1 tag.</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">13:14:01 UTC</span>

<span style="font-size: 90%;">I agree. So we should create an issue on this one</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">13:15:23 UTC</span>

<span style="font-size: 90%;">Ok, so now that we agree to work on v3, I will keep an open discussion here to work on it. Please take some time to review the v3 tagged issues and make your comments</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">13:15:29 UTC</span>

<span style="font-size: 90%;">is there anything else to discuss?</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">13:16:13 UTC</span>

<span style="font-size: 90%;">set the channel topic: OWASP Coraza Web Application Firewall</span>

**Roshan Piyush** <span style="color: grey; font-size: 90%;">13:16:15 UTC</span>

<span style="font-size: 90%;">I would like to get PR [235](https://github.com/corazawaf/coraza/pull/235) to 2.1</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">13:16:57 UTC</span>

<span style="font-size: 90%;">Sounds fair, there is a 2.1 milestone, feel free to assign the PR</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">13:19:22 UTC</span>

<span style="font-size: 90%;">Ok, so any other topic?</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">13:19:42 UTC</span>

<span style="font-size: 90%;">Thank you everyone for your time, fantastic meeting</span>

**fzipitria** <span style="color: grey; font-size: 90%;">13:22:30 UTC</span>

<span style="font-size: 90%;">Thanks for leading it _@Juan Pablo Tosso_!</span>

