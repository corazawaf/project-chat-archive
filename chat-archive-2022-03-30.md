### Wed, Mar 30th, 2022

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:01:21 UTC</span>

<span style="font-size: 90%;">Hey! welcome to OWASP Coraza monthly meeting! you may check the topics here: [https://github.com/corazawaf/coraza/issues/180](https://github.com/corazawaf/coraza/issues/180)
This month we are discussing:
</span>

**bxlxx.wu** <span style="color: grey; font-size: 90%;">12:02:20 UTC</span>

<span style="font-size: 90%;">Hi</span>

**ShiMing Q** <span style="color: grey; font-size: 90%;">12:02:51 UTC</span>

<span style="font-size: 90%;">Cheers!</span>

**airween** <span style="color: grey; font-size: 90%;">12:02:59 UTC</span>

<span style="font-size: 90%;">hey, with an half eye, I can be here... :stuck_out_tongue:</span>

↳ **Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:03:25 UTC</span>

<span style="font-size: 90%;">Even your half eye would be useful :stuck_out_tongue_winking_eye:</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:04:27 UTC</span>

<span style="font-size: 90%;">Regarding the project status:

</span>

**walter** <span style="color: grey; font-size: 90%;">12:06:16 UTC</span>

<span style="font-size: 90%;">nice work!</span>

↳ **Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:06:40 UTC</span>

<span style="font-size: 90%;">thank you Walter</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:06:57 UTC</span>

<span style="font-size: 90%;">Any question about the project status or shall we move to the pending feb stuff?</span>

**walter** <span style="color: grey; font-size: 90%;">12:07:39 UTC</span>

<span style="font-size: 90%;">I haven’t followed closely but I am very interested in the Apache and Nginx integrations, could you tell a bit about their maturity?</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:08:25 UTC</span>

<span style="font-size: 90%;">Sure, we haven’t worked a lot on the apache integration but libcoraza is already working, but it still leaks some memory. _@airween_ has done a great job testing it and building the autotooling with _@fzipitria_</span>

**walter** <span style="color: grey; font-size: 90%;">12:08:27 UTC</span>

<span style="font-size: 90%;">I’m currently busy designing Our Next Webserver Architecture® and I hope Coraza can play a role here :slightly_smiling_face:</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:09:46 UTC</span>

<span style="font-size: 90%;">The nginx connector is basically a fork of the libmodsecurity connector. It is compiling, the autotooling is ready and we are missing some progress regarding the transaction intervention and logging. _@fzipitria_ has taken care of it for the past few weeks. I would have expected students from GSOC to participate but it seems like there is not much interest</span>

**airween** <span style="color: grey; font-size: 90%;">12:10:33 UTC</span>

<span style="font-size: 90%;">I've already started to implement an [ftwrunner](https://github.com/digitalwave/ftwrunner/) like tool, but last 3-4 weeks were terrible in my job, so I hadn't do much time. But now I see the light at the end of the tunnel, so I hope in next few days I can work on it</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:11:33 UTC</span>

<span style="font-size: 90%;">Still, this is a core project in our roadmap, until we find a maintainer</span>

**airween** <span style="color: grey; font-size: 90%;">12:11:42 UTC</span>

<span style="font-size: 90%;">there is an important deadline of our important project, after that I can focused again for CRS/modsec tools</span>

↳ **Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:12:07 UTC</span>

<span style="font-size: 90%;">Thank you Ervin, we are looking forward to it! Good luck on your important project</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:12:48 UTC</span>

<span style="font-size: 90%;">But most of the interest on Coraza has been through our HAProxy SPOA connector, which _@bxlxx.wu_ has taken care of</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:14:04 UTC</span>

<span style="font-size: 90%;">Does it answer your concerns _@walter_?</span>

**walter** <span style="color: grey; font-size: 90%;">12:14:08 UTC</span>

<span style="font-size: 90%;">yes!</span>

**bxlxx.wu** <span style="color: grey; font-size: 90%;">12:14:30 UTC</span>

<span style="font-size: 90%;">I’ve finished most of coraza-spoa’s work and I’m testing it</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:14:55 UTC</span>

<span style="font-size: 90%;">great! thank you everyone, we are moving to the first feb pending issue</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:15:13 UTC</span>

<span style="font-size: 90%;">So the people from the zap project uses part of their budget to create issue bug bounties</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:15:56 UTC</span>

<span style="font-size: 90%;">so basically it seems legit for us to label some issues with a bounty label and gift a shirt, it’s doesn’t seem like much but it’s a great internal effort and it’s done with a lot of love</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:16:32 UTC</span>

<span style="font-size: 90%;">the average price for a coraza shirt with shipping is ~14USD</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:16:44 UTC</span>

<span style="font-size: 90%;">that will be payed with the coraza budget from sponsorships</span>

**fzipitria** <span style="color: grey; font-size: 90%;">12:17:08 UTC</span>

<span style="font-size: 90%;">Awesome</span>

**fzipitria** <span style="color: grey; font-size: 90%;">12:17:09 UTC</span>

<span style="font-size: 90%;">:smile:</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:17:11 UTC</span>

<span style="font-size: 90%;">some countries would be more expensive to ship</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:17:27 UTC</span>

<span style="font-size: 90%;">hey _@fzipitria_ welcome!</span>

**ShiMing Q** <span style="color: grey; font-size: 90%;">12:17:27 UTC</span>

<span style="font-size: 90%;">:+1:</span>

**fzipitria** <span style="color: grey; font-size: 90%;">12:17:40 UTC</span>

<span style="font-size: 90%;">Hey! Was commuting, sorry :)</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:17:51 UTC</span>

