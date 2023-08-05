### Wed, Apr 27th, 2022

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">11:55:08 UTC</span>

<span style="font-size: 90%;">Meeting starting soon </span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:00:42 UTC</span>

<span style="font-size: 90%;">Welcome to the OWASP Coraza monthly meeting</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:02:31 UTC</span>

<span style="font-size: 90%;">_@Roshan Piyush_ _@JC_ _@bxlxx.wu_ you joining?</span>

**JC** <span style="color: grey; font-size: 90%;">12:04:35 UTC</span>

<span style="font-size: 90%;">Yep I am here.</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:06:11 UTC</span>

<span style="font-size: 90%;">_@fzipitria_ is also not available today, so it’s going to be a small meeting</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:06:50 UTC</span>

<span style="font-size: 90%;">So about the project status! I want you to know that we are reviewing GSOC applications for our three projects, GraphQL, coraza-server, and rate limiting, we have 6 applications and we are very proud of it (10% OWASP applications)</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:08:06 UTC</span>

<span style="font-size: 90%;">We released v2 (stable version)</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:08:30 UTC</span>

<span style="font-size: 90%;">And we fixed the following issues:
Thanks everyone for your contributions</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:10:08 UTC</span>

<span style="font-size: 90%;">Finally, I would like to welcome _@Roshan Piyush_ to the core, he is an amazing engineer and a modsecurity expert. He understands coraza pretty well and he is a highly skilled developer and researcher</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:12:03 UTC</span>

<span style="font-size: 90%;">The report for CRS compatibility</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:12:19 UTC</span>

<span style="font-size: 90%;">CRS is preparing v4 and they have made some awesome upgrades</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:12:32 UTC</span>

<span style="font-size: 90%;">sadly we haven’t been able to pick up and we have had some compatibility issues</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:13:16 UTC</span>

<span style="font-size: 90%;">we are currently experiencing issues with 32 tests but we are fixing them asap. You can find the status in this PR [https://github.com/corazawaf/coraza/pull/224](https://github.com/corazawaf/coraza/pull/224)</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:14:11 UTC</span>

<span style="font-size: 90%;">Regarding Lua, it is going to be supported as a plugin</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:14:21 UTC</span>

<span style="font-size: 90%;">The C wrappers (libcoraza) are undergoing tests, we are still having issues with the garbage collection. We are also having problems with the log callback function.</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:14:59 UTC</span>

<span style="font-size: 90%;">It seems that we don’t have much people today but don’t worry! I will leave the topics over here and feel free to comment them :slightly_smiling_face:</span>

**airween** <span style="color: grey; font-size: 90%;">12:15:34 UTC</span>

<span style="font-size: 90%;">The C wrappers (libcoraza) are undergoing tests, we are still having issues with the garbage collection. We are also having problems with the log callback function. - logging function is important for Nginx connector too, I guess</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:19:23 UTC</span>

<span style="font-size: 90%;">Yes, it is important, we are having a design issue, Coraza has a Waf type, it represents a Server in nginx. Basically our logger is attached to the waf (Server)</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:19:33 UTC</span>

<span style="font-size: 90%;">Modsecurity expects a logger per transaction</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:19:55 UTC</span>

<span style="font-size: 90%;">we can still make it work but it requires more testing</span>

**airween** <span style="color: grey; font-size: 90%;">12:24:06 UTC</span>

<span style="font-size: 90%;">Modsecurity expects a logger per transaction - are you sure? It seems it works with (WAF) instance based logger

see this:

[https://github.com/digitalwave/ftwrunner/blob/v1.0/dev/src/engines/ftwmodsecurity/ftwmodsecurity.c#L27-L31](https://github.com/digitalwave/ftwrunner/blob/v1.0/dev/src/engines/ftwmodsecurity/ftwmodsecurity.c#L27-L31)

I just added the callback function to engine itself, not to the transaction</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:25:00 UTC</span>

<span style="font-size: 90%;">    Transaction * transaction = msc_new_transaction(
        (ModSecurity *)engine->engine_instance,
#ifdef MSC_USE_RULES_SET
        (RulesSet *)engine->rules,
#else
        (Rules *)engine->rules,
#endif
        NULL);I believe the last NULL is a second logger</span>

**airween** <span style="color: grey; font-size: 90%;">12:25:16 UTC</span>

<span style="font-size: 90%;">yes, but that's optional</span>

**airween** <span style="color: grey; font-size: 90%;">12:25:36 UTC</span>

<span style="font-size: 90%;">the first one is suggested</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:25:37 UTC</span>

<span style="font-size: 90%;">still, I think that should make things easier but we still have the GC issues</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:26:01 UTC</span>

<span style="font-size: 90%;">we are receiving errors when we call the logger</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:26:45 UTC</span>

<span style="font-size: 90%;">Maybe there is a type casting error, we will eventually figure it out. I will give it more priority once we fix the Include function</span>

