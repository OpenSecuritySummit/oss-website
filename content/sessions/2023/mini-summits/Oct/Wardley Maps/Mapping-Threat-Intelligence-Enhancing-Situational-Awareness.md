---
title        : "Mapping Threat Intelligence: Enhancing Situational Awareness (Panel)"
track        : Governance
project      : Risk and Governance
type         : working-session
topics       : Wardley Maps, Threat Intelligence
featured     :
event        : mini-summit
when_year    : 2023
when_month   : Oct
when_day     : Mon
when_time    : WS-16-17
hey_summit   : https://www.linkedin.com/events/7114744059448995840/
session_slack:
#status      : draft
description  :
banner       : https://github.com/OpenSecuritySummit/oss-website/blob/main/content/sessions/2023/mini-summits/Oct/banners/mapping%20threat%20(1).jpg?raw=true
organizers   :
     - Dinis Cruz
     - Marius Poskus
     - Simon Wardley
     
youtube_link : https://youtu.be/pw7PImph7pk
zoom_link    : https://us06web.zoom.us/meeting/register/tZwpde2trzotHNcOON-YniljAeYDo4a59zUf
---

## About this session
This topic focuses on using Wardley Maps to map threat intelligence and enhance situational awareness. Panelists will discuss techniques for mapping threat intelligence sources, analyzing the relevance and credibility of information, and integrating threat intelligence into decision-making processes. They will also explore the role of Wardley Maps in identifying emerging threats and improving incident response.

### Outline:
- Understanding threat intelligence mapping using Wardley Maps
- Techniques for mapping threat intelligence sources and analyzing their relevance
- Assessing the credibility and quality of threat intelligence information
= Integrating threat intelligence into decision-making processes
- Enhancing situational awareness and incident response through threat intelligence mapping

## Transcript:
Dinis Cruz - 00:00
You. Hi. Welcome to this open security summit session in October 2023.
And we're joined by Simon Wardley and Marius Poskus. You know, has to
be one of my favorite topics, especially, I have to say, the thing I've learned
the most in the last 510 years that changed my perception. I have to add
Gen AI to that now. I have to say, Simon, but, you know, I still feel that it's
one of those unexplored areas that has so much that we need to do to
figure out how to really use it. And it's not perfect, but it's way better than
a lot of the things that we use. So big fan on worldly maps. So, Simon, I
know you got some things you want to present to us. Why don't we start
there and then we start the Q A out of it.

Simon Wardley - 00:49
We can do perfectly. Happy to. I put some slides together because we're
talking about weak cycles. But before you've already dropped the Gen AI
bomb in here, I've got to say, the difference between Chat GPT Four and
the multimodal version of Chat GTP, the more visual version, is night and
day. It's enormous. It's astronomical. Because part of the problem is this
goes back to the concepts of NICUs negropants and architecture by
yourself. So the process of design is conversation going on between two
designers, or possibly within the mind of one designer, two identities. But
it's a conversation. But that conversation in text form was very much
limited by rules and syntax and styles. And of course, this goes all the way
back to Jonah Friedman's work on graphical conversation theory.

Simon Wardley - 01:53
Getting into that graphical form, it's now much more about objects and
relationships and context. It's a bit like when you're coding how we often
have whiteboards behind us to actually explain the problem on the
whiteboard that we then code. Well, we've been trapped in that world of
code, the world of storytelling and text and all the rest of it. But the new
version of Chat sheet, it is totally. This is what I've been waiting for. I
wrote a post on this back in May last, earlier this year, which was
following one from previously. The fuss about conversational
programming, the medium is so important. So it's enormous. If you
haven't played with the multimodal form, I can throw maps in there, get it
to interpret the map. I can have a discussion with it, build a bet. It's just
incredible.

Dinis Cruz - 02:44
So I would argue that's another pivotal point. But for me, the bit that it
was already doing, which was the big game changer, was a understanding
context. So I can have a dialogue with it, but more importantly is the
ability to translate that into a context that I give it. So, for example, the
biggest problem I had in the past was how do I tell that story in a way that
makes sense to that individual, for that culture, for that experience in a
way to even at the point of the journey, that individual is that could never
scale. Now we can now we can tell the story and make sure the story is
coherent.

Simon Wardley - 03:19
I'm going to disagree with you here. Good on a panel is that beforehand
were talking about styles and rules and syntax and basically giving orders.
So it was like, I need to improve this code, et cetera. And were still
trapped in that world of text. I think what we've got with the multimodal
forms enable us to ask questions in a completely different way and it is a
huge transit. So everything before they release the multimodal version, I
think will be forgotten to history. I mean, it was sort of exciting. This is
where it's actually game on. This is where it really is a fundamental
change and it's the medium by which we can have the conversation. But
anyway, I've got some slight and weak signals. Well, on mapping, because
I have to talk about mapping, of course, intelligence and.

Dinis Cruz - 04:14
Connecting the dots, right, and providing context, right. For example, just
maybe so we can tide a lot of this on mapping, threat intelligence and that
situation awareness. My challenge a lot in the past was how do I translate
the situation awareness that we have here to that target audience? And
even with the map, right, even when I got a map, I was able to create
analysis. So I was always being very frustrated because I could use maps, I
could visualize in maps, I could think in maps. I always struggle to
communicate those stories and to provided that.

Dinis Cruz - 04:50
And now I can see how I can do that in a way that leads the individual
almost to they'll be consuming the worldly maps, and then as they ask the
questions, you can zoom in and go, oh, let me show you what actually
happens behind the scenes. Where in the past, there was too much of a
chasm there on that part.

Simon Wardley - 05:10
Okay, I'm going to agree and I'm going to explain why I agree as well. But
we'll get there. I'm going to share some slides. I've always got a current
research project while I've got one going on in video gaming. Coming up.
Did sustainability. I did cybersecurity. I think I'll spend a few minutes.

Dinis Cruz - 05:30
Taking yes, my ass before, because you've done a lot of great work and I
joined a couple, but I know if you finish it off, it'd be great to see the
outcome of that research project.

