---
title        : "Shift-Right Security: Emphasizing Post-Deployment Monitoring and Response (Panel)"
track        : DevSecOps
project      : DevSecOps
type         : working-session
topics       :
featured     :
event: mini-summit
when_year    : 2023
when_month   : Oct
when_day     : Mon
when_time    : WS-15-16
hey_summit   : https://www.linkedin.com/events/7111115511110787072
session_slack:
#status: draft
description  :
banner       : https://github.com/OpenSecuritySummit/oss-website/blob/main/content/sessions/2023/mini-summits/Oct/banners/shift-right%20(1).jpg?raw=true
organizers   :
   - Dinis Cruz
   - Omer Yaron
   - Marius Poskus
  
youtube_link : https://youtu.be/FrT52Ca5bkU
zoom_link    : https://us06web.zoom.us/meeting/register/tZUkf-urrjMpGtLDM5cezDhS7ybg28mmiYdp

---


## About this session
This topic focuses on the concept of "shift-right" security, which emphasizes monitoring and response practices after the software is deployed. It examines techniques for detecting and responding to security incidents in production environments, including log analysis, anomaly detection, and incident response automation.
### Outline:
- Introduction to shift-right security and its significance in DevSecOps
- Monitoring and analyzing production logs for security insights
- Techniques for anomaly detection and behavior-based security monitoring
- Incident response automation and remediation strategies
- Collaboration between development, operations, and security teams for effective incident response

## TRanscript:
Speaker 1 - 00:00
You. Hi. Welcome to this first session of the Open Security Summit in
October 2023. We have an amazing content this week, and we're going to
start with a bang of shifting right security instead of shifting left without
going all the way to the right and emphasizing the post deployment
monitoring and response panel. So it's me, Omar and Marius. I think
maybe Omar Mario, just give a quick introduction about yourself and then
we can kick start. Right.

Speaker 2 - 00:35
So regarding incident response, I used to work at the Israeli serve the
Cyber Emergency Response Team, and we used to work for trying to
understand the apt threats and state nation kind of actors. And right now,
until recently, I was the head of research for Enzo Security, and were
acquired a few months back by SNC. So currently I'm on the SNC.

Speaker 1 - 01:17
Kind.

Speaker 2 - 01:17
Of ASPM and also risk and strategy product at Snake. So that's it.

Speaker 1 - 01:27
Cool.

Speaker 3 - 01:29
My name is Marius. I'm Vice President of Cybersecurity for Glo Financial
Services. So I essentially run the cybersecurity program for Glo. We are a
fintech business.

Speaker 1 - 01:42
Boom. Let me do a positioning here. Right. So I think there's a view, which
by the way, is correct, right? Like the sooner we do security, the best.
Right. One of the things I always like with the deployment, basically the
monitoring and incident response is that in a weird way, it's the perfect
validator for everything we do. So I'll give an example. So one of my
favorite things is to run P Three incidents. As P one, you take a mid level
incident, you run it as a P one, you put a lot of resources, you put a lot of
your team.

Speaker 1 - 02:21
And usually the reason, the business reason I say that is, for example, if we
discover a vulnerability from monitoring or we have an incident that the
customer told us about, the P One is not the particular incident, it's not
the particular fraud, it's not the particular thing that it was done at the
time. Right. Because that might be a P Three from a business point of
view. The P One is because we missed things in here. So can you guys
expand a bit on this concept of, in a way, using almost our monitoring and
our instance response as almost validators that the other security
measures that we're doing and the other areas of security that we don't
have major gaps?

Speaker 3 - 03:07
I'll start with from one particular angle. I think when you look at most of
the organizations and most of the big breaches nowadays, a lot of stuff is
happening based on and we always talk about, oh, it's because of human
error, but we never look at sort of problems upstream, why we allowed for
human to make an error, what's the root cause? And that's the problem, I
guess. Cybersecurity, I think, is still an immature program if you compare
to something like aviation and things like that, where we put a lot of
emphasis in testing to make sure that humans are less likely to make
errors. So I think we need to obviously think a bit more programmatic and
talk about and do more root cause analysis of why things are happening,
why we get incidents.

Speaker 3 - 04:04
We talk a lot about technical solutions, but what's the business processes
and procedures upstream that allows things to be missed. So I think that's
the main thing where we need to think more proactively and be more
proactive in addressing the issues. I'm a big proponent what you just
discussed. So I like to build sort of modular security pieces that anyone
who's building, whether it's infrastructure, whether they're building code,
they can reuse security pieces, whether it's what's the whitelisted image
that we use for our infrastructure machines? What? Scanning tools, what
things we need to deploy within those machines to make sure that they are
reporting. Whether it's our seam, whether it's our monitoring. The more
you can add and allow teams to leverage that, the easier life will be,
basically.

