---

title        :  “Shift Left” Isn’t What You Expected 
track        : Risk and Governance
type         : working-session
topics       :
featured     :
event        : mini-summit
when_year    : 2023
when_month   : Apr
when_day     : Tue
when_time    : WS-15-16
hey_summit   : https://us06web.zoom.us/meeting/register/tZcoce-upzgjG9M-9D1b1KYGbt2W7wC20R-w 
session_slack:
#status       : draft
description  :
banner       : https://pbs.twimg.com/media/Fs5YdBeXwAIeehQ?format=jpg&name=medium
organizers   :
   - Chen Gour-Arie
  
youtube_link : https://youtu.be/7Hv3B_x4FyI
zoom_link    : https://us06web.zoom.us/meeting/register/tZcoce-upzgjG9M-9D1b1KYGbt2W7wC20R-w 
---


## About this session
Let’s address the elephant in the room — “Shift left” hasn’t had the impact on our software security as many of us expected it to have. While it does have much merit and has influenced security in an indispensable way, I argue that “shift left” should be viewed as a tactic in a larger management strategy rather than a comprehensive solution to solve application security woes. Just as software development is a very complicated process with many layers, “shift left” should not be viewed as a straightforward, linear effort. This presentation will review the success, concerns and potential of “shift left”  and how we can “restart” the process by applying it a little differently.

## Session Transcript:

Dinis Cruz - 00:00
Hi. Welcome to this open Security Seven session in April 2023. And we
have Chen here, which is going to expand on why shift left isn't what you
expected. We already had some interesting conversations before and we're
looking forward to see where Chen is taking this from. Over to you, Jen.

Chen Gour-Arie - 00:19
All right, thank you very much for having me and thank you for the
opportunity to talk about this subject here. So I'm Chen, I live in Tel Aviv.
I'm a co founder and chief architect of Endosecurity. My passion is around
building things, but professionally I've been more busy with breaking them
for, I guess the beginning of my career was a pen tester for many years
and then that led me to take more and more interest in the side of
software engineering. I think the second half is more about engineering
cyber solutions and so I can still be active on these two realms. What we
are building at Tenzo is an SPM solution. We are building it to allow
sustainable and scalable AppSec by working on building all the bits and
pieces that are necessary to be able to list all your assets. Also in the same
way, to list all your controls and get some feedback on the status that you
have in each control so you can handle and focus on the critical alerts.

Chen Gour-Arie - 01:26
This is a very interesting experience to build this kind of innovative
application, but it takes us into places that we need to really think about
how this is done and what's inside in application security as a realm,
what's going on inside so many frameworks, so many ways to approach
the problem and think about it so naturally. Because our flow is to list an
asset and then understand the controls and then measure the controls.
Defense metrics approach is very relevant to adopt as a way of thinking
about this. This is some of the work of one of our advisors, Sonilu, and it's
about thinking about the problem in a way that you use NIST security
function and then list down the areas of technology that you have and
your application. We are here in this tier and then you think of how to
combine the right combination of technology, people and processes in a
way that will allow you to make sure that you're covered in each and
every one of these activities, these functions of security.

Chen Gour-Arie - 02:33
This approach is very systematic and this is why we attend. So we relate to
it very much. It builds on a well adapted structure of security functions,
framework, and then you also drill down on each area and you think you
have three tools at hand. It's always a solution, a technology, a process
that you can try to adapt throughout the organization and the people that
you can operate within it when each and every one of them have the pros
and cons building too much on process can create antagonism and can
break down in different places. You don't have enough people to do all of
the tasks and your technology is not able to do some of the tasks. The
right combination and the right visibility into your defense metrics is an
approach that we attend or we really like to include in our process of
thinking.

Chen Gour-Arie - 03:27
We are playing with it because in application security, the Identify, Detect,
Protect convention of NIST sometimes challenging to adapt, to apply
directly to everything that we do. So we're always busy with it. We are
mapping in it. We have this open project, the AbSec mapping vendors can
subscribe, can submit their solutions and then we list the solutions. We
give of information about each solution, let you also see what kind of
vendors have and also open source tools inside. The main purpose of this
is to help to assist everybody in the community in understanding this
landscape of application security. You can also kind of a tiny tool to build
your own map and then see what kind of things you can have for
infrastructure as code security, what kind of things are out there, and also
open source solutions and then kind of try to lay down the things that
you're doing to have another perspective on this.

