---
title        : "Zero Trust Architecture: Strengthening Cloud Security Posture (Panel) "
track        : Governance
project      : Risk and Governance
type         : working-session
topics       :
featured     :
event        : mini-summit
when_year    : 2023
when_month   : Oct
when_day     : Thu
when_time    : WS-17-18
hey_summit   : https://www.linkedin.com/events/7112924520931336192
session_slack:
#status      : draft
description  :
banner       : https://github.com/OpenSecuritySummit/oss-website/blob/main/content/sessions/2023/mini-summits/Oct/banners/zero%20trust%20architecture.png?raw=true
organizers   :
     - Dinis Cruz
     - Nathan Case
     - Ogechukwu Okonor
     - Gabriel L. Manor
     - Or Weis
     - Oded Ben David
     - Maciej Owsiany
youtube_link : https://youtu.be/TuHNfroFzdY
zoom_link    : https://us06web.zoom.us/meeting/register/tZwrf-yoqzIvE9Xay3GRcqLXma694AOxBYd6
---

## About this session
This topic focuses on the implementation of Zero Trust Architecture (ZTA) in cloud environments. It examines the principles and best practices of ZTA, including micro-segmentation, multi-factor authentication (MFA), and continuous monitoring, to enhance security in a cloud-centric ecosystem.

### Outline:
- Introduction to Zero Trust Architecture and its Significance in cloud security
- Micro-segmentation and network-based access controls
- Multi-factor authentication (MFA) and continuous identity verification
- Leveraging automation for policy enforcement and anomaly detection
- Case studies highlighting successful implementations of Zero Trust Architecture in the cloud

## Transcript:
Ogechukwu Okonor - 00:00
You.

Dinis Cruz - 00:01
Hi, welcome to this open Security Summit session in October 2023. And
we're gonna we have a really cool panel, a really amazing set of panelists,
and we're going to talk about Zero Trust architecture and strengthen
cloud security posture. Very hot topic these days. So maybe just a quick
round the room, the virtual room, everybody gives a quick introduction.
Don't we start with you.

Nathan Case - 00:27
Okay.

Ogechukwu Okonor - 00:28
I'm OGE. Okonor. I'm a lecturer in cybersecurity, University of
Roehampton. It's interesting to be in this panel today to talk about Zero
Trust architecture. Knowing that as technology evolves, so is the
complexity around technology and finding a subtle balance whereby we
can have maybe say, a good atmosphere of managing the things that goes
around the network, the devices, the users, is interesting and I'm happy to
be here. Thank you.

Dinis Cruz - 01:11
Nathan.

Nathan Case - 01:13
I'm Nathan Case. I am the CISO for CORSIA. I am currently speaking for
myself and all of my views are my own, obviously. So as we go through
this, I'm really excited to talk about Zero Trust and to figure out what
everybody else thinks about architecture and how we can make it more
secure. And maybe if we go back to the pre banter, we can even bring
some AI into it. We'll have to see how that goes.

Dinis Cruz - 01:36
That's my interest, how to make this thing scale. We kind of know what
needs to be done. We just need to make it really scale. So magic.

Maciej Owsiany - 01:46
Hi guys. My name is Maciej Owsiany. I'm a technical architect, Planet it
one of the largest MSP providers in Oxfordshire. And the team that I'm
working with, we're literally just writing strategies for the businesses. So
we speak to the executives, to the businesses and just basically making or
providing a good solutions for them. So the It system is more user friendly,
but it's also as secure as it can be at the same time. So obviously I'm quite
interesting in the subject that we will be talking about today. So yeah,
cool. Glad to be here.

Dinis Cruz - 02:26
Oh, too. Gabriel and you can call.

Gabriel L. Manor - 02:28
So gabriel yeah. Gabriel I'm director of Developer Relations permit IO.
I'm in the software engineering landscape for the last ten years and have
been since the beginning days of Zero Trust at the It perspective on
network. So it will be really delightful to talk today on the way Zero trust
modeling became across the year from a very It network hardware term
into something that every developer messing around.

Dinis Cruz - 03:06
Yeah.

Gabriel L. Manor - 03:06
So I'll start with a short intro on zero trust itself, where it came from and
what it meaning today. Well, so Zero Trust is a term that start became
common, like I think between six to eight years ago from the walls of It.
So in the world before the cloud and with all on prem network, the
network being like complied by hardware, by ports, I were authenticated
and authorized to the network by connecting my laptop to the wall to the
port in the wall and that authenticate and secure me to the network. And
then the security model were based on perimeters instead of my identity.

Gabriel L. Manor - 03:55
The security were based on the perimeter and my identity, like my IP, my
physical Mac address, et cetera, with all the cloud and the way that, for
example, a modern company does not have a network in their It, they have
just the network from the ISP. And they use things like VPN and things like
Know Zero Trust Network, cloud Native network. So there is no
importance anymore to any perimeters because every session could be
different from every time an API being called or some network being
called and that bring a new security model called Zero Trust. We do not
trust anything anywhere, for every request, for every packet, for
everything. We want to know what is the identity behind this, what is the
device behind it, what is the behavior behind it, and then we can get better
decision about our security.