Speaker 1 - 05:02
Yeah.

Speaker 2 - 05:05
So yeah, I think there's a lot to that question and a lot to that answer also
because the thing is that application security kind of the whole space was
very changed over time. Many of the tools are also in an effort to shift left,
right the industry. And a lot of the tools wants to doesn't matter if it's tools
that run by an attacker or a pen tester or an hacker, a white attacker. So
that's one kind of thing to understand that there's always going to be
fallouts, there's always going to be missed things no matter what. And still
there are p one, p two, p three.

Speaker 2 - 05:59
But it's true that a lot of efforts of a lot of organizations also are like to
get a sense of if there's something that's like a problem that we are
proving in a specific organization might point to something. That could be
done better at the platform level or being dealt with a single time across
the board and open a real issue and solve it. And also in terms of incident
response, it's true that you want to have logs and capabilities and those
kind of elevations that you want to test. You don't want to meet with a
new kind of attack surface first time when it's a real incident. You might
want to practice and see the full kind of how do you react and see that if
you have any pitfalls or any blind spots you can fix it for the next event.

Speaker 1 - 07:03
The practice is kind of my point, right? So the idea is that instead of
waiting for the P ones and you have your dusty old playbooks that nobody
ever going to use and not have things, if you practice using those low level
incidents then you really improve your practices.

Speaker 3 - 07:23
Because I think the important bit as well in here is everyone develops a
certain level of playbooks, how do you respond to those specific scenarios?
But we all know that incidents does not always follow the playbook
scenarios. So your practice and muscle sort of memory training allows you
to better respond to various situations. And as well I think you need to sort
of look towards what culture you're building out within teams because you
don't want someone blindly following playbook if it leads down the rabbit
holes and non holes. So we build the rules for people to follow, but we
need to empower people to neglect the rules to make sure that they make
the right decisions when they need to.

Speaker 1 - 08:09
So in a way that could be a bigger incident, right? Like for example, if you
think about it, if you have a playbook and then somebody is following the
playbook blindly, you almost want to create an incident on top of that.
Because in a pragmatic way the quality of the playbook should be directly
related to the fact that when the last time it was used, it added a lot of
value and it made a lot of sense. So a good playbook in a way gets better
with every incident, right? Keeps being refined and a bad playbook is
ignored and then you know, already you answer that actually the way that
thing occurred has nothing to do with the way we thought it was going to
happen. Actually this is what happened.

Speaker 1 - 08:46
So that's why you want to capture because I view playbooks as the future
questions or the sequence of questions that you want to ask, right? This
occur, ask these five questions, get these answers, okay, that occurs, ask
these five questions. So then it's like a tree, right? A real playbook should
really be a graph. You go here, you go there and at every stage you should
have almost like okay, now I need to know this, now I need to know that.
Because incident sometimes we'll go back and say oh, actually the real
question we only ask on hour ten or day three or whatever. But actually
we should have asked that question right at the beginning. And I see that
in the incidents that we handle.

Speaker 1 - 09:25
And the reason why we put a lot of resources in the incidents is because
we build those playbooks, we build those practices and we really go from
incidents that sometimes take two or three days to incidents the same
thing takes 2 hours and is even better handled because we put all the
processes in place and the technology.

Speaker 2 - 09:43
Yeah, and I think that also it goes to the point of the changes that we used
to kind of view. A lot of it security realm was about response to events that
are the developer station or server stations and a lot of the time today the
handlers are applicative, they are a GitHub action or something like that
are developers. So there is actually a new sense of forensics for
application that most teams are not really I don't think they need to go
and kind of see lateral movement within the application, CI and so on. It's
kind of like what is the real incident response kind of job, right? The
description of that kind of who does that in the team? Is it like a dedicated
job? Is it an outside team?

Speaker 2 - 10:57
Is it like a lot of people, just when I meet them at organization, it's not
really clear because it's not like, okay, someone hacked a computer. We
know what to do. We can rotate his keys, but what keys should we rotate
this? And so there should be a playbook for those because you should kind
of with time address it enough to understand that you need to have a
playbook. And in terms of generally elevation and how you treat it, I think
at most places you consider someone who is something that was reported
externally by some whitehead hacker or some reporting tool as higher
level of incident generally rather than something was discovered internally.

Speaker 1 - 11:54
Yeah. So, Maris, let's go back to I really like that where we're going with
the whole idea asking why did the human made the error or why did the
error occur? Forgetting if it's human or not. Right. And what I like about
the shifting the right side of security is that it's very fact based. Right. In
an interesting way is the more you go to the left, the more hypothetical
you become. Yes. The more impact you can have with the change. But also
the more sometimes you don't have context where the more to the right
you are, the closer you are with something actually happened. This is data,
right?

