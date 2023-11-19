---
title        : Kubernetes Clusters Network Security
type         : working-session
topics       : Kubernetes. Network Security
featured     :
event        : mini-summit
when_year    : 2023
when_month   : Oct
when_day     : Mon
when_time    : WS-17-18
hey_summit   : https://www.linkedin.com/events/7110035220086575104
session_slack:
#status       : draft
description  :
banner       : https://github.com/OpenSecuritySummit/oss-website/blob/main/content/sessions/2023/mini-summits/Oct/banners/Network%20Security.jpg?raw=true
organizers   :
   - Dinis Cruz
   - Nathan Case
  
youtube_link : https://youtu.be/u47zb0zJ1X4
zoom_link    : https://us06web.zoom.us/meeting/register/tZUvdO2qqTIoGdyk4oKgHK48W1-Dj5cvXEuk

---


## About this session
Description: Learn how to secure network communications and segments within Kubernetes clusters to thwart unknown threats at the network level.

### Outline:
- Implementing network policies in Kubernetes.
- Network segmentation for enhanced security.
- Monitoring and analyzing network traffic for anomalies

## Transcript:
Dinis Cruz - 00:00
You. Hi. Welcome to this open Security Summit in October 2023. And I'm
here with Nathan, and Mario is going to join in for a bit, right? And we're
going to be talking about Kubernetes Clusters network security, or I guess
Kubernetes security, right? Because that's really the key topic. So, Nathan,
why don't you kick us off?

Nathan Case - 00:22
So I guess the question becomes, like, as we look at this whole thing, first
of all, hey, I'm Nate. Secondly, my views are my own. Yada, yada. Not the
company, all of that. But today, as we speak about this, the real question
becomes kind of this discussion about what is security and what is
network security in Kubernetes? And what can you expect? What should
you expect, what should you hope mean? When you asked me to do mean,
like, honestly, I kind of sat back and okay, like, I just did a talk about
Cubeshark. We can totally talk about Cubeshark. The company I'm
working for, CORSIA, has a new product called Cast, which is kind of an
extension of Cubeshark. And there are new things that you can do there.
There are a handful of stuff on open source projects we can look at online.

Nathan Case - 01:05
But when it comes to actual security, I mean, what do you guys think? It
feels like the network security of days gone by when I used to play with
switches and hubs and routers and coax connections, all of that's gone.
And I think we end up with this really interesting, logical setup that,
frankly, hasn't existed before.

Dinis Cruz - 01:25
One of the things I've done, which I still feel it worked quite spectacularly,
was to build a large number of very small clusters. And I arrived there
from a point of view of having the least amount of moving parts by having
lots of problems with scaling, right? And this was a project where I had to
go from small amount to file spring process to large amount of files. And
there's this interesting spot where you start to fight Kubernetes, right? You
start to fight the system, and then it's kind of like this thing where
eventually everything starts to break, right? Because you either struggle
with the backplane, you struggle with the network, you struggle with the
ability to start new pods.

Dinis Cruz - 02:15
It's almost become, in a weird way, I felt this anti pattern that suddenly the
more stable things become, the more locked things become, the more solid
they were. But I was like, hold on. The whole point of Kubernetes is this
dynamic load, right? It's go up, go down, go up or down. So I started to
go into this mode of, okay, what's the smallest cluster that I can do?
Because in a way, the irony is that it's almost like you go, okay, you need
multi nodes, you need multiple big clusters, because you get resilience. And
I start saying, yeah, but I'm actually losing quite a lot, so I start going,
okay. So I got to the point where we created one node, and it was one
node cluster that had one, basically deployment. We had very small
number of pods that were per application.

Dinis Cruz - 03:08
And then the thing that was really interesting is that from a design point of
view, it really forced you to think, where do you store things? What's
persistent, what's not persistent? There was tons of problems that existed.
It's like the HS two. I don't know if you're in the UK or not. Are you in the
UK?

Nathan Case - 03:25
No.

Dinis Cruz - 03:26
Yeah, there's a big shit show here because we had this massive megalomial
project of building one thing super big, right? And then of course, he blew
up. Costs got bigger and bigger because the complexity got bigger and
bigger with the project. Right. When I was basically thinking about this
was like, small clusters actually have lots of advantages because you can
scale up and down very easily. The only question there's a bit of state. But
in a weird way, I like that problem because it forced me to take state away
for sometimes parts of the cluster which actually make the cluster itself
disposable, because it's almost like, think about it, we take Kubernetes, the
parts should be disposable, but then are the nodes disposable and is the
cluster themselves disposable?

