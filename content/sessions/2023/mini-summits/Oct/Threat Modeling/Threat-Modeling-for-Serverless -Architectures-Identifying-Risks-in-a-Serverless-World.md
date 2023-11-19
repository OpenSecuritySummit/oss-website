---
title        : "Threat Modeling for Serverless Architectures: Identifying Risks in a Serverless World (Panel) "
track        : Threat Modeling
project      : Threat Modeling
type         : working-session
topics       : Serverless Architectures, Risks
featured     :
event        : mini-summit
when_year    : 2023
when_month   : Oct
when_day     : Wed
when_time    : WS-17-18
hey_summit   : https://www.linkedin.com/events/7110026446877646848
session_slack:
#status      : draft
description  :
banner       : https://github.com/OpenSecuritySummit/oss-website/blob/main/content/sessions/2023/mini-summits/Oct/banners/serverless.jpg?raw=true
organizers   :
     - Dinis Cruz
     - Luis Servin
     - Ayse Vlok
     - Omer Yaron
     
youtube_link : https://youtu.be/LU3f5_mRkII
zoom_link    : https://us06web.zoom.us/meeting/register/tZIvcO6rpjguG9c_BAbjihJ47vwkSsjYjPRw
---

## About this session
Discussing the unique security considerations and risks associated with serverless architectures and exploring how threat modeling can help identify and mitigate potential threats.

### Outline:
- Overview of serverless computing and its security implications
- Analysis of common security risks and vulnerabilities in serverless architectures 
- Techniques for conducting effective threat modeling in serverless environments
- Real-world examples and case studies of threat modeling in serverless deployments

## Transcript:
Speaker 1 - 00:00
Right.

Speaker 2 - 00:04
Welcome, everyone, to the Open Security Summit 2023. It's October 18
and we have a panel session regarding threat modeling for serverless
architectures, if I'm not wrong. Yes, that's what we're going to discuss.
And we Denis Cruz on the line, Ayse Vlok from Vlog, Louis Servin, myself,
and I'm not sure who else is joining. Is Omar already on the call?

Speaker 1 - 00:38
Not.

Speaker 2 - 00:42
All right, so it's us three, I suppose, and any guests. So welcome and let's
heat it up.

Speaker 3 - 00:53
Maybe a quick introduction.

Speaker 1 - 00:54
You and I want to do a quick introduction.

Speaker 2 - 01:00
Sure. Ayse, would you mind going first?

Speaker 4 - 01:04
Yeah, sure. Hi everyone. My name is Ayse. At the moment I am the head of
Platform Security Engineering at Densu. My background includes security,
governance and compliance, security operations, security engineering,
cloud security, and now I'm heading a security engineering function.
That's it for me.

Speaker 3 - 01:31
That's a big job.

Speaker 2 - 01:35
So I'll introduce myself. I'm Louis Herbin, security architect, currently in
the role of platform security lead at a very big shipping company called
Hapacloid. I have a bunch of experience over ten years in application
security, having created and rolled out application security programs with
a strong focus on threat modeling at this is my fourth company where I do
this. So it's been a journey.

Speaker 1 - 02:07
Yeah.

Speaker 3 - 02:08
I'm Denis Cruz, I'm the CISO of.

Speaker 1 - 02:11
Holman Barrett, a UK retailer and a chief scientist of Glasswall, a UK
kind.

Speaker 3 - 02:16
Of reasonably big startup these days. And I've been doing threat model, I
think since the beginning, I think, when he barely wasn't called threat
modeling.

Speaker 1 - 02:28
I'm a big fan and I think it's a key part of the solution. So, looking
forward to this session.

Speaker 2 - 02:39
Perfect. So how shall we start? Shall we ask each other questions? Shall
we put a topic on the table and try to move around it?

Speaker 3 - 02:47
Yeah, I think that's a good one. In fact, maybe just from a scalable point
of view, why don't we just.

Speaker 1 - 02:55
Start with that topic of how to scale threat modeling? And that post you
were just mentioning about using GBT, especially the new visual element
of it, right. To try to make a good dent on it.

Speaker 2 - 03:13
Certainly. So I work currently with about 800 developers, growing to 1000
within the next couple of years, probably, and we're trying to roll out our
application security program right now. One thing we have been
discussing, or where we're putting the emphasis rather than the
discussion, so we're already active on this, is having cybersecurity
champions in every single development team. So we'll have at least 80 to
90 security champions in the company, and every security champion is
embedded within their team. So at least we have someone who has heard
of security in the team who can be our inside person. He or she will help
do these activities and make sure that these activities take place. But then
the question of threat modeling is difficult, first of all, because it has
several stages. So diagram what do you need as a diagram for threat
modeling?

Speaker 2 - 04:21
Very often we have boxes joined by arrows, by lines. What is the context,
what is the reason of this arrow existing and joining the two boxes? What
information can we take out of the diagram? Many times we don't have an
intention. Why is there a connection between two boxes? And that makes
threat modeling in an automated way very difficult because you cannot
look at the intention. You cannot see whether there's something there just
by looking at the diagram that screams of lack of encryption or anything.
You might have the port, perhaps the protocol, but you have no idea,
really, in most diagrams I've seen so far whether that is actually still
current. I have yet to find a single diagram in all my experience, that is up
to date. Right.