Speaker 1 - 12:29
So if you look at that, why the error occurred, that visibility and that
instance response, in a way, those are the signals that we should be
exploring to understand why do we got lucky, right? It's a bit like, hey, we
just found some malicious guy inside our building. He happened to be
making coffee. It's like in the coffee machine or helping himself to the
snacks. But if that person had walked to the right instead to the left, you'd
have found our vault. Now, usually we'll go and says, oh, no problem,
because the only thing you were doing was eating some snacks. But I think
we should go. How is it even possible that person, for example, bypassed a
bunch of controls to allow them to be in that part of the building?

Speaker 1 - 13:19
My key point here is that let's do that when we're not in a mission critical
situation where we're facing with a massive advanced attack that will
respond and we don't have a lot of margin for error, let's do that a bit
sooner when we get those signals that told us something wrong happened.

Speaker 3 - 13:37
There's a thing I think sometimes we need to be proactive and go into
deeper levels understanding our staff potentially attackers psychology.
When I talked about, for example, stuff like human error. So we're talking
about, for example, simple example, phishing. Why people click on
phishing links. Nobody looks at how many emails do people need to open
per day? Is it their job for example, to open attachments? Like invoices if
that's their job, opening those emails. Twenty four, seven or say whatever,
eight or five. Every single day they need to open 200 emails. It's very
unlikely that they will always going to spot a phishing attack. So you're
relying on that person who's the last line of defense. So how we can help
them, whether it's end user awareness training, whether it's tools,
understanding motivations. Why, for example, something like MGM
account hack.

Speaker 3 - 14:39
Why does people divulge their credentials? What's the culture we are
building in a team? Are people disgruntled? Are they not happy? What
could lead to inside their attack?

Speaker 1 - 14:54
But I think it's more interesting to think, let's assume that they will do it,
right? Let's assume they will click, let's assume that they will diverse their
credentials. In a weird way, it's almost like a honeypot, right? I view that
as I'm more worried by the fact that why didn't we pick up that something
bad happened? Why didn't we pick up that the next thing that the
attackers did? Because I love the statement of a zero day is not an
invisibility cloak, right? Like, okay, you click on the link, but that doesn't
make the attacker invisible. If anything, all the other actions are visible
and we should have enough process systems, understanding, visualizations
right, to detect that, hey, this just happened, right? That installer just got
executed. That credential just got compromised over here.

Speaker 1 - 15:45
And we should have, again, the whole not the bandwagon, but the zero
trust model where suddenly if you're trying to access highly sensitive data
from a device that we don't recognize, we should go, hold on. That should
not be possible.

Speaker 3 - 15:59
And I think it leads to I even made a post today, I asked a couple of weeks
ago about cybersecurity professionals. What's your non negotiables when
you step into a new role? And normally we start talking people MFA, how
to protect credentials and users and user awareness training and all of
that. That is all great. But I think most organizations, what they lack is
asset management and visibility into all of the assets. So if you're missing
10% of your assets, yeah, it doesn't matter what you're going to do, it
doesn't matter what controls you're going to apply. If you can't see 10% of
your assets, how they are configured, whether they are hardened, that
talks into visibility. Because the thing is, and the problem.

Speaker 1 - 16:38
Is that's how I do it. So if I have anything related to a device that we don't
manage, I raise that as a P one. Because I'm like, we just got an
unmanaged device that we had no idea where it came from, but we know
it's ours or we know it's part of our domain. Right. So for me that's the P
one, but ideally you want to almost edge your luck to say, let's have those
before it's the big one. Because guess what? Doing normal business
development, people would do things that are the same. They're not
malicious, but they will be doing things from unmanaged devices that we
go, oh, that's a bit fishy. Exactly.

Speaker 3 - 17:15
And that's the thing. Not having visibility, you can't detect things. So
making sure you have a proper asset management and then you build on
that. You build how you on board assets, how you gain visibility and shift
towards that. Right. To make sure that you have that monitoring in place,
you have detection, you keep training and going through scenarios. I
always say to people, failing to prepare equals to slowly failing to prepare.

Speaker 1 - 17:43
Yeah, exactly. Well, let's bring Nitin a little bit because I think he asked a
really good question.

Speaker 4 - 17:52
Hi Denise. Hey Marius. Hello Mar. I had a question for you.

Speaker 1 - 17:58
Right.

Speaker 4 - 17:58
So as we look at the incident side of it, would love to get on your thoughts
on with the incidents which are happening. How are you encouraging your
teams? And it could be the AppSec team, it could be the development
teams, it could be others to learn from that. So say for example, as part of
an incident and a few of these which have happened recently, where there
was like a code related bug or there was like secrets related bugs which
were there.