Simon Wardley - 05:38
Oh, it's not written up yet. The time between when the research project
finishes me right up is quite some time because I've got but I will show
you. I will show you. All right, let's get started. Anyway. Too much chatting
for me.

Marius Poskus - 05:54
Can you see that?

Dinis Cruz - 05:55
Okay, yes, we can.

Simon Wardley - 05:56
Right? So let me go view full screen mode. Okay. So very quickly, I'm
going to talk about origin, how I got into maps, and that's going to be
super quick. And then I'm going to talk about patterns, and then I'm going
to talk about the problems with weak signals. Okay? So for me, this all
started running a company, didn't know what I was doing, completely
clueless. Ended up reading Sun Tzu's The Art of War. So Sun Tzu taught
about five factors mattering, competition, have a purpose and moral
imperative. Understand your landscape, the environment you're competing
in. Understand the climatic patterns, so how the landscape is changing.
Understand doctrine. So the principles of organization. Then you're into
gameplay. And this overlaps very nicely with John Boyd's UDA loop. You've
got the game. You observe the environment. That's what landscaping
climatic patterns are about.

Simon Wardley - 06:50
Then you orientate yourself around this space and then you're into sort of
action, or decision action. This is where you're into the whole sort of
leadership part. And this got me really into landscape. What do we mean
by landscape? So that got me into maps. And I read loads on military
history and all the rest of it, things like this. And I got really excited by
maps. And so I asked my company, everybody who was working for me,
give me your maps. And they gave me loads of maps, customer journey
maps, my maps, systems maps, loads of them, business process maps. And
I took one systems map. Here it is. A number of components connected by
connections. Took one component, CRM, moved it and asked, how has the
map changed? And the answer is, it hasn't.

Simon Wardley - 07:40
Which is unusual because if I took a geographic map and I take a map of
the world and move, I don't know, Australia, put it next to the UK.
Obviously that has changed. It hasn't changed here because it's not a map,
it's a graph. And so the thing that every single map I had in common was
none of them were actually maps, they were all graphs. And just to explain
the difference there very quickly, the three images at the top, they're all
graphs. Three places nottingham, London, Dover, connected by two roads,
m one, M two. Roughly, they're all identical. The three images underneath
it are all maps, and they are completely different. And the reason why they
are completely different is because of a compass, because that gives a
property, and that property is it gives space meaning.

Simon Wardley - 08:31
So the difference between a graph and a map is in a map, the space has
meaning. So you can't just simply move a component and it remains the
same just because the connections are the same. So that's the distinction
between a graph and a map, and space only has meaning. Well, obviously,
when you're mapping against some form of landscape. Now, in order to do
this, you need three basic components. Anchor, such as magnetic north,
position of pieces. This is north, southeast or west of that, and consistency
of movement. So if I go north. If I go south. And so that's where I started.
And the example I always do is a tea shop. If you're mapping a tea shop,
you start what's the anchor? The public consuming tea, the business who
wants to sell cups of tea, right? Well, that's anchors that's.

Simon Wardley - 09:18
Not enough cup of tea has needs. It needs tea. Cup needs hot water, Ketle,
power. So you've got a chain of needs that describes position through a
concept of visibility. And then of course, all of these components are
evolving. And so that gives you movement and evolution. And so this is
what you end up with is a map. And in this map, if you move a piece, it
fundamentally changes the meaning of a map of the map, because it's a
map. There we are. That's super simple. All right? Patterns. Turns out
when you start mapping out spaces, you learn lots of patterns. There are
climactic patterns. There's doctrine, which is about organizational
patterns. There's leadership patterns. There's about 30 Climactic patterns,
40 doctrine, about 100 different forms of gameplay. All right?

Simon Wardley - 10:07
So I'm going to talk about Climactic patterns and then bring in weak
signals into this. So the climactic patterns here's the horrible list that I'm
going to talk about is everything evolves through supply and demand.
Competition components can coevolve. Higher order systems create new
sources of value. Efficiency enables innovation. Success breeds inertia
very simple patterns that come out of mapping, which you can apply to a
map. So an example, this is compute roughly in 2004 using these
application. Best coding practice on a runtime on operating system or best
architectural practice on compute. That was 2004. The first pattern you
learn is everything evolved. So we knew that it would eventually become a
utility. Sure enough. AWS Et Two 2006 the next pattern you learn is past.
Success breeds inertia.

Simon Wardley - 10:59
So all of those with big data centers and lots of practices in that space had
inertia to the change. Perfectly normal. The next pattern you learn is that
as underlying components evolve, you get a change of practice. So we go
from high meantime to recovery, to low meantime to recovery. So we go
from scale up to scale out. We go from disaster recovery to chaos engines.
So we're distributing systems now. We're using chaos engines. We're no
longer doing things like capacity planning. We don't need to do that
anymore. We're not having to do N plus one anymore, all those sorts of
things. Okay, the next pattern you learn oh, and those new practices, we
gave a word we called DevOps eventually. Efficiency enables innovation.
Standard pattern commodogation. So as things become a commodity, you
get the appearance of new things like Netflix.

Simon Wardley - 11:57
Higher order systems create new sources of value or worth basic standard
patterns useful for investment. So when I look at a map, I can basically
see what's changing. I can go where we should invest and also where we
should not invest. So existing practices and servers in the data center and
it's simply by using this map more complicated version. This is how at
Ubuntu we attacked the market. We were like 3% the operating system
against Red Hat, Microsoft, they had all the money, all the people and
everything else. Took us 18 months. We took 70% of all cloud. Not
because we're genius, we just knew where to attack. Really simple.