Chen Gour-Arie - 04:32
In the process of building this database of all this knowledge, Iratenzo, we
face a lot of discussion about how things should be done, why things
should be done, what is the best approach, what kind of frameworks we
have and what is the other differences. Also about things that are more
like a trend or an approach that is even wider, like shift left. We get to this
discussion a lot and what does it mean exactly and how to do it, is it
DevSecOps or not, what is it like, what's inside exactly? We are very
consistent in our approach to try and map a good defense metrics. So if
we go down.

Dinis Cruz - 05:18
A little.

Chen Gour-Arie - 05:18
Bit deeper into this question, we can already start to break it down also
from the threat perspective, realize the full threat and then this gives us an
idea on what kind of assets should be under the jurisdiction of Upsec. Here
is just a simplified, top level, stride approach to all the things that make up
your full application stacks, again in very high level. When you think about
tampering related problems, so you need to consider your CI CD pipelines
themselves, the external supply chain, the internal supply chain, and then
also the instrumentation and everything that is actually operating your
application. All these under the risk of tampering. You as application
security function, you have to think of fortifying this threat, fortifying your
assets from the threat of tampering across the stack. This is what makes it
so complicated. We break it down to actual activities in the NISS security
function domains.

Chen Gour-Arie - 06:18
We already have some more familiar names for those of us who are not
doing stride every morning. We already see categories of tools and how
they help in breaking this down. All this is something that happens every
day in every company that exercises application security. All of a sudden
there is this okay, we need to shift left, we need to try and shift left the
same way that developers shifted left testing. So who does this? This is our
generally speaking, our team. We have the leaders of the team, usually the
manager and their architects. They're about building up some protection
into the environment and including the right processes for validation for
testing. That is not part of what we today most teams do as part of their
DevSecOps gig. Not all of them, but on the other side of the architects
that are into the content, understand the application to its logic and to its
business logic functions and then help build up the right protection around
it and within it and the right processes to validate it.

Chen Gour-Arie - 07:32
We also have today a growing trend of DevSec ops and DevSec ops. We
have instrumentation, a lot of testing tools to cover up for a lot of the
identify vulnerability identification process. We get asked in all this what is
shift left? Who is doing this out of this team? Is it something that someone
else do? Should the developers own it? What part of it should developer
own? Who is the owner in general? This is what this talk is about. We are
going to talk about what is it a perspective, white perspective on what
shift left is just looking different perspective of shift left not necessarily in
security and what was the impact of it. I think we will drill down into the
discussion on how does it look today in application security? We will wrap
up with some discussion on things that maybe we should consider as first,
easier and more impactful steps to shift left and to inspire a shift left
movement for security inside an organization.

Chen Gour-Arie - 08:46
So what is it? If we think about the dev SecOps as the DevOps as a
delivery model or framework to think about, a way to think about how the
software factory works. The software factory works in phases where from
the moment something is in the ideation phase up to the level that it's been
operated and been kept operated and maintained in production and then
usually it feeds back into evolution of the software start add a new feature
or fix a problem and go all the way back until this problem is operated.
The infinity loop was already something that we all familiar with. Shift left
is if you think about this loop and you spread it one long line, the left is the
start, that is the side that starts from the developers from the create phase
of the story. The right handmost side is the right where things are
operated, things are already in production, things are already materialized
into something that is part of our business, part of our dependency chain
and it's harder to move.

Chen Gour-Arie - 10:02
Here is the beginning, here is the genesis of all software. It starts from
someone has an idea and then wrote some code and shift left is about
moving things here because then it would be easier to control the
evolution and fix problem before they get into a place where it's a bit
harder to get rid of what kind of things we can shift left. If you think
about this as a broader term, not only security shift left security, but
broader term, the creatives. On the leftmost side you can't shift it more to
the left because it's already at the left testing and security testing can be in
the intermediate side, it can be pushed as much as possible to the left and
then the rest of the flow is alleviated from those tasks to a point.
Something that is maybe not usually conceived as a shift left activity, but
all the effort of describing elements of your deployment in terms of the
actual artifacts, but also the topology and the way that your production
environment operates and artifacts communicate with each other.

