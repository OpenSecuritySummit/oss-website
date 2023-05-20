---
title        : ChatGPT impact on Cyber and Application Security (Panel)
track        :
type         : working-session
topics       :
featured     :
event        : mini-summit
when_year    : 2023
when_month   : Apr
when_day     : Thu
when_time    : WS-15-16
hey_summit   : https://us06web.zoom.us/meeting/register/tZ0vcOCurjkvGdC6Zcca0TAt1WFKg4-ZKYXZ
session_slack:
#status       : draft
description  :
banner       : https://github.com/OpenSecuritySummit/oss-website/blob/main/content/sessions/2023/mini-summits/Apr/Chat%20GPT%20Impact.jpg?raw=true
organizers   :
    - Dinis Cruz 
    - Nathan Case
youtube_link : https://youtu.be/HxGBKlaXOEw
zoom_link    : https://us06web.zoom.us/meeting/register/tZ0vcOCurjkvGdC6Zcca0TAt1WFKg4-ZKYXZ
---

## Session Transcript:

Dinis Cruz - 00:02
Hi. Welcome to the Open Security Summit session in April 2023. This is a
very topical topic because it's about Chatgpt impact on cyber and
application security. We have a great set of panels. Dennis. I run the open
security summit. I'm the Cecil of Honor Barrett and the chief scientist of
Glasswall. Sam, we can do by you.

Sam Stepanyan - 00:25
Yeah, I'm Sam Stepanyan. By day. I'm an independent application security
consultant, but also volunteer as OAS planted chapter leader for the past
seven years. I also a project co leader on two of OAS projects, OAS
Network and Oasp WAF evaluation criteria. I made numerous
contributions to OAS, including Oasp Zap and Oasp Top Ten. So that's
me.

Dinis Cruz - 00:50
Maybe. Nathan.

Nathan Case - 00:52
Hi, I'm Nathan Case. I am a security advocate for datadog. I spend most
of my day talking about security geeky stuff. This is about as geeky as it
gets right now. I'm really excited to have this talk. I am decidedly far more
on the security side than the AI side, so I'm excited to see where this goes.
Obviously, views I express are my own, not data dogs.

Dinis Cruz - 01:12
Exactly. Scott?

Scott Katie - 01:15
Scott katie. Longtime application security practitioner, enterprise
architect. Just starting the journey into, like, AI type activities, but been
following kind of Gary McGraw with machine learning. Been part of OS
for quite a while. That's an interesting topic, taking Open and pulling it
into Chat GPT to kind of help provide more information to people and
how you validate that.

Sam Stepanyan - 01:45
Right.

Scott Katie - 01:47
So I'm real interested in the topic. Happy to contribute. Have to drop it
half past.

Dinis Cruz - 01:54
That'S. All right. I think what we could do is let's stay away from the
whole privacy feeding data to the models thing, because let's kind of
assume that these versions and the next versions, for example, are the
models will have solved that people will be able to create models on top of
private data. People will create models on top of things that let's not look
at even again, some of the poisoning of the models, because I do feel that
there's an area here which is the people who control the models can
actually do a lot of stuff, including to identify malicious access, et cetera.
And we know part of that. Right. Why don't we start with, in a way, what
is the big difference with, I would say, the GPT, the Chat GPT like
technologies and the AIS that came before. Right. I'll add that for me, it
was context.

Dinis Cruz - 02:52
It was the ability to have a dialogue, was the ability to express what I want
instead of reverse engineering what I want into a Google search and then
go and hunt for articles that kind of have what I want and then find
almost like 80% of what I want and then start to start again. Right. So,
for me, it was that Iron Man Jarvis kind of dialogue that I never really had
before with anything that was AI specific. What about you guys say?

Scott Katie - 03:26
Yeah, it was getting back, asking a question, getting a single answer
composed from multiple search results instead of a list of search results
that then you had to dig into, because then you dug into them and you
went on long trails, so you didn't get the, I would say, context and
conciseness.

Nathan Case - 03:44
Well, and I would go so far as to posit. This is one of the first times I'm
going to go back and give you a memory that I have of five years ago,
speaking to a security vendor that was telling me about his wonderful AI
product. We talked about it and the more discussion we got into it, I was
like, well, you're just doing this huge if then else a thing that's not really
like machine learning or AI. That's just a really big if then statement,
which cool, but not really what we're talking about here. I think this is the
first time we've actually been able to say it's contextual, it understands,
it's able to search on general words and sentiment that you give it and
then give you back. Reasonable results, though how reasonable becomes a
question of how well it's been trained.

Sam Stepanyan - 04:32
Yeah, and from my side, I think I was mostly impressed, of course, with the
fact that it understands code, it writes code, and of course, one of the
topics we're going to discuss today, it actually remediates the
vulnerabilities in the code. This was my big revelation, kind of exactly with
a pinch of salt. The fact is that, again, because we created a lot of content
over the past 20 years and a lot of people complain it's quite difficult to
navigate this content. If you just go to a search engine like Google and you
ask about vulnerability, you're going to get thousands, if not hundreds of
thousands of responses. Depending on what you click and you read those
pages, you will still not understand what's going on. I think that's the
ability to get this summary. There's even a way to ask Chat GPT to explain
a vulnerability like you are a five year old or if you are an eight year old,
which I think is quite unique.

Sam Stepanyan - 05:32
This is something what we didn't have even though AI was in security for a
long time. But, yeah, I think every single SaaS vendor which claimed that
they have AI, I've never actually seen it successfully applied until now, that
we're seeing in Chat GPD, which I think is probably going to affect a lot
of SaaS vendors well, because of the topics we're going to discuss next.

