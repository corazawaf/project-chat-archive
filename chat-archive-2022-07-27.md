### Wed, Jul 27th, 2022

**Roshan Piyush** <span style="color: grey; font-size: 90%;">12:02:11 UTC</span>

<span style="font-size: 90%;">:wave:</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:02:15 UTC</span>

<span style="font-size: 90%;">Hello and welcome to our monthly meeting</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:03:23 UTC</span>

<span style="font-size: 90%;">Our agenda for today is:
</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:04:52 UTC</span>

<span style="font-size: 90%;">_@fzipitria_ _@bxlxx.wu_ _@JC_</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:05:49 UTC</span>

<span style="font-size: 90%;">Ok so regarding de project status.
Two PRs has enhanced Coraza performance by more than a 200% using CRS
There have been some upgrades for the collections engine and a full replacement of the aho-corasick implementation for the pm and pmf operators</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:06:17 UTC</span>

<span style="font-size: 90%;"></span>

**Roshan Piyush** <span style="color: grey; font-size: 90%;">12:06:33 UTC</span>

<span style="font-size: 90%;">So do you think we need more more on the aho-corasick side?</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:07:00 UTC</span>

<span style="font-size: 90%;">So according to my research, modsecurity takes 90mb of memory to handle CRS</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:07:06 UTC</span>

<span style="font-size: 90%;">Coraza used to take 900mb thanks to aho-corasick</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:07:12 UTC</span>

<span style="font-size: 90%;">with the new implementation coraza takes 300mb</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:07:17 UTC</span>

<span style="font-size: 90%;">we still have to make some magic</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:08:00 UTC</span>