Speaker 1 - 18:27
Right.

Speaker 4 - 18:28
How are you now taking those learnings and saying, hey, I could have
stopped this if I go and make a slight change earlier in the process. So
maybe as part of my SAS scanning, maybe as part of my secrets or other
things that I'm doing earlier in the development cycle so that I can now
kind of reduce the impact of this vulnerability class. So I'm just going to
pause there, see if there's any if that question makes sense.

Speaker 3 - 18:58
Yeah, I think for me personally, I always think about any particular
security initiatives. It starts with top down approach. So whether you start
launching AppSec, program, vulnerability management program, any kind
of program where you're trying to get better maturity and discover things,
it's how does the roll down from the top? How are they supported?
Because everyone's talking about nowadays AppSec DevSecOps, but
normally it's still siloed. You have a DevOps and then, oh, let's bolt on
security on a DevOps and it's all of a sudden it's going to become
DevSecOps. And I always say to people, if you truly want to reach
DevSecOps, it takes at least twelve to 18 months to build a culture, to
build the Security Champions Network. How are you going to incentivize
those security champions? That's the one thing I think some organizations
always miss.

Speaker 3 - 19:53
We always talk security is sort of a measurement of quality of the code. So
if you can build security and quality into development, KPIs build Security
Champions Network how you can incentivize them through whether it's
gift cards, money, security conferences. When you start talking and start
understanding developers, pick anything that for example, developers that
missed in a code. If you can showcase a high breach of the missed code
and how does that help businesses to reduce the potential spend? Save on
bottom line, save the bugs. We're always talking about shifting left
because production bugs fixes is normally ten times the cost if you can fix
them in a sort of threat modeling exercises. So just grasping that
understanding and why we're doing things, because normally developers,
they get a ticket in their, say, jira fix that bug, they don't have a context.

Speaker 3 - 20:56
So for them, it doesn't mean nothing, yes, I'll fix it, but what's the
concept? What's the outcome of that bug if it goes into production and
then the learning curve, because once they learned the outcome, that can
happen, what's the risk? But chances are you won't see that same bug
from the same team next time. So to me, that's how you go about it.

Speaker 2 - 21:22
It's a good question, and for me, it's a lot of to do with confidence of the
developers in the tools and in the responses they get. And right now, I don't
think that as a whole, as a field application security gives a lot of
confidence in findings and we need to do a lot better. And a lot of the
things that goes there, it's really important that they'll be discussed
because it's a fine line of agreement and kind of acceptance between right
security and the RND, and we can tone those knobs to fit it better. And so
if it's transparent, what do I mean by that? So a lot of the times tools are
reporting false positives, and we want the developers to understand what
are the efforts that we add to the tools to not let that interfere, right.

Speaker 2 - 22:28
To kind of overcome it. Okay. And if they are persuaded, it has like two
meanings. First, that they understand that it's something that they need to
deal with and that it's real, hopefully. And two, that they can maybe
suggest things and they have a lot of more knowledge as to what can be
automatically signed as a mock or a test or whatever and build more
confidence in the findings. But still, I think reproducibility for me when I
was developing, when you have a bug, a state of the task could be cannot
reproduce, and that's it. So I don't believe in giving developers bugs that
they cannot reproduce because they either won't fix it or they won't fix it,
right. Because they can debug it and they can understand it.

Speaker 1 - 23:29
Okay. But if you look at the case that Nathan was mentioning, in a way
that solves the false positive because it is a true positive, right. Like, we
know it's been exploited and we know it's connected an incident, right?
So, Nathan, one of the reasons why I do put a treaty as a P one is because
you need the development resources. You see, the problem is, when you
treat it as a normal incidence, the objective is let's reduce, I would say, the
impact of the bug, right? And usually it's about stop the exploit, do
something about it, plug the hole, right? Get it there, right. In a lot of
cases, that could be done reasonably quickly, right? Because it's almost
there's a signal, right.

Speaker 1 - 24:14
There's something that you can do very quickly that would, if not solve the
vulnerability, broke the path, the attack path, right. The reason why you
kind of want to run it as a bigger incident is because you need the
resources to do what Omera was talking about, which is, let's make sure
that we connect the dots, right? So it's not a false positive. So, for
example, write a unit test, write integration tests. Write something that
replicates the problem. So when you go to the devs and you say, hey, guys,
we need to fix this, right? It's actually a real exploitable path in their
environment.