Dinis Cruz - 05:55
Well, I think every single SaaS vendor should be on the work processing
because their whole business could disappear, right. As soon as somebody
integrates equivalent Chat TPT like models. Because if I can go to the
point, in fact, I haven't fully tested yet. The latest version of Copilots, I
don't know if you guys used it, but the latest version of Copilot actually
claims to actually look at the whole code. Have you guys seen that one?
GitHub copilot, right. The first version was which is already pretty
spectacular, I have to say, right. It already was really good at creating
really good recommendations. The new version apparently I haven't tested
because I don't think they have fully released it actually claims to look at
the whole code, including writing unit tests. With the whole coding context
now from there to actually finding all class of security vulnerabilities and
connect all sorts of stuff, that far, right?

Dinis Cruz - 06:55
It's almost a darker heavy lifting to be able to do that, man.

Nathan Case - 06:59
It's an interesting question. Can you ask your chat GPT to create you a
framework by which you can complete your code quicker? I mean, dude, I
can think of all of the things that I've had to code in my lifetime and the
amount of code that I've written that was just, gee, does this work? To get
past that section and go right to the, well, this is perfect. We have a hard
enough time getting people to evaluate should I actually do this, that or
the other, or evaluate variables as they go into code. It's a little scary
because there's some level of discipline that you have to make sure that is
actually enacted here.

Dinis Cruz - 07:34
Think of the questions you can ask, right? If I go back to my old two
platform days, right, I still feel that I was doing stuff that today people still
don't do, right? The way I got crazy success was by imagine this on a
SaaS engine, right? I got to the point where I would delete all the rules
from the database. I had access to one of the engines, right? I would
create a call graph of everything. I would taint every entry point and
external point. I would get millions of traces, literally millions of traces.
The beauty of that is that I will spend some time mapping the inputs and
the outputs, and then I have this almost real time view where the data
arrived and the ability I then have to really very quickly say, I care about
that. I care about that. I don't trust this and even to say, okay, so this XML
file contains the glue between these web service and now web service
there.

Dinis Cruz - 08:25
So you go like that. You go to the database and you come like that. So
create those trees. That context, which is really what advanced static
analysis can actually give you. That's kind of how you really can do this.
My problem was I couldn't describe the model right now, I still am getting
to the point where I could start to describe the behavior that I want for the
Web services, the behavior that you want for all these things. And that's a
game changer.

Nathan Case - 08:51
I think it's interesting to be able to say like this, well, if you.

Scott Katie - 08:56
Can create the pattern, then you can take a large code base and boil it
down to what fits the pattern and what doesn't, and then focus on what
doesn't, right? So you can apply that to MIT. You can apply it to testing
security, testing even stuff like code, like checking in comments and having
a consistent framework for that where people might not even put that in.
If you could generate comments from code that's written, hey, that's a
really big game changer, because every developer, that saves, like, a half
hour of time, right? If you have a security researcher looking through that,
instead of maybe I have to switch from one code to another and learn, I
can just reach through the comments and find the pattern that doesn't fit,
that's a really good use of it. It'll save time.

Dinis Cruz - 09:45
What I really like is that it really now aligns security with engineering. I
think there was a trend with engineering where we kind of threw with the
baby with the bathwater by saying, you don't need architecture diagrams.
What you need is quick iteration. Documentation is not that important.
Yeah, everybody wants it, but nobody seems to have the time to do it,
right? To be able to start to describe the code, like, for example, a threat
modeling session, 90% of the threat modeling is just getting a freaking
decent architectural diagram. Once you have it, you find the threads left,
right, and center, right? Imagine being able to be programmatically
created. Imagine taking a code based and saying, hey, give me an
architecture diagram of this. Describe me this code in, UML, give me a dot
version of this code at this level of abstraction, right? That would be
massive.

Nathan Case - 10:31
But that's the issue, though, right? You have to trust the process by which
it was created. That's really what I'm getting at, is how do we evaluate
that trust?

Dinis Cruz - 10:41
Because real world comes into play. I don't have a problem with changing
between mistakes because I catch them, right? Like, the dude f******
makes up s***, right? That's fine. In a way, I just love the fact when he
makes a mistake in the first answer and you correct and you go, oh, yeah,
you're right.

Nathan Case - 10:57
I think that's the key point right there.

Dinis Cruz - 11:01
This is an existing vacuum. So, for example, even those recommendations,
even that stuff, you have feedback loops, right? In fact, you can even have
another engine mapping up the feedback loop, so you can even use the
output of one as a prompt to the next one, right? We're now operating at a
much more efficient level. Before you had to find the people who
understand the code to describe what the h*** that meant, right. Even,
like, the legacy stuff, right? Most developers didn't write the original code,
so they don't f****** understand it. Right. To be able to say, this is how we
believe it works, then reality come into play. You can even say, Here are
the logs, right? Can you match these logs with the architecture? Or Find
me all the places where these logs that I know for real are being invoked?
Match this architecture.

Dinis Cruz - 11:48
That was a question that before would be impossible on us to ask, right?
Yeah. Now we're not far off to Nathan.

Scott Katie - 11:56
Your point about creating a framework and then you go code, maybe take
the code and put it in a framework.

Nathan Case - 12:02
You can evaluate, which is cool, which is just d*** awesome. Right. I feel
like we've been talking over you, man.