Dinis Cruz - 04:14
Because or else you end up with this gigantic cluster that by the time it's
up, nobody really understands how the cluster is actually being set up,
right?

Nathan Case - 04:25
To me being the old guy and saying that to two old guys, but rolling this
all the way back to the day when we used to have Sans and deal with a
Brocade fabric infrastructure and deal with VMs that would sit on top of
that. And then you deal with network switches and blade switches that
would have to sit on top of that. As we start looking at resilience and we
start trying to understand what security is, and I say this because it feels
right to me, and push back, please, if you think I'm wrong. And like, you
would never but still, the concept being that one of the things that was
always really hard was to understand the impact of all of the pieces, parts
that went into the whole thing that you were building and we used to have
to deal with.

Nathan Case - 05:11
This is my backplane. And my backplane is going to support 20 gigs. And
if we have a 20 gig backplane, that means that I can sacrifice ten gigs for
network and ten gigs for storage. And then all of these things start coming
in and it feels like we're back to almost the exact same thing with
Kubernetes, where I've got a Kubernetes cluster and now I've got to figure
out what are the actual resources that I've got the ability to begin to
architect with. And if I start to build out an application that goes over
those resource bounds, then it doesn't really matter anymore.

Speaker 3 - 05:42
I think there's a few things from my perspective, what I see these days is
that obviously Kubernetes has a layer of abstraction, but people do not
intimately understand because you have a number of layers. You have the
whole container security. You have container networking security, and then
you have obviously host supporting the container security. So people do
not understand that. How do you apply security context at the container
level? Then you go into something like Open Policy Agent Apparm, or how
do you secure intercontainer communication? And then you go into
runtime security, something like Falco deployments. There is a lack of
knowledge and understanding because most of the containers building is
done either via DevOps or developers themselves.

Speaker 3 - 06:34
So having we discussed in previous sessions how we can build those
security reusable blocks, so how we can whitelist a number of container
images that has specific security solutions already built in. So you say just
use this. There's a big disconnect, I think, especially when you start
leveraging things like AKS. If you run a production cluster, you get
obviously Microsoft image that's quite secure. But then if you run the dev
clusters, you use all sorts of images. There's obviously riddle with
vulnerabilities. How do you address the change between development
cluster and production? Because obviously people testing code in various
environments, but if they don't match but.

Dinis Cruz - 07:15
That'S the beauty, but even beauty of small clusters. See, the beauty of
small clusters is that you can run them locally. So you have the same
cluster throughout, right? I always felt that the only difference between
local pre prod, so local dev, QA preprod prod, the only difference should
be scale.

Nathan Case - 07:38
That's why I'm pushing back to the resource question, though, frankly,
because as you start looking at deploying into Azure, you look at
deploying into a cloud provider, take your pick of who all of a sudden
you've deployed to two data centers, and those data centers might be 100
miles, 150 miles apart. So now, as we look at if we're looking at security
from the vulnerability question that you just brought up, or the question
generally that Marius just talked about, where we start looking at the
images and all the other pieces that go into your Kubernetes cluster, what
does it become? Does it become possible for me to evaluate network
availability, latency things that I normally would have looked at in a
networking implementation for a larger enterprise?

Dinis Cruz - 08:21
Not really. Well, see, this is the thing. If you have smaller clusters, right,
you can simulate all of that because and by the way, smaller could be two,
three, four, or five nodes, because the cluster or the cluster of clusters,
right? That environment is the app, right? So the thing about that, for
example, that particular example is that if you can spin up your
environment, you can now run your simulations, right? You can say, okay,
now give me this traffic, now do this so what was very interesting is that
were able to build very focused testing tools. Again using kubernetes,
right? Actually, using lambda functions actually was really cool to scale
up. That could generate an insane amount of traffic. But we able to test,
you know what we found? We found that check this out, right?

Dinis Cruz - 09:12
There was a moment where I was deploying the same Kubernetes.
Remember, this is one node per, but each EC two instance is a Kubernetes
node. Each one, right? Each EC two instance is a Kubernetes node. We did
this test where I was running, I think it was about 150 EC two instances.
So I had 150 clusters across. I think it was five data centers. And then you
had 15, right? Basically, because I got to the point where I built a
command line. It was very scary, right? Because I had a command line, I
was like, spin this up. How many regions? How many easy to instance per
image? And it was the same image everywhere, right? We will run it. You
know what happened? After a while, we start to detect wild
inconsistencies in AWS infrastructure, right?

Dinis Cruz - 09:59
So you would have literally the same request sent to 150 instances, right?
And every now and then and we will keep turning the volume up, right? So
we keep finding the point where they were really hot, right? And there was
instances that were fine all the time. There was instances that had a
wobble and there was instance that had fucking leisure heart attacks,
right? And then when I realized and I remember chatting the AWS guys on
it's like, yeah, because it depends on the neighbors. But think about it.