Gabriel L. Manor - 04:57
So when we are modeling it, we are not looking on parameters anymore,
we are looking on more details or more inspectful trust. So we are not
trusting anything in one hand, but by the other end we are getting much
stronger security model.

Dinis Cruz - 05:16
Yeah, it's one of those things where I think the name is completely wrong,
right? Because in a way I think it's a good one because the concept is
sound but it's almost like context driven trust. It's kind of like you start
with zero trust, fair enough, but then you evolve into giving trust access
based on what you know of who the user is, where it is, what he wants to
do, all sorts of properties. And in fact, the more properties and the more
variables you can add to the mix and the more adaptive that model is, in a
way, the better it becomes.

Gabriel L. Manor - 05:52
Yeah, exactly. So it's kind of confusing because you say zero trust but then
you gain much more trust than you have ever before. Yeah, the name is
maybe not the best one, but again, everyone familiar with it today and
hence we can build nice context and behavior based on Zero Trust with
100 trust.

Ogechukwu Okonor - 06:17
I think the name somehow captured what the intention was, which is never
trust anybody, no matter what, when it comes to the infrastructure and the
It lifecycle. Because looking at it critically is all about security strategies.
So what are the strategies we can put in place to make sure that we are
who we tend to be or who we are today? Because every day things change,
people change, intention changes, pressures of life can also change how
people perceive things from yesterday. That means if I have some
percentage of trust today and the person tends to change, why I'm still in
that yastic of that percentage. You see, I'm vulnerable to threats.

Ogechukwu Okonor - 07:09
So it's technically reflecting what it's meant to do, whereby no matter
what, no matter my relationship with you, when it comes to it world there
is no any trust anywhere unless I can test your trust and validate that you
are trustworthy for the moment I'm with you, which can be subject to
change. The Nest moment bringing us to the cardinals when we talk about
it from the academic point of view, looking at the Nest framework where
it's always saying try to verify never trust. Make sure that the person is
who it tends to be, look at the policies, look at the privileges, they must
not have it because they used it yesterday, they have this privilege because
they need it now.

Ogechukwu Okonor - 08:00
And once it's done, try to always continuously look at what people are
doing, how the system work, the devices, the users and when you look at it
based on the cloud point of view then it becomes a little bit more complex
because you now classify it into having the cloud centric one and the user
centric view. So you are looking at the cloud centric where you are looking
at different embodiments of cloud in multicloud system and the
compliances and the people with the third parties sometimes you can't
even control them. So zero trust still fits in well with the scenario.

Maciej Owsiany - 08:47
If I could just add a little bit to that. So obviously, I think for those who
may listen to us and may have not clue what the ZTNA aspect is, an entire
concept. I always like that metaphor when someone explained long time
ago, when obviously these days the cybersecurity is super important, the
data being everywhere, all of those SaaS services and things like that,
where we actually don't know where the data is in 100%. I always like
that comparison that it's almost like obviously one of the principle is that
we always have to verify never trust but always verify the parameter or
the device. And it's almost like, let's say if you know the employee and you
know that employee is in a building and has a badge, you cannot always
assume that employee needs to have access to the data.

Maciej Owsiany - 09:47
I always like that metaphor when I was explaining what is a ZTNA model
and how the entire concept works. But basically today we look at that
employee and we may say, okay, is in a building. It was here yesterday. It
has an access to that certain data within a building. But we don't know
what could have happened a week or two weeks ago. And maybe that
employee has already been sort of let go from the job and cannot be in
that building anymore. And that's sort of the principle of ZTNA
architecture that we always have to check the devices, we always have to
check the environment that is accessing from and trying to access the
data. So I think I don't know myself. I've always liked to explain it this
way to the people who had no idea about the ZTNA concept and overall.

Ogechukwu Okonor - 10:42
Yeah.

Gabriel L. Manor - 10:49
So I think specifically the nice thing that happened from zero trust
network architecture is the way that it shifted into zero trust software
architecture because it became like together with the trend of OAuth in
JWT. Today, when I'm authenticating a user to a session as an application
developer with no matter which network is just on the Internet, I
practically authenticate the user every time they are doing a request,
which is something that never happened before. What we did is like having
one session for the user with a session ID. After they put once a password,
we just know that it's them, right? And then we have parameter, we might
check their behavior, check if something change in the location.

Gabriel L. Manor - 11:46
Today with JWTs, which is JSON web token that we verify every time a
user passing them, we are authenticating user every moment they are
requesting something from the cloud. And not only that, with the modern
authorization framework, every small, let's say, encapsulated function call
in the cloud is happening with completely zero trust. And that's nice to see
that the network trends came together with the application trend. And
today if we are looking on cloud native architectures like Kubernetes and
very modern cloud native network mesh and Envoy and stuff like that, we
can see that these both zero trust trends, one is the zero trust network
architecture and the other is JWTs. And the way that we are authenticating
user and devices became together into like zero trust application
architecture.

Dinis Cruz - 12:48
But we still have a lot of complexity, right? I think we elevated the
abstraction layer a couple notches up, but I still feel that in most apps, the
complexity of the relationships is still really hard to understand. And that's
a blocker for adding more zero trust because at the end of the day, you
could only do this when you can really understand or able to model the
behavior that you want and then you can apply those controls on top.