Chen Gour-Arie - 11:18
This effort has been greatly pushed to the left with infrastructure as code
approaches in the last few years and had a tremendous effect. This is
definitely something that can be decided, an organization can decide that
they expect that part of activity that is about taking a code and preparing
it for operation in production can be pushed to the left and be done by
developers. What is the motivation? The motivation, as said before,
everything starts from the code. Everything starts from this moment in
time that someone had an idea. In an enterprise environment, this idea is
different maybe than in your basement. Still it's the same thing that you
have some an idea and then you build up plan and start building it. All you
need is a computer and an IDE and you can start code it. Every piece of
software that we're using started from there.

Chen Gour-Arie - 12:21
The idea of bringing more and more to this point in time is about saving
time. Later things get more complicated, things get more convoluted in
one another and it's a bit more difficult to spot and fix. The actual things
that you shift left, things that we touched before, is that to make testing
something that developers are in charge of? Kind of by the book testing is
core activity for developers. And they test with code. They write code to
test their code, which always give some a paradox kind of question, like
who tests the tests? This is already a standard and everybody is doing this
and also packaging and building up the artifact, the containers and all the
information for further integration and deployment is already also being
adapted as a standard. These are the kind of things that we can shift left
and when we dive in more, let's try to look this in the eye and answer is it
useful for us?

Chen Gour-Arie - 13:43
If you are looking at your end of the year performance report for your
engineering organization and or even for even larger than that, even for
the full company? It is I think something that many managers face is this
question am I leading the right balance between investing infrastructure,
making things more, investing in Velocity, making things run faster in most
cases but still stopping and investing in some kind of an infrastructure? Or
should I keep just building the same way I do? Is this process right? Is it
slowing me down? Things that part of the decision making that is inspired
by thinking that we should shift left activity to save time later, not all of it
is successful in the same level. If you think about containerization or any
other type of packaging I think that it speaks for itself. When we look at
all these public and private repositories of artifacts and amazing array of
possibilities to orchestrate them into an operating production applications,
I think that we can definitely say that the approach of moving part of that
job to the hands of the developers, to the beginning of the plan has been
very successful.

Chen Gour-Arie - 15:14
Everybody that practices it is very happy with the results and the impact
that it has on their velocity. Infrastructure has got the same way. Maybe
you can even kind of think about it together. It's maybe one thing with two
faces and then another thing that we find very successful because it is not
necessarily critical but it adds a lot of value and it's not hard to
accomplish. Attribution or the developers attribute facts or simply who
they are for example using code owners. This is an approach that is very
useful and has a lot of impact on the visibility that the organization has
into artifact, into the code, into what's happening and greatly improves
the ability to lead a good response practices. Instead of response become
faster and more effective and visibility in general is improved and it's a
great supporting asset for organization that is living, breathing, actual
production and needs to adapt to things that happen in real time, things
that are a little less successful.

Chen Gour-Arie - 16:44
I'd say maybe it's a bit dangerous, it's a bit risky to say because a lot of
people are advocating patterns like TDD and extensive use of testing. Of
course this is something that is a must have for every organization that
wants to lead a healthy engineering organization and be on top of a
quality control. To control the quality of their outcome, but it is a large
investment with varying level of impact. I say this because not all test
flows are the same. When we talk about unit tests, sometimes it makes
much more sense, but sometimes to conduct a full end to end test would be
very expensive in terms of investment and limited in its ability to actually
grasp the full potential of what can happen throughout this end to end
scenario and give false results. It's a lot of investment and if you haven't
done it right or if your problem space is too complicated, this investment
would not necessarily pay off.

Chen Gour-Arie - 18:02
I think this is why we can see in most mature organizations that already
have a large function in R and D, we can see also some layers of quality
assurance processes, whether automated or manual, that are the kind of
mitigation control for everything that was missed by the tests. The tests
are being complemented by quality assurance manual or automated.
Which means that it's a little less effective than if we compare it to
another activity that was shifted to the left like containerization, where
you don't expect the people who were used to code the It infrastructure or
system infrastructure and now called DevOps. They are not expected to
give attention to every new image that you publish or to every new
TerraForm configuration that the developer is building or to a new Argo
template. Those things are built with a framework and agreement between
engineering teams and can scale up very easily.

