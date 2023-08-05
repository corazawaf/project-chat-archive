### Wed, Mar 29th, 2023

**JC** <span style="color: grey; font-size: 90%;">12:02:04 UTC</span>

<span style="font-size: 90%;">Hi everyone, for today's meeting I would like to propose a change in the way we vote things. I believe, voting on the meeting is problematic as it assumes everyone is on the call, also delays decisions to the meeting which sometimes need to be addressed before the meeting. What I propose is that discussion can happen in the meeting but voting should happen over a GitHub issue for a week (so everyone can catch up) an then do simple majority.</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:04:35 UTC</span>

<span style="font-size: 90%;">Also I think we should release a RC2 because of the plugins api</span>

**JC** <span style="color: grey; font-size: 90%;">12:10:30 UTC</span>

<span style="font-size: 90%;">Yeah, we closed al tickets labeled as v3 as of now and thanks to _@Matteo Pace_ we have a promising list of exceptions in ftw which means that we are sooo close to the final v3.0. I would wait for a release in go-ftw and fix the issue with host in coraza to release 3.0.0-rc.2 if that makes sense.</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:11:15 UTC</span>

<span style="font-size: 90%;">_@fzipitria_ any idea if the fix is coming soon?</span>

↳ **JC** <span style="color: grey; font-size: 90%;">12:11:42 UTC</span>

<span style="font-size: 90%;">I think the fix is in place we just need a release cc _@Matteo Pace_</span>

↳ **Matteo Pace** <span style="color: grey; font-size: 90%;">12:12:09 UTC</span>

<span style="font-size: 90%;">Yep, just saw that also Felipe approved it. yay [https://github.com/coreruleset/go-ftw/pull/132](https://github.com/coreruleset/go-ftw/pull/132)</span>

**JC** <span style="color: grey; font-size: 90%;">12:11:25 UTC</span>

<span style="font-size: 90%;">I think plugins API was the last change API wise.</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:12:15 UTC</span>

<span style="font-size: 90%;">rc2 will probably be the last rc, right?</span>

**JC** <span style="color: grey; font-size: 90%;">12:12:30 UTC</span>

<span style="font-size: 90%;">I hope so.</span>

**Juan Pablo Tosso** <span style="color: grey; font-size: 90%;">12:15:43 UTC</span>

<span style="font-size: 90%;">regarding the default config, we should add commented response body processing rules and remove rules we don’t support, like: 200003, 200004, 200005</span>

↳ **JC** <span style="color: grey; font-size: 90%;">12:16:08 UTC</span>

<span style="font-size: 90%;">Please do create an issue for this.</span>

**JC** <span style="color: grey; font-size: 90%;">12:16:38 UTC</span>

<span style="font-size: 90%;">Related our branch strategy in the line of v3 I also wanted to discuss the branch naming. Right now we have v3/dev but soon we will move a trunk/master/main branch. I would like to call for a vote to see what branch name we should adopt as there is no consensus on it. I will create an issue on this but just wanted to highlight this here.</span>

**JC** <span style="color: grey; font-size: 90%;">12:46:48 UTC</span>

<span style="font-size: 90%;">Any other topic people would like to highlight?</span>

**fzipitria** <span style="color: grey; font-size: 90%;">12:58:06 UTC</span>

<span style="font-size: 90%;">Have a good time off! _@JC_</span>