Nathan Case - 10:31
Neighbors and a whole bunch of other infrastructure.

Dinis Cruz - 10:35
But think about what that means. It means that we had to add code to our
clusters to be aware of your environment. So even if you think you have 20
gigs, you might not have 20 gigs.

Nathan Case - 10:47
And that's exactly what I was getting at, was plan the resource plan
outright.

Dinis Cruz - 10:52
But no, but this is the difference. It's not even planning is your cluster has
to adapt itself. So we had a mode where and, you know, the beauty of this
architecture is you put load balances in front. You know, what was the
solution? Actually, eventually, the solution was kill it. Literally, we got to
the point where once the health checks got to a point, reduce the traffic.
So take it off from the load balancer, let it die off and kill it. And even
AWS guy says, yeah, that's the better way. Because if you start a new one,
you're going to a different location, right?

Nathan Case - 11:23
Yeah. And that's the point, is that in many cases, really, what you want to
do is set up this setup where you're looking at multiple points in your
application. And if there's a particular instance that's not working
correctly, you need to know. And that might be just setting up a simple I
mean, I've done it before with pings. If you can't ping X or you can't get
an Http response from just kill it.

Dinis Cruz - 11:44
Yeah. But try doing that at node level and it's very hard.

Nathan Case - 11:48
It's hard, yeah.

Dinis Cruz - 11:49
That's why the smaller again, the cluster. And then for me, the solution
here was to actually create clusters of clusters, even app, because then you
can say, what are all the resources?

Nathan Case - 12:02
But then I'm going to push back and say, at what point have you gone too
far? At what point have we abstracted to the point of just the silly? Would
it have been easier to just use, I'm going to say elastic beanstalk.

Dinis Cruz - 12:16
Well, there's a point where lambdas might be perfectly fine, right, but
that's a very valid point. There's a point where, in a way, there should be
an evolution, right. There's a point where lambdas are not good enough or
too expensive, right. Then that's when you go containers. And there's a
point where containers gets too big, that's where you go to the cluster and
the moment where in a way, I think it's almost like we try to optimize
something that should not be optimized, which is this idea that, oh, I have
one cluster, I have five clusters. Usually people don't have five clusters.
They have one big fuck off one and a couple of redundancy ones. Right. At
least that's what I've seen a lot. It's very risky, right?

Dinis Cruz - 12:54
It's very risky because it means every time you push a new update, you risk
blowing up your entire cluster.

Nathan Case - 13:00
I think Marius has got a point here, but after Marius goes, then I've got a
point back to you.

Speaker 3 - 13:04
I think that's where you mentioned kind of I think if you discussing
Kubernetes deployments, obviously it comes down to cost, but you need to
get to the point where you can ultimately run a proper chaos shop, where
you can inject faults continuously to evaluate where the problems occur.
So being proactivity then, instead of reactive, and then you can plan,
because obviously you foresee particular growth, whether it's traffic,
customer acquisition and things like that, where you can potentially get
ahead of the curve where the problems might occur. And that will feed into
your design questions, essentially.

Nathan Case - 13:47
Yep. And I think you're hitting exactly what I was going to hit Marius, and
apologies, I'm a little under the weather today, but I completely agree with
you. This is security and resilience by design. You can't just pretend that
it's going to be OK because you're using Kubernetes and building your
application so that it is aware of both the infrastructure that it's on and
frankly, the limits of the infrastructure that it's on. And if it realizes that,
you know what, I really can't get to this machine over here, maybe it's
time to spin up another alternative because I'm not working right.

Dinis Cruz - 14:21
I think the bit I like to expand more in terms of security is I always find
that the less moving parts, the better, right? So if you take that to an
extreme and this is where I feel there's a potential that we haven't fully
fulfilled here, which is that we should be absolutely brutal, for example,
with the size of images, absolutely brutal with what's inside the
containers, even what's inside Kubernetes. It's not because the normal
Kubernetes deployment has these features that you wanted. It's almost
like, what is the minimal viable deployment that you can do? But here's
the problem. This is the thing that I don't think you experience until you
really experience kubernetes as a disposable unit is that if you can spin up
kubernetes clusters super easy.

Dinis Cruz - 15:08
And by the way, at the moment, last time I checked, AWS clusters or azure
clusters still take, like, minutes, and I'm like, what the hell are they doing
playing chess, right? A cluster should start, right? So if your cluster
doesn't just start super quickly, you can't experiment, right? Think about
it, every experiment takes ten minutes, 2 hours, whatever, and you can't do
that so you can't lock things down because you need the interactivity of
the experimentation.