<span style="font-size: 90%;">that’s ok, thank you for coming</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:19:07 UTC</span>

<span style="font-size: 90%;">So does everyone agree with the new shirt gifts?
Some additional points
</span>

**fzipitria** <span style="color: grey; font-size: 90%;">12:21:00 UTC</span>

<span style="font-size: 90%;">I would say we send them a form or similar after their PR is merged?</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:21:40 UTC</span>

<span style="font-size: 90%;">Ok, but how do we avoid other malicious users from filling the form in his name?</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:22:14 UTC</span>

<span style="font-size: 90%;">Nvm, we will solve this internally, it’s not a big deal</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:22:20 UTC</span>

<span style="font-size: 90%;">but do we all agree with the gifts?</span>

**bxlxx.wu** <span style="color: grey; font-size: 90%;">12:22:48 UTC</span>

<span style="font-size: 90%;">Are there any other options?</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:22:58 UTC</span>

<span style="font-size: 90%;">well, zap pays bounties in cash</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:23:26 UTC</span>

<span style="font-size: 90%;">we could only afford like 15~ issues paying 100 usd</span>

**bxlxx.wu** <span style="color: grey; font-size: 90%;">12:23:55 UTC</span>

<span style="font-size: 90%;">Maybe we can set a few more options for users to choose. After all, the express fee is a huge expense</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:24:46 UTC</span>

<span style="font-size: 90%;">maybe instead of a shirt, depending on the difficulty on the issue we could gift like a coraza kit: mug+shirt+stickers+etc</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:25:18 UTC</span>

<span style="font-size: 90%;">I’m not a fan of money, we are an open source project and we do everything for the community</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:25:40 UTC</span>