Nathan Case - 13:18
I would say that we're kind of dancing around a couple of questions here.
We definitely have the zero trust network architecture, which is what a
couple of us have already talked about, right? We're going to set up a
physical hardware available. We're going to set up a physical hardware
identification from my laptop all the way out to a server somewhere and
evaluate whether or not I actually am me the entire time that I'm
communicating with this target. And that's good. That's really important.
The problem is that, as Gabriel pointed out, that doesn't really mean much
if the attacker is actually on my laptop.

Nathan Case - 13:51
If my laptop has already been popped and we're beginning to see attacks
go through that zero trust connection between my laptop and the target
application, then all of a sudden, we begin to wonder, well, why is Nathan
beginning to do these things? And what data might be leaking out to the
side. And I think as we kind of pull back and I'd kind of like to pull the
discussion back a bit and start looking at what are the things that we
actually need to provide zero trust for. Certainly my laptop is important
and the non person entities in line here are important. We want to make
sure that those are consistently and continuously identified.

Nathan Case - 14:27
To Gabriel's point JWTs being exceptionally important, we want to make
sure every time somebody makes a request, that request is authenticated
all the way back to me to make sure that it actually came from me and it
actually went to the server and it wasn't somebody trying to laterally move
in our environment. And as we look at all of the architecture and all the
options in front of us, I kind of want to look at it from the architecture
point down where I want to make sure that the architecture has been laid
out so that the laptop is connected to the server or the infrastructure in
such a way that we're sure that it's the laptop and then all of the things
that happen in between that tunnel.

Nathan Case - 15:05
Assuming we've created a tunnel, then those things also are assumed or
proven rather not assumed to have come from the laptop and have
executed and been sent back. And I think that's one of the ways that we,
as I suppose security geeks, as architects, begin to be able to prove long
term that the things we're doing are actually helping. It gives us a nice
detection ability, it gives us a nice ability to identify people and hardware.
So I agree with you Gabriel. I think that's the way to begin. I just want to
make sure that we pull all the way back out.

Maciej Owsiany - 15:46
Yeah, go ahead.

Ogechukwu Okonor - 15:48
I also want to add that for every organization and business, they have the
reason why they want to apply zero trust. So what one organization define
as their assets and their priority based on their own business use, case and
requirement can be very different from the other. But the only good thing
about zero Cross that cuts across everyone is that it's making people talk.
Users, clients, everyone wants to get your own view of what works for
your deployment and it's bringing that harmony and community whereby
we can look at it as this is the best practice that is already working based
on this architecture. And if I try to borrow some of the mechanism used in
this, it can also work on my own architecture, fitting into my own business
drive and the priorities around the business.

Ogechukwu Okonor - 16:44
So it's not just like a one way methodology that works in a static manner?
No. If it's not dynamic, then it can fit into cloud posture and it becomes a
little bit compromised.

Dinis Cruz - 16:55
I can see hand off just to help the sequence of events. Right. So if it wants
to go, please finish. I just going to say that next.

Nathan Case - 17:09
I think it's an interesting statement to make about cloud. So it depends on
how you've implemented your cloud, I think. OG. Is that the appropriate
way? I'm sorry, I didn't ask to begin with. So I would tend to push back on
the statement and say Ogie. I believe that architecture in general is
independent of whether it is static, dynamic, transitory, take your pick of
word that you would look at the cloud with, but rather the architecture
that would go in and make a zero trust model work for your particular
customer. I think the statement that you made about community and
communication that kind of brings that architecture point all the way
back to the very beginning.

Nathan Case - 17:57
If we're trying to architect a zero trust model for, I don't know, pick a
company that's more than 100 years old and they're looking to go ahead
and implement that zero trust model in an application that's 20 years old,
that's going to be a really hard thing to do. Yes. Is it possible? Absolutely.
Is it easy? Absolutely not. And as we look at the things that we're
developing now, as we look at the cloud first applications, the serverless
applications, it becomes really easy for us to spin up both endpoints, both
the proof of my laptop and the proof of the API endpoint inside of I'm
going to go with AWS because that's where I'm familiar.

Nathan Case - 18:34
Going to go to the endpoint inside my VPC that's connecting directly to my
API gateway and that actually allows me to get all the way out to my
serverless cluster and then all the way back into my laptop pretty easily.
And I can then go ahead and do Gabriel's JWT evaluation of each
discussion point of each API request and return. So I think as we get into
it's a question of architecture. And that architecture that builds the
community that you just talked about really has to happen at the very
beginning of the application, or it's a very intense conversation about the
20 year old app, if you will, as we try to figure out how to put the walls
around that really old application and figure out what that is. That's
actually one of the reasons I work for Porsche.

Nathan Case - 19:18
That's one of the things that Porsche can do.

Maciej Owsiany - 19:23
That's why I think Nathan, if I can add to what you just said, I think it's
important for businesses to obviously make an investment. Understand it
doesn't work for every business. But what we're trying to do from our
perspective, if we're designing those systems, we're trying to push
businesses to invest money into just more modern up to date system
because obviously then a ZTNA concept, it's much more harder to
achieve. And as you've mentioned, if someone have perfectly designed
architecture from the server point of view, from again cloud point of view
and stuff like that but if the one parameter of that architecture is the
software which is over 20 years old, which is not patched properly, and
just other things after that, then obviously it's going to be much harder to
get that ZTNA concept achieved in the longer term.