Nathan Case - 15:36
Let's be honest, I mean, it's expensive to experiment that way sometimes.
Just in full disclosure, I have four clusters in my house right now, so it is
what it is, and it's just what I'm running here at home, and that's fun and
I'm enjoying it. There's no real reason for me to run Kubernetes in the
house. I mean, come on, that's just silly, but at the same time, it adds
value, right?

Dinis Cruz - 15:58
You can experiment, right.

Nathan Case - 16:02
But back to your point, and to the point that in general, I think there's
some point at which we're going to have to start looking at what is the
minimum viable container that we can actually run. So it's become more
and more concerning to me as we've talked about different software
supply chain attacks and seen different reality as we look at network
security, that's fine. But the reality is, if my implementation, if my image is
so bloated with, I've got a full installation of Take Your Pick of OS, and
then I'm running my little app inside of it.

Dinis Cruz - 16:34
I really like those light images. Right.

Nathan Case - 16:37
Well, the hardened images, yeah, I think we need get to the point where we
just automatically run a script at the end of it and it looks at it and goes,
oh, I see you're just using these three things and rips out.

Dinis Cruz - 16:45
So here I'm going to bring the good old these days, gen AI, right? And
LLMs, that's another area where I think it can add crazy value. Imagine a
world where we take an image, we feed it to a Gen Tweaked, an agent
that's been tweaked for understanding that, and we say, Start removing
things, right?

Nathan Case - 17:05
I don't even know if we need Gen AI to do it. I mean, can't we just do it
with a basic process, call and figure out what's running because you need
contact.

Dinis Cruz - 17:11
Okay, I think you could do it like that, but that's very complex, very fast
because I think you need a level of reasoning, you need a level of logic that
is very hard to code. And I could see how having an LLM that has a series
of prompts and maybe not one, maybe two, three, four or five LLMs
working together, I could see how that's much more usable and practical
than trying to code. Because to be honest, I think people have tried to do
it. The problem is you need a degree of context, you need a degree of
understanding and even what's the objective that is very hard to code.

Speaker 3 - 17:50
Yeah, I think you can leverage Geni in a few things because as we
discussed in the beginning, things like mapping of the traffic between the
specific containers. So Genai potentially could help you build a map. Who
needs to talk with what? But I think, as Nathan mentioned, I think we
need to take up a notch because the one thing that is always missed yes,
we do in agile sort of deployment and agile code changes and all of that,
but drift Analysis, it's one sort of area that's always neglected.

Dinis Cruz - 18:31
What do you mean?

Speaker 3 - 18:32
Leveraging something like Open Policy Agent where we can define how
our production clusters should look like to make sure that we are alerted
from people a making mistakes and B just going berserk on some new
innovation that they decided, oh, just deploy and see what happens.

Nathan Case - 18:54
Even if it's just a basic like I'm using this open source library and today it
changed from A to 8.1 and all of a sudden it's pulling in a bunch of other
stuff. I mean, just the drift associated with that alone is significant. And
not looking at the packages, not really understanding what the packages
do or not understanding some of the impact of those subs is going to be an
issue. And it's great to say I've got my S bomb and yay, but if you're not
actually running it while if you're not getting an S bomb that actually
includes all of these other things, I'm not sure it really matters much.

Speaker 3 - 19:28
It's not even that. I think what you just mentioned, it's a very important
area to address. I think loads of developers do not understand even how to
build a secure image. What's the best practice in terms of building as
minimal image as possible, making sure that it doesn't run unnecessary
updates and just pulls the correct packages that it only needs to run.
That's another area where supply chain is a massive task at hand.

Nathan Case - 20:00
It's true.

Dinis Cruz - 20:03
And that is an area that I think the new generation or the next generation
of bots can make a massive difference. Right, because understanding that
context is really hard and I feel that being able to explain the intent, like
you just said, imagine Nathan, take that simple case. You want to be able
to describe. This is a mission critical system. It has his properties. I expect
this, I expect his blast radius. I expect that is something that we can now
start to describe, to try to codify that will be crazy difficult. We can
describe that behavior. And then we say, by the way, here's a Kubernetes
config file. By the way, here's a helm chart. Is that helm chart going to
break this particular situation? Look, I've fed TCP dumps, even git
commit. Have you fed a git commit to Jtpt?

Nathan Case - 20:57
No, actually I haven't ever tried that.