<span style="font-size: 90%;">[https://printify.com/app/products](https://printify.com/app/products) here you can check the list of items for sale, everything can be personalized with the Coraza logo</span>

**fzipitria** <span style="color: grey; font-size: 90%;">12:26:12 UTC</span>

<span style="font-size: 90%;">We can circle back on this with options</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:26:29 UTC</span>

<span style="font-size: 90%;">ok, we will discuss it during the month, we have many other topics</span>

**fzipitria** <span style="color: grey; font-size: 90%;">12:26:32 UTC</span>

<span style="font-size: 90%;">Maybe someone wants just cash for amazon, or alibaba, or similar</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:26:48 UTC</span>

<span style="font-size: 90%;">seems fair</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:27:20 UTC</span>

<span style="font-size: 90%;">Regarding the project values, I would just keep them:
Simplicity, extensibility, innovation, and community
Anything you would add or remove?</span>

**JC** <span style="color: grey; font-size: 90%;">12:28:27 UTC</span>

<span style="font-size: 90%;">Simplicity, extensibility, innovation, maturity and community</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:28:47 UTC</span>

<span style="font-size: 90%;">could you elaborate on maturity _@JC_?</span>

**JC** <span style="color: grey; font-size: 90%;">12:31:38 UTC</span>

<span style="font-size: 90%;">I think one of the good things about coraza is that we not only want to be a port of modsec but include new features but good well proven features are already designed so we just need to reinforce that and provide other new features, in that sense I think we should be careful about what we include because we would have to maintain that for long, maybe “maturity” isn’t the right wording but being careful with what we introduce and how is key IMHO.</span>

**JC** <span style="color: grey; font-size: 90%;">12:32:04 UTC</span>

<span style="font-size: 90%;">Something that express that we won’t introduce things half baked.</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:32:38 UTC</span>

<span style="font-size: 90%;">you are right, we are innovative but we must be professional on how we propose new features</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:33:33 UTC</span>

<span style="font-size: 90%;">maybe something like “built with enterprise focus?”</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:33:53 UTC</span>

<span style="font-size: 90%;">_@fzipitria_ any idea on a word we could use?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">12:34:24 UTC</span>

<span style="font-size: 90%;">I would say that is part of what maturity covers</span>

**walter** <span style="color: grey; font-size: 90%;">12:34:34 UTC</span>

<span style="font-size: 90%;">yeah or maybe stability?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">12:34:38 UTC</span>

<span style="font-size: 90%;">stability</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:34:48 UTC</span>

<span style="font-size: 90%;">_@JC_ do you agree with the word stability?</span>

**JC** <span style="color: grey; font-size: 90%;">12:34:59 UTC</span>

<span style="font-size: 90%;">Yeah +1 on stability</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:35:10 UTC</span>

<span style="font-size: 90%;">great, stability it is</span>

**fzipitria** <span style="color: grey; font-size: 90%;">12:35:22 UTC</span>

<span style="font-size: 90%;">Awesome</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:35:25 UTC</span>

<span style="font-size: 90%;">any other comment on the project values so we can move to the next point?</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:35:58 UTC</span>

<span style="font-size: 90%;">Where to store coraza research: I think we should enforce the usage of the website, alternatives are confluence github wiki</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:36:38 UTC</span>

<span style="font-size: 90%;">Our website is basically a lot of markdown documents</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:37:34 UTC</span>

<span style="font-size: 90%;">Should we focus on the website?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">12:38:04 UTC</span>

<span style="font-size: 90%;">Website for the win</span>

**fzipitria** <span style="color: grey; font-size: 90%;">12:38:13 UTC</span>

<span style="font-size: 90%;">It doesn’t make sense to add other tools</span>

**fzipitria** <span style="color: grey; font-size: 90%;">12:38:26 UTC</span>

<span style="font-size: 90%;">The website is easily editable. It is markdown.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">12:38:37 UTC</span>

<span style="font-size: 90%;">We can include mermaid and other diagrams also</span>

**bxlxx.wu** <span style="color: grey; font-size: 90%;">12:38:55 UTC</span>

<span style="font-size: 90%;">use [coraza.io](http://coraza.io)?</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:38:57 UTC</span>

<span style="font-size: 90%;">Great, it seems we are keeping the website for it. It will be important that all developers are aware on how to update it, but it is super simple</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:38:58 UTC</span>

<span style="font-size: 90%;">yep</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:39:44 UTC</span>

<span style="font-size: 90%;">Great, let’s move</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:39:49 UTC</span>

<span style="font-size: 90%;">Side projects status:
</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:40:44 UTC</span>

<span style="font-size: 90%;">Also, _@bxlxx.wu_ suggested to split coraza-spoa from coraza-server, any comments on that?</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:40:57 UTC</span>

<span style="font-size: 90%;">and keep coraza-server only for GRPC and REST</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:41:19 UTC</span>

<span style="font-size: 90%;">to be honest, it’s fine to me to have them merged, that way we can share the configurations and deployment options</span>

**bxlxx.wu** <span style="color: grey; font-size: 90%;">12:41:23 UTC</span>

<span style="font-size: 90%;">I separate the HAProxy connector from the coraza-server. I think the coraza-server is a project with wider compatibility. It supports any middleware service. So, the spoa shouldn’t appear in the coraza-server.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">12:43:13 UTC</span>

<span style="font-size: 90%;">I’m fine with that</span>

**fzipitria** <span style="color: grey; font-size: 90%;">12:43:30 UTC</span>

<span style="font-size: 90%;">To me this is only an interface</span>

**fzipitria** <span style="color: grey; font-size: 90%;">12:43:56 UTC</span>

<span style="font-size: 90%;">Where rest/grpc/spoa are different ways of communication with servers</span>

**ShiMing Q** <span style="color: grey; font-size: 90%;">12:44:12 UTC</span>

<span style="font-size: 90%;">How the coraza-server will support different protocols, like spoa, GRPC….</span>

**fzipitria** <span style="color: grey; font-size: 90%;">12:44:12 UTC</span>

<span style="font-size: 90%;">If the interface is well defined</span>

↳ **bxlxx.wu** <span style="color: grey; font-size: 90%;">12:46:10 UTC</span>

<span style="font-size: 90%;">This is OK, but in terms of products, I think it is different</span>

↳ **fzipitria** <span style="color: grey; font-size: 90%;">12:48:12 UTC</span>

<span style="font-size: 90%;">Agreed</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:44:21 UTC</span>

<span style="font-size: 90%;">Ok, so if _@bxlxx.wu_ will become the code owner for the coraza-spoa I’m fine with it too</span>

↳ **bxlxx.wu** <span style="color: grey; font-size: 90%;">12:45:16 UTC</span>

<span style="font-size: 90%;">no problem</span>

**fzipitria** <span style="color: grey; font-size: 90%;">12:44:29 UTC</span>

<span style="font-size: 90%;">_@ShiMing Q_ Using an interface?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">12:44:35 UTC</span>

<span style="font-size: 90%;">Like a “connector”</span>

**ShiMing Q** <span style="color: grey; font-size: 90%;">12:45:58 UTC</span>

<span style="font-size: 90%;">Then those will be in separated project? SPOA, GRPC, REST..</span>

**bxlxx.wu** <span style="color: grey; font-size: 90%;">12:46:40 UTC</span>

<span style="font-size: 90%;">SPOA is a single project</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:46:40 UTC</span>

<span style="font-size: 90%;">Technically there will be only one project for GRPC and REST</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:47:19 UTC</span>

<span style="font-size: 90%;">Ok! so we are ok on this?</span>

**bxlxx.wu** <span style="color: grey; font-size: 90%;">12:47:21 UTC</span>

<span style="font-size: 90%;">coraza-server supports grpc and rest because these two protocols are common</span>

**fzipitria** <span style="color: grey; font-size: 90%;">12:47:47 UTC</span>

<span style="font-size: 90%;">I would say we start with SPOA as a single project, as _@bxlxx.wu_ proposes. And then we regroup and take a look afterwards</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:48:08 UTC</span>

<span style="font-size: 90%;">Great, so we should move to the next topic :slightly_smiling_face:</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:48:28 UTC</span>

<span style="font-size: 90%;">about the README, could we skip it ? we have many other important topics</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:49:12 UTC</span>

<span style="font-size: 90%;">Ok, so I added an extra topic, _@JC_ wants to use Coraza in WASM</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:49:15 UTC</span>

<span style="font-size: 90%;">[https://github.com/corazawaf/coraza/issues/210](https://github.com/corazawaf/coraza/issues/210)</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:49:55 UTC</span>

<span style="font-size: 90%;">Basically we would have to add compilation flags to Coraza and split some files for compatibility</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:50:20 UTC</span>

<span style="font-size: 90%;">for example, we would have to create
bodyprocessors/json.go
bodyprocessors/json_tinygo.go</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:50:39 UTC</span>

<span style="font-size: 90%;">and the compiler would pick whether to use the json code or the tinygo code</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:51:59 UTC</span>

<span style="font-size: 90%;">Are we fine with it? _@JC_ could you take care of the tinygo compatibility? I mean, create tests and maintain the _tinygo files</span>

**JC** <span style="color: grey; font-size: 90%;">12:52:39 UTC</span>

<span style="font-size: 90%;">So there are some limitations around the libraries one can use in tinygo, for that we can do two things:
I would go for second option as it will be easier to maintain and we can make coraza prepared to get into wasm world</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:53:20 UTC</span>

<span style="font-size: 90%;">Compatibility right now means removing encoding/xml and replacing encoding/json with another json parsing library. These changes would only be compiled when you use tinygo</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:54:03 UTC</span>

<span style="font-size: 90%;">_@bxlxx.wu_ and _@fzipitria_ any comment?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">12:54:37 UTC</span>

<span style="font-size: 90%;">I would say second option, for sure</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:55:02 UTC</span>

<span style="font-size: 90%;">Great, so _@JC_ would you be able to help maintaining that?</span>

↳ **JC** <span style="color: grey; font-size: 90%;">12:59:47 UTC</span>

<span style="font-size: 90%;">YEs</span>

↳ **Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">13:00:03 UTC</span>

<span style="font-size: 90%;">great, thank you José Carlos</span>

↳ **JC** <span style="color: grey; font-size: 90%;">13:00:10 UTC</span>

<span style="font-size: 90%;">(Carlos)</span>

↳ **JC** <span style="color: grey; font-size: 90%;">13:00:16 UTC</span>

<span style="font-size: 90%;">I mean José Carlos</span>

↳ **Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">13:00:27 UTC</span>

<span style="font-size: 90%;">fixed :partyparrot:, sorry</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:55:43 UTC</span>

<span style="font-size: 90%;">I mean, encoding/json is a super safe library, I wouldn’t replace it</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:56:05 UTC</span>

<span style="font-size: 90%;">and there are no alternative xml decoding libraries</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:56:42 UTC</span>

<span style="font-size: 90%;">Ok, so we are moving to the next topic</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:56:46 UTC</span>

<span style="font-size: 90%;">Windows compatibility</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:57:10 UTC</span>

<span style="font-size: 90%;">do we need it? should we consider it when writing new code ? Should we add it to the contributors guideline ?</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:57:19 UTC</span>

<span style="font-size: 90%;">Should we also add tests?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">12:57:26 UTC</span>

<span style="font-size: 90%;">I would say we don't</span>

**fzipitria** <span style="color: grey; font-size: 90%;">12:57:58 UTC</span>

<span style="font-size: 90%;">Unless someone wants to maintain it</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:58:02 UTC</span>

<span style="font-size: 90%;">Ok, so what if we wait until we get an active “windows” contributor? Because none of us are windows users</span>

**fzipitria** <span style="color: grey; font-size: 90%;">12:58:12 UTC</span>

<span style="font-size: 90%;">Yes</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:58:18 UTC</span>

<span style="font-size: 90%;">Great</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:58:42 UTC</span>

<span style="font-size: 90%;">Seems fair to me, any additional comment on windows compatibility?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">12:59:32 UTC</span>

<span style="font-size: 90%;">Not from me</span>

**bxlxx.wu** <span style="color: grey; font-size: 90%;">12:59:48 UTC</span>

<span style="font-size: 90%;">+1</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">13:00:08 UTC</span>

<span style="font-size: 90%;">ok</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">13:00:41 UTC</span>

<span style="font-size: 90%;">Great, next topic Response body processing</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">13:00:50 UTC</span>

<span style="font-size: 90%;">do we need it? is it a v2 issue or v3?</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">13:01:12 UTC</span>

<span style="font-size: 90%;">basically it would allow us to process response body like:
SecRule RESPONSE_ARGS:user_id "@gt 1000" "id:1000,phase:4,msg:'Response user ID > 1000'"</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">13:01:42 UTC</span>

<span style="font-size: 90%;">It requires api breaking changes</span>

**bxlxx.wu** <span style="color: grey; font-size: 90%;">13:02:38 UTC</span>

<span style="font-size: 90%;">vote for v3</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">13:03:24 UTC</span>

<span style="font-size: 90%;">Great, I think it doesn’t need more discussion</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">13:03:42 UTC</span>

<span style="font-size: 90%;">Regarding project versioning, what should be our strategy?:
Feature-based
Whenever a feature that is considered core or awesome is required to break compatibility we release a major version. It could easily lead to 3 major versions per year.
Anual based
We release one major version that would break compatibility per year (or some other period)
To be continued</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">13:04:07 UTC</span>

<span style="font-size: 90%;">Should we tag a new version each time an important feature will break the api?</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">13:04:38 UTC</span>

<span style="font-size: 90%;">or should we tag new versions annually? or bi-anual</span>

**fzipitria** <span style="color: grey; font-size: 90%;">13:06:36 UTC</span>

<span style="font-size: 90%;">I would say feature based</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">13:07:14 UTC</span>

<span style="font-size: 90%;">Ok!</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">13:07:33 UTC</span>

<span style="font-size: 90%;">So the next three topics are just discussions, because they will indeed be implemented</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">13:07:35 UTC</span>

<span style="font-size: 90%;"></span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">13:07:39 UTC</span>

<span style="font-size: 90%;">any comments on that?</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">13:08:32 UTC</span>

<span style="font-size: 90%;">I would like to discuss about the debug log mechanism, should we switch from just using logger.Debug(…) to:
if tx.LogLevel == types.DebugLevel {
 logger.Debug(...)
}</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">13:08:54 UTC</span>

<span style="font-size: 90%;">It requires more lines of code, but it’s more efficient as logger.Debug() will always process the strings even if there is no debug</span>

**walter** <span style="color: grey; font-size: 90%;">13:09:18 UTC</span>

<span style="font-size: 90%;">well spotted, I don’t know how much of a performance impact it is…</span>

**fzipitria** <span style="color: grey; font-size: 90%;">13:09:39 UTC</span>

<span style="font-size: 90%;">I'm hoping in another meeting</span>

**walter** <span style="color: grey; font-size: 90%;">13:09:42 UTC</span>

<span style="font-size: 90%;">could the logger itself not look at the LogLevel and return early?</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">13:10:07 UTC</span>

<span style="font-size: 90%;">thank you _@fzipitria_</span>

**walter** <span style="color: grey; font-size: 90%;">13:10:21 UTC</span>

<span style="font-size: 90%;">passing the string to the function is just a pointer I think, or does it copy? :thinking_face:</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">13:10:38 UTC</span>

<span style="font-size: 90%;">I’m not sure why, but I see the logging functions in the performance graphs</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">13:10:44 UTC</span>

<span style="font-size: 90%;">even if there is no logging</span>

**walter** <span style="color: grey; font-size: 90%;">13:10:51 UTC</span>

<span style="font-size: 90%;">wow</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">13:10:57 UTC</span>

<span style="font-size: 90%;">that’s because in order to encode a coraza log you must use the following syntax:</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">13:11:13 UTC</span>

<span style="font-size: 90%;">logger.Debug(“Some log”, zap.String(“transaction_id”, someid”))</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">13:11:18 UTC</span>

<span style="font-size: 90%;">so there are some reflection processes</span>

**walter** <span style="color: grey; font-size: 90%;">13:11:20 UTC</span>

<span style="font-size: 90%;">ah!</span>

**walter** <span style="color: grey; font-size: 90%;">13:11:37 UTC</span>

<span style="font-size: 90%;">yeah then I think this could be a quick win :slightly_smiling_face:</span>

**walter** <span style="color: grey; font-size: 90%;">13:11:40 UTC</span>

<span style="font-size: 90%;">well, maybe not quick, but not hard</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">13:12:02 UTC</span>

<span style="font-size: 90%;">yep, it could be a slow process of replacing the logs</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">13:12:20 UTC</span>

<span style="font-size: 90%;">Great, so that was all, we managed to discuss everything this time</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">13:12:25 UTC</span>

<span style="font-size: 90%;">any other questions or comments? :slightly_smiling_face:</span>

**walter** <span style="color: grey; font-size: 90%;">13:12:37 UTC</span>

<span style="font-size: 90%;">no just applause :clap:</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">13:12:56 UTC</span>

<span style="font-size: 90%;">thank you everyone for participating! Great meeting</span>