Speaker 1 - 24:52
And then if we then have the horsepower and that's why it's important to
bring people to the party, because you want to look at what other bugs
you have that are similar to this, and then what other near misses you
have. And the beauty of that is that you can take those maybe mid level
findings or findings that were in that category of going, we don't know, or
no exploit being published, et cetera, or no exploitability right now. And
you can flip all of them and going, oh, by the way, we now have evidence
that this has been exploited, right? And then you can use that to try to fix a
lot of things. But I would also argue that fix things during the incident.

Speaker 3 - 25:35
I'm great fan of chaos engineering. And then you can flip and keep going,
and iterating forward. That's why I said top down support. Imagine you
get top down support. So, say, let's do a week CTF. All the teams switch,
all the dev teams. You try and find bugs in another team's code, and you
just do a full week CTF.

Speaker 1 - 25:58
Imagine, but do it on top of this incident. Man. The thing about that, right,
what I found is that there's a connection, there's a human connection
incidents not just to that, but to kind of everything around it that doesn't
exist when it's artificial, right? And that's why if you do a tabletop exercise
or by the way, CTFs is brilliant. I'm not saying don't do that. I'm just
saying that the scenario that Nathan was talking about, which is on the
top of a real incident, there's a whole almost blast radius that you can
leverage. And at that moment in time, you know, my trick, Nathan, is to
find the spots that we don't have good answers. If you especially during an
incident, there's always a nebula period.

Speaker 1 - 26:46
And what you'll find is that very quickly people move into the let's address
the problem, not why is this a problem? Right. So it's almost like it's not
just like imagine there's the little dot that you got to hit, but there's also a
blast radius that you can now exploit, right, to say, let's say, for example,
as a vulnerability on a website that allows you to read data from the
server, right. Then you can say, okay, so in principle, all the secrets could
be compromised. Right? Now don't wait for evidence that the secrets have
been compromised because nobody's going to argue, especially if you
haven't. First of all, there could be a real scenario, but more importantly,
nobody's going to argue that it's not valid because there's now a path. We
got somebody that was browsing the directory structure. The data was
there.

Speaker 1 - 27:37
The fact that the person has, wear it or not, is less important than let's
minimize the impact of this. So suddenly you raise the questions, why do
we have secrets in the source code? So suddenly you can have the teams
have a lot more empathy to all the tickets that talk about secrets in source
code. Because you go, see guys, that's why we worry about that. So then
instance like this, it's not a problem. Then you look, why is that container
running as root? Or why is that container overprivileged? Or why is that
not locked down as much as we could? Because if it was, none of these
problems would exist.

Speaker 3 - 28:14
Yeah, and you can keep digging deeper and then that's how you build
secure processes going forward. Why did it slip into the repository? Why
do we have secrets there?

Speaker 4 - 28:28
Yeah, I've seen one organization use the five wise. So let's say there was
some obscure it's a niche bug like related to access control or user
authorization. So now what you do is you look at that and then you say,
hey, how do we go and check? Because developers tend to leverage each
other's code. How do we go and check which are the other 1520 other
places where the same issue has happened? And now on the back of the
incident that you have, you can now give visibility to those developers in
terms of, hey, because of this one thing, think about these other 20 places
where the same issue is happening.

Speaker 4 - 29:10
And because you've got the leverage from this incident, you could actually
go ahead and either get them to, of course, fix it, as Dennis said, plug the
hole, but also say, hey, how do I check for the next time that this 21st place
does not happen?

Speaker 1 - 29:23
Yeah. So now let me bring my favorite topic, right? Which is this is the
moment of the conversation that I always got a little bit depressed, right?
Not visibly, but if my heart a little bit will die because I knew that we
couldn't scale, we couldn't do what you just described, right? Because to
do what you just described required us to be able to have a level of
understanding of code. Let me rewrite this. For that to be possible, we
would need to be able to take that incident, take a particular app, a
particular environment, a particular development, particular code base,
and write that incident translated for that environment. Right. Now, up
until recently, for me, that was impossible. You couldn't do it right. We
tried. Or you needed a huge amount of human power, which again, didn't
scale at all.

Speaker 1 - 30:12
So this is the area where I think Gen AI will make the crazy difference,
right? It's not on the writing stuff automatically, it's not on replacing
humans, it's not on writing code, all that stuff that people get very hyped
about. I think it's the ability to write messages or to explain what we want
in context and have an event where, let's say if I take your, you know,
nithyan the workflow where you go, you feed the bot and say, look, Chat
GPT, I say, look, this just happened. Here's the impact. Now I'm going to
speak to this team and that team has this and this and these findings. Now
explain to me or explain that team the impact of this. And that's massive
because we're now translating this into business context.

Speaker 1 - 31:04
And that is the kind of things that actually Chat DBT does really well. So
what do you think of that?