Dinis Cruz - 20:58
Dude, it's freaking awesome. Look. So we're now using it to create
change requests, right? And then to describe pull requests. So imagine a
flow. You know what I found really interesting is as a developer, I actually
enjoy reading that because I found that it described nicely what I was
better than developer. And sometimes I go, oh, shit, yeah, I missed that
one. Actually, I did change that in the code. But also, even when you make
a little mistake, it doesn't matter. You tweak it, right? So it's still your text,
it's still your pull request, it's still your commit, but the quality and you
can also say, give me a business analysis. Give me a technical analysis.
Give me in fact, can you say, give me a security analysis of that? So
imagine that world where imagine that for a helm chart.

Dinis Cruz - 21:46
Imagine having a helm chart that describes that.

Nathan Case - 21:49
Now timeout before we tell everybody that's ever going to watch this
video to go out and find yourself an LLM and ask it to look at your git
commit and your code. Please make sure you've talked to your CISO,
looked at your internal governance policies, and made sure that you're
allowed to do this so that information doesn't accidentally fall into the
wrong.

Speaker 3 - 22:07
Property.

Dinis Cruz - 22:08
Have Pet open source project that you can do that solves that problem.

Nathan Case - 22:12
Sorry.

Dinis Cruz - 22:13
No, that was good. Exactly. Yes. Don't go and face their confidential
disclaimer into Chat.

Nathan Case - 22:20
Well, actually, I feel like I need to say this now. Sorry.

Dinis Cruz - 22:23
Well, but to be honest, I think we can already say that these days you
really should have private models. Right? Look, Azura has pushed
bedrock.

Nathan Case - 22:29
That's a great thing to say, but man, the private models aren't nearly as
good as the public ones. And it's always going to be that type of thing.

Dinis Cruz - 22:37
Yeah, well, Azure OpenAI is not that bad. I think it's treadling really close.
Yes. Chat GPT. By the way, have you tried the model one where you can
upload an image?

Nathan Case - 22:50
No, I have not yet.

Dinis Cruz - 22:52
Simon Worley was like that's the game changer. I think it was really a
game changer before that. But I agree that's a game changer. Dude, you
can now do an architecture diagram, go to Chatty bikini and says, give me
an idea, transcribe this, give me a flowchart, give me this in plan to ML,
give me this in thing, right? It is pretty freaking cool, right? It's a big game
changer, right? But I think the point were just talking, which is how do
you create a small possible Kubernetes cluster, for example, or a small
possible image? I think in the past that was really difficult to do because
you couldn't explain intent. And I think we're going to be able to start
describing intent, right? And in fact, you'll be able to start describing even
an image.

Dinis Cruz - 23:39
Imagine being able to build an image where you say I want this image to
be unusable apart from port 80 and apart from Nodes or Python or Go or
this binary. And that's it. That's all you should have. You should have what
is the minimum viable Linux environment that is required? Start deleting
everything else, right? In fact, experiment, do chaos on top of it, run it, run
your tests and then start deleting stuff that you don't think could be
usable, right? But imagine doing that in a way that we can describe it,
right? And imagine that the next generation of an Llam that actually
understands the Linux kernel.

Nathan Case - 24:18
Well, yeah, I was going to say, I mean, go so far as to say that I've done my
Git push and we've gone through the whole thing at this point. And instead
of the build that we would normally do, it actually goes over to the LLM.
The LLM builds out the image that would be appropriate to what you just
asked for. And it's only those things as opposed to everything else and
there's really no interaction whatsoever. I mean, none of this stuff is
rocket science as such.

Dinis Cruz - 24:42
The only thing I would say there the caveat, I would add, and I think this is
where I think some people I think are flipping. So I don't think the LLM
builds it. I think the LLM analyze creates the pull request.

Nathan Case - 24:56
I was going to say propose a.

Dinis Cruz - 24:57
Modification and then there's a build pipeline.

Nathan Case - 25:01
That was I would go so far as to the hardening scripts, almost, and I
would agree with you where you're just looking at the hardening scripts.

Dinis Cruz - 25:06
And then the other variable here, I think discussion sometimes is that like,
for example, even in this workflow, if you think about it, I'm not saying
that you let an LLM loose it does his magic and then come back tomorrow
and go, hey, here's your build. What I'm saying is that the LLM is going to
have a conversation of commits, pull requests, changes, et cetera, that is
completely logged, is completely justified, that we can then go back and
analyze. And Mario, this is where I'm tying up almost all the sessions. This
is where when you then look at our situation awareness and instance
response, we should be able to go back and I missed this bit. Oh, this
should not supposed to be there. And the big paradigm shift for me, let me
show you this image, right?

