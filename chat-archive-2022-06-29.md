### Wed, Jun 29th, 2022

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:00:30 UTC</span>

<span style="font-size: 90%;">Hey everyone, welcome to our monthly meeting </span>

**bxlxx.wu** <span style="color: grey; font-size: 90%;">12:00:47 UTC</span>

<span style="font-size: 90%;">Hey</span>

**fzipitria** <span style="color: grey; font-size: 90%;">12:02:58 UTC</span>

<span style="font-size: 90%;">Hey!</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:03:43 UTC</span>

<span style="font-size: 90%;">_@Roshan Piyush_</span>

**fzipitria** <span style="color: grey; font-size: 90%;">12:03:57 UTC</span>

<span style="font-size: 90%;">Yes?</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:04:23 UTC</span>

<span style="font-size: 90%;">I think we are good to go</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:04:41 UTC</span>

<span style="font-size: 90%;">this will be a special meeting, we are not going to review project status, but v3 issues</span>

**Roshan Piyush** <span style="color: grey; font-size: 90%;">12:05:06 UTC</span>

<span style="font-size: 90%;">Here</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:05:11 UTC</span>

<span style="font-size: 90%;">there are two issues: [https://github.com/corazawaf/coraza/issues/267](https://github.com/corazawaf/coraza/issues/267) and [https://github.com/corazawaf/coraza/issues/246](https://github.com/corazawaf/coraza/issues/246)</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:07:09 UTC</span>

<span style="font-size: 90%;">So first of all, it’s important to notice that coraza v3 is not a huge change to the existing version, but an upgrade to fix design bugs, enhance performance and implement small additional features like response body processor and persistence</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:08:06 UTC</span>

<span style="font-size: 90%;">I would like to discuss the new variables engine, considering currently each variable is a map[byte]map[string][]string</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:08:20 UTC</span>

<span style="font-size: 90%;">there is a specific issue on this one: [https://github.com/corazawaf/coraza/issues/268](https://github.com/corazawaf/coraza/issues/268)</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:08:44 UTC</span>

<span style="font-size: 90%;">we must consider that it must be faster, more dynamic and support persistence</span>

**Roshan Piyush** <span style="color: grey; font-size: 90%;">12:10:20 UTC</span>

<span style="font-size: 90%;">This is going to impact performance with reallocation as golang likes contiguous memories.</span>

**fzipitria** <span style="color: grey; font-size: 90%;">12:11:36 UTC</span>

<span style="font-size: 90%;">What do you mean?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">12:12:02 UTC</span>

<span style="font-size: 90%;">For proxy variables?</span>

**Roshan Piyush** <span style="color: grey; font-size: 90%;">12:14:29 UTC</span>

<span style="font-size: 90%;">Traversing them individually is fine. But we should not do dynamic A+B in the transaction.
Also, there is a precedence order of values that starts coming into question.
For example. If both get<k1, v1> and post<k1, v2> exists, Would merge store the order.</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:15:13 UTC</span>

<span style="font-size: 90%;">what about abstracting all variables with a single return type? We can use arrays instead of slices and we could use sync.Pool to reuse the allocated resources
type VariableResult struct {
  Collection [50]rune // Or strings buffers
  Key [100]rune
  Value [100]rune
}

func (...) Key() string{
// we get Key until 0x00
}Regarding the function, we could use a class instead of a function, so we can cache the results</span>

**Roshan Piyush** <span style="color: grey; font-size: 90%;">12:16:23 UTC</span>

<span style="font-size: 90%;">So extending the variable mechanism to support dynamic variables is good. But we should not drop native variables.</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:18:23 UTC</span>

<span style="font-size: 90%;">you are right, we must keep order in mind</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:18:33 UTC</span>

<span style="font-size: 90%;">ok, we are going to follow the discussion on the issue, any other comments?</span>

↳ **fzipitria** <span style="color: grey; font-size: 90%;">12:20:02 UTC</span>

<span style="font-size: 90%;">All good</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:19:46 UTC</span>

<span style="font-size: 90%;">Please, _@Roshan Piyush_, add your inquiry to the issue</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:20:22 UTC</span>

<span style="font-size: 90%;">Great, next topic: Replace request body processor with generic Body Processors (Request+Response)</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:20:33 UTC</span>

<span style="font-size: 90%;">The current Body processor is designed only for requests</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:21:26 UTC</span>

<span style="font-size: 90%;">the main problem right now would be to understand which variables are we filling whether it’s a request or a response. Also we must consider that some body processors should not be enabled for responses, like multipart, or urlencoded</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:22:07 UTC</span>

<span style="font-size: 90%;">also there are special cases where the response is going to be slightly different from the requests, like GraphQL</span>

**fzipitria** <span style="color: grey; font-size: 90%;">12:22:34 UTC</span>

<span style="font-size: 90%;">What about responses with Range? Won’t those use multipart in the response?</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:23:20 UTC</span>

<span style="font-size: 90%;">Interesting</span>

**fzipitria** <span style="color: grey; font-size: 90%;">12:23:23 UTC</span>

<span style="font-size: 90%;">Ideally body processors would not care about the request/response</span>

**fzipitria** <span style="color: grey; font-size: 90%;">12:23:42 UTC</span>

<span style="font-size: 90%;">The only thing they need to know is which variables they will be filling</span>

**fzipitria** <span style="color: grey; font-size: 90%;">12:23:45 UTC</span>

<span style="font-size: 90%;">Right?</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:24:11 UTC</span>

<span style="font-size: 90%;">We must take note of that one, we expect users to use http.Response and it should abstract us from the response multipart, but custom implementations might struggle</span>

**fzipitria** <span style="color: grey; font-size: 90%;">12:24:17 UTC</span>

<span style="font-size: 90%;">And that might depend only on the phase?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">12:25:30 UTC</span>

<span style="font-size: 90%;">I agree we need to make body processors agnostic of the request/response.</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:25:41 UTC</span>

<span style="font-size: 90%;">Also, I think we should tell users to avoid Ranges if they are buffering requests in Coraza, as Coraza will still buffer it and it won’t do any good</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:26:29 UTC</span>

<span style="font-size: 90%;">I don’t think it will depend on the phase, it should have a function for requests and a function for responses</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:26:45 UTC</span>

<span style="font-size: 90%;">ok, so we will create an issue on this one with this notes, any additional comments?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">12:26:59 UTC</span>

<span style="font-size: 90%;">No, let move it to the issue.</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:27:24 UTC</span>

<span style="font-size: 90%;">Regarding the Debug logging interface</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:27:42 UTC</span>

<span style="font-size: 90%;">Currently we have many issues with Zap, because it uses a lot of reflection and low level features of golang</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:27:53 UTC</span>

<span style="font-size: 90%;">it’s not friendly with compilers like tinygo and interpreters like Yaegi</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:28:34 UTC</span>

<span style="font-size: 90%;">We should replace it with a custom login interface and implement a new log library, we could use the native log or we could use something like logrus</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:28:54 UTC</span>

<span style="font-size: 90%;">The new interface must be replaceable and removable (disable debug on building), so it will be framework agnostic</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:30:08 UTC</span>

<span style="font-size: 90%;">Structured logging is super efficient, but we won’t be able to keep using it, as we should consider that people using debug are not expecting high performance</span>

**fzipitria** <span style="color: grey; font-size: 90%;">12:30:52 UTC</span>

<span style="font-size: 90%;">I think we should be agnotic</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:31:08 UTC</span>

<span style="font-size: 90%;">Additional subtopics: How to classify a log message in the golang log levels, any good practices to write debug logs?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">12:31:12 UTC</span>

<span style="font-size: 90%;">And if the user wants to run slow on purpose, that’s their prerogative</span>

**fzipitria** <span style="color: grey; font-size: 90%;">12:31:51 UTC</span>

<span style="font-size: 90%;">We need to use standard levels</span>

**fzipitria** <span style="color: grey; font-size: 90%;">12:32:05 UTC</span>

<span style="font-size: 90%;">And of course, the max debug number should be trace</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:32:25 UTC</span>

<span style="font-size: 90%;">yes, we can’t follow apache log classifications</span>

**fzipitria** <span style="color: grey; font-size: 90%;">12:32:39 UTC</span>

<span style="font-size: 90%;">That would be somewhat equivalent to the modsecurity debug level 9</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:32:43 UTC</span>

<span style="font-size: 90%;">and everything higher than 6 should be considered trace, not an exception. For compatibility</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:34:07 UTC</span>

<span style="font-size: 90%;">Ok, any other comments, or should we continue?</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:35:09 UTC</span>

<span style="font-size: 90%;">Ok, let’s move to persistence</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:35:36 UTC</span>

<span style="font-size: 90%;">This issue is linked to the new variables engines, as we need dynamic variables to support persistence</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:36:07 UTC</span>

<span style="font-size: 90%;">also, we must consider that we cannot support locking transactions while using persistent variables, as it could create deadlocks and high performance impact</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:36:53 UTC</span>

<span style="font-size: 90%;">Maybe we should just support assigning strings and mathematical operators and create update queues?</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:37:06 UTC</span>

<span style="font-size: 90%;">should we care about race conditions?</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:37:27 UTC</span>

<span style="font-size: 90%;">what’s going to be the default persistence engine? [https://github.com/dgraph-io/badger](https://github.com/dgraph-io/badger)</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:38:14 UTC</span>

<span style="font-size: 90%;">Also, should we read persistent variables in real-time or should we cache them?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">12:38:37 UTC</span>

<span style="font-size: 90%;">Ideally everything should be configurable</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:40:43 UTC</span>

<span style="font-size: 90%;">any comments on this one? it requires a lot of work</span>

**Roshan Piyush** <span style="color: grey; font-size: 90%;">12:44:00 UTC</span>

<span style="font-size: 90%;">You have mentioned everything I had in mind.</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:45:04 UTC</span>

<span style="font-size: 90%;">Ok, I will leave an open discussion: [https://github.com/corazawaf/coraza/discussions/272](https://github.com/corazawaf/coraza/discussions/272)</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:45:59 UTC</span>

<span style="font-size: 90%;">Regarding Tinygo and Yaegi compatibility</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:46:28 UTC</span>

<span style="font-size: 90%;">tinygo is interesting as it will allows us to run using WASM</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:46:44 UTC</span>

<span style="font-size: 90%;">And we need yaegi to support a traefik connector</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:46:53 UTC</span>

<span style="font-size: 90%;">I think the traefik connector would be the most popular one</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:47:42 UTC</span>

<span style="font-size: 90%;">It’s just a matter of how we organize files, I think we must rethink many packages and split into more files to create more building tags</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:48:01 UTC</span>

<span style="font-size: 90%;">for example, should each directive have a file? Should each variable have a file?</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:48:12 UTC</span>

<span style="font-size: 90%;">that way we can just disable them by marking the file with a tag: [https://kofo.dev/build-tags-in-golang](https://kofo.dev/build-tags-in-golang)</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:49:13 UTC</span>

<span style="font-size: 90%;">that’s something that can even be done for v2</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:50:19 UTC</span>

<span style="font-size: 90%;">Ok, this topic and the following topics will be handled offline:
</span>

**fzipitria** <span style="color: grey; font-size: 90%;">12:51:19 UTC</span>

<span style="font-size: 90%;">I don't think your name should be removed</span>

**fzipitria** <span style="color: grey; font-size: 90%;">12:52:00 UTC</span>

<span style="font-size: 90%;">That's not how it works</span>

**fzipitria** <span style="color: grey; font-size: 90%;">12:52:34 UTC</span>

<span style="font-size: 90%;">But we can add the project also below</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:53:14 UTC</span>

<span style="font-size: 90%;">well, that will be nice, if none has a problem with it</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:54:10 UTC</span>

<span style="font-size: 90%;">Ok so I think we are good to go, it was a fine discussion, feel free to create new issues or discussions regarding what you expect for v3</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:54:28 UTC</span>

<span style="font-size: 90%;">I think before creating the v3 branch we should consider what can be implemented in v2</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:54:35 UTC</span>

<span style="font-size: 90%;">so we avoid as many differences as we can</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:56:42 UTC</span>

<span style="font-size: 90%;">thanks everyone for joining !</span>