Sam Stepanyan - 12:17
It's just a couple of things to add. Basically, the ability to add comments to
the code, I think what Dennis has mentioned, I think that's revolutionary
by itself. Obviously, if we just walk away from us being security people,
right. It's the amount of productivity that it's going to add when you are
trying to do reverse engineering and triaging of vulnerability in a legacy
code is absolutely huge. Right. Because obviously we have two types of
problems, right. In application security, we have problem number one, how
to make sure that the software which is being built right now is secure,
and how do we remediate vulnerabilities in the legacy software which was
built years ago by someone else? So there's two sides to the problem. The
comment writing feature, I think it's very good in the same way that it can
actually generate documentation. Again, you can ask it to generate
documentation as if it was read by a five year old, for example, or to a
different audience.

Sam Stepanyan - 13:13
And the same thing with the vulnerabilities. What I found very interesting
is that you can ask it because obviously, when it finds vulnerabilities, you
can say, explain this vulnerabilities, like, I'm a CEO, I'm a non technical
person, and it will still do it. I think evaluate, because we are all techies,
right? We have a problem of speaking to the management, speaking to the
board, and actually explaining what is the actual risk, trying to say, oh,
there's a deserialization issue, or the words like cross site scripting or
server side request forgery, that just sounds like Chinese to any CEO and
some CTOs as well. I think the fact that it's a language model and it can
actually utilize the language to make things simpler, I think is quite
important.

Nathan Case - 13:57
You've touched on something that I want to get into here, if you don't
mind. You touched on reverse engineering, so there's always the forensics
or the reverse engineering of malware that I don't know if I've seen
anybody use chat GPT for. You have obfuscated code that someone
obfuscated because they don't want you to figure out how my malware is
working. I think it would be really interesting to begin to look at, can we
actually reverse engineer active malware with a Chat GPT like system that
actually lets us figure out real quick what was the trigger and how do we
fix it.

Dinis Cruz - 14:33
I totally think that's possible, right? I think that's just a case of having the
right fees, right? I want to play with you saying, can you explain these
JavaScript codes, 4K codes, and if you ever seen it, that was two K codes
where you feel what the h*** it is, right? And you can explain it. Right. I
think that's really cool. Sam, on your world, I think would be really cool,
for example, to write Waft rules based on codes, right? But also find gaps,
right? Take for example a firewall and say where are the blind spots on
this? What actually is actually happening here?

Sam Stepanyan - 15:07
Not just the WAFF rules. The most amazing thing is, again, going back to
SAS, right? Mostly SAS people, it writes the SAS rules and it drives them
because there's now there's a SEM grab and Code QL. And there's an
example. Obviously my waste on the chapter called Leader Sharifman. He
actually spent, I think, a week in Chat GPT and he actually managed to
write something very useful for his team. He shared actually I know,
obviously were in a chat bone, but Dennis, would you be able to allow me
to share my screen? I think I should be able to, yeah, you can, yeah,
because I can share the GitHub repo where that's created called Infosec
open AI examples. Here you can see an example of CWE explanation
which is written by Chat GPT and it is written for developer and it
explains what the code is vulnerable and it also remediates the code.

Sam Stepanyan - 16:08
After it remediates the code, you can ask Open AI to write the Semgrap
rule which will detect it and prevent it in the future. And then a code QL
rule. I haven't tried it, but we should be able to also write a mod security
CRS rule for the WAF as well. Also to stop it on WAF if it is a vulnerability
which can be stopped on the WAF. Here it is doing sanitization and input
validation. So there you go. You can see these are all the examples. This is
all available in this repo. There's also Python code test python code that
you can play with. I think this is absolutely fantastic and let me just switch
back to the actual code.

Nathan Case - 17:00
I would love to play with that after this.

Sam Stepanyan - 17:03
Exactly. Obviously the languages, it was implemented in several
languages, so I can show you the languages where it is proven to be
working. That's java, python, c, sharp, swift, kotlin, PHP, rust, go and
JavaScript. Basically Chat GPT will analyze the code we'll describe the
vulnerability in the code, we'll show an example of vulnerable code in the
language, we'll show an example of remediation, and it will create
Samgrep rule to detect vulnerability and create a code QL rule to detect
this vulnerability. These are all the CWE for which this has been basically
demoed in this project. Yeah, I will copy paste the link in the chat. I'm
going to stop sharing now. So there you go. That's the working example.
And it's proven to be working.

Dinis Cruz - 17:54
The built in check is then we can review that and we can make sure that
it's right, but also we can adjust it, right? We can say, okay, this is actually
all well explained, or this thing here, and then it might not be perfect the
first time around. It doesn't need to be perfect, but think about it after
510, 20, 5000, those examples, the next one is going to be much better,
right? Absolutely. Even more interestingly, then you can even say, okay,
now write the Http request to trigger that exploit, right? You can even
think about, okay, now deploy that rule in front of one and then verify that
rule actually works. Right.

Nathan Case - 18:28
I think that's the thing, though, and the reason I bring it up is because this
is the FUD that people are going to try to throw at this. When you look at
it, what we're looking at is way better than anything we have today. I
think it's really hard to argue that, oh, an error here or there is going to
really make this okay. Yeah, I get it. Mistakes are going to happen. We
have the way to correct, move forward.

Sam Stepanyan - 18:53
That's why we're humans, right? It still requires humans to review and
confirm. Dennis, as you said, it still sometimes doesn't get it right on the
first time, but you can ask it to correct itself and it will do.

Nathan Case - 19:06
At the moment, get it right the first time at a college.

Dinis Cruz - 19:11
Exactly.