Dinis Cruz - 25:50
Because I did a presentation on what's it called, on why everything should
be a cyber expert. But there's one picture that I showed in there that for
me was the big game changer, which is this. Can you see my screen? So
that one why everyone needs to be an AI expert. So I presented this. But
the screen I really want to show is this one here. Have you seen this
image?

Speaker 3 - 26:21
No.

Dinis Cruz - 26:21
Have you seen this one? Okay. This was the one, ironically, was a visual,
but was the one that made me really understand the power of generative is
that the square in the middle is the original painting. The rest was created
by Gen AI. The same way that, for example, here, you got the Mona Lisa
and then you got the expansion, you got Nirvana and you got expansion,
you got, for fun, metallica on a cake.

Speaker 3 - 26:54
I think the point is what we're talking about and what you mentioned is
having all of the deployment and all of the builds and all of it in LLM.
Because what we discussed, I think, and the main topic today is we don't
have enough context normally to make right decisions.

Nathan Case - 27:14
Well, and roll back to the Metallica image, to Marius's point here. Roll
back to the Metallica image. Yeah. Neither does Marius's Point. Metallica
is not right. That is not a cake. If the LLM gets the wrong idea here,
Marius, that's going to look bad, right?

Dinis Cruz - 27:33
No, it will. But you know what the power of this is that let's say even this
happened, right? Okay, so let's take the analogy, right? This happens.
Somebody builds a cake, right, with the Metallica logo, right? In the past,
the cost of creating that in a different scenario will be massive, right? In
fact, will be as big, if not more than creating the cake. And that visual,
right? The power of the way the generative works is that cake is one of
billions that you could have done based on the input that we provide. So
when we come around and maybe on an incident we discovered, oh, it's a
cake, it should not be a cake. You can go back and you can now modify
the prompt and say, actually it's like this. Like this. Like this. Like this,
right?

Dinis Cruz - 28:21
So that for me is the big paradigm shift. The big paradigm shift is that
what the generative bit does. It means the creation is now cheap or the
modification based on the prompt that we can then test and we can
validate and we can diff. We can do all that stuff that.

Nathan Case - 28:39
Assumes a human catches it, though. I mean, that's the issue, right? Like
to Marius's point, and I apologize, marius, I feel like I cut you off there
pretty hard. Is that where you were.

Speaker 3 - 28:50
Was. Yeah, exactly. Because the point is, as you say, yes, it's cheap to
experiment, but if you push the cake into production, what's the outcome?
My point is that, yes, we can use LLM, but as long as we said enough
context and we used it in the background while we did a number of
commits, number of builds and then they build a context. Of what we need
from security, what developers need, what's the business goals, and then
we only start slowly saying, oh, it has enough data, it has enough context
to know where it should be driving towards. Because if you just ask to
build, say, today, I just plug it in and say, build me a secure image, it's
going to build you a cape.

Dinis Cruz - 29:37
But see, here's where I would draw the line today. See, I would argue
today you don't want the LLM to create the cape. Right? You don't want
the LLM to create the output that ends up being in production. You want
to use the LLM to aid the human, to augment the visibility, to augment the
understanding of what's there. And that's a very different proposition. And
that's where hallucinations become less of a problem because there's
enough checks and balances in the system. So if I ask an LLM to say,
here's a bit of code and analyze this for me, whoever wrote that or
whoever's in this loop can say that's right? That's wrong. Right? And then
even if you do analysis on top of it, eventually you're going to figure out,
well, that analysis was wrong. So you can modify it if you've.

Speaker 3 - 30:25
Got checks and balances in place. Yes, that's the point. What we discussed
earlier, you said you don't want the LLM to build, you want the pipeline to
build. But if it just goes automatically by the pipeline build into the
production, then.

Dinis Cruz - 30:37
Obviously we have yeah, but we shouldn't allow that. By the way, that's
already happening today anyway. How much commit today happens on
your pipelines that nobody really checked properly? Right? If you have dev
team shipping 2030 5000 times a day, how many of those commits have
been looked at from the security team? Yeah. Even if you have static
analysis and dynamic analysis, right. The percentage, even if you have is
still that is already happening today.

Nathan Case - 31:04
Right?

Dinis Cruz - 31:04
We're already shipping to production code. But I'm not saying we should
allow the LLMs to do that, even with automation. I'm saying we should be
using them is in the steps in the middle to allow us to understand context.

Nathan Case - 31:18
I think as we go there and we push back to the original topic that were
supposed to be talking about, which is networking in Kubernetes, if we can
look at these things that actually build out the build scripts for us, if you
will, that will allow us to build out the cluster that we're going to get in
the end and deploy the application. It would be really great if we could
then go ahead and comma. And could you give me a network security
mapping or detection system that would allow me to see things that are
not supposed?