Speaker 2 - 31:13
Hang on, I'm saying a lot of now those talk about moving from
vulnerability management to risk management. And that's basically the
idea of getting the context for every environment. Because if someone
broke your staging environment, which you have mock data, then okay, I
guess it's nice, but if it's production with PII data of customers, then it's
very different. Shifting left gave us a lot of understanding around the team
and around the code. And if you go to, like, you now have swagger that
might describe your API, or protobuff that might describe clients and APIs
very clearly, but tying it together with where everything is deployed is kind
of going to be, I think, the golden standard for understanding your risk for
every kind of issue or incident.

Speaker 1 - 32:22
Yeah. What do you guys think? Myers gen AI for this.

Speaker 3 - 32:28
I think Genai has obviously its applications, I think is obviously just as
with anything else. It depends how you build the model and what data you
use. If you have enough data, enough context, and enough sort of data
points to leverage it. Yeah, it's great.

Speaker 1 - 32:47
In this case, we do, right, because we have the incident, we know the team
is going well. We might even have the vulnerabilities that exist on that. You
can even throw in some of your policies. So. You can now build a coherent
narrative, even to do list, right. For one is to happen, but you can now
build almost like the whole project description, why are we doing this?
What's the business impact, what's the risk impact, what's the technical
resources, what to do, et cetera, all based on that piece of evidence and
that particular event, which in this case, again, is what Nitin was talking
about.

Speaker 3 - 33:23
Yeah, because it will allow us to better correlate events, to better
understand how does that, as Nitin said, or as we discussed, how does that
one thing impact everything else around, where let's scan all the code,
where there is duplications of that potential problem. And let's do a nice
summary for me, because instead of creating lists and lists of lists, how do
we risk over it and what do we really care? Because I think the one thing
that historically insecurity, we've been kind of problematic with know, we
find hundreds and hundreds of issues and then we shout to everyone, oh,
we need to fix everything. We need to fix everything.

Speaker 1 - 34:03
We need context, right?

Speaker 3 - 34:04
Impossible. Yeah.

Speaker 1 - 34:06
So actually, Michael, can you join in? So Mike Hidalgo here, and we go
back quite a long time, and he's also very heavily involved in threat
modeling. And actually, I was listening to Gary's McGraw, one of the
recent podcasts, and one of the things he said was one unsolved problems
is scaling threat modeling, right, is how to scale. And I think if you connect
to this again, one of the problems we always had in the past was how do
we have good data and how do you create threat models in context where
in a way, imagine if a thread model is now dynamically generated from
data. It means that when the scenario that Nitin is talking about,
something just happens, we can now connect. That right.

Speaker 1 - 34:50
So we can start to have these threat models that feed from context
analysis of an architecture that has already been created by an LLM.
Right? But then the thread modeling itself can be dynamically generated
or updated as events occur.

Speaker 3 - 35:06
Yeah, that's true.

Speaker 5 - 35:07
I was thinking when you mentioned AI for this, definitely a really nice Use
case is really threat modeling, where you can have all of this data
populated from multiple places. That can help you even to brainstorm.

Speaker 1 - 35:22
Right.

Speaker 5 - 35:23
Because at the end of the day, threat modeling is about collaboration,
right. So if you are able to ask the right questions to the right problem,
maybe you can work backwards from a given incident right, to try to find,
oh, this is the use case I do have, what are my potential threats? How can
I improve this? How can you go from the detection to the prevention? So
this is really a game changer. Specifically, as you wanted to scale right
across multiple teams.

Speaker 1 - 35:48
Now you can translate the thread model to all sorts of different audiences,
right? Imagine the thread model as the foundational graph. In fact, I
always found that the challenge with thread model was either non fisibility
or too much visibility, non f granularity, too much granularity, right. Where
now you almost can have these foundational thread models and then we
actually use an LLM to translate that to a particular audience. So you can
have context whether you can have your findings, you can have your
vulnerabilities, your exploits, where your monitoring then becomes a key
piece of that because it gives you almost the evidence that whatever we're
seeing on the left, actually there's the impacts on the right.

Speaker 5 - 36:30
Yeah, absolutely. And also as a second opinion, right. Specifically in terms
of threat model, where you need several feedback loops, right, and you
need to have more people involved asking the right questions. These kind
of models can give you a lot of visibility, things that you are not even
considering when looking through the eyes from the detective perspective.

Speaker 1 - 36:51
And I always think the view that especially in this bit here, it's not about
the gen AI and the LLMs, right, to replace the whole lot. Right. It's about
augmenting our capabilities. So, for example, in the past, the best, most
effective threat models experience I had was my team was creating threat
models, and I was almost just reviewing it. And I would be able to be very
productive because I was able to see which teams actually were doing
okay, which teams were not even on a ballpark, like, which ones have no
idea where they were looking at, and which teams actually went over the
top. But also I noticed I was being very productive because I could use my
experience, I could teach others and then I would review it. Right.