Simon Wardley - 12:36
All right, so when it comes to weak signals, there are a whole bunch of
things you're looking for when it comes to this particular set of patterns or
this sort of change, evolutionary change, past success, breeding inertia,
lots of people complain, dismissing the future system, high levels of
efficiency of the future system. A new set of changing practices should be
emerging which are associated with speed. You should see rapid
innovation with people built on top and those new systems creating value.
And those are things that you can look for if you're looking for a change
in the marketplace caused by climactic patterns. And a classic example of
this we saw in 2014. So by 2010, the emerging practice got new name
DevOps. By 2014, the runtime further up the stack started become more
of a utility and it had exactly those patterns.

Simon Wardley - 13:31
Which is why in 2014, you should note, should have known AWS Lambda
was going to become huge. This is where we need to go much more into
the serverless space. Which is why your strategy should have changed
because everything underneath it eventually is now heading towards the
new legacy. Your strategy in 2016 is completely different from what it was
in 2008. Your focus should have been on serverless, the emerging practice,
et cetera. And that's what we're seeing grow today. All perfectly standard.
I just want to reiterate that your strategy in 2016 is totally different from
what it is in 2008. And the guide to it should have been those signals.

Simon Wardley - 14:13
You should have seen the efficiency, you should have seen people building
things rapidly on top, lots of inertia, lots of people resisting this change,
those practices associated with speed, rapid development of new things,
with new sources of value, et cetera, they're all the sort of signals that you
look for. So you can read more about that in a wonderful book called The
Fly will Affect by Dave Anderson. And then you get to another set patterns,
leadership. So let's have a look at those. There's a whole bunch of them
which we're not going to go through except for one. Sensing engine is a
particular model called ILC. It's a very simple model. You take something,
you turn it into a commodity, you expose it as an API so other people can
build on top.

Simon Wardley - 15:00
You mine the metadata because they're building on top of your API, so you
have to bill them. So you mine the billing data, see what is becoming
popular. So you identify new components in that industrialized new
component services. The people you've just chewed up scream, oh, they've
eaten our business model. Everybody else cheers because they can more
rapidly build new things. On top of that, it's a very simple model. You get
everybody else to innovate for you. You mine metadata to spot future
patterns, you commoditize to component services. And the reason why you
use this model, it's written back in I wrote it back in 2005, is now your
rate of innovation, customer focus, efficiency, all increase with the size of
the ecosystem people building on top. You use it to climb up the stack on
the right hand side.

Simon Wardley - 15:51
So you compute machine learning, engines, platforms, whatever it
happens to be, you're building up on the right hand side of the stack. Now,
you'll read about this in a book called Reaching Cloud Philosophy. AWS's,
second ever book. It's got about 17 pages of mapping in there. It's got the
IRC model in there. Basically, it describes how they chew up industry after
industry. It's very simple to spot. You look for certain patterns. So known
for providing components focused on enabling others to build harvesting
of ecosystem, obsession with efficiency, obsession with customer focus,
considered highly innovative, despite the fact they're not doing any of it.
Rapid growth up the stack. So if you spot those particular signals, you
know somebody's playing that game against you. Now, that's one bunch of
climatic patterns and a bunch of signals associated that's one specific
leadership pattern.

Simon Wardley - 16:46
There's a bunch of signals associated with that. Of course, there's a
massive amount to this field, but you can reapply this in other areas. So if
I look at something, this is the automotive industry. This was done in 2015
at DVLA, looking at how it was changing. So this was where it was going
in 2025. Many, many things becoming much more commodity like
increasing use of intelligent agents, et cetera. You simply overlap China's?
Gameplay? We see them doing exactly the same sort of game. Heavier
focus in terms of climbing up the stack, efficiency one side, they're
encouraging joint ventures and of course, accused of harvesting the
ecosystem. It's all the same thing. It's basically a classic ALC model.

Simon Wardley - 17:33
And if you know that the bigger their ecosystem gets, the same with
Amazon, the more innovative, efficient, customer focused they are, the
more impossible they are to play. There are ways of countering that, but at
least you know the game they're playing, right? So now here's the
problem. That's all wonderful stuff, and there's a wonderful book come
out called Leading by Week Signals, which has loads of maps in there. It's
by Peter Gomez and Mark Lampert. So I've been having a look through
that. It's got lots of forms of maps in there, but the problem with the book
is it's probably only got an audience of about a thousand people. The
reason people is most people don't understand their landscape. We
compete in multiple landscapes, not just territorial, but obviously
technological, economic, social and political landscapes.

Simon Wardley - 18:22
And if we just have a look at the economic and technological landscapes,
we have very poor understanding of the environment. We've seen this from
all the problems we've had with supply chains in the economic space. So
our first problem is we've got very poor awareness of the landscapes we
are competing in. That's assuming that we realize that we are actually
competing in landscapes. But there's a second problem, and for that, I'm
going to share something else. Can you see a mirror board?

Dinis Cruz - 18:58
Yes, I can. And that's leading by week signals by Peter Gomez. Right.

Simon Wardley - 19:04
Yes, it is. And Mark Lambert. So what I did is I took about 60, OD people
who are all so I run these groups where we look at an industry like
defense, like healthcare, like finance, education, and we try and map out
the space and understand what's important, where to invest. And so we
did one on cybersecurity. So I took about 60, 70 people, all from different
parts of cybersecurity. And the first thing we do is ask them what matters.
And so they came up with a load of things that matters phishing attacks,
security target attacks, detection, disk, trust loads. All of this stuff
matters. All right, that's great. How do we work out what of all of this
stuff actually matters? Well, the first thing I ask them to do is group it into
themes, or what we call perspectives.

Simon Wardley - 19:58
And so they group this into things like risk management, security
awareness, procurement, infrastructure, threat, identity, data, people, a
bunch of different themes. And then what we do is we ask them self
organizing to group map out the most of those themes. In fact, they
choose a number of them, I think it was about six. And they chose to map
out people, technology advancements, risk management, security
awareness, data and threat. Now, this is all done over a period of 10
hours. And so what they do is they go and map out each of these areas.
Now, why would you do that? You do that because I want you to imagine,
you want to find out what are the most important landmarks in, say, Paris.
But no one's ever been to Paris.