Dinis Cruz - 31:45
Can you write the rules for me? Can you give me the error rules?

Nathan Case - 31:47
Can you give me the for example, it's basically Iptables. Why is this a hard
thing?

Dinis Cruz - 31:53
Because it's because until you have an LLM, the cost of engineering was
great.

Nathan Case - 31:59
I understand that. What I'm saying is, as you talk to the LLM, this is just
IP tables.

Dinis Cruz - 32:05
It is, but the level of complexity is too high. If I go to you and say, can you
take your helm charts, your live processes, your execution logs, your IP
tables, your flow data or your analysis of it? Can you mash it up and give
me a view and inconsistencies you turn around and going, Great. Give me
two to $5 million of development and I build it for you. And even what you
build might be highly freaking locked in and customized. That. Question
with an LLM, you can now look at that problem very differently. You can
look at creating abstraction layers at every point and then connecting the
dots and connecting the intents.

Dinis Cruz - 32:44
And I think there's going to be a huge amount of innovation there because
we now can ask these questions in ways I think we can now start to ask
questions, say, can you start to output data in ways that are easy to
understand? Can you start to output intent from your information? Which
we're going to have other vulnerabilities and we're going to have to deal
with it, et cetera, but at least that can be checked. At least we can start to
learn to trust or not to trust some of these analysis. And, you know, at that
moment in time, the smaller the LLM, the less scope he has, the better it
will be. I want an LLM that only understands IP tables. That's it all he
does.

Dinis Cruz - 33:23
I want an LLM that only understands network diagrams, blah, blah, has a
very small subset, doesn't need to write poetry, doesn't need to know about
NIST, doesn't need to know all that shit. Just needs to have enough context
that we can then prove with behavior, with analysis, with battle hardened,
and with idea, with evidence eventually that it does that really well.

Nathan Case - 33:47
Totally agree with the thought. Please, go ahead.

Speaker 3 - 33:49
Question nathan, I wanted to pick your brains a bit. So we discussed
about correct image builds. Some things like app armor, open policy agent
and things like that. How we build secure clusters from the get go. What's
your vision about? People might miss or might not know how to do these
things, so instead they say, oh, let's plug in runtime protection. Something
like Sysdig or whatever datadog or any other sort of company that uses
runtime protection and just see how they can help secure us. Kubernetes
from the other angle, what's your view between the two thoughts of.

Nathan Case - 34:36
So, a long time ago, in a galaxy far away, I worked at AWS, and we
released some really interesting stuff in Lambda. And a company that no
longer exists. I believe it got acquired. And a friend over in England
actually wrote a script that would strip everything out of the lambda
container that you didn't need. And it would just automatically, like, you
would push your script, it would run, it would strip everything out of the
lambda container that you didn't need, and it would remove all of the AWS
permissions that it didn't need to have. And it was cool.

Dinis Cruz - 35:13
That's cool. Where's that feature? Where's that feature? In AWS. I want it.

Nathan Case - 35:20
I don't know. I stopped working at AWS a while ago. I apologize. But it
was one of the coolest things that I've seen Dave do in a long time, and it
was really legitimately helpful. And I Think What I'd Like To See, to
Answer The Question in Sort Of A Roundabout Way, marius Is More This
Concept Of and Kind Of Going All The Way Back To in Days Of Yor And
Yonder when we used to have to build out a sand and plan out what the
backplane was going to do and understand all of the implications for all of
the different drive speeds and how the fiber channel was going to interact
with all of these things.

Nathan Case - 35:56
I think there's something to be said for it would be really nice if we could
get Kubernetes to just load up and go, hey, you're using this and you don't
need that, and automatically strip it out. I don't care who it is. Honestly,
it'd be really nice if we could just accept the fact that realistically, we don't
need 90% of the container we just uploaded. And even if I can just run a
function that spends a day running it through a significant number of
different interactions on the API layer and then gives me a list of, hey,
these are the things you actually need, versus These are the things you
actually have, it doesn't strike me like it's that much of a walk to do it. I
think Netflix had something called Goat for a while, didn't they?

Nathan Case - 36:38
That did a very similar sort of a thing. And it's one of those things where,
from a security geek point of view, it would be really nice to be able to
build out my hardening scripts that way, as opposed to having to hand jam
the whole thing.

Speaker 3 - 36:50
Dennis, you ready to build a company? We just got an idea.

Dinis Cruz - 36:55
Yeah, I feel it starts to be doable now. Right?

Nathan Case - 37:02
I think we're on the edge. Yeah, I think we're right at the precipice of you
could do that.