Sam Stepanyan - 19:13
This is what someone saying, that Chat GPD is really like an intern, right?
Basically it's an intern who you can ask and go and do some research and
do some googling and bring the information back together as a project.
So that's essentially what it does. The thing that we're missing, this is a
very early stage, right? Because Chanjibiti really entered our lives in the
past four or five months, right, and it's very early and I'm looking forward
to evolution. It's going to get significantly better very soon. Organizations
who are already utilizing the power of it, I think they're understanding
how much further they can take it. Obviously it's particularly the learning
bit, because if we can basically feedback the human learning. It was
actually for our AppSec purpose, right. We ask you to find vulnerabilities
in the code. And let's say I had this issue.

Sam Stepanyan - 20:05
For example, there are five vulnerabilities in the code. Chat GPT found
four out of five and explained this four out of five. I asked myself, hang on
a minute, but there is another deserialization on line 55 of this file and it
said, oh yes, I apologize, I missed that. There is a deserialization and here
is how you should be remediating this. And it gave me the example. The
thing is it didn't actually use the fact that I corrected it to learn and
enhance its own knowledge base. It doesn't make the same mistake next
time, but I think it's coming right. That's the next phase.

Scott Katie - 20:40
Security is trust the verify, right?

Dinis Cruz - 20:43
Yeah.

Scott Katie - 20:44
Learning is you learn when you make mistakes. Because if you do it right
the first time and you don't know, you.

Nathan Case - 20:51
Don'T know.

Scott Katie - 20:57
That'S at least the way I'm approaching Chat AI is if I can trust and then
verify something, then I could probably automate it. I know I have some
known good, but you have to iterate that I think.

Nathan Case - 21:14
We'Re moving to a place here, too, where the number of known
vulnerabilities, the number of known issues in code is reaching a we don't
have enough humans on the planet to deal with this point. As we look at
something like this, we're going to have to figure out how to automate our
way out of the mess that we're creating because there aren't enough
fingers left in the planet to hunt and peck for each of these vulnerabilities.

Scott Katie - 21:38
How do we correct this or time?

Dinis Cruz - 21:42
To be honest, that is something that I feel keep element here. I think for a
long time my main worry was I couldn't see how we could scale, right. The
only thing that didn't happen, I thought it would happen, I thought the
attackers would get a lot more efficient and effective than they were. I still
feel that we still have the pace where for the amount of vulnerabilities that
exist and for the complexity of the exploits of the ones that do exist, you
still assume that apart in some places, most attacks are not leveraging
highly advanced things, right? Of course there's a couple of places where
they are, but I feel that this is the first time that I see a scale solution.
Because in the past, most of our solutions I would go, this will never scale
at large. If we really need to run this up, if we really need to start
protecting all the NPM registries and all the dependencies that we've got
and the dependencies this finally, I think gives us a good way to do that.

Dinis Cruz - 22:45
The scalability of security practices. I think the difference now, and it's
interesting because we are all of a generation, right? The difference now is
that are we going to be able to adapt, right? Or is the new generation
going to completely stream all this where for them. GBT is what Google
was for us. Also the difference is the time scales are much shorter. Right.
Google took ten years, 15 years, right. To really gain this thing, where this
is going to happen in a couple of years.

Nathan Case - 23:18
I think it's more like a couple.

Dinis Cruz - 23:19
The question will be, how do you protect against the AI agent itself? That's
the next evolution, right, of this. I think in going back to the topic of this,
if we can now start to leverage these technologies, we can actually make a
huge amount of the security industry a lot more relevant because as you
guys just mentioned, that these might make mistakes. Come on, our
industry is a crazy offender of producing bad things, bad data, bad
information, not connecting, not talking to each other all that, right?

Nathan Case - 23:52
Well, just thinking about I mean, like, we had talked about mist before we
got started. It's not something that's horribly used in the States, at least to
my knowledge right now. At the same time, you look at some of the things
that you could do with, hey, I'm going to go ahead and shove a whole
bunch of information into this model and come up with potential issues.
That's insane.

Dinis Cruz - 24:18
Yeah, we in a nice place where I think we have a lot of the foundations in
place. Right. If you look in terms of Nest, in terms of all our information,
there's a lot of good thinking that has been done in the last 20 years of
security that I think is right for really taking to the next level. ASVs is a
good example. It's great, but until you can create the 20 page of ASVs that
matters to that application, it is never going to take off effectively. And I
think that's amazing. Imagine feeding ASCs, feeding the source code and
saying, okay, which ones are relevant? In fact, imagine feeding it the
policies, feeding, you see compliance, feeding you the requirements,
feeding you the risk, feeding you the thread factors, right? And then say,
okay, now take this. Now give me what I should care about, where should
focus, right.

Nathan Case - 25:10
Especially on a privately trained model. I mean, yes, I can spin you all
sorts of scary stuff about a publicly trained model and an evil insider
doing horrible things to you, but are you telling me that evil insider isn't
going to find an easier way to deal with your stuff? Come on.

Dinis Cruz - 25:27
Exactly.

Sam Stepanyan - 25:32
Yeah. I've noticed Timo Pagle joined, and Timo, for those who don't know,
is a project leader of a fantastic Ovas project called Devsep Cops Maturity
Model. I think it would be great to bring him in and hear his opinion on
how chat GPD can help in development of maturity models.

Dinis Cruz - 25:55
Yeah, if you can join in.

Speaker 5 - 26:06
You directly ask me.

Dinis Cruz - 26:09
Yeah.