Maciej Owsiany - 20:16
So absolutely agree with what we just said.

Ogechukwu Okonor - 20:19
Yeah.

Dinis Cruz - 20:20
The comment I was going to add is that when you implement a good Zero
Trust strategy across the multiple areas, and I think we can agree that you
start an acquire network, go all the way to the app and the roles and et
cetera, right. There's significant business benefits, like literally significant
business benefits, right? In fact, we just deployed recently a new office and
everything was Zero Trust. It was super quick, effective. The business
decides to change in a last minute, oh, we're going to go to that one, not
this one, right? Office, which happens, right? And were like, cool, fine.
Does he have Internet? That was the first question. Does he have Internet?
If he had, off you go. Right?

Dinis Cruz - 20:58
And even like our warehouses now and a lot of our deployments and even
our stores, I would argue that a lot of times in security, what we are a
really good canary in a coal mine analogy of other problems. Right? So I
would argue that if you cannot start to implement the Zero Trust
strategies or let's say Zero Trust architectures, you have much bigger
problems and you actually should start to address them because that will
impact the business. Right. These days, I think the advantage of having
clean, effective modern architectures versus not is literally the difference
between being profitable at this level or that level, being effective at this
level versus that level.

Nathan Case - 21:36
What?

Dinis Cruz - 21:36
I think a lot of people, and you guys make an interesting comment that I
would disagree a little bit, which is the solution to improve a system,
which by the way, you have systems that were deployed last month that
already legacy, that are already a massive shit show, right? So you don't
have to go back 20 years to find systems that have been badly
implemented and badly deployed that already are a massive mess, right?
So I think the way to always do transformation is to hollowing out, right?
It's basically you take a bit, you move, you take a bit, you move, you
replace, you do a replacement on top of the other one, make sure this is
good, get rid of that one now go to the next bit and then that is an
evolutionary step.

Dinis Cruz - 22:15
But my key point is that the business advantages of implementing what
we're asking here, which is segmentation, good control, good visibility,
good role based access, the side effects are massive from an organization
point of view. So it's almost like, ironically, security is not even the main
beneficiary of a good Zero Trust deployment. I think security can be the
driver because I think it touches us in some ways more than initially other
teams and we are very motivated by implementing zero trust network
because they allow us to do our job much better and have a lot better
visibility. But there is very real business benefit for implementing a lot of
these strategies and practices.

Gabriel L. Manor - 23:02
I think one of the things that came to my mind after Megan made a
statement about OAuth is the way that zero trust is letting us chaining
security. What I mean, so I used to work on a product, it's a famous
product called AAA server Authentication, Authorization and Accounting
Server which is server for many traditional network. Using that you can
have a session in your network and then you can check for postures, check
for password, et cetera. Authenticate an authorized user to the network.
Now, the way that traditional network work was like a session, usually
time based session. So someone connects to their computer in the morning
and let's say the username password has like lifetime of 24 hours. So every
morning they came to the laptop, connect the laptop and then the session
start.

Gabriel L. Manor - 23:56
And if we need to get to strength this session, we use strategies like
postures. So we say hey, we see that something suspicious happened in the
perimeter something happened in the laptop, some software is not updated
and then we update the session, we strength the security but in the end we
are always in the same session. If for example, something happened to this
particular huge 24 hours session, everything were failed. The way we zero
trust is we are not vertically scaling our sessions anymore, we are
horizontally scaling them. So we have like many micro session that for
each one we can decide on the right security model for this one. So we
have the network session that I'm connecting to the network in my home
which has a perimeter and has some limitations.

Gabriel L. Manor - 24:49
So I cannot access some cloud services because this particular session is
not enough and then I'm connecting to the VPN but that doesn't mean
now I have a session for everything, we have another session. So for
example, I can now access some cloud services because the it can be sure
that I'm in a secure network and then I have another session for a specific
cloud service but that doesn't mean I have a session for other service. At
the end when we analyzing it, we can still analyze it once because at the
end I have one identity but the trust is getting to zero. So the way we are
now scaling session in this horizontal chaining of session, getting much
secure way for networks which is zero trust but also making a stronger
connection between applications and network.

Gabriel L. Manor - 25:44
So we don't need to have contract between applications and network to
decide security and decide session and based parameter we can have each
product, each application, their own network and other ensure that they
trust on the contract that they are on this is another point that I feel
getting better with Zero Trust.

Maciej Owsiany - 26:08
So I think, Gabriel, we just said obviously it also applies to the
segmentation of the network. Absolutely. And it's really important because
also, I'm just referring to what you said, Dennis, previously, that some
businesses, even if they applied some of those concepts of ZTNA, it will
benefit them. Because again, if we're looking at the businesses which have
been segmented previously so whether the right VLANs were in place,
whether as you said, Gabriel, they were accessing one session, but they
could not have access others, it makes them essentially much more secure.
Because again, you have the one identity, you're accessing it from one
device, but it doesn't give you access to pretty much entire network. I
think the segmentation it's the right approach in terms of what businesses
should do. I think we should just.