Speaker 1 - 37:32
At the end of the day, you always need somebody as an expertise to sign it
off. But the ability the problem in that world was then the cost of creating
the new versions was very high. So things became out of date. We could
change that. Yeah.

Speaker 5 - 37:50
And even get maturity. Right. You get to that stage faster.

Speaker 1 - 37:55
Right.

Speaker 3 - 37:55
With the right tools, especially, I think you can take it up to the next level.
We're talking a lot about technical stuff, but when you create a tools that
based on gen AI, who can take and analyze specific, whether it's
procedure flow, specific architecture flow, you can expand to nontechnical
teams.

Speaker 1 - 38:14
Absolutely.

Speaker 3 - 38:14
Imagine some of your nontechnical teams start building a specific business
procedure, specifically business workflow, new product, before they even
go into the technical routes. They can get the early outputs of where the
potential risks and dangers lie to make the informed decisions as early as
possible. And that's, I think, to me is invaluable.

Speaker 1 - 38:34
But that was always the elephant in the room of thread modeling. Right.
In another world, we could have been a lot more brutal with the dev teams
and saying, dude, you don't have an architecture diagram that isn't up to
date. Like, what the fuck? Right? Like, come on, seriously. Right? But we
can't say that, right? And to be honest, the system is rigged against the
devs and the architects. So it's not their fault. But it's insane. Right? It's
like, imagine you're doing a security review of a building and you go, okay,
can you give me the schematics? And they go, yeah, we don't have it. Well,
I can draw you how the building works, I can give you a drawing of where
the doors are, how you go in, where the vault is. Right. But it's insane,
right?

Speaker 1 - 39:12
The application, the networks, the cloud environments, nobody
understands how the hell that thing is set up these days. Right?

Speaker 2 - 39:20
Yeah. So threat modeling really part of it. I think usage should be kind of
sometimes the first place that everything comes together in a single review
of flows instead of like, I don't know, APIs review and stuff like that. So in
that essence, a lot of the time we don't save like I see a lot of teams that
uses to do threat modeling and then it archived somewhere and no one
sees it. And that should be validated the next time there's an incident.
Should be validated against the last. Exactly understand why it didn't
come. And also we live in an agile world where APIs are not static and
they're changing. And some changes should require have another security
look and some doesn't.

Speaker 1 - 40:14
So you just touch a topic that I would love if we became more real is new
stuff should be an incident. So for example, if you have a new API that just
popped up that nobody knew about, that should be an incident.

Speaker 2 - 40:28
Yeah, because back to risk and the ability to have some kind of a priority
because there are some things that you would want to set that knob very
high if it's PCI related.

Speaker 1 - 40:42
Exactly, right. That's the thing. So monitoring gives you that. So if you
think about it, monitoring is our I think when you guys just mentioned it
should be the validation of all our understanding.

Speaker 2 - 40:56
You need to have a policy regardless of what you currently have. You need
to know what you want as an organization to say like, you know, that I
don't know, you cannot accept whatever, something that doesn't have a
second review or not. And then you go and check what is the status if
something is violating it or not. But we need to understand what the
organization need to have a policy what should go under review or not.
Regardless if he have one single review member, like one single
application security in his organization or not, he needs to know, does he
want a security review?

Speaker 1 - 41:39
A really cool project to do would be to use LLM to write the policies of
what happens today. Like for example, imagine reverse engineering your
existing policies from what you see in your monitoring and instance
response because that's real data, right? So for example, you say we have
a policy that things don't get reviewed. We could say actually, your policy
should say actually, your policy should actually say, we don't review code
before it goes live. Or we don't review.

Speaker 2 - 42:15
That'S where your controls should be. That's how you should set well,
number.

Speaker 1 - 42:20
What? I'm saying is that we could be a bit passive aggressive here by
creating policies that when you read it, you're going, well, I'm not
comfortable with this policy.

Speaker 3 - 42:27
And I think one thing that we very rarely talk about, and I think the more
I've been digging into it so normally in organization who develops policies,
GRC department.

Speaker 1 - 42:38
Oh, yeah.

Speaker 3 - 42:39
Who has to follow is engineering and does GRC know how engineering
there's people who creating policies who have no clue.

Speaker 1 - 42:51
What exceptions you need the connection again, that's where I feel again,
Genai can make a massive difference is connecting basically a policy
which fundamentally is a risk based or how we want to behave with
reality. In fact the policy should be a graph, right?

Speaker 2 - 43:09
Translating policy into actions yes, but more importantly connect them.