Simon Wardley - 20:47
So you send one group out there to map Paris, and they come back with a
map. They've obviously mapped it from a perspective how do you know
the map's right? It's wrong. They might have mapped it from the
perspective of the nicest places to buy pizza. And so they will say the
number one place is Pierre's Pizza Parlor. Okay, fine. So what you do is
you send multiple groups out to map it from different perspectives, and
then you can ask the question, what are the most important landmarks
across multiple maps? And then you can aggregate that together. So this is
what they did they went through as a group, they map.

Dinis Cruz - 21:22
Out their particular overall and now he's going through the sorry.

Simon Wardley - 21:29
That's all right. Does that make sense, by the way?

Dinis Cruz - 21:31
Yeah, no, it's really good. No, exactly. I was just seeing your praises here,
but keep going. I unclick the mute.

Simon Wardley - 21:40
Hey, no problem at all. So they map out things like cybersecurity from the
perspective of people. So they've added a whole bunch of components in
here and they're looking at things like risk management, total
stakeholders, assets, situational awareness, protection, et cetera. And then
they do it from all of these. So they're broken into different groups. We
run this all in parallel. So you've got one group down here who was
mapping it from the point of view of awareness, and one group who are
mapping over here from the point of view of risk management. Now, you
can see they circle around this area because that's when we ask the
question. Once they've got a map and they've got embedded in their
perspective of the landscape, we ask them the question, what matters?
Okay, where should we invest?

Simon Wardley - 22:27
And get them to highlight the most important area. So, from the
perspective of cybersecurity risk management, they highlighted things like
better risk analysis skills, LLM data. Now, that's not that one.

Dinis Cruz - 22:40
Sorry, can you just zoom in? Because I think that one for me has one of
the best examples of why LLM is going to completely make a massive
change in our industry. So let's zoom out a little bit. Sorry. So you can see
what we've done here, if you look at it, is that you basically have multiple
elements of the cybersecurity industry, right. From a risk point of view.
Right. And then the interesting argument was you see that LLMs in the
bottom right? Kind of they're allowed the LLMs that it's allowed on the
bottom right. Yeah. Your mouse. The argument were talking about was
that before Shi GPT, that was all the way to the left, right? So for me, it's
a great example.

Dinis Cruz - 23:25
I've used it several times to explain why sometimes things change
overnight or change very quickly, is because that LLMs before track GPT.
And you probably can argue, maybe even now with the visual element, the
multimodal was kind of to the left. Now that it's there, it means that all
those security LLMs, which are pretty primitive, are going to go very fast.
In the past, I almost sometimes view this as gravity, right? In the past, the
security LLMs struggle to move to the right because they were anchored
by the LLMs Foundation. That was, in a way, on Genesis. Now that the
LLMs are getting close to commodity or very productized, they're going to
pull, right? The gravity is going to pull all the security LLMs.

Dinis Cruz - 24:08
And if you're one of those guys at the top, in a way, you either embrace
that and then your strategy should be changing because you'd know the
security alms are going to move all the way to the right very quickly.

Simon Wardley - 24:21
So one way to test whether that is true is going all the way back to the
weak signals in here. And here we have our pattern, things industrialized.
So are you seeing lots of signs of inertia because of past success in
previous ways of doing it? Are you seeing this as an evolutionary change
associated with efficiency? So is that going on? Are you seeing a change of
practice associated with speed? Maybe it's got new terms like prompt
engineering or whatever. Are you seeing rapid innovation built on top with
new sources of value being created? Because if you are, then you know
this is the stage that you're actually at.

Dinis Cruz - 25:00
Yeah, well, I guess the answer to every one of those is check. Right? And I
think the thing that I found most fascinating is the inertia. I have to say
that I see so many people, even companies or individuals, that I could
totally see the inertia because I could see that they look for the flaws and
going, oh, that's not why it's relevant. And I'm like I have this analogy of
talking to somebody, saying it's like Jarvis, right? You know, iron man
jarvis. That we have Jarvis. And people now say he's not good enough.
Because when we asked Jarvis to sing, he didn't do a good job. Or we ask
him to do hallucinates. Jarvis hallucinates. Yeah, but what do we think
innovation.

Simon Wardley - 25:39
Is other than a hallucination? I mean, hallucination is not a bug, it's a
feature. But anyway exactly. Now, anyway, we do this across all of these
different maps and then what you do is you've now got multiple
perspectives. So we've got in total, here we are, nice little summary
diagram. We got six different perspectives. Data organization,
cybersecurity in the perspective of awareness from risk management. And
on each of these maps now, the group have highlighted what's important.
So with people regenerative culture, regenerative supply chain, these are
the words that they use. Risk management skills, better risk analysis,
security awareness, et cetera. They've highlighted the most important
areas. And then what we do is we aggregate across the lot. Okay? So it's a
simple task and bring it all together, aggregation. And then by finding
themes which are most common, you create a priority list.

Simon Wardley - 26:43
And it turns out that your priority list in cybersecurity is about building a
resilient culture. That the top four things seem to be about building a
resilient culture. Rapid growth of AI, cyber immunity, I. E. Organizations
constantly attacking themselves and getting used to being attacked in
order to harden themselves up and learning. So you end up with these sort
of core themes, which then what we do is we go and do an examination of
what's going on in the wider space. This is by comparing analysts against
what the actual group comes up with and what we discover is that the
analysts are mostly focused on process automation, continuous
monitoring, digital sovereignty, nation state, god knows why. They get
excited by that sort of stuff.

Simon Wardley - 27:34
Whereas the group itself was more about resilient culture, cyber immunity,
rapid growth of AI, and actually awareness of the supply chain
management. You got to learn about that sort of stuff. So this is where
Spons and all the rest of it come into play.

Dinis Cruz - 27:48
Could you just explain me better, Mark, how to read this? So what does
the colors it will.