Dinis Cruz - 37:06
So he's an interesting question. That's why one of the slides I have on that
presentation is that everybody should either be panicked, be very excited
or a lot of people are ignoring it. Right. But what I think is interesting in
the next couple of years is going to be which industry is going to innovate
more? Is it the security industry or, for example, the developer industry?
Because, for example, what you describe could be done by a dev tool or by
a security tool. We don't care. We just want one of them to do it. Right.

Nathan Case - 37:31
I disagree. I completely and utterly disagree.

Dinis Cruz - 37:34
What do you mean?

Nathan Case - 37:36
I think security is smoke. I think as a security geek, I kid you not. I think
security is just development that we've tried to make special and different.
And the reality is development.

Dinis Cruz - 37:48
We live on the outskirts of inefficiency of industries.

Nathan Case - 37:51
I really think that we should just embrace the fact that security is
development and it should be a development tool, and that's just good
development.

Dinis Cruz - 37:58
I agree with that. No, I'm saying that which side is going to innovate? Are
you going to do this from a security angle?

Nathan Case - 38:05
I would hope that we do it.

Dinis Cruz - 38:06
From a development or you do it from a development angle? Where that?

Nathan Case - 38:09
I would hope we do it from a development angle and we grow towards
security.

Dinis Cruz - 38:12
I agree.

Speaker 3 - 38:14
Angle. It's more chances to succeed. Because if we'll be done from security
angle, the marketing will be, oh, we make your Kubernetes 100% secure.
We 100% protect from breaches and all DA DA. And it will become a
snake oil, and nobody's going to use it.

Dinis Cruz - 38:30
Yeah, but what we should be doing in security is saying, we make your
product faster. Resilient. A read only container is super resilient. Right.
Like the ability to diff the containers, the ability to, like I said, measure
that delta. The thing about security is that we do have a bit of a different
perspective. In fact, when I was a CTO, I argued that my understanding of
what was possible is very different. Like the Kubernetes model that I
described to you guys. I arrived there from both I was CISO and CTO. I
arrived there from two hats. I wanted a small possible container from a
security point of view. Small possible development. I want to lock it down
easily, and I want the small possible piece from engineering point of view.
Right.

Dinis Cruz - 39:14
I had to argue with Kubernetes experts because they said that's not how
Kubernetes supposed to work. Literally. They just didn't have the mental
bandwidth to take a little step back and going, okay, maybe that's what I
was designed. Yes, you master and slave are not in the same box, but
maybe that's not a bad thing. Right. But it was funny. Cool.

Nathan Case - 39:34
That's why I go back to the discussion about, like, forever ago, when we
used to have to think about all those little pieces. You were going to build
out a data center and you had to know, where do all those go?

Dinis Cruz - 39:44
Now? It should be disposable right now.

Nathan Case - 39:46
It's all this big, and the data center is literally yeah, but our Clusters are
massive. The intel nuck in my basement.

Dinis Cruz - 39:52
Yeah, but our clusters are massive at the moment.

Nathan Case - 39:54
They are? Yeah.

Dinis Cruz - 39:56
So are they a pets? They should not, but they are. When was last time they
got rebuilt? When was last time? Can you go and delete it all?

Nathan Case - 40:06
Let's see. Last time they got rebuilt from scratch. From scratch? Let me
check. Hang on. They've been up for one day.

Dinis Cruz - 40:15
Good. What about your production in your company? The production?

Nathan Case - 40:19
That's a different question. That's none of my business. I don't ask those
questions right now. It's all good.

Dinis Cruz - 40:27
Cool. I think it's a good session. I think any final remarks, comments on
this?

Speaker 3 - 40:35
I would say that Kubernetes security is becoming more and more
prominent question that needs addressing. And I think what we just
discussed in terms of we need more fresh ideas, looking at different angles
and stepping away from what is needed. I think sometimes we do security
and development through not necessarily of security, but we make it more
complicated than it has to be. And it becomes sort of a barrier to entry
where we border ourselves and saying, oh, we do this very complicated
things that nobody could understand. Therefore we lack innovation and
perspective from different angles. I think that's where we need to.

Nathan Case - 41:16
And we get into diversity there too. Not that we don't have three white
guys talking on this, but at the same point, diversity of thought and
diversity in general in doing this type of thing is desperately important.
Because if you don't do that, the only thing you come up with is the exact
same idea over and over.

Dinis Cruz - 41:36
And I think there's a couple of startups we already described on this
presentation. Right. I do feel that the Gen AI is the game changer here. It
brings capabilities that before were just too complex to do, but not to
make the cake to analyze on the way to the output. Cool. Brilliant guys.
Thank you. See you around later.