Speaker 2 - 05:18
In Agile development, diagrams are the last documentation is the last
thing that gets updated. It might be part of the definition of Done, but it's
never updated. So I can try to put a diagram into Chat GPT or ERUs Risk
or any other platform, recreate it there. But what is the value of that if the
diagram is not current? So the biggest challenge for scaling this is the
value of threat modeling is the conversation you have around the system,
around these possible shortcomings and possible attack scenarios derived
from vulnerabilities or shortcomings in the code. So I'm not really sure
this can scale. I think this will remain at a craft level for a number of
years. I mean, you can verify in the implementation level on the cloud
many things that will alert you of vulnerabilities, but that's not threat
modeling, right?

Speaker 2 - 06:23
That has happened already. You couldn't prevent something. So I'll give
the mic to Aisha. Maybe she has a better idea or want to comment on that.

Speaker 4 - 06:35
No. I think you touched upon a couple of dilemmas that I've experienced
in my career as well, and I've seen one of them. Is it's definitely true that
documentation and diagrams are the last update? Sometimes developers
don't even know the latest status themselves to be able to provide up to
date one. So if the diagramming problem was sort of solved, it could help
with the scaling. In the past, I used like AWS perspective. There are a
couple of companies coming up now providing solutions, but with that is,
like you said, you're looking at what's already in place rather than design
stage. So that's more like a security review, retrospective trying to put
something in rather than bringing it together. And I like the idea of threat
modeling becoming a sort of an event sort of thing, bringing people in
together and understand.

Speaker 4 - 07:45
It's sort of like an awareness session that you can get in as well as what
you're trying to do with the modeling itself, with the action items
afterwards. Yeah. So those are the comments that I can really make. One
thing that I've in my experience I've experienced sorry, in my career I
experienced is that infrastructure configuration have sort of been left out
quite a lot. I I did briefly in the past look into incorporating all that in.
Hence me looking into if applications are becoming more and more
serverless reliant on native cloud services, then configuration, access
management, IAM configuration of certain services, your pipeline, how
you push them, become really important as well. Right?

Speaker 2 - 08:50
Yeah.

Speaker 3 - 08:50
So I think you're touching on a couple of interesting points.

Speaker 1 - 08:52
Let me ask you this question. If we had good up to date documentation
and good up to date description of intent of what the code is supposed to
do, or it does, actually, and good visual representations I e. Diagrams on
that in a sort of diagram as code environment where you can version
control it. Would that change the threat modeling landscape and the
practices that we have today?

Speaker 2 - 09:24
It could if we're consistent across teams in how we document and create
these diagrams. The thing I don't see talked about too often is what
exactly is worthy of being diagrammed and how do you want to diagram?
Because even though the infrastructure might have a web application
firewall in front of the application, sending everything to the wasp
basically makes harder the analysis afterwards because what you want to
see is the connections between the user and the thing with a transparent
was, as if the request had passed already. The was and hit the backend
service or the load balancer. So many diagrams I see get lost in too many
details and the right level of detail is incredibly important to get value fast
out of a threat model or data flow diagram, if you want to call it that way,
first of all.

Speaker 2 - 10:26
And second, do we need diagrams for security purposes or should one
diagram suffice? And I'm convinced one diagram is enough, but we just
need to be methodological across teams on how we do it. And yes,
diagrams as coded would be fantastic. But then it's a new paradigm which
is not taught in whatever people learn how to code. Right. It's something
that the teams, the organization have to agree on and create competence
on and then it's up to someone in the company to set the path, create the
training material and get everyone on board and haggle a little bit, even
take and make sure that everyone has something similar, at least. Aisha,
you want to say something?

Speaker 4 - 11:22
No, but I want to ask you if you can give more information, tell us more
about like Dennis said, in an ideal world, if we had the right diagram up to
date, it's reflecting the architecture and the application as it is for security
purposes. How does it work with chargebit, if you can? A little bit
elaborate on that.

Speaker 1 - 11:56
So the reason I asked that question was a bit loaded because I think a lot
of the conversations we have about Jet GBT and NLMs are a bit not very
well aligned. So I like the analogy these days, you know, Jarvis from the
concept of Iron Man. Tony Stark uses Jarvis as kind of his system. You
guys get that reference. I think what happened here was we invented
Jarvis and then we asked Jarvis to write poetry and sing and then complain
that it's making up lyrics, right? But meanwhile, it's Jarvis, right? It has
that capability. So when I think about the AI gen AI, I'm not thinking
about, for example, something that's going to create code and you ship it
and you look at it.

Speaker 1 - 12:45
So this is a perfect example of we can use chattbt to create
documentation, we can use chattbt to create architecture diagrams,
basically to start creating that documentation that I think we can all agree
that up until now, the development workflows has failed to create. If they
could create it, they would have it, right? So I'll give you a good example.
You can take a git diff I e what change in a know commit, and you can
give it to chat GBT, and it gives a really good analysis of what was there,
right? So if you start to extrapolate that, it means that, for example, you
can go to chat GBT and say, explain me this function. Right? So let's say
you have a class. You first get chatgbt to go, explain me each function,
and then you can go explain how the class does.