Simon Wardley - 27:56
Be when I write it up. So the yellow dots is I aggregate a whole bunch of
analyst reports and run them through the same process so I can see what
they think is high priority, what they think is low priority. The purple dots
are where the group was. And then what I do is also I take the entire list
and I send it through Chat, GPT and Bard because they're trained on
large sets of data, so they give me a sort of background signal of what the
general market feels. So I ask Chat, GPT and Bard to order them as well.
And so that's the red and the blue. So the ones you concentrate really on
are the yellow and the purple. And you can see there's quite a big
distinction.

Simon Wardley - 28:36
So the only area that the group agreed with the analysts on was the rapid
growth of AI. That was the only space. Otherwise there's quite a big
distinction between what they thought was important. Now, the reason
why I mentioned this is because you think about resilient culture, cyber
immunity. So it's about making your organization capable of coping with
shocks and being constantly under attack. So improving its hardness to
those sorts of shocks. I mean, those are obvious sort of things, but that's
not what was being mentioned in the analyst report. And I think it was the
next day, I think, Denise, it was either yourself or with another group. This
whole conversation, this ridiculous idea there was a CISO quite proudly
showing off a board of shame that they were using in their organization.

Simon Wardley - 29:27
So they would do phishing attacks and everybody failed, went on the
board of shame, which is almost the reverse. This is not how you build a
resilient culture or build up cyber immunity. This is actually how you
dismantle any form of culture that you have within that organization. You
create a system of fear and it's almost the reverse of what you want to do.
So this leads me to the second problem, because the first problem is that
we don't understand our landscapes anyway. So the weak signal stuff is
really exciting. I'd love it, but for most people it's fairly irrelevant because
we don't actually understand our landscapes. And the second problem we
have is the utter idiocy that we do in places, even basic things like how we
build resilient cultures, which obviously should be a focus, I'm afraid.

Simon Wardley - 30:18
In some places, we're not even doing that at that point, I'll go quiet.

Dinis Cruz - 30:25
So how do you measure that? Because I have to say, one of the
frustrations that I feel we still have this is a good one to bring Mario's on
this is that I still feel that a lot of security, it's still a marketing exercise.
And I'll give you an example. Imagine three organizations. One has that
CISO, one has maybe the other extreme super more enlightened. And I
completely agree that's what not to do. By the way, one has great
practices responding quite well, and then one in the middle. At the
moment, we don't have a good way to let the market promote and reward
the good player.

Marius Poskus - 31:12
Yeah, I think you're very right. I think it all stems from what Simon
mentioned about the culture. I think loads of organizations are still
carrying that legacy view of security, saying no security being stick instead
of a carrot. So I'm always the kind of person that always thinks about
how we can communicate and collaborate with people to actually help
them understand how the security work. Like phishing simulations. It's
never a blame culture. It's always about how you encourage people to
report bad behavior because you build a two way collaboration. You
always encourage instead of noticing someone who failed you're, noticing
people who might detect the emails and praising people for their good
work. That's how you breed. I think the culture sort of spin. We never say
no. And that's one other thing. We actually talked within my team last
week.

Marius Poskus - 32:25
When did the last time we said no to someone in security? And we couldn't
remember. We never say no. We always say yes. But let's look at from
security perspective, what do we need to be able to say? Yo, yes. For
example, what are requirements of security to be able to say yes? And
that's how we always we're always playing around availability and
security. Because I think sometimes people forget there's loads of
organizations that add security for the sake of security.

Simon Wardley - 32:55
Can I just say I love that? Absolutely love that. Thank you. Back in the
1990s, I used to run security for an organization called Harrods, which
obviously as in the It security. And one of the things I would do is attack
the organization. Of course, when we found weaknesses, rather than go
round them, because unfortunately, there was a big culture of fear in that
organization. Rather than go around, beat people up, we'd involve them in
the group to do the next round of attacks. Because you'd learn from the
process. So it wasn't a case of go and hit somebody with a stick, put them
on a wall of god, I can't believe in 2023 somebody puts up a wall of
shame. I mean, that's just anyway, I love hearing the words that you were
saying.

Marius Poskus - 33:46
Yeah, it's always either involvement or another thing that really helps. I
think for us is make it personable. Whenever we have examples of safe
phishing, we always trying to relate examples of various banking scams,
SMS scams that we find in the wild and how it relates to people's, external
families, external sort of known people circle, and how we can relate. That
how you're enhancing your security knowledge, not only for the job you
do, but your personal life, how you protect your personal bank details,
your personal money and personal details, as in what can be used for
nefarious purposes. So I think when you connect those two dots, it always
sort of a big light bulb goes up in sort of people's head.

Dinis Cruz - 34:33
But we need a way to share this information. And I think a really good
sign is a sign that the insurance industry is really raising the bar because
they got burned quite spectacularly by distributing insurance as confetti
for a while and then got burned right. Because they were not evaluating
correctly the security posture. And now they're starting to put pressure.
And even if you look at that simple example, which I would argue, it's
almost like if they don't have the awareness to understand why that's a
problem, we can bet that there's going to be another 40 things they're
going to be doing wrong. It's almost like the canary on the coal mine. But
we need a way to expose that. We need a way for the market to become
more efficient.

Dinis Cruz - 35:15
In fact, we need a way for the senior management to understand that's
what's happening and the need. Right? And maybe the senior management
loves it. Great. And maybe it's a cultural problem within the organization.
Okay? Right. There's a moment where you draw the line a bad company is
going to be a bad company. Right. But it might not be that their customers
are that happy with it's. Kind of like pollution. Right? So in a weird way,
we now have very little acceptance for companies that claim all sorts of
things and behind the scenes they polluting like mad and they're
destroying environments and they have really bad ethical practices. I think
we need a way and I think Maps is part of the solution. I think Maps is one
of the ways this can work quite effectively and also translating it to
particular audiences.

Dinis Cruz - 35:59
So you reward the teams that are doing a good job, the teams that build a
good culture. If anything, Mares is giving us better arguments when we
justify why we do certain things. Right.