Dinis Cruz - 27:19
Advantages are critical. Right. And I think this is where I think in security,
we don't in fact, I don't think it's a security. I would say in technology we
need better ways to show the value of what we're driving and to show the
value of, for example, the resilience that you get with segmentation of
networks, the reduction of the blast radio that happens on networks.
When you do have segmentation, when you do say, look, I'm having really
interesting conversation with the business now where we mapping not
necessarily our crown jewels because we know them, but we're mapping
some of the playbooks of what happens in certain scenarios. It's kind of
like, hey, the thing is on fire, who do we run to protect? Right? It's kind of
like we assume we're going to lose half the business, which we save first.

Dinis Cruz - 28:05
And it's interesting because your instinct might be wrong, right. You might
be going and protecting the wrong things, where let's say in a retail
environment, we want to make sure our stores are still operating. If they
operate, we have two to six to 8 hours to do things. Our warehouse can be
down for a day, right? It shouldn't be. It's a massive problem, but we can
recover from that because any space, we can put things in place. Right.
But it's important to know what does it take. But also, for example, the
warehouse should be one of the last ones to go down. So it's important to
start understanding. And segmentations allows you to have a much better
understanding of the blast radius. So you can say, look, if that thing there
catches fire, it's okay, we have our fire doors closed.

Dinis Cruz - 28:49
We block that environment. Right. So then we prevent spread into other
parts of the organization. That zero trust. Control is a key part of that.

Nathan Case - 29:00
I think you've touched on the reality, though, Dennis, and Magic, that the
real world implementation of Zero Trust is much different than the
conversation we're having right now. And the sad reality is that many of
the network administrators that are going to go, hey, cool, I'm going to go
take your pick of zero trust provider. I'm going to go buy that zero trust
provider and we're going to get rid of our VPN. Wait, what? That may well
be the conversation that they have, but the conversation isn't just, I'm
going to go install your zero trust provider on everybody's laptop and
connect it back to the networking core.

Nathan Case - 29:36
There's a whole set of work here that I think gets kind of we've talked
over it and around it, but somebody's actually got to do the micro
segmentation so that they have the ability to connect and prove that my
laptop is my laptop. And it's really Nathan sitting here, and I'm really
connecting off to the application that we need to have Nathan connect to.
And I can no longer laterally move inside of my network or inside of my
company's core, which is a massive change for many people.

Dinis Cruz - 30:07
But again, connect that to exactly right. If you connect that to the risk
profile. So the other thing that we're working, I agree with you because
we have our graph. You know me, I always map everything in graphs.
Right. And now again with Gen AI, we started to get to a point which I
always wanted, which is to be able to not just go to an executive and say,
here's your top risks. Here's the stuff which to say, hey, here's your risk
profile, here's what you own, here's what your team owns, here's the side
effects. And by the way, if that dude from your team is compromised,
you're blowing up that environment over there. Right. And in a weird way,
it's allowing the business to protect itself. So there might be business. They
go, that's fine, I'm okay, I'll take the risk.

Dinis Cruz - 30:46
Maybe other business who go, whoa, hold on. I don't want my
environment to be blown up because that team has this thing. And then
you start asking really good questions, why do you need it? Who needs it?
And then you make people accountable. You say, hey, it's impossible for
security to maintain all the roles. Right. It just will never scale. It has to be
almost whoever's making the decision. We need to give that risk and that
mappings to that risk owner. And that's the person that needs to be able to
make those decisions. And sometimes they get wrong and we work with
them or we get their boss to validate it. Right. But that scales.

Maciej Owsiany - 31:23
Exactly. And also just to add to this one, again, the world that we're living
today, it's much harder to control in terms of the devices.

Ogechukwu Okonor - 31:35
Exactly. Because sometimes we want to map it in our head. But when it
comes to practicality, it's not that so practical to know that I'm trying to
map this. It's always mapped against devices and data. So you are looking
at where would the breach come from and what are the. Suspected attack.
So if I can be able to map according to this target audience and target
device based on the behavior system point of view, then I can assign some
kind of policy or whatever to be able to trace the behavior and the things,
the transaction that goes through. However, it's easier when you're under
a simple or small enterprise, but when you come into multi cloud
environments, maybe you are using Azure and AWS or you are using your
on premise with the parameter security around it, and you've outsourced
to third party too.

Ogechukwu Okonor - 32:36
It becomes a little bit tricky in the sense that I'm trying to shrink my target
parameters based on these, to make sure that I've assumed the core
principles of zero trust, which is assume breach at all time. So that it
makes you suspicious of everyone's activity and be able to segment people
based on rules and policies so that if anything happens, I can be able to go
to the puzzle and equation to see where the red light started from and
trace it down to that. But it's easier when it's smaller than when it gets
into a complex cloud architecture. It becomes more tricky. I can see Natan
is like, no, I don't agree with that.

Nathan Case - 33:34
Yeah, I don't agree with you. And I respect the point of view. I'm trying to
figure out trying to.

Dinis Cruz - 33:42
Figure out.