Speaker 1 - 13:34
And you can even start to connect the dots. So you can start to get chatgpt
to create documentation about how an application works. And you can
also use it to create, even if not fully. Now, we're not that far off because
the hard part is already done. And the hard part is to have a system that
understands code. And it might even be that Jgbt is not even the best one.
It might be that AWS code Whisperer or whatever it's called, or even
Copilot has been trained like that. But we can have an Llam that basically
is able to understand code, understand meaning that's more important.
Not just the code, but the meaning of the code and what is doing. And
then you connect the dots. So eventually you will have an application
mapped. We're not that far off.

Speaker 1 - 14:24
And once we start to play at that world, in a way, we do threat models on
top of it. But the first step is to have code that is actually explained. And
it's not necessarily just documentation of the code, is the intent of the
code, is what the code actually does.

Speaker 2 - 14:43
The question is whether the code is the right level to create.

Speaker 1 - 14:47
Sometimes might be I don't understand what they kind of don't know
what it is right now. Go on, Luke.

Speaker 2 - 14:54
Sure. The question is one of levels of detail, right? So at which level do
you want to do your threat model? So we've discussed this in the past, you
and me. And I like to take an approach in which I start from a very high
level, in which I try to understand the business case, create use cases
around it, and start going to the details. Using chat CPT to look at the
code is starting already at the details. But then I would need to look at the
details. I would need to look at the infrast code. I would need to build
upon that, perhaps ask UBT to build the domain model or the business
concept around it. I'm not sure that's necessarily the way to go without
chatty. Perhaps hallucinating too much.

Speaker 1 - 15:41
But if you do it in bits, right, why wouldn't that not be possible? Why
would it not be possible to feed, to stay? And by the way, Asia, when you
talk about mapping infrastructure, you spot on, because that's a massive
blind spot that we have in our threat models, in our security reviews,
because you need the context of whatever the application that we're
reviewing is running at the right. But you can now do this kind of analysis
almost at a lot of levels. And then, more important, you can do analysis of
analysis and of analysis. And if you keep raising the abstraction layer, you
should arrive at Lewis, the top level architecture. But the beauty of this is
that I'm not saying that this is all done automatically. This should all be
done by the humans in the loop very finely.

Speaker 1 - 16:28
But it's very easy for somebody who understands the system to confirm or
deny or say, no, this is right, this is wrong. And then you kind of add some
training to the system or to the data, and then you start to get good
representations of reality. And even if you think about it, even if that's not
fully possible, you can start to connect the logs to say, look, even although
we don't think this is possible to go from A to B, we've seen logs from our
firewalls, from our internal systems, from our traffic flows. That actually
means that traffic did arrive here. But a lot of this stuff in the past were
impossible.

Speaker 1 - 17:04
And I think now with the LLM, as I can understand context, can
understand complex data, even raw data like data dump or a firewall log
or an im policy, this is becoming reality.

Speaker 4 - 17:20
Yeah, I think it's just too exciting. Once again, my brain is rushing right
now, thinking of all the possibilities at the moment. It's endless. Because
imagine you could also give permissions to be able to query your cloud
itself and carry out the API calls to check its actual status as opposed to
what it thinks the risk is and everything. So it's not impossible. I think that
just imagining it is just brilliant. Think of it like a giant, very, extremely
well informed machine that's going to be able to tell you see the big
picture, because that is the trickiest bit, being able to see the big picture at
high and low levels all at the same time.

Speaker 1 - 18:18
Okay, here's a very important concept, right? And the big paradigm shift
that I kind of did when I was looking at the models recently is I thought
that we had to train the models, right? So I thought that you had to take a
model like, for example, that vision that you just showed of the big picture.
One way to kind of do it is to pump all the data and train the model like
that. Right? But I'm not sure that's what best architecture for that. I
actually think that what you have is you have lots and lots of explanations
and small parts of basically the puzzle that we can now glue together. And
we can have models analyzing data from other models or keep feeding it,
but at every space we have basically documentation level. Does that make
sense?

Speaker 1 - 19:15
It's almost like even if you start with a source code, look, take a simple
function. You could take a function in the source code and you can say,
analyze this function, tell me what it does. Right. Technically, tell me
exactly what it does. And then you could say, okay, give me an architecture
flow for this. And then you can say, okay, so this is a function that is
supposed to, let's say, get a file from this on this particular scenario. So
now you can do analysis on the behavior of that function and you can even
start to do analysis on the business function of that function, right, but
every one of these needs to be stored, for example, in kits, right?

Speaker 1 - 19:52
So every piece of the puzzle, the problem we always had in the past is
what didn't scale was the maintainability of this data. That's the problem.
The problem was you could always sit down and map the whole
architecture, but by the time you finished, you would have changed, right?
And if you figure out something was wrong, you couldn't easily modify it.
But now we're going to be able to. So I kind of imagine what you just
described, not like a massive model like a Chat GBT for App X, but almost
like a Chat GBT or a code analysis engine that we then feed the right level
of abstractions as almost the embedding, the prompts, and then ask
questions. And that also makes it very easy to understand what's going on,
very easy to understand the outcomes.

Speaker 1 - 20:46
And you're also reducing the complexity of what basically the Chat TBT
needs to be looking at. And also you reduce hallucination, but by a lot
because you're almost seething the data that is doing the analysis.

Speaker 4 - 21:06
I got it. Yeah. It's like in my head, the analogy I'd use is like instead of an
elephant, think of a cheetah. You just want the agility to be able to pick up
that fluidity of the end state to keep the diagrams up to date, right?