Speaker 5 - 26:09
I'm not having answer. I have to think about answer, right? It's not
something where we can directly have a good answer. What do you think
might be very able to ask GBT? A problem which I'm having is to identify
at which level should an activity be? Right? I estimate kind of expert
judgment, how much effort is it, how is the value? There are things which
would be nice to ask Chat GBT about the opinion, but currently I would
think it doesn't have a good opinion. I didn't ask, but I assume it doesn't
have a good opinion.

Dinis Cruz - 26:52
You should try. You'd be surprised.

Nathan Case - 26:57
As we get into this, I think looking at Chat GPT and what it's going to be
good for is the first step. Right? If we look at a process, let's pretend that
we all own a company and we're going to go ahead and use Chat GP to do
a thing. I like Timo's concept of what is the actual output and what money
can we make, what is the driving force for doing a what do we get out the
back of it? I think as we look at code review, as we look at some of the
things that we could probably have it do, there's a pretty substantial
benefit coming out the back of that could probably be monetized from the
CFO and say, hey, without this many errors, we will have this much more
money because we've saved this much time. I think as we get into it, that's
probably the way to go, though, if that's your point, Timo.

Dinis Cruz - 27:44
Ish yeah.

Speaker 5 - 27:48
That'S how you could express it.

Dinis Cruz - 27:52
Let's look at your example. You have the Devse maturity model, right? I
think models like those, I think the real value is they set up the best
practices. The problem is always how do you connect that with reality and
actionable items. What's interesting is to say, here's the latest version and
you think about it. Some of these things you need that ingestion, right?
Here's the latest version that has been modified. This is this week's
version, whatever. This is the latest version of a particular maturity model.
Here is now the code, or the organization structure, or the systems, or the
things, or the practice or the CI pipeline that the organization has. What
are the next things that should happen? Right. What is the maturity model
of the organization based on the standard? Those are the kind of
questions that you'll be able to ask something like Chat TPT once you can
feed some of these data in there.

Dinis Cruz - 28:47
In fact, I think it's interesting because the latest version already allows
you, I think it's 10,000 words or something like that, to feed data in. We
also need to start thinking about how can you package things in a way
that you can actually feed the model right. Ask the question on top of the
model. Yeah.

Speaker 5 - 29:07
It would be very nice to. Give all the project source code to it and then it
tells you where you are, right, that would be amazing. You don't need to
sing, it just says that is done, that's not done, that's the next step. Yeah,
that would be very cool. I think a lot of questions can be answered when
you just give your code, right? Because you do infrastructure as code
nowadays. Actually every point, not every point, but most of the points in
such a maturity model you could probably get a good answer.

Dinis Cruz - 29:45
One of the things I like about where Microsoft is going with this bing, if
you go up some keep showing that's great. One of the things I like about
this evolution is that they start to show the sources and I think that's going
to be an evolution here. Right. I think the whole idea that it's also black
magic will move before because we want to know that, right? Because you
can even want to have one model kind of analyzing the other model
answers to say how much of that is actually true, how much of that is
actually made up. Because there is things called now the auto AI. If you
guys seen those, which is when they actually try to automate and create
and basically have this really nice workflow where you almost start to
think about here are the tasks you want, here are the models you're going
to use, here's the structure, here are the tasks.

Dinis Cruz - 30:32
At the end and when you do that, you start to be able to feed it a lot more
complex data. Timothy, to your point, right, you should say here's my app,
he's my architecture, here's my environment, he's my AWS environment,
right. Here's my logs. Here is 2GB of cloud trail logs right now apply. Now
the devsecos principles or the DevSecOps thing here. Those are the kind of
questions that before would be crazy to answer, right? Just think about it.

Nathan Case - 31:03
I mean, I don't have to write IAM ever again. No more IAM rules. Off you
go.

Dinis Cruz - 31:10
You now start to write intent, which is different. So you start to write
rules. So your rules should be the intent. This is where it gets really cool
because now you start to hit the business requirements. You start to say
what I want is for these users to do this that thing. What I want is for this
project to have these properties.

Sam Stepanyan - 31:29
Dennis, can I also add one very important clarification? You can also ask
make the suggestions based on the assumption that the business type is
medical or health, government, utility.

Nathan Case - 31:44
And all the regulations.

Sam Stepanyan - 31:45
And this is all the regulations. That's where I found very good value, right?
For example, we can take any of the requirements and just say okay, what
do I need to address if I am a medical organization? What do I need to
address if I'm a bank and please prioritize this for me if I'm an automotive
manufacturer or airplane manufacturer, I think that's a very great value
of large language model context.

Dinis Cruz - 32:14
Right, and the whole point of the maturity model is exactly that. Right. If
you look at, again, maturity model as an example, you should say where
are we and what are the next steps and where should be the priorities?
Again, you can still verify that, but the ability for that to scale is
enormous.

Nathan Case - 32:33
Well, just looking at the I think the regulation point that Sam made is just
horribly pertinent, especially with EU and GDPR and all of the crazy stuff
that we have to start looking at is what is actually PII. Okay, we're going
to go ahead and write this regulation body, that's great. This corpus of
text can be sucked into and I get that this can't happen yet sucked into
Chat GPT and go ahead and look at my code and tell me if any of this
code is actually putting to logs something that is PII. That's been one of
the gremlins for privacy for years. All of a sudden we have PII going to
logs accidentally and oh my God, what the h***? To be able to pull that
out and say, well, look, we've seen all of this stuff and this function right
here is going to do that bad thing.

Nathan Case - 33:19
I mean, even just a highlight over three or four of those places as opposed
to having to read millions of lines of code to find that huge benefit, makes
high trust a h*** of a lot more achievable.