Speaker 1 - 43:14
So it should be a graph, right? So you should be able to look at imagine
being able to look at a policy and say, that policy is currently no enforced.

Speaker 2 - 43:21
Yeah, because normally what you have and here it applies, but it's broken,
because.

Speaker 3 - 43:28
Normally what you have is you create a set of policies, and policies are
reviewed by senior leadership who has no clue what these policies mean.

Speaker 1 - 43:35
But even when they do right, the problem is enforcement, right?

Speaker 3 - 43:37
Yeah but as I'm saying, you need people who actually so say if I'm writing
secure software development policy, I need an output of all the software
development teams to make sure that it aligns to their day to day work.

Speaker 1 - 43:49
So I then I'll try to be passive aggressive in saying I've done things in the
past, I say that policy is not forcible that policy today is completely so
we're breaking that policy left, right and center and here's a risk for you
to accept. So now your choice is you either change the policy or you
accept that it's completely broken and there's no way you can do it in the
next year. So that's again, how you can bring the responsibility of people
signing up the policy to say you shouldn't be signing up a policy that
actually has no chance in hell to being usable.

Speaker 1 - 44:21
Right, but the problem I always had again in the past is that you don't
need one policy if you think about it, right, you need ten, 5100, 200
versions of that policy because you need that policy adapted to that team,
to that environment, to that situation. See that's the important thing and
that's where we always failed because there was no way around it because
you either had a policy that was small, effective, easy to understand, but
not specific. Or you had crazy specificity to cover all the edge cases, but
then nobody could consume it.

Speaker 3 - 44:55
Yeah, but that's why if you do specific, you should never put it in a policy. I
think that's why you need to have sort of a governance structure. You have
a policy that's very non specific. Your policy shouldn't change over number
of years.

Speaker 1 - 45:06
I agree. Well, yes or no, right? Yes, the top one shouldn't. But you need to
translate what that policy means to that team, if you think about it. So
that means you need a custom version of a policy for a team, for a culture,
for an environment, even for a language that they speak, in fact, even not
just speaking language, for particular languages. Right?

Speaker 3 - 45:28
Yeah, but that's what I'm saying then I don't think it sits within the
programming language. Whether it's standard, whether it's guideline. The
overarching policy should be highly generic because you never put say, oh,
we use AES 256 in a policy.

Speaker 1 - 45:41
Yeah, but then is to connect down. Right. So again, if you look at the
policy says you should use encryption, they say on here, union needs to
translate that policy to say, for example, if you use this framework, the
policy will say implement, use native encryption functions, that's it or
others use this particular framework. Others, you have to write your own
good luck. Right. Or anything you do here needs to be code review. Right,
but that's, I think where it failed all this because we didn't have the
manpower to create that translation.

Speaker 2 - 46:14
So I think this goes generally to development and not specifically to
security. And this is why we see a lot of backstage and developers portals
is now a big things because it's hard to maintain all of that framework
kind of changes across multiple teams and security needs to be part of this
adoption of developers and suite. I know that there are efforts to do add
all of the security that currently is available to as plugins for those
platforms.

Speaker 1 - 47:02
Right. Guys, we almost of the hour last minute. Any final thoughts?
Mario? Michael omer. Any final comments?

Speaker 3 - 47:10
I think we kind of discussed a lot of things within shifting right. I think the
key goal in shifting right and understanding monitoring in response of it is
having the visibility into your assets and having visibility into the
monitoring because obviously you can't respond to something that you
can't see. And then we discussed building muscle memory and practicing
scenarios to understand the root cause and look at the incidents
downstream and continually reengineering your playbooks to inform the
future paths and future succession is key into our sort of environment. So I
guess that's sort of the main things that we should take forward.

Speaker 2 - 48:10
Yeah, I'd say that generally the entire industry of application security has
to do a lot and to come up with some better tooling to allow a lot of the
testament that we want, but that we want to have to issues that we find
from right to left, wherever. But when we come to the entire part of
security grown in shift left and can attribute a lot of information, but it's
now lacking the kind of right context for that information that we should
get from shift right. And also that everything needs to be treated as a
whole. So you have to understand how any incident, you can't just resolve
it. You need to go back and understand how it relates to practices, how it
relates to current tooling. It's not just something to fix and forget and you
should leverage it wherever you can.

Speaker 1 - 49:20
My point is that I do that during incident because it's when there's a lot of
energy on it. And I feel that my last thought for me is that I think Gen AI is
going to allow us to connect those dots in a way that before was just
impossible. Allow us to create context of context all verified by humans, of
course, but allow us to have a scalability level that we can never before.
Great, guys. Well, this went really fast. It's really cool. Okay, another topic
and I see you guys in the next sessions.

Speaker 3 - 49:48
Yes, see you. Thank you.