Speaker 1 - 21:28
Kind of, yeah. You should be able to zoom in and out, but it's almost like
at every layer of the zoom, you're loading different data points into your
prompt. You could have analysis that talks about the architecture. You can
have a layer down that talks about data flows. You can have another layer
that contains information about the business analysis. So this allows us to
bring a lot of context into the layers. But it's almost like we use Chat, GBq
or whatever, LLM to provide context and to do the analysis. Almost a
translation from one part to the other. But then we store it and that's what
you feed to the next analysis. Did you know, who needs these more than
we? The developers. Right. And the business, because they need it too.
Imagine you need to maintain that system, right?

Speaker 1 - 22:36
Imagine maintaining a system that you don't understand. Imagine
maintaining a system that there's no architecture diagram for it.

Speaker 2 - 22:42
That's really hard.

Speaker 4 - 22:44
Every system I've seen in my life, we've been there.

Speaker 1 - 22:49
Yeah, but then talk to the developers and see how stressed they are. Right.
And there's a reason why. Because they having to maintain a system that
they don't understand. And they do understand. It left long ago, right?

Speaker 4 - 23:02
Yeah, exactly. I would definitely love to see it in action. And I'm most
interested in the Gluing part. Look, there might still be things that will
require, like you said, the qualitative analysis of what's coming out.

Speaker 1 - 23:23
Here's the thing. Right? Every one of those requires qualitative analysis.
That's, for me, is the key piece of the puzzle. Every one of those outputs
has to be analyzed, verified in a way signed off by somebody who
understands the context. The difference is that scales because it's a one off
exercise. Right.

Speaker 2 - 23:48
Who is the person who will be doing that? Very often, I find, when I start
asking questions about the system, developers are very knowledgeable on
the classes they're using, the libraries they're using up to a level. Then
sometimes they have to switch off to someone who is like the DevSecOps
person or the ops person who knows the infrastructure. But then these
people, whenever you ask them about the business context, they can never
explain to you, why does this system even exist? What is the business
context?

Speaker 1 - 24:23
I agree, but think about this, right? So you do that exercise and you've
done the mapping and then the threat models in your head. You now have
probably one of the best views of the application, correct?

Speaker 2 - 24:40
Certainly, yeah.

Speaker 1 - 24:42
Because you connect the dots, right? You follow the things. Like you said,
you talk to the SecOps guy, he gave you this. You talked to the
development team, he gave you that. You talked to the business analyst.
Give the puzzle the problem. What you didn't left behind was a the
knowledge and the way to get that knowledge. So imagine doing the same
thing, but every time you ask that question, you put that to an LLM and
going and you look at the outputs of the LLM and then what you're doing
is you're confirming it's almost like imagine you're confirming that is the
creation of that knowledge correct? Is the prompt that created that
knowledge correct? Is this LLM that I use to create a logic correct?

Speaker 1 - 25:23
Because if it's not, then you have a problem, but if it happens to be
correct, then you know you have a good LLM, a good prompt that now is
able to produce, for example, a technical analysis that the technical
person confirms. Yes, that's how it works. That the business analysts go,
yes, that's how it works. And then if you add this to the mix that, for
example, this doesn't need to be right, because eventually we will be able
to fine tune it. So, for example, if there's a security vulnerability or you do
analysis, oh, that path is wrong, which is one of the things sometimes we
find in thread models, right, find blind spots. How your curves.

Speaker 1 - 25:58
The problem is at the moment you have no way to go and verify or to
change the logic that created the artifact, where in this case you have to
go back to whatever LLM or whatever prompt was used to create that
artifact and go, oh, we need to fix that. So again, these scales a lot more.

Speaker 2 - 26:21
Which then makes the threat model of the LLM even more exciting, right?

Speaker 1 - 26:26
Exactly, right.

Speaker 2 - 26:28
So not the threat model of the system, but of the LLM, right? So where do
you hold all this information? How do you keep it in house if you're a
commercial company so that you don't leak data inadvertently when
someone for a sample architecture from your company, right?

Speaker 1 - 26:50
But that problem starts to be solved already because you already have
private models, right? So if you use zero OpenAI, if you use bedrock, a lot
of those are already private models that they're not using your data, right?
And again, Google's Vertex already has massive claims on they say your
data is your data. Right, like that. But I also raised the question that in a
weird way, the less powerful and expensive LLM, the better, as long as it
produced the right results. So, for example, you already have a lot of
scenarios where with a good prompt charge, EBT 3.5 is better, faster than
4.0, right, so then you're right, the LLM becomes by far important, but we
can verify the output of the LLM, which is why I always say that the
feedback loop is so critical.

Speaker 4 - 27:51
Yeah, sure, there is definitely some prompt crafting that will need to be
refined. Difficult though, that's the bit that how do you verify? Are you
going back to the beginning where you're like, okay, well, I still don't
know what the end state is. No, but GPT verify with it because it already
has the information of end.

Speaker 1 - 28:24
State, then look, you verify it. Like for example, I would love to learn from
you on how you approach a thread model, but I can't at the moment,
right? Is or you might say you like to learn from me. I would like to learn
from imagine being able to get in the brain of Michael Howard when he
does a threat model, right? Or Adam schulshi. Go. That ground. Right?
But if I could see the prompt that you asked that helped to create an
output that you confirmed was correct, I could do that. And in this case,
it's you who verify it because you can look at it. Right. The problem is you
go from an art form where you go from A to an output which is in your
head, versus a by an LLM, the output you break a little bit.