Dinis Cruz - 33:31
Yeah. If there's no describing intent, this is like the worldly maps. This is
an evolutionary step, right? This is one of those where the way I think
about this is like the thing about really cool the worldly maps is that you
got the genesis commodity, right? Now we don't know which one will jump
from product to commodity. Right. Like you think about it before charge
GPT, who's going to get that first? If you make bets, you probably say
Google, right? Maybe even Apple or Tesla or other organization or some
of the AI things. What these guys did with the GDP four was they made an
evolutionary jump. Now we can predict what will happen next because the
next jumps are not that great. They're just little evolutionary little things.
The big jump has been done. If you look at, for example, like we talk
about Google, I stop using Google for now because I prefer to describe the
intent that I have.

Dinis Cruz - 34:27
Unless it's an esoteric thing, I now spend my time describing what the
intent I have and refining the intent that I have, which is a lot more
efficient way of doing it.

Sam Stepanyan - 34:36
Yeah, but are you actually using Chat GPT? Because obviously, again, very
interesting point about Google losing in this race because as I just shared
as my screen from Microsoft Bing search engine, because Bing actually
combined the chat GPT with live internet search results. Even though it
takes a while because it thinks about answer, what it comes back with is
actually probably exactly what you describe in terms of what you want to
achieve. So there you go. Here just ask about again, since Timo is here
about OS devseco's maturity model and it gave me the precise answer and
it suggested me the next question, which is how can I implement this
model in my organization? Again, it provided me some information, what
needs to be done to implement in my organization. Itself suggests the
question what are the benefits of using Fseco ops maturity model? I think
these additional prompts and the fact that it kind of leads you down a
path.

Sam Stepanyan - 35:38
Probably we've all seen this answer suggestions from Outlook or from
Microsoft teams or whatever, even from LinkedIn when it suggests you
some answers. They were completely nonsensical up until now, because
now it actually makes sense. For example, there you go, it says, well, you
need to carry out a self assessment of your organization security practice
and say well, how do I do this? And it tells me more. Only Microsoft Bing
has it at the moment. Google thing still needs to catch up.

Dinis Cruz - 36:21
Jtbg UI will give you this, right? Again, this is just on the Bing
environment, right? But it comes from there. It seems that's the thing, it's
the feeding of the model, right? What gets interesting is when you can give
it data, when you say here's my organization. To be honest, this is where
the next discussion, for example, again, let's go back to DevSecOps model.
I think we now need to think about how can you create, how can you feed
data that is relevant to the DevSecOps model, that allows good basically
not just the review, but the analysis. Because think about it, in the past you
create a model, then you go how do evaluate this? That would be a
massive manual effort to do it, right? Because how do you review it?
Where now we can say, okay, if you are on this, let's say if you have
Google cloud, right, then you need to get this data feed.

Dinis Cruz - 37:13
If you have AWS, then you get that data feed. If you have GitHub, then you
get GitLab, you get this feed, right? That can then be the feeding of the
data to the model, right? You can have the actions, and then you start to
have the feedback loop, right? As time changes, you can then say okay,
and then you say okay, here was the last analysis, here's where we are
now. How much have we progressed and what are the next steps?

Nathan Case - 37:44
I think as we get into it. I mean, beyond all of that even, let's look at it
from an operationalist point of view. Let's pretend now that we're all
operationalists and we have to keep our company alive for the next. Take
your pick. How cool would it be from a DevSec Ops model to be able to
say code one side, camera here, code one side, and monitoring an Ops on
the other. Now not only can I tell you that both things actually are being
evaluated, like I'm looking at your code and I have the monitors for
operations to hand them and say this is actually getting monitored all the
time. The observability for this is right here. Being able to click on it and
go back to the actual function that monitor is testing. I mean, the ability
so geeky incident responder in me goes, oh my God, I can actually look at
all of these things and say this goes back to this set of code and this is why
this is happening.

Dinis Cruz - 38:37
It's a game changer. This is what I'm saying. I think the security vendors,
which are critical part of infrastructure, they really need to step out
because most of the tools now for me started too primitive. Really. I
cannot ask this kind of question. Really, I'm going to have to SQL or this
kind of complex queries. I want context, right? A lot of the times, a lot of
the engines, a lot of the business build engines on top of it. They need to
restructure to say they need to be using a chat DBT like environment.
They need to start creating their graphs in a way that is consumable by
that. I think that's the biggest transformation is that now graphs will
really scale because that's why these engines can consume very well. We
can now use graphs for context, but we don't have to create them.

Dinis Cruz - 39:25
We just have to almost start thinking about the instructions for how to
create a model around it. There's already a nice marketplace for models,
so we need to start have models again for the bits that we use, right? You
could even argue that every framework should eventually come up with a
model that understands how that framework behaves because every
framework has things that are unique to them. The Spring framework, the
Express framework, the Fast API framework, whatever, the Net Rest API
framework, all those frameworks have behaviors that then once you have
a model that understands it, you can ask so much better questions on it.
That's why I think that's a big game changer. I think in the security world,
what I will say is that we are well poised to leverage this. I think the good
security team should not be driving a lot of innovation because we should
be on a forefront with all these transformations.

Dinis Cruz - 40:31
The next thing is how can we change the business with it? Right. Because
a lot of because I got to the point for me where I feel I need to understand
the business in order to protect the business, right. Most of the changes
that we want to do are changes to the business. I see that the real
interesting opportunity here is help the business to understand itself, drive
change there so we can push the security changes with it.