Chen Gour-Arie - 19:10
All the developer needs to do is to take responsibility for the activity of
describing those elements of the code, where in tests they take full
responsibility in building the code and sometimes even base their design
flows with, say something like TDD on the notion of testing. The results is
usually still need someone else's attention to make sure that it's proficient
and that it's at the point that they wanted to we move into the next type of
testing, which is shift left security testing. It becomes more dangerous
because when a bug slips by the test and by QA and ends up to production
and meets users and come up through the channels of bug alerts, it is clear
that the developer was built. It there is a gap now and this is
misfunctioning. Something is misfunctioning and you should get the
attention. The case of security is not the same because there is some gap
between the validity of the report and the actual defect.

Chen Gour-Arie - 20:31
In many cases and many of the engines that are about producing alerts
regarding security. The part of code quality is that is related to security.
Those engines are usually creating noise. When this noise meet the
developers, it jeopardize one of the most important things from
cybersecurity perspective, and it's your cooperative relationship and the
buy ins of developers. In other terms, in more simpler terms, if you pitch a
problem if you pitch a problem that is that they it's not real and cannot be
prioritized by developers or something that they really need to give
attention. To, and you pitch it again and again, automatically, in large
volumes, you most possibly end up losing the buy in of developers and
them saying to you, I don't care about this subject in general, which makes
this approach dangerous . You could maybe get a lot of reports, so
counters of things that are probably problematic with your code base or
even with your running applications.

Chen Gour-Arie - 21:48
To trial them and mitigate them will be more challenging to get this to a
point that the developers have agreed to fix the final backlog. And you
don't really usually affect functionality. Many times it's only just like a
synthetic gate on your way to production. When it's too synthetic,
creators, makers will bypass it, will just go around it. One hand, the effort
that requires for triaging to truly triage and introduce only true problems
like usually what comes from QA feed will be real problems. This button
doesn't really does what it's supposed to do, the pop up doesn't show up.
In security the feedback will be there is a potential vulnerability reported
by this tool but to say here is an exploit in many cases requires a lot of
effort and there is not enough people to validate this and give you this
kind of assurance, but on the other end you cannot delegate it.

Chen Gour-Arie - 23:02
Shift left is actually touching specifically this point it's also about we don't
have enough system people, let's try to scale up the way that we are
describing our infrastructure, that's one thing. We also have situation
where we don't have enough QA people or we don't want to invest too
much in QA. We want to bring more of the abilities of QA to the beginning,
to the left. With security it's more problematic because in many cases the
developers are not fully aware of the consequences of security defects. It's
one of the places where it's most apparent is in questions revolving calls.
Just to explain calls to a person, even if this person is developing a web
solution that just to explain calls usually this explanation comes in the
setting of why did you enable Course with credentials to every domain that
is out there? You go through an explanation of 1 hour on how course
works.

Chen Gour-Arie - 24:17
Frankly, even if they are very interested, they will forget it in about a
couple of weeks. Two months or a couple of months. Next time might
make next time they might do it again. Because for them more crucial that
their testing environment is working properly. And this slows them down.
So they just enable this goal setting. In many cases we cannot shift left a
triaging. There is not enough knowledge and understanding of the
problem. A lot of reports, the numbers surely can easily antagonize an
organization and they cannot really prioritize this. When you cannot easily
prioritize something you go into lengthy discussions on priorities which
takes a lot of your time and usually also don't lead into something that is
useful. So it's a lose situation. Just keep a discussion and this could look
like prove that this FCA report is exploitable. They don't have the capacity
to prove this.

Chen Gour-Arie - 25:31
But you should solve it. Because maybe even if it's not exploitable today, it
will be exploitable tomorrow. Because tomorrow one of your developers
will invoke the function that is vulnerable in this package. The response
from the engineer would be we are very busy with things that happen
today. Let's worry for tomorrow. Tomorrow. This is a very common
discussion that we hear on the sidelines as we try to help the teams build
up a good relationship and solve those problems. The bottom line is that
the main thing that security teams should be after the way personally I see
it is the buying in of their partners because eventually it's very rare that
security teams are actually applying fixes. They're instructing and
prescribing fixes. The people who are actually applying the fixes are the
engineers and if we don't have their buying we failed as security teams.