Speaker 2 - 29:27
Yeah, it's breaking a little bit. No worries.

Speaker 1 - 29:42
I think you were yeah, maybe go to the serverless mode more talk about
serverless.

Speaker 2 - 29:57
Sure. Okay. Aisha would need to rejoin. She cannot hear, something broke
on her side. So how do you approach serverless? Right? So, yeah, it would
be great if Chatt would do everything for us, but at the moment it can't.
Or not everyone knows how to do it, so maybe it can, but we don't all
know how to use it that well to get the output. So we still have to do it by
hand. So how do we approach a serverless architecture? And I think here
the question is are we using serverless as it intended to be or are we taking
our knowledge from the old way of systems like we used to build them in
the early two thousand s and try to apply it to serverless architectures?
Right? So one thing that is crucial in the cloud is identity. Identity is the
perimeter.

Speaker 2 - 31:06
So how are we looking at identity? That's one of the first questions I ask
my stakeholders. So how do you identify your lambdas, your Azure
function with the services? They consume themselves and very often
they're still using passwords or they're using things that they shouldn't be
using. And even if they're using key vault, why even store the key as an
environment variable which can be leaked and not use the native identity
and access management functions or identity that you can provide to a
lambda function and thus have a very granular access to the services and
get rid of the whole password story. Right? So that's one of the first points
I usually ask for when I'm doing a threat model, because that's usually a
high gain, low hanging fruit that almost everyone is Ailing from.

Speaker 2 - 32:08
One other thing is, okay, we all know that there is a possibility for server
side request. So I trick the server, the function to do a request on my
behalf so I could trick it to dump environment variables I could trick it to
make a request to an external server. I could trick it to make a request to
something inside my network and get more data the function shouldn't
have actually access to. So the second question I usually ask when
discussing serverless architectures is, okay, identity is clear. Now, how are
you limiting connectivity for this function? Are you grouping them inside
network security groups or are you doing something to cluster them and
isolate them from the outside world?

Speaker 2 - 33:02
So those are like the first two points I usually attack when looking at
serverless architectures because you have to start somewhere and those
are like the easiest places to start and get some feedback. Hardly will both
issues be considered from the get go in any architecture I have seen. So,
Aishen, maybe you want to give a trick or two on how you do serverless
threat modeling.

Speaker 4 - 33:30
First of all, maybe I can talk about my gripe with it and the industry as
well. So while it is different, right, it requires cloud knowledge, it requires
cloud provider specific service knowledge as well, right? So let's begin
with that. In our industry, that is what you will need to have if you're
carrying out threat modeling for service architectures. And it also requires
knowledge around how to best securely configure them, how to best have
the state of your already existing infrastructure because it's sitting on top
of it as well. If we look at like an AWS environment, let's just go with AWS
example. Starting from do we have a multi account approach to all the
way down to which execution role is my Lambda using? All of that would
need to be so first graph is that it was fun when I did it.

Speaker 4 - 34:34
Not really doing a lot of them anymore, but I will still be championing for
incorporating infrastructure and configuration into threat modeling
everywhere I go, I guess. Yeah, so definitely it is so multifaceted. You've
got to look at your access management, you've got to look at your existing
architecture it's sitting on top of you got to look at what the application is
doing, which services it's using. You got to look at its perimeter or the
existing toolage that it can be using for security, for perimeter protection
purposes. I make it sound really gloomy. It is definitely possible and fun.
There is a lot of guidance right now. It requires sort of pushing threat
modeling outside of the generic idea of how we used to do it with Stride,
et cetera. But looking at it more from lower level details and then ongoing
checks thereafter.

Speaker 2 - 35:56
Do you think stride is still the way to go to look at serverless architecture?

Speaker 4 - 36:03
It was an example of a traditional way of approach of freight modeling.
Whereas when you look at services architecture, not only do we need more
people with that knowledge that we don't have enough of, but also a
different approach to threat modeling. Altogether.

Speaker 2 - 36:29
Yeah, I think Strive I heard the comment. I think it was Gary Macro who
made it. Or Brooke Schunfield. That stride was great if your business was
creating operating systems, which is the roots of the methodology in
Microsoft. Right. But I find it very limiting when looking at cloud
architectures because there's a lot more to consider. I mean, it's a nice
attack library when you're starting and don't know what to do next. And it
rhymes and it is easy to follow, but it's very limiting and it will not really
help you. And thus perhaps we need to change how we do threat modeling
as an industry and move a bit away from this simplified model of strife
because it's not really working for the cloud, I think.

Speaker 4 - 37:30
Certainly isn't. And there isn't really a specific framework that I've come
across with or specific approach that completely works because like I said,
it really depends on what service architecture you are, which cloud you're
on. Right. So now I'm working more with Azure. I'm trying to switch my
mind from AWS to Azure. There are many things that are transferable, but
also very different things as well. And another challenge when you're
threat modeling for service architecture is some of the strings that are
being pulled for those configuration. For example, IAM, Role, et cetera,
may be centrally managed. So you're looking at not just your app teams,
but also platform teams as well who are providing that sort of backbone
to developers to build upon.