<span style="font-size: 90%;">I have created some benchmarks for CRS: [https://github.com/corazawaf/coraza/pull/301](https://github.com/corazawaf/coraza/pull/301) I will soon merge them to v2 too</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:08:41 UTC</span>

<span style="font-size: 90%;">Also there is a new github action that will tell us if there is a performance regression alert:</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:11:14 UTC</span>

<span style="font-size: 90%;">Any question regarding the current status?</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:11:19 UTC</span>

<span style="font-size: 90%;">shall we pass to v3?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">12:12:57 UTC</span>

<span style="font-size: 90%;">:wave:</span>

↳ **Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:13:12 UTC</span>

<span style="font-size: 90%;">Welcome Felipe</span>

↳ **fzipitria** <span style="color: grey; font-size: 90%;">12:13:46 UTC</span>

<span style="font-size: 90%;">:bow:</span>

**fzipitria** <span style="color: grey; font-size: 90%;">12:14:12 UTC</span>

<span style="font-size: 90%;">Just wanted so say that this has been an awesome effort, thanks _@Juan Pablo Tosso_!! :clap: :clap:</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:14:46 UTC</span>

<span style="font-size: 90%;">Thanks Felipe, we have received a lot of help from the community too :slightly_smiling_face:</span>

**fzipitria** <span style="color: grey; font-size: 90%;">12:15:08 UTC</span>

<span style="font-size: 90%;">Of course :slightly_smiling_face:</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:15:11 UTC</span>

<span style="font-size: 90%;">Regarding v3. There have been many improvements and API changes
First of all, the variables engine has been transformed and now we have a system similar to modsecurity. There are multiple variable types with different helpers and generic helpers. It allows us to safely handle variables programmatically and transparently read them for rules</span>

↳ **Roshan Piyush** <span style="color: grey; font-size: 90%;">12:17:59 UTC</span>

<span style="font-size: 90%;">I promise to take this as a priority.</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:15:57 UTC</span>

<span style="font-size: 90%;">The only problem is that I have undone _@Roshan Piyush_ fixes for case-sensitive/insensitive names</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:16:21 UTC</span>

<span style="font-size: 90%;">I have temporarily disabled tests using these features until fixed</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:18:32 UTC</span>

<span style="font-size: 90%;">We are trying to merge the v2 PR that replaces all tests with testify. Thanks _@JC_ for the great effort in migrating ALL tests</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:20:02 UTC</span>

<span style="font-size: 90%;">We are also working in persistence, it’s a bit fuzzy yet but I think we have a clear idea on how to achieve it. [https://github.com/corazawaf/coraza/tree/v3/dev-persistence](https://github.com/corazawaf/coraza/tree/v3/dev-persistence)</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:20:29 UTC</span>

<span style="font-size: 90%;">_@fzipitria_ proposed [https://github.com/dgraph-io/badger](https://github.com/dgraph-io/badger) as the default persistence engine</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:22:42 UTC</span>

<span style="font-size: 90%;">There is a function called tx.ProcessRequests. it takes an http.Request object and processes phases from 1 to 3
[https://github.com/corazawaf/coraza/blob/v3/dev/http/http.go](https://github.com/corazawaf/coraza/blob/v3/dev/http/http.go)</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:23:06 UTC</span>

<span style="font-size: 90%;">I think this is a very high-level function and it limits creativity from developers</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:23:11 UTC</span>

<span style="font-size: 90%;">that’s why I would like to remove it</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:23:35 UTC</span>

<span style="font-size: 90%;">Altough it’s a widely used function</span>

**Roshan Piyush** <span style="color: grey; font-size: 90%;">12:23:57 UTC</span>

<span style="font-size: 90%;">Why not leave it as a wrapper of what we like to implement?</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:24:52 UTC</span>

<span style="font-size: 90%;">we could leave it at the examples directory</span>

**fzipitria** <span style="color: grey; font-size: 90%;">12:25:47 UTC</span>

<span style="font-size: 90%;">IMHO, phases should register themselves</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:26:32 UTC</span>

<span style="font-size: 90%;">cool, so everyone agrees on transforming it into an example?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">12:27:16 UTC</span>

<span style="font-size: 90%;">This should be a CoR pattern</span>

**fzipitria** <span style="color: grey; font-size: 90%;">12:27:42 UTC</span>

<span style="font-size: 90%;">So anyone can add phases, effectively letting devs adding phases at will</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:28:03 UTC</span>

<span style="font-size: 90%;">They can, they are just tempted by the automatic helper</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:29:18 UTC</span>

<span style="font-size: 90%;">I’m still not quite convinced we have an agreement on this one, so let’s take this discussion further</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:29:42 UTC</span>

<span style="font-size: 90%;">Regarding v3 response body processors</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:30:36 UTC</span>

<span style="font-size: 90%;">Now we support request and response body processors</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:30:52 UTC</span>

<span style="font-size: 90%;">if an API returns a JSON payload we can read it using ARGS_RESPONSE:json…..</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:31:33 UTC</span>

<span style="font-size: 90%;">We have implemented limited XML support with only two xpath expressions for compatibility with coreruleset</span>

**fzipitria** <span style="color: grey; font-size: 90%;">12:32:32 UTC</span>

<span style="font-size: 90%;">The only question is if we are trusting the answer on the declared content-type</span>

**fzipitria** <span style="color: grey; font-size: 90%;">12:32:59 UTC</span>

<span style="font-size: 90%;">And what happens when we cannot parse it</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:33:17 UTC</span>

<span style="font-size: 90%;">if we cannot parse it we fill RESBODY_ERROR_MSG</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:33:27 UTC</span>

<span style="font-size: 90%;">just like REQBODY_ERROR_MSG from request</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:33:49 UTC</span>

<span style="font-size: 90%;">also, Coraza by default doesn’t handle response body, a CTL must be used to force it</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:34:19 UTC</span>

<span style="font-size: 90%;">behavior is very similar to request bodies</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:34:40 UTC</span>

<span style="font-size: 90%;">the only problem is that when we get REQBODY_ERROR_MSG we cannot deny anymore</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:34:45 UTC</span>

<span style="font-size: 90%;">as the buffer has probably already been sent</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:35:20 UTC</span>

<span style="font-size: 90%;">for the caddy connector it would work, as the body is buffered for analysis</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:35:39 UTC</span>

<span style="font-size: 90%;">but we won’t be able to send a new status code, as it was already sent. just a different response body</span>

**fzipitria** <span style="color: grey; font-size: 90%;">12:35:48 UTC</span>

<span style="font-size: 90%;">Excellent</span>

**fzipitria** <span style="color: grey; font-size: 90%;">12:35:50 UTC</span>

<span style="font-size: 90%;">MAkes sense</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:37:14 UTC</span>

<span style="font-size: 90%;">Ok so I think that’s all regarding v3. Any question?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">12:38:26 UTC</span>

<span style="font-size: 90%;">Looking good</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:39:39 UTC</span>

<span style="font-size: 90%;">_@JC_ has made great efforts for the project, he has a strong interest in WAF and he has proven to be an amazing contributor, so I would like to nominate him for the core team</span>

**fzipitria** <span style="color: grey; font-size: 90%;">12:41:53 UTC</span>

<span style="font-size: 90%;">Awesome! Welcome _@JC_!</span>

**fzipitria** <span style="color: grey; font-size: 90%;">12:42:20 UTC</span>

<span style="font-size: 90%;">With a great power, comes a great responsibility! :smile:</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:43:22 UTC</span>

<span style="font-size: 90%;">So last topics! I have worked in two features that I would like for V2 and V3</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:44:13 UTC</span>

<span style="font-size: 90%;">the \@rest operator uses the same syntax as a OpenAPI spec path to match a URL pattern and fill ARGS_PATH. ARGS also includes ARGS_PATH</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:45:10 UTC</span>

<span style="font-size: 90%;">`SecRule REQUEST_URI “@rest /api/v1/users/{user_id}” “…msg:‘User id is %{ARGS_PATH.user_id}’”</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:45:24 UTC</span>

<span style="font-size: 90%;">Do we want this as a plugin or as a core feature?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">12:46:54 UTC</span>

<span style="font-size: 90%;">Very good question</span>

**Roshan Piyush** <span style="color: grey; font-size: 90%;">12:47:40 UTC</span>

<span style="font-size: 90%;">IMO as a plugin would be good, as rest is not closely followed and someone may want to implement their own version of rest as they have been doing.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">12:48:04 UTC</span>

<span style="font-size: 90%;">Plugins are more flexible probably</span>

**fzipitria** <span style="color: grey; font-size: 90%;">12:48:23 UTC</span>

<span style="font-size: 90%;">But I was wondering if making it core would help making the difference from modsec</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:48:40 UTC</span>

<span style="font-size: 90%;">the only problem with plugins is that we cannot programmatically create variables</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:49:15 UTC</span>

<span style="font-size: 90%;">Other security consideration, if we include ARGS_PATH in ARGS, it could be overlapped by ARGS_GET, /api/v1/users/5?user_id=4 would trick coraza</span>

↳ **Roshan Piyush** <span style="color: grey; font-size: 90%;">12:56:09 UTC</span>

<span style="font-size: 90%;">Ideally we should handle duplicates and not override here.</span>

↳ **Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:56:31 UTC</span>

<span style="font-size: 90%;">In theory coraza would fill user_id: [5,4]</span>

↳ **fzipitria** <span style="color: grey; font-size: 90%;">12:57:46 UTC</span>

<span style="font-size: 90%;">Yes, parameter pollution handling needs to work properly</span>

**fzipitria** <span style="color: grey; font-size: 90%;">12:50:37 UTC</span>

<span style="font-size: 90%;">CRS is taking a second look at PATH</span>

**fzipitria** <span style="color: grey; font-size: 90%;">12:51:06 UTC</span>

<span style="font-size: 90%;">E.g [https://github.com/coreruleset/coreruleset/issues/2699](https://github.com/coreruleset/coreruleset/issues/2699)</span>

**fzipitria** <span style="color: grey; font-size: 90%;">12:51:47 UTC</span>

<span style="font-size: 90%;">Just saying that more rules might include that in the near future</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:52:37 UTC</span>

<span style="font-size: 90%;">Cool, so let’s vote to bring it to the core or as a plugin: :white_check_mark:=core :eyes:=plugin</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:54:52 UTC</span>

<span style="font-size: 90%;">Ok, we are keeping it in the loop as we don’t have enough support for the feature</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:55:34 UTC</span>

<span style="font-size: 90%;">We are running out of time, any other topics you would like to discuss?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">12:56:17 UTC</span>

<span style="font-size: 90%;">No, I think we are doing good progress on the v3 release</span>

**fzipitria** <span style="color: grey; font-size: 90%;">12:56:46 UTC</span>

<span style="font-size: 90%;">And just a reminder for people to use the new testify framework when writing tests</span>

**fzipitria** <span style="color: grey; font-size: 90%;">12:56:57 UTC</span>

<span style="font-size: 90%;">… and reviewers to be aware of that</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:57:09 UTC</span>

<span style="font-size: 90%;">Yes, we should add it to the contributors guidline</span>

**fzipitria** <span style="color: grey; font-size: 90%;">12:57:10 UTC</span>

<span style="font-size: 90%;">Maybe also changing the PR template would help</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:57:56 UTC</span>

<span style="font-size: 90%;">Yes, I will work on that</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:58:17 UTC</span>

<span style="font-size: 90%;">Ok everyone, nice meetings, thanks for joining!</span>