Nathan Case - 40:56
I think there's that and I think that's the if you look at how, the
overarching, thing that's going to drive this into business is the fact, hey,
we can make more money on that. The reality of being able to look at
these things and be able to say from just the stupid simple things that it
could do. I was talking to a red teamer that got shoved into incident
response and he had to make a choice and he decided that he was going to
clear out all of the AWS API credentials for a service when he realized his
company had been hacked. I expressed to him that was probably a bad
choice. And he said, well, but why? I said, well, because you just caused an
eight hour outage for your website. That was bad. As an incident
responder, we can get that, we can understand that.

Nathan Case - 41:50
If you could build out a model that allows you to ask questions like that as
you're going and be able to say, hey, what's the right answer here? Be able
to have it give you a contextual response of, well, if you do that, these are
the things that are going to proceed from that thing. Now I don't expect it
to be able to say, no, don't do that's a bit much, but just give you a
contextual response about, hey, this is what's happening right now, it
would be really nice to know that I shouldn't delete the AWS API
credentials. These are the things that are going to come out of that choice
context.

Dinis Cruz - 42:22
Right, yeah.

Sam Stepanyan - 42:24
What you're talking about, Nathan, I think it's also decision trees, right. In
the context of security incident Response, that's actually one of the
advantage, that it can actually give you a decision trees. As we just seen in
my live demo, it can take you down a specific path so it can go deeper and
if necessary, go down to the line of code or particular change. I know
some companies already started doing things like feeding change requests
that they made to the configuration of the systems into it. That makes
interest of what change affected this incident.

Dinis Cruz - 43:00
Absolutely. This makes a decision tree scale. The challenge I always have
in decision Tree path is that to be really useful, it has to be very specific. In
order to be very specific, it becomes massive. Right. And then people get
overwhelmed, right? Because you need the detail. What this allows us to
do is to have context. You have a massive object model, a mass decision
tree, but you only see this bit. That bit, more importantly, not just a small
bit, is in context. In fact, this is an example where some of the next
generation of chat DBT like technologies, we don't want deviation. I think
at the moment with this first experimentation, we still at the mode where
we almost again, it's fun that image mistakes and it's fun that's 100%
correct. We can get to a point where we says we don't want that.

Dinis Cruz - 43:51
We want to say this is your body of knowledge, don't use anything else,
just use that. That's the current decision tree. What you need to
understand is what those words mean in the action of that. From a
decision point of view or the secrets of events, this should be your truth.
Again, we're not that far off on it. This is just a question of what data you
feed them on versus the model having. In fact, I think sometimes the cool
models are too powerful. We actually need less powerful. Some of these
engines that don't have all the emotion and don't have all the ambiguity,
don't have all the ability to come up with things, just have the ability to
understand and execute on certain things.

Nathan Case - 44:30
Well, something stupid simple like let's give it the corpus of Windows
Server code, just that thing. We're going to give it all of it manuals for the
last 20 years. I, as a new person coming out of college, need to do an ad
set up. How do I do an ad set up? Done.

Dinis Cruz - 44:53
More importantly, how do I do an ad set up? With this configuration?
Correct. This configuration is going to be different than that one.

Nathan Case - 45:03
Or even to ask me the questions about do you want to do this, that or the
other? These are the outcomes to your point about decision trees, in many
cases, the decision tree is actually the thing that the new person doesn't
have yet. They don't even know that. They don't know. How do I even
begin to ask that question?

Dinis Cruz - 45:19
I think that's the sweet spot now, right? I think companies who can
address that in security, we are such a complex world now that we are ripe
for that innovation. And I think that's what gets interesting. And it's like
Sam was showing it. You now can start some really lovely feedback loops
between the tools where you feed here and you feed that and then you
almost let reality validate it, if you think about it. If I'm saying that I have
a last rule, I have a rule here, I have a thingy here that's supposed to lock
this down. The next time you get the data, it should confirm that, right?
It's not a zero sum game. I think that's where it gets interesting is when
you feed models to models, when you chain them, which eventually it can
go south very fast. I think we also have a massive potential to accelerate a
lot of these things.

Dinis Cruz - 46:10
Yeah, cool. Right, guys? Oh, Sam's gonna give us another good example.

Nathan Case - 46:16
Sam's gonna do one more thing.

Dinis Cruz - 46:20
Yeah.

Nathan Case - 46:24
Sam'S on mute.

Dinis Cruz - 46:26
Sam, you're mute.

Nathan Case - 46:34
What Sam's showing us here is the summary of reporting on incidents,
which is interesting because it actually gives us the source code that it
came up with.

Sam Stepanyan - 46:41
The question here was, how can I use Chat GPD for security incident
response? But very interestingly. Right. It contains an ad. Can you see
this? It actually advertises Microsoft Sentinel and Defender.

Dinis Cruz - 46:58
Yeah, that's interesting. It was the answer above. Influenced by Microsoft.
I think there's a really cool tool that should be built, which is to
understand the bias of the engines. I actually think that tool is important
because we talk about these engines being sentiment one day, right?
Hopefully not that far. I think we need to start detecting that. I think we
need to start having almost like we need to start almost like pen testing a
GBT engine to see, for example, like that. Does he have bias? Does he
have bias on gender? Also, does he have buyers on data points? Does he
have bias against companies? Does he have buyers against well, it's.

Sam Stepanyan - 47:43
Owned by Microsoft and I just showed you an example how it was biased.

Nathan Case - 47:47
Obviously it's a little biased.