Speaker 4 - 38:29
So developers may not even be aware of that sort of threat, let alone you
explaining to them, take any action for it.

Speaker 2 - 38:40
Sure. One of the challenges, especially at smaller or small companies
startups, is they get a crew of developers to create the application and
that is fantastic. They are creating something new from the ground up.
But then who knows something about the cloud? Who knows how to
design a cloud? So if you tell them about a hub and spoke network
topology, they will just look at you with empty eyes and hate you internally,
right. And tell you that's probably not something I can do. Can I delegate
that to someone else? Why don't you do it? That's a big challenge because
they know about development but they don't know about the cloud. And
then this knowledge impedes creating the right thing. So they might come
to very wild ideas and want to open SSH for the VMs, if they have VMs to
the outer world.

Speaker 2 - 39:43
Because how do you then log in and you tell them, hey, there's passing
host and there's VNet and pairing. And they're like, I don't have time for
that, I have to do business value. You're just slowing me down. That's not
how we do things here.

Speaker 3 - 39:57
Can you guys hear me okay? I've stopped at service, actually. And by the
way, Aisha, you are so spot on with infrastructure. Don't lose that bone.
Right? That is absolutely critical, right? Keep on that one. I think there's a
couple of parts here, right? I think there's the part of understanding the
environment, understanding what are we looking at, right? And I think
that's more binary, right? It's like visibility. Do you understand it? Do you
know it? And the nice thing of serverless is, I would say standardized a
couple of layers, if you think about it, right? If you compare, for example,
serverless with other architectures, by definition they are other
architectures, right? You might have a net framework, a spring
framework, this framework, that framework, this thing, an EC two
instance running a Kubernetes, all those flavors.

Speaker 3 - 40:44
The good news of Kubernetes is that lambda, it normalized a number of
things that exist. And I actually think that what's missing a bit in our
industry is a couple of templates. Like you were saying, you're saying,
look, we know that in lambda functions, this bit is provided by the
infrastructure. But you need to look at that. You need to look at this. You
need to look at this, right? I'm a big fan of chain thread models, almost
like and threat modeling is by layer, where you almost say, for example, in
a way, you should do a threat model of your hello world lambda, right?
Like, if you take the hello world environment in a particular deployment,
what does it look like? What threads do you have? Because you might get
a whole lot of threads already, a lot of risks.

Speaker 3 - 41:27
Just by the way it's configured, right? By the permissions it's given, the
environment is running everything that's sitting next to it. Like you're
saying Lou is like, what's next to it? Right? So if I can go from that
lambda function, this to that, to know that's massive, and that's just
before you add a line of code to it. But the good news is, again, we can do
that, right? So we can then say, by the way, this application, if there are
any server side requests, include vulnerability, for example, it's game over,
right? Because there's no other protection or it's okay, right? Like it's
nicely segmented. The Im rule is really locked down. There's not a lot of
secrets, et cetera. And you're right, that is specific.

Speaker 3 - 42:09
But on the other hand, I would ask, and I would say that the cloud
providers should give us these threat models, or at least we have a
community driven threat model. And that's the reality. And in fact, it
should be vetted by the experts.

Speaker 5 - 42:24
I mean, you have some of it, right? AWS has a security paper for every
single one of their services, and that is a bit a threat model.

Speaker 3 - 42:33
Now, it has to be in a threat model structure, right? By the way, this is also
where I think the LLMs will help a lot, because I think they can help us to
understand this and to create customized views of this, right? But we need
those layers, we need that analysis. And this goes back to that point.
Verifying it, right? Like you want the experts to look at that and go yeah,
that is correct. That's not correct. For example, if you talk about tricks on
lambda functions, I would say one of the big gotchas that I don't think a
lot of developers are aware of, an architect is the fact that the cold start in
a lambda function actually means that you have state between sessions.

Speaker 3 - 43:11
Which for me was really weird because I thought the whole point of
serverless was not to have state between requests. But it's not true, right?
Like if you start a lambda request and if you start a process and the
request ends and the thing is frozen, but that process will still be there the
next time the next lambda invocation, you add a file to disk, guess what?
That file will be available the next time it's invocated. So that means state
can actually be a massive problem again, depending on your application,
depending on what you do. Right, but those are specific. And here's the
thing.

Speaker 3 - 43:48
When you go from one platform to the other, I always find actually, the
security documentation to be really good to tell us what actually changed,
because the security crowd tends to ask how it works, what is actually
going on here? Versus sometimes the Dev crowd I can focus more of how
does it work? Oh, it's still python. Oh, I haven't changed my code a lot.
Cool, let's go.

Speaker 1 - 44:08
Right.

Speaker 4 - 44:08
It's either security or Phenops that will have the bird eye view because
they want to see exactly how much it costs. What do we have here? And
security wants to see how is it?

Speaker 3 - 44:20
So my point there was that I think there's one element which we need to
understand how it works. And that's what I was saying, that we very align
with the tech crowd and the business who also would like that. But like
you said, Louis don't have the time, they haven't been given the time. And
the reason they haven't been given the time is because they haven't been
asked or it's not seen as a requirement to deliver and that's the main
reason why they don't do it. Right. But I think there's the other part of it
is, once we have that, how do we do security reviews on top of that? And I
think strides it's a good one because it's a waste to start.