Nathan Case - 33:46
What the best retort would be. So logging an understanding of an identity,
regardless of whether that be a machine or a person, what have you've
touched on a couple of things there. One is the identity appropriate for
this action. And I think the question of identity is key. So are you really
you? Is Gabriel really Gabriel? He looks like he might be an AI. To me. If
Gabriel is an AI, how do I prove that he's really Gabriel? Well, I've got
behaviorals. I've got all sorts of things that can prove to me that he's a
human. We do really funny things with the mice, with the mouse pointer.
But all of that there as an identity or a fingerprint of a human is fine.

Nathan Case - 34:40
I think as we get into the part that I disagree with most, it was really
around the concept of it becomes more complicated when you get into the
cloud and a cloud implementation. One of the things that I've seen having
built lots of data centers, is that when you build a data center hundreds of
square feet or hundreds of thousands of square feet, and you have lots and
lots of servers, and you have to figure out how they're all connected.
People make really bad decisions really quickly, and when you put them in
the cloud, in many cases they can make fewer bad decisions because they
happen to do it a little bit differently than they would do it in a data
center.

Nathan Case - 35:14
So in many cases, in my experience, I've seen people be able to implement
in a large cloud just as well or better because I have the ability to control
some of the services directly and those services are directly mapped to an
API. And because they're directly mapped to an API, I can then go ahead
and get the logs. But many of those things then become a question of and
to your point and the part that I agree with is that humans do stupid
things. We just do. I almost locked myself out of my hotel room last night.
But those types of things that happen because we don't have time or we
don't think or we don't make the choices that we need to make.

Nathan Case - 35:53
And I'm not 100% sure that it's dependent on cloud data center or frankly
the network that I keep in my basement. I think it turns into more a
question of did I actually spend the time to arc detect it correctly and did I
spend the time to actually think about I need to figure out how to evaluate
that. You're you and I think that's an identity issue.

Ogechukwu Okonor - 36:12
You have the time and you spent it right trying to do all the calculation.
Still, we are human. There is what we call human factor whereby
accidentally with no intention of doing those things is always
misconfiguration issue. So things can happen.

Nathan Case - 36:30
It's a question of configuration versus architecture. If we're talking
architecture and the five of us sit down and we spend a week and we
architect something, the goal would be that we've checked each other's
errors and certainly bad things can happen. But the question of
misconfiguration becomes a question at that point of should we have
automated this better? And not a question of necessarily zero trust or
identity.

Dinis Cruz - 36:54
See more and more. First of all, I have a massive problem with the word
stupid, right? And basic.

Nathan Case - 37:00
I owned it myself.

Dinis Cruz - 37:03
But even now in example, it's not that you were stupid. You put it in a
place where you can make a big error, right, or a big problem, right?
Because first of all, if it's basic, people would do it, right? I think the worst
thing we can do in security is why don't just do it? It's so simple, it's so
basic that is so offensive. If you're on the other side and you go dude, step
on my shoes for a second and you realize it's nothing like basic. But the
thing about the stupid part, and I think again, we do that in security and
I've been guilty of that too in the past, right, is the fact that I really like if
you haven't seen the Three Mile Island analysis and story, which is pretty
amazing and it was a nuclear disaster in US.

Dinis Cruz - 37:39
And there's a great analysis where they did a review of it and for some
good reason, the people who did the review were actually really good. So
instead of looking at the root cause of the problem which they figured out
what physically actually happened that led to the nuclear problem. Yes,
there's a sequence of events, but what they did was they look at the
secondary stories, like this story that they put a whole bunch of people
that used to run a nuclear reactor in a submarine in a power station and
they never made the transition effectively. So your signals in a nuclear
reactor, in a submarine are very different than the signals that you care
about in a power station. Right?

Dinis Cruz - 38:22
And I think what's very interesting is that those second stories, which is
the thing that happened, or the real root cause, which, for example, in
most vulnerabilities, you know why, is because there was no time given to
proper testing, no time given to architecture, no time given to reviews, no
time given to education. That's why the vulnerability was created, right?
And these days I like the human events because you know what they are?
They are your warning signs. So my argument these days is that if we
allow a user to do an action that has a massive impact, the user is not the
problem, right. Even to the point of malicious, right.

Dinis Cruz - 39:06
Because even if the user is malicious, right, even if it's an insider, to be
fair, you will be extremely unlucky that the first time that you see
something from a malicious insider is the one, is the really clever one who
really going to do a lot of damage, who's really going to basically cause a
massive problem. What you're going to have is you're going to have a lot
of, let's say, inexperienced or not very sophisticated users that are going to
try to do something malicious and they're kind of going to do something
bad, they're going to kind of stumble and they're not going to be able to
really do a lot of damage. I don't think what we sometimes do very well is
pay attention to those. So in a way, I like the users because the users
should have common sense.

Dinis Cruz - 39:48
They need to do their job and if they cause a lot of damage, it's not their
fault. It's our fault. These days, we don't allow engineers to go to
production or we shouldn't allow engineers to go into production and
going, yeah, let me just click on things to see what works, right? We have
change control, we do infrastructure as code, we have peer reviews. Why?
Because we've learned that even the best person might make a mistake
and the stakes are so high. But what you also do is you catch the mistakes,
you catch the errors.

Dinis Cruz - 40:15
And then again, my view would be very simply, every time a bug is
reported that you don't know about or a security issue that you don't
know about, that should be a P one or at least a P two, because for that to
happen, 20 things have failed already, right?