Dinis Cruz - 47:49
Exactly. Right. But that's an important point. Right? It's an important
point to understand the bias of this. Right. I think it's one of those cases
that as the technology matures, it's again, we need to understand the
framework that we're dealing with because this is going to become all new
very fast. We're going to expect to talk to our engines, we're going to
expect to talk to this going back to the Microsoft copilot. If you look at
there's a whole ratchet of copilot products and they're launching out for
Word, for PowerPoint, for all these things, right? So they're really raising
the level. We need to start framing, but also identifying the buys and
limitations of the engine. Pen testing is a good cooler, the engines
themselves, right?

Nathan Case - 48:34
Different sort of pen test.

Dinis Cruz - 48:35
Yeah, different sort of Pen test. Right. But understand those blind spots.
Right. I feel that because you can feed one to the other, we will basically
ratch up quite effectively a lot of the stuff that we're doing.

Nathan Case - 48:48
We teach them to feed one to the other and then we teach it to feed one to
the other, what happens? We make skynet.

Dinis Cruz - 48:56
That's the thing. It's when you have actions. But that's an interesting
concern. Right? I think it's a valid concern that these pads leads to that.
Billy, may I ask a question?

Speaker 6 - 49:15
Yeah. Can you guys hear me?

Dinis Cruz - 49:17
Good. Perfect.

Speaker 6 - 49:21
I was just going to chime in about the bias thing. I actually seen people
test that to see if it has a certain bias based on different views or things
like that. What they were able to determine was that it will have a bias
based on how you frame a conversation. If you ask it I don't want to start
a warrant here or anything, but if you ask it something like point out the
ways that this political leader is a tyrant and it will post exactly that. It'll
post all of the things against that particular leader. But if you post a
question.

Dinis Cruz - 50:18
Where.

Speaker 6 - 50:18
It'S more political or more of an equal footing, then it will try to answer it
based on that. I think what it really boils down to is people are going to
get the answers that they really want until they can make it more of a
megaworth checks for that kind of context.

Dinis Cruz - 50:49
That's why if you think that almost, I guess, to our world, it's interesting
to think that we could have a world where we have a security bot that is
used by developers, by engineers, by practitioners that we have already fed
our BIOS. In that way the bias could be a good thing because we want
specific things to occur. We want specific frameworks to be used. We want
security practices to be used. Right? If you imagine, like, if you have a
developer running a web service and using a bot to help it, we want the
bot to already think about the best way to deploy the web service, the best
way to protect it, the best way to authenticate it, to validate all that jazz.
Right? It's an interesting way once you understand how we can influence
an engine. I agree that the way you ask the questions, you can determine
the output, but it's also a way to understand your audience, right?

Dinis Cruz - 51:46
I'm assuming now this is in an environment where you can see the
feedback loops. So cool, guys. We only are look, I've learned a lot of good
stuff, Sam. Thanks for sharing those. Those are really cool, right? I think
we need to do that one of these every two months because things are
going to change so fast, right. We need to start showing some good
examples of this going on.

Sam Stepanyan - 52:10
Going back to your favorite topic for people who haven't seen Dennis's
talk at OAS London about using Jira for managing your security program.
So, of course, one of the things that you can use, and I've seen people
started using Chatgpt Impact on advice, for example, publication security,
just create Jira tickets. With a text in this, Jira tickets will be context
specific and very relevant and in a language which can be understood by
software developers find who's doing that.

Dinis Cruz - 52:39
I haven't seen good examples of that. Let me know who's doing it. Let's
invite them to do a session. Right? I would love to see that. Cool. Any final
words on this topic?

Sam Stepanyan - 52:52
I think it's very important for us to understand that this is all very new and
we're already seeing some very exciting developments. I had conversation
with a few vendors and saying, well, are you threatened by this? They said,
no, we actually embrace it. That's where I see probably in the next year,
we will see security vendors, SaaS vendors, and just cybersecurity vendors
actually embracing this technology. Finally, the AI on the data sheet is
going to mean something. Not just we use AI and machine learning, so
please buy us. And we also use blockchain.

Dinis Cruz - 53:25
Right.

Sam Stepanyan - 53:25
The usual buzzword. So I think this evolution is coming. Again, we have a
responsibility from security engineering perspective. Just make sure that
it's also secure. The use of it is secure. I know we haven't touched on
topics like privacy and giving it personal data, company data, and
company intellectual property, such as source code. That's probably a
topic for next conversation.

Nathan Case - 53:51
Hacking GPT is a different thing.

Dinis Cruz - 53:56
Any final thoughts, Nathan?

Nathan Case - 53:59
I think we need to approach chat GPT and frankly, any of the other chat
bots. Very much the same way we approached Cloud and very much the
way we approached, I don't know, databases back in the 80s.

Dinis Cruz - 54:12
Right.

Nathan Case - 54:12
I mean, this is a change to the way that things work, and that's okay. It's
not the end of the world. There are going to be things that we need to
work through and there are going to be errors and we're going to screw
up and we're going to fix it and it'll be okay.

Speaker 5 - 54:34
Yeah, I think it will be amazing. In the future, maybe only the person who
can ask the right question will get paid in a good way.

Dinis Cruz - 54:46
Yeah. Well, it's more reality now than it was four months ago. Right. I
think it's like the Internet, right? It changed a lot, but then we evolve and
we go to the next level. Right. I think the difference is going to between
the people who use it and people who don't use it. I think that's why we
need to learn how to use this very effectively. Cool. All right, guys, thanks
a lot for this one. We starting to move the needle and I'll see you guys in
the next one.

Sam Stepanyan - 55:13
Thank you.

Dinis Cruz - 55:14
Thanks, guys.