Speaker 3 - 44:53
But the best malls experience I had is when I had teams that would do as
much as they could with stride, with this, with that. And then I would
review it, and I find myself being insanely productive because it's almost
like they've done the legwork, they've done the bits, and all I would find is
the blind spots, in a way. I would then use a bit more security experience to
go oh, what about this? What about that. The good news is they learned so
they wouldn't make the same request again. So it's almost like it was a
great way to feedback, because in a way, it's almost it didn't matter if in
the beginning they missed some threads. What matter was that they got
the documentation, they got the structure, they got the flow, they did a
first pass.

Speaker 3 - 45:31
And you know what happened in the end, which I found really funny? I
became a voice of reason, which is really weird for me, because they will
go over the top, right? So suddenly they will have these massive threats
about a gui that's not random enough. And I was like, Right, guys, went
from Incremental 12345 to guides, right? Okay, right. But it's interesting
because then again, developers and sometimes security crowd, they can be
quite binary, right? But that was great because then we get to define the
risk appetite, okay? And also we can find standards of how we want things
to happen, right? But then we need to collaborate a lot more. And I still
think that and this is I go back to my LLM.

Speaker 3 - 46:19
It's like if what you do is a prompt with data, with the output that you
verify, we can now share those LLMs. We can share that prompt. And
those prompts are important because there's an art form in how to create
that. But imagine, like, even know when you're describing I was imagining
a prompt. I was imagining a prompt, which is right here is Louis first five
questions for a dev team. And then you can see that to a bot, and you go,
hey, guys, can you talk to Louis bot? Lewis threat modeling bot, right? And
that has your first five questions. And then imagine you're taking that, and
then that create a nice view for you. And then you're reviewing that and
you go, oh, okay, guys, can you ask another five questions here, right?

Speaker 3 - 47:04
So that allows you to scale a lot more and allows, in a way, your team to
scale a lot more. True.

Speaker 5 - 47:12
I mean, take my money, where do I buy it?

Speaker 3 - 47:17
But we're not that far. This is what I think is cool, right? The reason I'm so
excited about LLMs these days is because forget about all the other crap,
right? That has tons of problems. But this is real. This already works
today. And in fact, the Chat GBT that we have, and Claude Too and
Copilot, they already do this really well.

Speaker 5 - 47:42
I think that's interesting. Can I ask Copilot to create a data flow diagram
of a project you can GD code?

Speaker 3 - 47:53
Well, the thing about this, you have to understand how they work, right?
Because you have to understand the context window. Does that make
sense when I say that is what you put in the middle, right? And that's
limited. So they cheat. They don't cheat. What they do is they do an ounce
of analysis and then they feed that in. So you can totally go to Chat GPT
or Copilot and say, here's a bit of code, give me an architecture diagram,
give me in fact, the latest visual element of Chat GPT is awesome because
you can now do a fucking diagram, right? And then going, Boy, dude,
analyze this. And you can say, hey, does this match the code right?

Speaker 4 - 48:32
Inherently doing it? Or is it like a plugin that you'd have to use for the
diagrams? Because I've not tried that one before.

Speaker 3 - 48:39
So Chat GBT, they annoyingly only well, they've been doing that for a
while, but well, at least in UK, where I am, it got released a couple of days
ago, four or five days ago. So if you go to Chat GBT, well, you need to use
the paid version, which you should invoice your company, right? That's
what I always tell my team, right? But the paid version had the advanced
data analytics, which is pretty awesome, by the way, if you guys haven't
used that. Again, that is pretty insane, right? The data analytics, where it
writes a lot of the code, you can ask all sorts of cool questions and
visualizations, but the second part is they just added the ability to upload
an image. So you can literally upload that's what that guy was doing, that
dude that was doing thread modeling.

Speaker 3 - 49:18
I think one of the persons, like, you upload an image, a diagram, and then
you start to connect from it.

Speaker 5 - 49:25
That's the one I saw. I found the potential exciting. If I were working for
EU's Risk, I could be a bit scared.

Speaker 3 - 49:33
Well, they need to leverage it, right? Like, this is the thing, right?

Speaker 5 - 49:37
It's a chance and it's a threat, right? With two s. Either they are caught by
it or they cut with it.

Speaker 3 - 49:45
A lot of this I did a presentation yesterday, which I've been doing recently. I
said, look, you should be panicking and be very excited at the same time.
And if you're not, you're going to be like Nokia, right? Like Blockbuster,
right? The only difference is going to happen faster.

Speaker 5 - 50:03
Definitely.

Speaker 2 - 50:06
That's exciting.

Speaker 5 - 50:07
Now, the companies, especially big companies, are risk averse and new
technologies excite many people. But then it falls to us in the security
department to do the risk and compliance analysis and determine whether
the risk or the use is more or less for the company, right?

Speaker 3 - 50:28
So we pushed a policy, by the way, I'm trying to open source, but I'm glad
to share it. We pushed a policy that fundamentally said don't connect with
the outside world yet, because the prompts we don't really control, but for
internal use and internal workflows, don't put any personal data on it and
it's okay. And this was Chat GBT, so we actually about to push and update
that policy because we're now devopsing our policies, right? So we're
putting an update to our policy where we're actually saying, if you're
using OpenAI or if you're using AWS bedrock, you can start to put,
especially if you can control the region where it goes. So you can start to
use it. But I don't think most of the use case we needs a lot of advanced
cases. It's just people learning how to use it, right?