Chen Gour-Arie - 26:36
Yes.

Dinis Cruz - 26:38
Here one of the things is also to make sure that there's a good feedback
loop, right, so that you can really understand what you want but also you
can gamify this right, so that the teams can see when they do something,
they can see quickly that hey, you just made a difference. Also there's
nothing wrong with identifying which are the teams are doing really well,
which are the teams that sometimes are not as good, right? And also
prioritize them. So you have context in there, right?

Chen Gour-Arie - 27:09
Exactly. I think that this exactly leads me to my next slide when we talk
about the things that we should be shifting left and these things are about
preparing and a right step in this direction would be to think of what
would be the first smallest step to bring this buy in. At the end of this buy
in, when the organization is fully committed, they will shift left everything
and they will want ID level integration and commit on checks on the
commits and full CI CD integration they will want and they will want to
build it for themselves. As application security you cannot jump to this last
step of the way. You have to go through the steps. The first, easier steps is
to focus more on attribution and more on having them play with the
concept of instead of enforcing the security controls directly.

Chen Gour-Arie - 28:20
Start a discussion that is visible because it is done the coders way with
files in repositories that describe what needs to be done and that will start
describing what the organization is going to do about application security.
For example. Some building blocks of this would be that you need to think
about that it only happens when they get the buying, when they decide it
does. Because even if you get a jurisdiction to run a bunch of tools in your
CI, if the end result, the user experience of the developers is not good
enough, they will drop from this lane, they will bypass it and drop from it.
It has to come when they decide it is time. You need to focus on things that
benefits multiple groups. I think that one thing that shows here is for
example, code owners is something that has a lot of functionality across
organization.

Chen Gour-Arie - 29:17
You can use it for many different things, you can use it for measuring
performance, but also for setting up the right channels for dispatching
messages when there is a problem and then also giving access to some
artifacts if you did it right and you're confident that you have the controls
to manage it. It benefits a lot of interest groups inside an engineering
organization. It's a good example because it's kind of simple and scalable
in a way that everybody can benefit from it. As you do this, as you think
about the first thing that you should have your developers do and it is not
automated testing the first thing you should have developer do, you need
to think about how you can take from that. Also and get two of the, I'd
say, most critical things that you need, which is the data. Ability to report,
ability to communicate things that are relevant both for developers and
for their managers.

Chen Gour-Arie - 30:18
To reflect picture that is relevant for the workflows of the developers but
also for the managers so they can later on increase the investment on
things that you're doing. Shift left can really help you if you choose the
right things to shift left in the beginning. Things that we can start shifting
left today. The Attribution is to push the adoption of patterns such as code
owners as a security, as something that security has a stake in. Code
owners is something that we need to give context exactly like I said before.
Even take it, you can take it to the next level with starting to declare
security facts and also maybe information about the security lifecycle of
the artifact. I've seen teams actually been on a talk about threat model as
code start building threat model concepts into code. You would get the
context, the visibility and also the participation of developers as the first
lighter step before we start answering some questions that usually would
lead to problems when it will be about the severity of this specific bug.

Chen Gour-Arie - 31:45
You see a team of ten people discussing the severity of a specific bug when
you know that the numbers in the scanners are like 10,000 times larger
and those people are crucial and their time has been wasted. One of the
things that you should be focusing shift left on the first step at least would
be to declare your security facts to give context to the code, to where
developers are active. It can happen in the natural manifest. Some
manifests give you room for some code manifest gives you room to declare
this information. Like if we talk about the node package manager
manifest, there is a lot of room in there to declare it. Or you can create
your own file or at least you should stick to some basis that are already
fully adapted. Like code owners it's very known and adapt this as your
first step, first tiny step in shift left and build on top of the ability to see a
wide context your future plans, where you can say okay, the first citizens
in the entire inventory that are going to fully onboard in.

Chen Gour-Arie - 32:55
Testing in static code analysis testing in CI would be those ten artifacts
because they said that they need more help in security in their Attribution.
They said this is a critical artifact. We want class A security. When you
come to them, they're already ready for it because they kind of ask for it
in the way that they attributed their information about their artifacts.

Dinis Cruz - 33:19
Just a quick one on these code owners. This is code owners for security or
code owners in general, like who owns a particular bit of code.