Marius Poskus - 36:10
Yeah, I think I'm a big proponent as well. Sometimes people forget that
security is part of the business. We need to align security to business. How
comes some of the security professionals, when you talk, when you ask for
a security professional, how does your security program help your
business? Bottom line, they always get mind boggled. Oh, bottom line is
not our concern. But that's the thing. How do we build accountability?
How do we make people understand what security is all about. That's one
thing that is always.

Dinis Cruz - 36:45
I.

Marius Poskus - 36:46
Guess it's not portrayed very well because sometimes people hide behind
accountability and that's what needs to change, I guess, as our industry
matures.

Dinis Cruz - 36:58
But then we are the problem, right? The security professional is the
problem.

Marius Poskus - 37:02
Some of them, yes, some of them are.

Dinis Cruz - 37:06
I think there's maps. What I like about, and I'm going to keep throwing
the other lens into this. I think we can scale that now in ways that before
whereas it's not possible I think it's now possible to take a map, a
visualization of practices that a company is doing, and provide narratives
that are anchored in a way I bias throws a particular way that we can
then get some good data on the back of it and going, that's okay. That's
not okay. I'm telling you, I have that problem. I have freaking suppliers
coming out of every bed of the organization and it's going to go even more
because we're going to get a marketplace, right? So I really want to make
sure that I can push security down and understand the metrics in my, for
example, third party supply environment.

Dinis Cruz - 37:58
So how can we scale that, Simon? How can I get I will put a policy that
says I want every team to give me a worldly map of security, of how you
operate.

Simon Wardley - 38:10
It's not just an organization in terms of a company problem. This is a
massive problem from a.

Dinis Cruz - 38:15
Nation state, but let's solve an organization problem.

Simon Wardley - 38:21
But a classic example of this, one of the best I've seen, it's not a map, it's a
graph is the work which was done by the Complexity Group in Vienna for
Hungary. So what they did is they took VAT transaction. You know,
whenever you transact with someone else, there's value added tax and
Hungary collects them at transaction level. So they were able to graph out
the entire economy, which is amazing. And what they found is there were
90,000 old companies, and I think it was about 100 companies
represented about 70% of the systemic risk of the entire economy. And it
was something like about 30 companies were about 25% or something. So
any one of those 30 having a problem, you lose 25% of your GDP. But
most companies have that terrifying thought.

Dinis Cruz - 39:12
Most companies are like that. In fact, I would argue that most internal
systems are like that. The challenge is, in fact, I had this exact
conversation with my team a couple of weeks ago where we had a big
incident and we're now mapping, for example, which parts of the
organization that we going to leave to burn, which parts well, in a nice
way, but which parts we're going to run straight away. Because those are
the 20% that keep the stores open, right? They are the 20% that if they are
alive, we can deal with the rest. Okay? But if they have a freaking heart
attack, then we have a problem. No.

Marius Poskus - 39:49
Go ahead, Sam.

Simon Wardley - 39:49
Well, I was going to say if you think about the Hungary example, other
nations can't do that. The UK, we don't collect transaction level VAT
records. France won't do so until 2030. So they're operating in spaces
where they do not understand their landscape. So you cannot see the
pattern. So we get hit by shops all the time and yes, absolutely, it's true
with organization. This is why things like Spom software bill and
materials, okay, it only gets you to the point of graphing and there's a
world of difference between when something's a commodity and when it's
custom built. So ideally we want to get to math, but we're lacking the
basic information. This is why the Typhoon this was about weak signals.
Weak signals. It's like Irobot, we're like hacker, bloke blah. That's great,
but it's fantasy for most people.

Simon Wardley - 40:37
And it's fantasy because they don't even have the basic understanding of
the landscape. And even more terrifying, they're not even doing the basic
simple things of building resilient cultures within what they've got already.
So there's an awful lot of groundwork which is almost why Weak Signals
is I love the topic, I love books like this. I think this book is great and
there's some really good stuff and I can see but it's a bit like how the
analysts always want to talk about nation state security. What's the point
if you don't actually understand the landscape?

Marius Poskus - 41:09
That's the thing, I don't know why, but for some reason nowadays we keep
talking about tools, about innovation and about this new shiny blinker
3000 that's going to solve all our problems. But people keep forgetting
why would you start talking about nation states if a script kitty can breach
your defenses? Because maybe you don't have ten visibility in your assets.
Maybe you don't even started doing the basics. Like you don't have your
data flow mapped and you don't know where the data is going and where
it's stored, how some of your assets are managed from hardening
perspective. That's why I think in a way it sort of underlines the problem
because what we spoke within when I was in Sansis or Network event
2010s was all about reducing the likelihood of risk.

Marius Poskus - 41:57
And I believe that 2020s are shaping now in saying we can't reduce
likelihood anymore because it's inevitable that something's going to
happen. So let's work on resilience how we can maintain business
operations and reduce the impact of that cyber attack and let's not focus
about likelihood anymore.

Dinis Cruz - 42:15
Look, I argue that my job as a CISO is to allow the business to take risk.
Yeah, that's my job. My job is to make sure the business takes the right
amount of risk with the right amount of understanding, with the right
amount of mitigations in a way that incidents don't become crisis because
the business needs to operate at a level of risk. It happens all the time. We
have stores open, right? You can walk into a store, right? We don't have
military guys at our stores. When you go and buy your vitamins, by the
way, we have great new products, poland America. Yeah.

Marius Poskus - 42:49
Because there's a thing like if you.

Dinis Cruz - 42:50
Look at the latest, very healthy, but a dude with the machine gun and a lot
of security guards at the entrance is not going to really work very well.
Although it might make it more secure.

Marius Poskus - 43:00
If you look at the latest Greg's von de Gras book, he's poised a very
important question. Every year the cybersecurity budgets are getting
bigger, but we're not getting less breaches. We're getting more breaches
every year while we're spending more on cybersecurity. So there is a
fundamental yeah, but.

