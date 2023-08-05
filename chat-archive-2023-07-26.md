### Wed, Jul 26th, 2023

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:03:46 UTC</span>

<span style="font-size: 90%;">hello everyone ! welcome to our monthly meeting</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:04:58 UTC</span>

<span style="font-size: 90%;">[https://github.com/corazawaf/coraza/issues/851](https://github.com/corazawaf/coraza/issues/851)</span>

**Matteo Pace** <span style="color: grey; font-size: 90%;">12:05:41 UTC</span>

<span style="font-size: 90%;">Hello! :wave:</span>

**JC** <span style="color: grey; font-size: 90%;">12:06:04 UTC</span>

<span style="font-size: 90%;">Aloha</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:06:06 UTC</span>

<span style="font-size: 90%;">_@fzipitria_ is right here with me, so I guess he is here in spirit:rolling_on_the_floor_laughing:</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:08:27 UTC</span>

<span style="font-size: 90%;">This is a repeated new, but Coraza graduated to production in OWASP!!! Congratulations everyone for this team effort. And thanks _@fzipitria_ for handling owasp communciation</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:09:23 UTC</span>

<span style="font-size: 90%;"></span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:11:04 UTC</span>

<span style="font-size: 90%;">is there any discussion around any of the active PRs?</span>

**Matteo Pace** <span style="color: grey; font-size: 90%;">12:13:12 UTC</span>

<span style="font-size: 90%;">About [https://github.com/corazawaf/coraza/pull/827](https://github.com/corazawaf/coraza/pull/827): I just wanted to know if the idea seems right, or if there are any concerns about it. If it is just in the backlog, no problems :slightly_smiling_face:</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:14:44 UTC</span>

<span style="font-size: 90%;">I’m not sure, but now that you are touching this, like 226 has a bug: [https://github.com/corazawaf/coraza/pull/827/files#diff-6f6aa9e1d64510d056daea5ce34cb7b3fb4376585c78379f9844f5f4318d5706L226](https://github.com/corazawaf/coraza/pull/827/files#diff-6f6aa9e1d64510d056daea5ce34cb7b3fb4376585c78379f9844f5f4318d5706L226) There is an extra \n</span>

**Matteo Pace** <span style="color: grey; font-size: 90%;">12:16:52 UTC</span>

<span style="font-size: 90%;">:+1: will address it (for the records [https://github.com/corazawaf/coraza-caddy/issues/87](https://github.com/corazawaf/coraza-caddy/issues/87)), fix the conflict and ask for a rereview</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:17:48 UTC</span>

<span style="font-size: 90%;">should we consider a default log message ? what happens if you create a disruptive plugin</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:17:52 UTC</span>

<span style="font-size: 90%;">like “send to captcha”</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:18:26 UTC</span>

<span style="font-size: 90%;">Maybe we should use a generic message like: Coraza: Custom disruptive action (Action Name).</span>

**Matteo Pace** <span style="color: grey; font-size: 90%;">12:19:03 UTC</span>

<span style="font-size: 90%;">and it is like the default case in the switch, makes sense</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:21:06 UTC</span>

<span style="font-size: 90%;">Regarding the deployment of HTTPS audit logs</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:21:12 UTC</span>

<span style="font-size: 90%;">should we make it part of v3.1.0 or v3.0.3?</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:21:16 UTC</span>

<span style="font-size: 90%;">it is not a patch, it is a feature</span>

**JC** <span style="color: grey; font-size: 90%;">12:22:07 UTC</span>

<span style="font-size: 90%;">I would vote for 3.0.3. While ir is a new feature it is not a fundamental change and also we still turn the gears on things like timeout</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:22:29 UTC</span>

<span style="font-size: 90%;">lgtm, if there is any comment let’s handle async</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:22:36 UTC</span>

<span style="font-size: 90%;">_@JC_ asked me to touch this topic: [https://github.com/corazawaf/coraza/issues/849](https://github.com/corazawaf/coraza/issues/849)</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:22:58 UTC</span>

<span style="font-size: 90%;">Basically our debug logs are inconsistent, there is no testing for debug and there is no guaranteed regression.</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:23:12 UTC</span>

<span style="font-size: 90%;">at the beginning we thought it wasn’t going to be a problem but we have seen several issues around this</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:24:17 UTC</span>

<span style="font-size: 90%;">Any proposal? or thoughts?</span>

**Matteo Pace** <span style="color: grey; font-size: 90%;">12:27:47 UTC</span>

<span style="font-size: 90%;">I agree that they require some work and care</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:28:36 UTC</span>

<span style="font-size: 90%;">in modsecurity, most regression tests are performed using debug logs</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:28:55 UTC</span>

<span style="font-size: 90%;">maybe we can extend our current testing engine to consume that?</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:29:14 UTC</span>

<span style="font-size: 90%;">for example, for ID matching we can use the debug log + the MatchedRule</span>

**fzipitria** <span style="color: grey; font-size: 90%;">12:29:35 UTC</span>

<span style="font-size: 90%;">I think there are different topics.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">12:29:48 UTC</span>

<span style="font-size: 90%;">We are messing error, audit and debug logs</span>

**fzipitria** <span style="color: grey; font-size: 90%;">12:30:17 UTC</span>

<span style="font-size: 90%;">Do we need tests for all log types?</span>

**Matteo Pace** <span style="color: grey; font-size: 90%;">12:33:53 UTC</span>

<span style="font-size: 90%;">If I am not wrong most of the issues are about error logs, and I feel that they also are the mostly used. I would start from them (also in terms of tests)</span>

**fzipitria** <span style="color: grey; font-size: 90%;">12:34:08 UTC</span>

<span style="font-size: 90%;">Excellent</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:36:01 UTC</span>

<span style="font-size: 90%;">well, I believe Matteo’s PR takes care of most issues</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:41:24 UTC</span>

<span style="font-size: 90%;">great</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:41:27 UTC</span>

<span style="font-size: 90%;">there was another topic</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:41:59 UTC</span>

<span style="font-size: 90%;">regarding blog posts, _@JC_ is not happy about medium because it might require a login, I was planning to use a medium page as our blog as it won’t require administration</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:42:16 UTC</span>

<span style="font-size: 90%;">we can use [coraza.io](http://coraza.io) as blog but it is annoying as it requires PRs and approvals to edit or create articles</span>

↳ **Matteo Pace** <span style="color: grey; font-size: 90%;">12:53:44 UTC</span>

<span style="font-size: 90%;">couldn’t it be also kind of useful for better quality going through a “review” process? (just looking for pros of this option :sweat_smile:)</span>

↳ **Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:54:17 UTC</span>

<span style="font-size: 90%;">I usually make like 10 revisions of my blog posts :face_holding_back_tears: </span>

↳ **JC** <span style="color: grey; font-size: 90%;">13:19:45 UTC</span>

<span style="font-size: 90%;">I agree with Matteo. I prefer collaborative process, also using a platform requires us to distribute credentials which is not great.</span>

↳ **Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">13:23:47 UTC</span>

<span style="font-size: 90%;">I don’t agree on this one. It would take a lot of effort to upload media and do edits. What about linking external sources ? </span>

↳ **JC** <span style="color: grey; font-size: 90%;">13:24:28 UTC</span>

<span style="font-size: 90%;">Why is that a problem? Upload media is a matter to reference an image.</span>

↳ **JC** <span style="color: grey; font-size: 90%;">13:24:44 UTC</span>

<span style="font-size: 90%;">What do you mean by linking external sources</span>

↳ **JC** <span style="color: grey; font-size: 90%;">13:25:07 UTC</span>

<span style="font-size: 90%;">Also, something I saw in OTel was that a GitHub action could check if all links in the MD were working and not broken</span>

↳ **Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">13:26:18 UTC</span>

<span style="font-size: 90%;">To other blog sources </span>

↳ **Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">13:27:06 UTC</span>

<span style="font-size: 90%;">Also no one takes care of coraza.lo and right now it doesn’t support a blog, as it was removed years ago . It would require many changes </span>

↳ **JC** <span style="color: grey; font-size: 90%;">13:33:13 UTC</span>

<span style="font-size: 90%;">I see. For simplicity [wordpress.org](http://wordpress.org) would be easier, we just need to sort out credentials, maybe a LastPass account would be required to be shared among team members.</span>

↳ **Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">13:34:37 UTC</span>

<span style="font-size: 90%;">I think it would be nice to host it ourself, as it would help us test coraza. But if no one agree with this one, I’m ok with [Wordpress.org](http://Wordpress.org) </span>

↳ **JC** <span style="color: grey; font-size: 90%;">13:36:44 UTC</span>

<span style="font-size: 90%;">I am OK hosting it but wordpress isn't the most secure platform so not sure</span>

↳ **Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">13:37:33 UTC</span>

<span style="font-size: 90%;">I mean, if we cannot trust coraza, who Can?
We could harden it, make it read only, disable plug-ins and templates, etc </span>

↳ **Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">13:37:36 UTC</span>

<span style="font-size: 90%;">We should be fine </span>

↳ **JC** <span style="color: grey; font-size: 90%;">13:39:32 UTC</span>

<span style="font-size: 90%;">Not talking only about web attacks but server attacks.</span>

↳ **Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">13:39:33 UTC</span>

<span style="font-size: 90%;">That would be a different meeting, but it doesn’t scare me </span>

↳ **Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">13:40:04 UTC</span>

<span style="font-size: 90%;">Oh, yes that’s a thing, but we can always use public key authentication and disable everything </span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:42:39 UTC</span>

<span style="font-size: 90%;">So it’s that or mounting a wordpress under [blog.coraza.io](http://blog.coraza.io)</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:43:14 UTC</span>

<span style="font-size: 90%;">IMHO, I know the concerts of security, but if we use a hardened wordpress without any plugin, we should be fine (famous last words)</span>