Chen Gour-Arie - 33:26
That's the first step. That would be the first step.

Dinis Cruz - 33:34
I don't agree. I think we should do it. It's almost like we are helping the
engineering process, isn't it? Because one of the things that should happen
in engineering is who actually owns what, who owns what repository. For
example.

Chen Gour-Arie - 33:50
We put our efforts on something that is clearly their interest. We can get a
lot of this very important context that we need. This is why this is a very
good option to start with because clearly serves the needs of R and D. If
your organization haven't already adapted, it helping them adapt
something that is engineering. You can I think we said in the beginning
that good security engineering is just simply good engineering. It's a bit
rude to just come as an outstander and send this to the engineers directly,
but say, what, I need to be able to find people quicker. This code owner
and I see that we're not really using it. Maybe we can invest in a few more
things that you can do when you have code owners, when you have proper
code owners across the organization. And then this is an.

Chen Gour-Arie - 34:47
Investment that everybody can understand. It doesn't bring a lot of
discussion on priority and will be a very good step in your whole shift left
journey.

Dinis Cruz - 34:58
Yeah, cool. Actually, just one more other thing on this one. One of the
things that is interesting is we have some projects and I've done some
really cool stuff and actually opens some assessments around it of using
config files in the repos. This would be a great place to put that, right?
Those owners where imagine each repo had actual mapping for the git
repo right on who owns it, what teams are responsible, what who
maintains it, et cetera. Directly at the code, almost at the code level that
will give you that information, isn't it?

Chen Gour-Arie - 35:33
Yeah, that's the code owners pattern, code owners fire pattern. Like I said,
we've seen teams that adapt it and also start to add security facts into it.
They put of the stride or any threat model result into those files and then
they can consolidate the information from those files. They put other
security facts, they put emergency slack channel information there
relation to business unit or to revenue stream. Information that is truly
critical for security teams that looks at a full picture to catch those
important places and be effective in giving them the right attention.

Dinis Cruz - 36:23
Yeah, absolutely.

Chen Gour-Arie - 36:28
All right, I guess is there any questions in the chat or anything else.

Dinis Cruz - 36:35
That peoplec map right, that you showed, which is awesome, right? I was
looking at it's pretty cool. How do you say is this open source? By the way,
this project, the project.

Chen Gour-Arie - 36:47
Itself is not open source but we will probably release it. We want to
improve code quality before but no, I'm kidding. The project itself is not
open source yet, but the data inside is open so everybody can submit and
everybody who submits after just basic screening just go inside and is
listed.

Dinis Cruz - 37:09
Yeah, because this reminds me on that I think was Tech Radar. How you
know that? From who created it? What I mean by tech radar. From
ThoughtWorks, right? Because it's actually quite cool, right? Because it
allows you to visualize right. A lot of the technologies. I think this is really
cool, but I think if you can open source this because for example, I feel
that for this to be useful, I would need to create a fork of it so I can store
the information of the particular units. In fact, I almost would like to have
one of these just for my security team. Because we now have engineering
capacities, but also to have this created for multiple teams. Because if an
organization of a distant size, this already is going to be very hard to do
this at organization level because every team is different.

Chen Gour-Arie - 38:16
The engine, you mean? Just a second. Just the engine itself that shows
those tired information with the search capabilities. This is what you mean
by outsourcing or the database?

Dinis Cruz - 38:29
Well, when I look at something like this, I think of like a JSON file. There
should be a JSON file that contains all the data, right. Because this is not
super complicated data right. That allows me to create the kind of maps
that you are showing on the other side, right, that kind of visualization.
We start to get a sense of what we're using, what we're not using, what
are the things that we want to do, et cetera. About this is you can even do
threat models on top of this. You can do all sorts of things like the ones
you guys have, right. You want a mode where people can maintain and
create their own and actually almost use this for all sorts of stuff because
this is quite a nice way to visualize it. This is really cool. The key would be
to how can you even customize this or save individual versions, right, so
that I can share with the teams and then we can start to maintain it.

Dinis Cruz - 39:31
I kind of view it as you want it in the case where the raw data should all
be stored, for example, on the GitHub repo. So you can even version
control that.