Nathan Case - 40:35
And that's the trick.

Dinis Cruz - 40:36
That's the trick right there. So users, in a way, you think, oh, I left my key
in the thing. But that's because you have a stupid authentication system,
right? These days you can have much better, right? Maybe use your phone,
use other things. And by the way, the key cards in hotels are let's not go
there. Right.

Nathan Case - 40:55
I didn't have my flipper zero with me. I'm sorry.

Dinis Cruz - 40:57
Exactly. Right. But I think that's, again, user experience. So more and
more, I like those P ones, P two S and P three S, and those things caught
by users because they will allow us, for example, to understand our blast
radius.

Nathan Case - 41:15
Let me pull back from that word stupid. I think that's probably part of it.
And I didn't mean to trigger you. I apologize. I'm looking at humanity as
humanity. One of the things that we tend to do is forget to clean out the
belly button lid, right? Like, we don't wash our feet, we forget to wash the
belly button. It's just one of those things. We don't do the basic hygiene
thing that humans are supposed to do. And when you look back at the last
100 years of humanity, that's a continued response. And to your, what
about the other 20 failures? And I think that's a great answer for it. It's
the monotony of every day that really gets all of us.

Nathan Case - 41:50
It's the thing that we don't think about because we've done it 50 times and
we forget to do it that one time that locks you out of your hotel room.

Dinis Cruz - 41:56
Yeah, but in business, I think we need to think of security as the side
effects of basically a lot of times, processes that are not well implemented
or not very well mature. That's why developers, again, have a massive
problem when we talk about developers as if they were doing it on
purpose.

Maciej Owsiany - 42:19
And also what you said, Nathan, I really like that, because you said if
something didn't happen 20 times, it doesn't mean that it may not happen.
Obviously, that's why the architecture needs to be designed perfectly. And
as you said, Dennis, we tend to blame the users because they've done a
stupid thing and they've done this or they've done that, but it needs to be
down to the system which is designed ultimately.

Dinis Cruz - 42:51
Then you also have the case of architects and systems that are designed
that are completely unrealistic. I never forget once this guy was showing
me this insane, probably the most beautiful authentication authorization
system I've seen, right? And the guy showed me that. And we're thinking,
can anybody else apart from you and that dude actually write this
properly? Write this in this way? And he's like, no. See, that's the problem,
right? The problem is you don't scale because your company is growing.
Now you're going to have ten people creating systems that increase the
attack surface, and you created a solution. So I would argue that it's bad
architecture. You could say that it's the most beautiful. In fact, it's zero
trust. Right? Amazing architecture.

Dinis Cruz - 43:36
But I would argue it's a bad architecture because in the real world it will
cause tons of problems because it's not.

Maciej Owsiany - 43:43
Which essentially I may be controversial here, but the concept sometimes
may not be ideal for all of the businesses, but part of the concept, as long
as those businesses will be implementing part of that concept at the time, I
think that is going to make them safer.

Nathan Case - 44:07
I think that goes all the way back to Gabriel and the original comment
that you made around application security and identity. It's a long walk.

Gabriel L. Manor - 44:22
I think, getting back to the AI discussion. Yeah. So I think the thing that
we are going to see sooner or later getting into software is identities that
actually based on AI, not Gabriel, that is maybe AI. So agents, bots, stuff
like that, we are seeing them getting more and more, especially where
there are advanced user. So for example, if you look on GitHub today,
every agent, let's call it every tool that you are running as part of your CI
CD is someone with identity and with all the supply chain security, we also
need to secure them. So, for example, if I'm now delivering code and I'm
running like eight, maybe ten tools on that code for security, for testing,
for code coverage, for static analysis, et cetera, each one of them is a
security pillar. Because they can change my code.

Gabriel L. Manor - 45:30
They can maybe stall it. They can even modify it on the way to production.
They can pretend to someone else. We saw like an attack a couple of
months ago that attackers pretend to depend about, which is a popular
bot by GitHub to fix third party libraries. They pretend to depend about
and make developers to think that they need to merge changes. But those
changes were vulnerable. So the pillars in the modern security are not
identities and devices anymore. They have much more meaning if, for
example, I have an AI boat that from their roles or from their
responsibilities can do the same as a human identity can do, but also have
a level of control as a device can do. So how do I manage all these
sessions? How do I manage all these pillars? How do I authenticate and
authorize them?

Gabriel L. Manor - 46:34
And I think this world of having much more than just identities and
devices, or identities and devices and servers is getting more and more
exciting with all these zero trust architectures and better security models.

Dinis Cruz - 46:52
Well, the thing about this is that if you think about it, the one thing we can
know and do a worldly map on this, and you could totally see, by the way,
the session on Monday on Worldly Maps had a bit on it where Simon really
talked about the innovate, leverage and commoditize, which is one of the
best ones I've seen. But we know that deep fakes identity impersonation,
the quality of the impersonation is going to go to the roofs. Right. It's
almost a question of when, not if. Now. And I think that actually could
have a positive effect. I think it's going to cause a big shock in society.