Dinis Cruz - 43:21
We also have a lot more interconnectivity, right? Like, come on. If you look
at the side effects of a cyber breach in 2023 versus 2020 or 2010, right?
It's kind of like it's very different, right? And there's a lot I think hang on.

Simon Wardley - 43:37
Yes, but remember, we also have very little understanding of the landscape
itself. Most organized, very poor understanding of the space. And I think
Marius is hitting on a really important point because from what came
from that cybersecurity group was the critical things of the four things
was awareness, CPA, landscape supply chain, software bill and material
supply chain management was in that group of four. And rapid growth of
AI. So that's the technology thing. But the real two big ones were resilient
culture and cyber immunity. And they're about people, not about
technology. So that's about how you build a culture which copes with
shocks and manages those shocks, and how you toughen up that culture
so that people become sensitive.

Simon Wardley - 44:23
And this is why that whole sort of wall of shame thing is such a daft or
creating cultures of fear are so incredibly daft things to do. So,
unfortunately, when I look at sort of the analyst reports, it's a continuous
monitoring, it's more analytics, more big data process, automation, big
one. Big one that's all about technology. So I think there's some
fundamentals here in terms of we've got to focus on the people and
building a resilient culture and building that concept of cyber immunity
within an organization. I think then, on top of that, we've got to improve
our awareness. Then we can start talking about these wonderful new
things. I think the real danger is people say, oh, well, AI will magically
solve this. I've got to say, I'm gray. Maris on here.

Simon Wardley - 45:08
Sort of the magical sort of like it is piece of data will magically do it.
We've got to get back to fundamentals.

Marius Poskus - 45:14
And I think on the back of that simon I think the great point is the big
talent shortage is another bull because we all know to me personally as
well, yes, you need some of the skills in specific niches. But when you
hiring security teams, most of the two of the most important skills for
myself is aptitude and attitude. You can teach the rest of them, but if
someone has the right attitude and aptitude to learn, it will be very easy to
get them and learn. The tech sometimes job descriptions and people hiring
teams saying, oh, we don't have specific talent shortage, I love that.

Simon Wardley - 45:56
And the reason why I love that, thank you so much for saying that, is
because it's often we've got a talent problem. It's always the people are
the problem. No, the people are the solution. They're your positive things,
they're not the problem. They are where the answer actually is, we've got
to change this sort of aspect.

Dinis Cruz - 46:19
So I've been trying to do this quite a bit, right. And actually, Sam, I would
like your views on this. So I'm a big fan of first of all, I completely agree.
We don't have a skills shortage. I think we have a skills transfer problem.
Right. What we need to get into cybersecurity is a lot more people from
other fields, because what they have is an attitude and a motivation and
an understanding and a maturity that we don't have right now. Right. The
way I think about this is I can hire somebody, let's say bands one to five,
right? Five is top, one is lower. I can hire a cybersecurity analyst at band
three, which is actually quite expensive if you think about it. Right. And I
would argue today there's a premium that we're paying because of the
skill shortage.

Dinis Cruz - 47:01
What I want to do is I want to hire a specialist at Band Four from another
industry, a doctor, an engineer, a poet, a restaurant manager, an individual
that really has a lot of great knowledge. And I want to bring them to
cybersecurity because they have that experience. The problem in the past,
and I've done a couple of cases, they've been successful. My challenge was
how to infuse that person with cybersecurity knowledge once they're ready
and once they want to drink it. And I have to say, I know that not a tool, is
not suit for everything but the gen AI ability that we will have not yet to
create customized learning paths, to create agents, bots training
environments that allow an individual to learn a much faster pace.

Dinis Cruz - 47:46
I feel that can be a piece of the puzzle that allow us to bring a lot more
people into our industry in a much more effective way.

Simon Wardley - 47:53
You do, but obviously I mapped out the education system with a whole
bunch of professors of education. We thought the education system was all
about maximizing opportunity and critical thinking, and it's not. It's about
producing social cohesion and useful economic units.

Dinis Cruz - 48:10
I'm going to start at the more.

Simon Wardley - 48:11
Involved bots and tools can have the dupe be used in a way that does what
you say, but it can also be used to create new balls of shame. So I would
be careful. You got to think about those. So we've got some questions.

Dinis Cruz - 48:29
One of them is Jim, do you want to jump in? Because I think you can ask
your question.

Simon Wardley - 48:33
So yeah, cheers.

Speaker 4 - 48:34
So Simon, I came to your session at the Center Park years ago and asked
you about risk and you pointed me this book which you can't see. It's
called The Search for Value and it relates ask you a question about risk
and you pointed to that book which has got lots of equations in it. But I
think the most useful thing it does is it shows that risk is in some ways a
reciprocal of business value, of stock value. It's a direct relation. So I
know that you're a risk guy and thanks so much for sharing the research. I
saw that risk analysis was an area of focus. I just want on that.

Simon Wardley - 49:14
Well, so the risk analysis in terms of this group, it was what are the major
areas? The ones that were right at the very top were very much about
people type stuff. So very much culture and cyber immunity and lower
down there was the concept of risk analysis. Now, from my point of view,
when we start talking about risk analysis, I'm talking about value, I'm
talking about things like capital flow. I'm using maps because I'm actually
using the interconnections between the different components because
every line in a map is a bi directional exchange of value or I give money
for a cup of tea or whatever and risk itself is just another form of asset
that flows in these sorts of maps. But in order to assess that, I've got to
actually understand the landscape.

Simon Wardley - 50:00
And so I've got a fundamental problem, is that I generally don't
understand the landscape. So without this sort of stuff, it's the same with
the economic system, it's mostly sticking fingers in the air and having a
good guess. It's exactly the same with sustainability scope three. It's all
estimation because again, we don't understand the components and the
connections between them. So I do like the risk management stuff, the risk
analysis. I'm going to say from my point of view, we've still got huge
weaknesses in actually understanding the environments that we're actually
operating. And until we do start to understand those, we're still going to
be in the world of guessing. Does that make sense?