Chen Gour-Arie - 39:40
Yeah. I'd love to have a follow up session with you to discuss what can we
do with it, how can we align it to this idea, which I really like. In technical
terms, it's a react front end. The back end of the data is pulled from this
submission tool, send it to a Monday form and we aggregate the data and
we just qualify just because sometimes people submit one line per each
category and then we just qualify it and then we publish it to S three. The
stack is very lean and very like you can see very quick. We can definitely
think of a way to think about it. Open Source Sound of Disabilities yeah, I.

Dinis Cruz - 40:29
Think it's cool because it also shows visually where you are. A lot of this is
what I like about it is to show the maturity of the different systems and
where you are within an organization or where we are within a team.
Even the shifting left, once you got this data, you can start to visualize it,
right? How far are you doing it, how far is actually working, et cetera.

Chen Gour-Arie - 40:51
Yeah, definitely. Like if you think about okay, so you would do is do SAS,
that would be your first block. Do it with open source, with mandate open
source and then I get of progress on Abstract testing but then I go and I
want to add so I will switch on this mode security WAF and I'll get
progress in this and also have a generic roadmap that talks about what
should come before. Like code inventory is a step that you take before you
start the testing. Let's talk about what kind of code we have, what kind of
artifacts, technologies we have. So, yeah, we are doing JavaScript, of
course, how could you not? You're progressing on creating this inventory
and altogether is your roadmap into this. I definitely get that people have
different perspective on this and the engine is quite flexible in trying
another thing.

Dinis Cruz - 41:52
Yeah, that's why I think you want to now foster the community, right?
Because only I think that the conversations that you can have from this,
that it only makes sense once it's easy and scalable. Until, for example, I
would be able to run this in an environment that I can create even a
private version of this. It doesn't make sense to me to involve the rest of
the security team or even the developers, because that's the first question
they're going to ask, where is the data going to be stored? How can we
visualize this, et cetera. This can be expanded pretty nicely to even other
domains, right? It'd be really cool to start to have, for example, risk
maturity levels and other maturity levels that you can kind of map in the
same way and then even apply color coding in terms of risks, in terms of
things that you want to do.

Dinis Cruz - 42:40
Because one of the things you touched that I really like is the idea of core
components and also the idea of when we talk about shifting and
accelerating in the world I live in, is that the balance is almost like how do
you strike a balance between the speed that the business wants to operate
and the freedom that part of the business wants to have and the security
controls and the guardrails that you can put around it? So to empower
them. Also, how can you align that with things that you don't want them
to reinvent the will? The more core components you can have, the more
effective those security things that we want to push onto the teams
become. The other thing that would be really cool is to zoom into this,
right? You can actually, even on these areas, almost like, let's say you
double click on it, right, and you could see the zoom in of that particular
area.

Dinis Cruz - 43:39
Now, in terms of this is to add right, what I'm saying, what you actually
see in there, right? Do you mean so basically imagine a world where, okay,
so you got avatar, but how well are you using it and what you're using it
for? Or some of the IAS, let's say, starting about the coverage, right?
Because it would be cool to also color code this based on adoption, right,
based on all sorts of metrics that you can have on this. It's not just the fact
that you have it sometimes it's easy to buy a tool, but it's actually being
used. Right. Do you actually have a tool being effectively adding results,
picking up stuff? Right. It'd be cool to also measure the health of this into
here.

Chen Gour-Arie - 44:21
Yeah, I have another slide, but a branch in the code that actually has this.
When you click this add to map, you're being sent to another form and in
this form it tries to collect your perspective on how effective this solution
is for your problem. Because then if you properly populate it with the
information about the type of code that you have and then in a community
sourcing approach of information and you can say that this sea solution is
the best or is adequate, at least for JavaScript. If a lot of people make this
connection and attribute for it, and imagine.

Dinis Cruz - 45:08
In a world where you then can say, okay, you can create anonymized
version of that, and then that's the data that people could submit to.

Chen Gour-Arie - 45:17
I think you should give me a call and we should have more discussion
about this and some ideas.

Dinis Cruz - 45:24
Yeah, absolutely. Cool, right? I don't think there's any questions here, so I
think we're good, man. No, really cool session, man. We'll talk to someone
and thanks for doing this.

Chen Gour-Arie - 45:35
My pleasure. Thank you for having me.