Dinis Cruz - 47:30
But the end of it could be a really demand, a real demand in strong
identity, in a real demand in really being able to identify who's who's,
saying what, how do I trust that entity versus that entity, even in business,
right. How to create trust relationships within things. And that's very
positive because at the moment, a lot of the identity requirements that we
have are still very fuzzy. And I think that will be quite positive. And again,
that's one of the pillars of zero trust, right. You need to know who's who.
So I feel that is know. In a weird way, the exploitation of know is going to
drive that. It's quite funny. I listened to the interview from Gary McGraw
recently, and somebody asked him if you know Gary McGraw, he's a
legend in our world, right?

Dinis Cruz - 48:17
Asked him, what is the biggest innovation in the last seven years? Right?
And he said, can I say ransomware? Because in it was a good innovation
from the criminals, but it actually drove a lot of behaviors. It made
security a lot more real, and it was going to happen anyway. Right. Those
die intersection was on the cars. It's just that you happen to be with that
particular thing. So sometimes an advance in the malicious capability to
do something creates the business drive to actually do some things for
real, because you cannot busk those things. Which is why these days, we
do have decent crypto, we do have decent tools. We do have different
encryption. Regardless, think about it.

Dinis Cruz - 49:00
Of a large number of key players not wanting us to have encryption in our
devices, we still have a decent level of encryption for most of us. Right.

Nathan Case - 49:13
Cool.

Dinis Cruz - 49:13
Any final words on this topic? You guys can continue for a bit. I do need to
jump into my other session, but feel free to continue if you want.

Gabriel L. Manor - 49:23
Yeah.

Nathan Case - 49:27
And I did google you. I hope that's okay. It looks like you're a teacher at a
school, at a college.

Ogechukwu Okonor - 49:36
Yes.

Nathan Case - 49:38
How does this play in for your students? I would think zero trust at a
college level would just be like mind numbingly hard.

Ogechukwu Okonor - 49:48
It depends on how you see it. So from which perspective do you want to
look at it?

Nathan Case - 49:54
From yours?

Ogechukwu Okonor - 49:54
Actually, I would assume from the students.

Nathan Case - 49:58
It just magically works.

Ogechukwu Okonor - 50:00
It's just that it's like a boss world. Everybody is talking about zero trust
then looking at it based on the reality around zero trust is interesting
whereby you can be giving a particular kind of network and tell you to
look at the kind of things you can do to be able to implement the principal
cardinals of zero trust whereby you look at the list privileges. Why did you
accept that and assign that to the risk privileges? What have you looked at
by quantifying that? These APIs or this part of the work will be assumed
targeted bridges and what will be the mechanism for verification and
authorization before you can give assets? So these are the areas that we
looked at, Paul. It's interesting to see from different perspective, too.

Nathan Case - 51:02
Yeah, I would think that can't be easy, especially at a college level, to have
to micro change or micro segment each of those pieces so that you keep
the students where they're supposed to be and give the professors like
yourself, the ability to control just like your.

Ogechukwu Okonor - 51:20
Little bits and trying to use because sometimes I try to look at it based on
different levels whereby we can use AWS as a vendor and use Azure as
another vendor and try to multi cloud them and see if you can still have
the same control. When you add just one vendor and you could see that it's
not just that easy. No.

Nathan Case - 51:48
Yeah. When you start getting into multi cloud, especially college, I imagine
there isn't like and I apologize, I didn't catch the university. Which
university are you from?

Ogechukwu Okonor - 51:59
University of Rohanson.

Nathan Case - 52:02
So it's a pretty impressive university.

Gabriel L. Manor - 52:04
Sorry, I have to drop off. So it was nice to meet you.

Maciej Owsiany - 52:08
Till next meeting you.

Nathan Case - 52:10
Gabriel a good one, but I think it's interesting because I would wagerly for
a university relatively well funded and I can't imagine you don't think so?
Okay.

Ogechukwu Okonor - 52:30
No, it doesn't work like that everywhere. It's always constraints around
that. But at least I would assume that open source that you can use
around and it makes life easier.

Nathan Case - 52:49
I think there's a long discussion about how you guys are working, how the
university is working through that. I hear the pain in your voice about how
you're implementing and it makes me sad. There's got to be a better way
to do that somehow, and I don't know what it is. I think you probably will
have to figure it out. But if there's anything I can do to help, I'm happy to
help out. But yeah, it sounds like it's rough.

Ogechukwu Okonor - 53:16
Maybe if you think there are better ways of implementing that will help.

Nathan Case - 53:26
You would know better than I would. I mean, the reality of you being.

Ogechukwu Okonor - 53:30
On remember, zero trust is what we are talking about. So no trust.

Nathan Case - 53:34
No trust. Fair enough.

Maciej Owsiany - 53:36
No trust.

Gabriel L. Manor - 53:37
Yeah.

Maciej Owsiany - 53:38
I actually found it quite interesting how we started talking about the AI
and obviously how this may actually make things more difficult in terms of
verifying who's actually who. And were actually talking about the AI and
Chat GPT just before we started recording a session. So it was quite
interesting how the conversation, what the conversation lead into. But
anyway, yeah, it was good to be on the panel. Nice meeting you.

Ogechukwu Okonor - 54:10
It's a pleasure. Bye.

Nathan Case - 54:12
To reach out if you'd like. I'll see you guys later. Bye.

Dinis Cruz - 54:15
Take care, guys. Bye.