Speaker 4 - 50:43
Yeah, it does. I suppose I was hoping that you'd talk about some technical
framework or decision making framework or ways of gathering
information. What do you think about the large language models? Do you
think they can help with risk analysis?

Simon Wardley - 50:57
So, as I said in the beginning, I think there's a huge change between Chat
GPT four and the multimodal form of Chat GPT because now we can
actually start having a conversation with them. It's huge, it's night and
day. It's that sort of scale and so I think there are I'm already using them
to help create maps and so forth off the space and starting to have
conversations. I think we're still very early days. I think there's some real
potential there once we get a handle on the landscapes because we
compete across multiple landscapes, territorial, technological, economic,
political and cultural landscapes. Only one of them, the territorial, do we
have a handle on, do we have maps and radars and all the rest of it and
that sort of stuff? The other four, it's often people talk about digital
sovereignty.

Simon Wardley - 51:51
Well, where are your borders? Where are you going to compete? Or
conflict with others, I should say, where are you going to cooperate?
Collaborate. You can't answer those questions without actually
understanding the landscape. We can do that in territorial. So we're
lacking those basic things. So your question, can it help? I think we're
getting there. We're starting to be actually able to have conversations
outside of the world of text. And so I think that's a massive improvement.
Does that answer your question, Jim? Yeah.

Speaker 4 - 52:20
Thanks so much and thanks for sharing the research.

Dinis Cruz - 52:22
Really interesting.

Simon Wardley - 52:23
Pleasure. Pleasure. Absolute delight.

Dinis Cruz - 52:25
So Jim, the way I connect that and I feel again, I think we have a golden
opportunity now to really make sense is to connect risk with other parts,
to have that situation awareness where in the past risk at top level was a
bunch of spreadsheets. Then you have a gap, then you had reality, then
you might have maps. I think we now can start to be able to graph them
out, connect them, create narratives and then use the maps to drive
behaviors, right, and to drive situation awareness. But it's the connectivity
that is super important. Like for example, do people understand the risks
of what the decisions they're making? A project, doing a project, does he
increase, does he decrease? Does he maintain your risk? I think that was
the thing that was always missing.

Dinis Cruz - 53:05
When the exec make a decision, do they understand the ramifications of
the decisions they're making? Right. And I think that in the past was
impossible. It was air gaps, right? It was spreadsheets or even system A
and system B, like Simon daddy's great picture of a company has 25 risk
systems, or 100 systems or 1000 systems. But I think we now have an
opportunity to connect them. There's a bunch of technologies and
processes and thinking that are converging, but I feel the LLMs provide
the connection dot between them that allows us to do translations in a
way that in the past was impossible or requires so much engineering cost
that nobody could do it. So watch this space. I think it's really cool. So,
final thoughts on last couple of minutes. You got another question from
Tristan. Yes, you're right.

Dinis Cruz - 53:57
If you can unmute yourself, you should be able to. But I can ask is what's
the threat intelligence equivalent of the hungarian VAT Records graph,
that graph that we can do on threat intelligence that gave us that visibility
and find those 50 or 20 mission critical spots.

Simon Wardley - 54:19
I think you're starting to see the requirement for the US government, the
Executive Order, the spombs, that's fashioning positive mean within the
Mozilla Group, they've got a particular system which is all about funding
open source projects which is coming out and it has some incredible
graphing capability because of how it redistributes funds within that
system. So there are ways of doing this sort of stuff. We're not there yet
though, to be blunt. We're not even talking maps here. We're talking
graphs of the connections between things. To be blunt, the only places that
I've actually seen where the market was able to create a deep
understanding of the supply chains is the International Material Database
System, which is in the automotive. And that's because the European
Commission came out with some pretty hefty legislation forcing to do so.
And pretty much that's about it.

Simon Wardley - 55:36
I mean, Spom is government action. I think it's going to require
government action. I think we're not going to get it until actually we have
a government department of the supply chain or equivalent across
multiple. I hear a lot of talk, people say we'll come together again, magic
technology, it will be sorted on the blockchain. I'm sure they say just throw
a bit of AI on there and magic will happen. But people like to keep their
information in silos, even though it doesn't make a great deal of sense,
even though the value is amplified by sharing it, they don't want to. So to
solve these problems, I think eventually you're going to need government
legislation.

Marius Poskus - 56:26
I would add a couple of things. I think one thing is we're currently severely
lacking is collaboration. So as you guys probably are aware, not that long
ago, only US government signed an Executive Cybersecurity order for
governing departments to collaborate on various cybersecurity issues,
which is just recent. We have a breakdown between government, private
industry and then vendors. I've been sharing my ideas about various
vendors and I think there are some vendors who are really changing the
landscape. I've been to a few calls where there's nothing talked about
sales pitches. It's a collaboration culture where people are allowed to
discuss various subjects under Chatham House rules.

Marius Poskus - 57:24
So I think vendors, private sector and government collaborating and
sharing knowledge, in some ways it's a way forward because it's us
against the bad guys and the more we can work together, the more we're
going to achieve. So how about some of the vendors? They're potentially
working with hundreds or thousands of companies, so they have a lot of
intelligence that could benefit the industry. So how we can collaborate and
share and knowledge and advance our collaboration, that's the way
forward, I guess.

Dinis Cruz - 58:00
Well, the Open Security assignment on that final note, right, is trying to do
is bid for collaboration right. I think we do a lot of collaboration here get
a lot of people together, share a lot of information. Everything is posted
on videos is out there. Right. But I agree we need a lot more and we need
to get some of us physically together but yeah, absolutely. All right on top
of the hour on this simon, thanks again. Always brilliant I love that you
gave actually what you created was a really lovely which I need to
package and publish in the summit side on I always need people tell
volume maps take one thing for I just tell you, and I go read that. See
that? The first 15 minutes. Nice and easy again, Marius. Thanks for
collaborations, and I see you guys next time.

Marius Poskus - 58:43
Thank you.

Simon Wardley - 58:44
Absolute pleasure. Take care. Bye.