Speaker 3 - 51:12
That's the thing.

Speaker 5 - 51:15
Definitely. Everyone needs to learn how to use it because it changes how
you interact with machines, right? But the question is, right now everyone
wants to use it and then someone has to do the analysis and someone has
to determine the risk and the policy needs to reflect this. And yes, it's what
you're saying, Dennis, definitely. And it's also the fine print.

Speaker 1 - 51:40
In.

Speaker 5 - 51:40
The terms and conditions of the AI companies.

Speaker 3 - 51:45
And by the way, if you do a threat model on chat CPT or prompts from the
outside world, it's ridiculous, right? Like went from having raw SQL, to
having people concatenating strings, to having parameterized queries hey,
cool, right? At least some level of security, to now prompt engineering,
which is like SQL injection on fucking steroids, right? Because in principle
you can modify the whole behavior of it, right? And that problem is not
solved because we don't understand the layers. In fact, I had an amazing
conversation yesterday where were talking about what happens if you
train a model with data, right? Customer data, right? And this is a DPO,
right? But then you do an erasure, right? So now you need to go and
remove the data for that user from your model. You can't, right? Exactly,
right.

Speaker 5 - 52:34
You need to retrain the model.

Speaker 3 - 52:35
You need to retrain the whole model.

Speaker 1 - 52:37
Right?

Speaker 3 - 52:37
And that's why I was kind of saying that I think the future of this is
actually to have highly specialized models who have reason, and then the
data is what we feed into it. That's the difference. And that's why when I
was saying about the code, it's like you have the raw code, imagine chant,
GPT analysis or whatever of each one will give us this value and then that
analysis gives us the next one, and then the next one, and the next one.
And as you go up this way, you start to get the bigger picture, right? You
start to understand the method view. But we can do architectural
diagrams on every single layer here, right? And the beauty of this is that
you can be here and you can say, oh, let me feed the infrastructure view,
right?

Speaker 3 - 53:18
Let me feed the business view here. In the past, this was impossible. That's
why people didn't figure out how to do it, right?

Speaker 4 - 53:25
That's easier to control when you want to centralized in a centralized way.
Highly specialized decoupled solutionizing.

Speaker 3 - 53:38
And serverless is actually an interesting example because the problem
space is smaller. Like for example, Lewis, imagine the scenario just talked
about to say, look, you should be using IAM policies IAM groups IMS for
service to server communication instead of passwords. We can now go
from a mode where imagine I can train a bot or give a prompt that is
focused on that I can train a bot to say, your job is to find this. If you find
this, here's our guidance, here's the technical documentation of how to do
it, provide information to the dev of how to do that transition and the
tests. So that prompt I just said, it would have been millions of pounds of
engineering to pull off. Now it's realistic.

Speaker 4 - 54:25
Are you talking about like remediating it?

Speaker 3 - 54:27
Actually, yeah. So this is where you can go from almost identifying to
remediation, right?

Speaker 4 - 54:33
Yeah. So imagine I'll give you another use case. It's already possible with
AWS, for example, let's talk about lambdas, right? So you give an
execution role to lambda, which can be an IAM role. It can be as
permissive as you want. So one of the best practices and secure way of
doing it is not allowing it like an admin level permission. And AWS has this
service that they also provide, which is it runs the lambda, does exactly
what it carries out the execution, sees what it's doing, tells you exactly
what to include in the permission policy. That's how you can formulate the
role. So you can get that entire process automated and implemented with
no impact on the application at all because you know what it needs to do.

Speaker 3 - 55:26
And if you train a bot to provide that, it can have guidance, it knows what
inputs to get. So a really crazy feature which is really good on chat DBT is
ability to have functions. So you can say, here's an API that depending on
the analysis, can give you the functions to call. So you can have a prompt
that eventually go, oh, now can you go and get me the change in IAM
policy? So the bot can now even start to react with live data and then say,
oh, actually, no, sorry, that configuration you made actually didn't make
an effect or is going to have this problem or blah, blah, blah. So there's a
level of intelligence that in the past we couldn't do, that we can do.

Speaker 3 - 56:10
I think we in fact, the next session, which we're going to have, by the way,
you guys should join because me and Sarah are going to do it. But I think
it's very relevant to what we are doing here, which know the chat GBT
gen AI privacy, right, which is I think is a massive uncertainty, but I also
think it's a massive opportunity because I think we can now do privacy
analysis that in the past was impossible because we couldn't scale. So I
think it's, again, one of those two angles. So, any final comments and
notes on the serverless since we're just finishing this one off?

Speaker 4 - 56:47
No comments. It's been really lovely talking to you. It's really informative
as well. So I'm definitely going to clear up sometime tomorrow to look up
the data analytics GPT site. I won't be able to join, but I'll watch the
recording, so it sounds really interesting. Nice chat.

Speaker 5 - 57:06
So from my side tomorrow we'll be doing another session on threat model
in Qatar. We'll be looking at a serverless architecture this time so as to put
into practice what I've been saying. Now, you've picked my curiosity and
this not being a work system, but a play system I just invented. I think I'll
try to get something from Chattypt and perhaps even fail. Live tomorrow
on that, but let's see how that goes.

Speaker 2 - 57:34
Cool.

Speaker 3 - 57:35
I'll join in, help you with that. Thanks.
