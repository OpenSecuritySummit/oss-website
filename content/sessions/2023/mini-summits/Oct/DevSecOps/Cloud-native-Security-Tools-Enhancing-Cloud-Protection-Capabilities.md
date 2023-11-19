---
title        : "Cloud-Native Security Tools: Enhancing Cloud Protection Capabilities(Panel)"
track        : DevSecOps
project      : DevSecOps
type         : working-session
topics       : Cloud-native Security, Cloud Protection
featured     :
event        : mini-summit
when_year    : 2023
when_month   : Oct
when_day     : Wed
when_time    : WS-15-16
hey_summit   : https://www.linkedin.com/events/7110652455767408640
session_slack:
#status      : draft
description  :
banner       : https://github.com/OpenSecuritySummit/oss-website/blob/main/content/sessions/2023/mini-summits/Oct/banners/cloud-native%20(1).jpg?raw=true
organizers   :
     - Dinis Cruz
     - Gabriel L. Manor 
     - Or Weis
     - Oded Ben David
     
youtube_link : https://youtu.be/z4QSyrtZCLQ
zoom_link    : https://us06web.zoom.us/meeting/register/tZcqd-igqDosHtIvoZ-7yXyjq1FEzqJyFC8f
---

## About this session

This topic focuses on the latest advancements in cloud-native security tools. It explores innovative tools and technologies designed specifically for securing cloud environments, including container security, serverless security, and cloud workload protection platforms.

### Outline:
- Introduction to cloud-native security tools and their benefits
- Container security and runtime protection in containerized environments
- Securing serverless architectures and functions-as-a-service (FaaS)
- Cloud workload protection platforms (CWPP) for cloud security management
- Case studies showcasing the effectiveness of cloud-native security tools

## Transcript:
Speaker 1 - 00:03
All right, so good afternoon everyone. We have here our friends from
Permit IO and led by their co founder Always, and then other technical
lead, Odete Ben, David and Gabriel Elmanor, their Director of Debril. So,
over to you everyone. We're going to have a panel discussion for cloud
native security tools. Enhancing Cloud Protection capabilities. Over to you
guys.

Speaker 2 - 00:39
Thank you. So it's really a pleasure to be here at the Open Security
Summit. We've been here in the past and was always a and as were
introduced, I'm happy to have with me some of my great teammates, Odet
and Gabriel. And our topic for today for this panel is cloud Native
Security Tools and how you enhance your cloud protection capabilities. I
think this is quite a huge topic to cover, so we probably won't cover all of
it in one go, but I think we can start touching on some key points here and
I think I'll kick us off and then we'll roll with the conversation. Also,
people in the audience, if you want to ask a question, please utilize the
chat capabilities here and we'd love to kind of take those into the
conversation as well.

Speaker 2 - 01:36
So, first and foremost, I think when we talk about cloud native security, I
think we need to talk about cloud native applications and understand
where we're standing there. So we've come a long way from monolith
applications running on your laptop or running on a server within a server
farm. Now, software is distributed. It's built of tiny components that are
all interconnected in some way, and all of them are performing critical
actions against a constantly growing distributed data plane. So we have
more information as part of our applications, more information as part of
our organizations, and more information as part of interconnections
between companies, customers, partners as well. And another thing that is
becoming more commonplace but is still rather new, is these software
components becoming intelligent.

Speaker 2 - 02:32
So AI agents, specifically large language models, are more often being
embedded into software and that's also changing dramatically how we
view those microservices. So in the past if we had a small microservice
that was running on Lambda, we knew that it's a very simple component.
Now you can't even know that anymore. It can have a lot of sophistication
and it can affect a lot of the area around that. So I think that's kind of
where we're at and where this discussion is kind of going to focus and I
want to take it with you folks. You, Gabriel. And you did. Where do you
think the main problems are today when we're trying to protect our cloud
native applications? Maybe, Gabriel, maybe you can.

Speaker 3 - 03:21
So you gave a nice brief introduction, usually when speaking about cloud
native security. So there are the four C's code, which is the application
code container, which is the tiny piece of the application that's running
cluster, which is where we built the architecture and cloud which is the
runtime that running our applications or architectures. I think that cloud
is not in you filled in security because the cloud is here for time. Also
containerized applications or applications are running independently is
not that new. I think where we see the most new trends in cloud native
security is code, where most of the software development organizations
today are looking in a trend called shift left or DevSecOps where we are
securing the application from the first line of code that we are writing.

Speaker 3 - 04:26
So we want to make sure that we are proactively secure our application
from the small piece of it like a code and cluster, which is mean for
specific architectures that taking containerized applications and running
them together in a cloud agnostic environment. So for example, the most
common example is Kubernetes, that you can take Kubernetes and run it
on every cloud provider. So you potentially agnostic to the cloud provider
you want and we need to find the new pillar to secure these kind of
architectures. So again, in my opinion the most fascinating thing to think
about new tools and new trends is code and clusters. But of course also
how we secure the cloud itself. The cloud does the runtime and
containerized or like artifacts of applications.

Speaker 2 - 05:29
Yeah, I think you can basically look at it as different perimeters of defense
that you have. This also I think works well as analogy to the real world.
So you have like a wall around your forts and you have your guard towers
and then you move closer and closer into the core of your compound. And
the more you move in, the more sensitive things are and the less protection
you have in place. I see Denise joining us. Hey Denise, were already
kicking this off without you.

Speaker 4 - 06:02
No, absolutely. Sorry I was a bit late. So I was just finishing the
conference.

Speaker 2 - 06:08
So I'll keep rolling with that thought and then feel free to kind of join in
and navigate the conversation. So as I was saying, you have different
levels of defense and the deeper you go, the more you move from the cloud
environment, you move into the code. Obviously the attacker landing there
has more ability to affect things and more ability to be more sophisticated.
And that's also to something you could be counterintuitive because you're
thinking oh, if I have someone locked in a container then I can limit what
they do. But because applications are becoming more and more
interconnected and they're becoming more sophisticated, they can actually
do more damage in the application level.

Speaker 2 - 06:56
So yeah, maybe their code is limited to running within that container, but
their effect on talking to other APIs and leveraging the secrets that are
available to that code and leapfrogging from there is not actually as
limited as you want it to be. So in the past with non cloud native
applications, I think running something containerized or on a separate VM
that provided a lot of protection. And nowadays, as we move things more
and more to the application layer, there's more sensitivity in the code area
itself. And that's something that I think not a lot of people have been
thinking about. Odette, do you have something to add here?

Speaker 5 - 07:36
Yes, I actually want to join to the last point and said that.

Speaker 4 - 07:47
When.

Speaker 5 - 07:47
We have a lot of applications that part of your application that talking
with each others, it's usually you don't think about securing your own
application from itself, you're thinking about how to protect it, as you
said, to build a wall. But now we are talking a lot more about zero trust.
Even inside the application, there are parts that shouldn't get authorized
to all the parts of the application. Quick example could be your fronted
microservice shouldn't get to your database. He should get access through
your back end or even a dedicated microservice in your back end that only
it allows full access to your database. So these, for example, show us that
the new cloud architectures take us to a new way of thinking about
authorization.

Speaker 4 - 09:03
Yeah, look, I could agree with that, guys. In fact, you remind me of this
little cartoon here, right? Can you sure. To see my screen? Can you see
this? Right? It's from XST, but it's a bit like, hey look, I got a user account
on the laptop. I can access Dropbox, Photos, Facebook, Gmail, PayPal,
bank, but at least you can't install drivers without permission, right? So I
think the key of all this is context, right? And I do agree that sometimes we
go and says, oh, now I'm in the container. It's good. Actually, no, because
a bit of code or a vulnerability in a container that has high privileged
access to assets can be way more dangerous than full access to a back end
system that has no data, no assets, no major criticality, right?

Speaker 4 - 09:53
I think that the key challenge is understand the context and making good
security decisions. And a lot of the times what we end up doing across
multiple generations of this is we throw the baby with the bathwater, so
we go, oh, we don't really understand this, let's go to the cloud. And then
you kind of ditch all those great sysadmins that you had and then you
realize that when you get to the cloud, you do still need those
understanding, right? And then you go, oh, let's now containerize this and
you did this stuff, now let's go everything over there. And then there's a set
of skills that are critical, like understanding role permissions,
understanding assets, understanding who accessing is, what and that stuff,
right?

Speaker 4 - 10:31
And that has been almost one of those elephants in our industry, especially
on security, that we almost used to say we don't understand it. Right?
There's applications that are there that there's nobody who actually
understands how that thing actually works. Especially when you look,
authentication authorization, right? Especially on role based stuff. There's
so much complexity sometimes that some systems have that it's crazy,
right. And in a way, the access is not just on an app, is the app is running.
It's almost like the Cascading privileges occur across the board on those
environments.

Speaker 2 - 11:04
Yeah, and I think that really highlights the point that in the end of the day,
there is no silver bullet. Like people looking for a silver bullet that say, oh,
I'll just take a container or I'll just take another, apply it and I'll be done
and good. That's not going to happen probably ever. But what you can do,
and that's the closest thing you can get to a silver bullet, is design security
into your product, into its core at day one, and continuously build that.
And I think components that are part of the application itself, primarily
authentication and authorization, those can bake in a lot of that security
aspect in an inherent fashion into your software. And you can be much
more clear and build zero trust connections.

Speaker 2 - 11:54
So you know, for each microservice, specifically, what is it allowed to do
and how you manage the policy for it, how it connects to your database,
how it connects to other services, how it connects to external services. And
you can enforce that across the chain constantly from the code that's
yeah.

Speaker 4 - 12:15
But I want to challenge you on this one, right? Because I think there's lots
of bodies on that road, right, and there's a lot of really good teams and
really good technologies on that road. And for a while we had these secure
by design, secure by default, and secure deployment, which actually good.
Actually, Google is recycling the Microsoft stuff on it. Right, but the
problem is complexity, right? The problem is there's a moment where I'm
the first one to say the better design, the better your architecture, the
more visibility you have. But I have to say, up until recently, I couldn't see
how what you described eventually works in practice. And I know there's
examples that you can do it and there's sometimes you can game the
system because some apps allow that to happen a bit more easily than
others.

Speaker 4 - 12:57
But I think the piece of the puzzle, or one of the piece of the puzzle that I
think we now have the ability to do is Gen AI brings us the possibility to
start to understand context across multiple layers. And that's a game
changer, right? Because what it allows us to do is the feedback loops that
allows good decisions to occur in the environment that you just described.
Because even if you design something really well, there's moments where
complexity and change hit the real world. And again, business
requirements change, et cetera. And without a real good understanding
and without the ability to connect the dots between the people who are
making decisions, people who understand it, to the information that is
happening to what's really being deployed and what's really going on.
Those systems eventually start to move away from that state.

Speaker 4 - 13:51
And I feel for the first time, look, Bruce Wayne, three months ago, four
months ago, you would say that, and I go, Cool, that's still a great graph.
And I think you guys build variations of this, right? And yeah, you can get
that with graphs, you can get that with connections, but without the
ability to start to applying context and start to have a dialogue and to
translate that to all sorts of different audiences so that you can make good
decisions, right? That for me, was the piece of the puzzle because now you
can go, not yet, but we quite close.

Speaker 4 - 14:21
You can start to go to understanding code, understanding cloud
formation, understanding changes, understanding the impact, understand
the behavior, and have almost a chain of bots that together start to tell
you, by the way, you're just connecting the dots now just to wrap up. What
I think is that this is going to reward good architecture, this is going to
reward good systems, because you're going to get to the point where the
analysis is, I don't freaking understand what the hell is going on here,
right. And it's too complex. We can't freaking understand it to, oh, no, this
is what's happening. This is the changes, this is the risks you're doing. This
is the situation where we are now. Right? And of course, that model
rewards good engineering. That model rewards security by default and I
think provides a feedback loop that was missing, right.

Speaker 4 - 15:07
So that teams can make great business cases because you can now see the
impacts when you don't use those good architectures. Does that make
sense how I'm trying to connect the loops here?

Speaker 2 - 15:19
I definitely agree on the architecture part and the loop that produces.
Like. If you understand your software and you approach it the right way
with the right fundamentals, you are much better positioned to face
attacks when they come and face new threats and challenges and
vulnerabilities as they surface up, because you understand what's going on
and you have the components in place to address it in a gradual and smart
way. I'm not so sure about the first point that you made with AI, like in
generative AI. Yes. You can now generate more code or.

Speaker 4 - 15:59
Have no, that's not what I'm saying. I want to use Gen AI to understand
the code. I want to use Gen AI to understand the roles, the mappings. So
imagine a world where you say a prompt that says you are a role based
assistant, right, or you're going to analyze Kubernetes docker containers,
right? Let's say, for example, right? Here's the policies. Here's how they
should work. Here's what good look like. Here's what I expect to see.
Here's a TCP dump. Here's an output of a mesh network. Here's in the
output of what's going on here's analysis of that tool. Now start asking
these questions. Right? That is what I think will allow us to do. Because
you allow us to understand the context of what's happening. Even more
interestingly sorry.

Speaker 5 - 16:47
The problem with it is when you're using Gen AI to generate tests or an
image, and you have four fingers in that image, it is okay. Or you have few.

Speaker 4 - 17:02
But just to clarify this, I'm not saying that the Genai creates the image.
What I'm saying Genai validates the image creation and helps to create
the pull request. That's a bit different, right? It's like I'm saying, here's my
standard for what my image should look like, right? Here's the stuff of the
image. Analyze those two and give me analysis. It's very different. And
from the analysis, you can create pull requests. So there's always a human
in a loop. What I'm making is I'm making the human ten x 100 x more
efficient to understand what's happening.

Speaker 2 - 17:37
I think if you're creating, if you need an AI to explain your system to
you're already in a dangerous position. First of all, the AI can be helpful
and I'm not against using it, but I don't think it's the right way to go about
it. Like if you've created something that is chaotic or messy and it's hard
to understand. I think that's the problem in the first place.

Speaker 4 - 18:02
You have that today. Like you guys run on AWS, right? Sorry? You run on
AWS. For example, what cloud do you run for? AWS? Are you telling me
that your IAM policies are absolutely matched to a T? To the permissions
that you guys use in your application?

Speaker 2 - 18:22
Most of the permissions that we enforce aren't in the IAM policies. A lot of
them are in the application level. And we do some doc fooding and we use
our own policy engine.

Speaker 4 - 18:31
But have you list get a list, man. Of every single permission and every
single thing that it's allowed. It's really hard to do because it's so complex.

Speaker 2 - 18:42
You have recursive aspects.

Speaker 4 - 18:44
I know, but it's not impossible. It's just complex. Right. The problem is, if
you take Im.

Speaker 2 - 18:50
Rules, the problem is impossible. Like there's the halting problem. If you
have something, a system that is complex enough and you have enough
connections, then it might take forever to.

Speaker 4 - 19:01
Iterate on again, take Im rules. Right. It's not a very complex problem.
Right. You have a bunch of permissions to a bunch of assets to a bunch of
resources. Right. The problem is that the way it's designed, it promotes
overprivileging, right. Even if you try to underprivileged and the reasons
why, it's very hard to take. Here's my role. I want to understand exactly
what was the intent of that role, and I want to analyze the usage of that
policy. And that's what I'm seeing now. That starts to be possible. It was
closely impossible.

Speaker 2 - 19:33
I think what you're suggesting might be doable, but I think it's a lesser
option to building it right in the first place. And if you know how you
assign them, and if you know that you have tests that you run that check
for them every time you change your policy, every time you change your
code, then you have a much easier time making sure that you're meeting
your own.

Speaker 4 - 20:02
I agree, but look, maybe you guys pull it off, but I have to say that most im
policies that I've seen, when you go to the details, in fact, I will even take
it to another level, right. Your im policies, okay, you have one or do you
have ten or 15 policies in your application?

Speaker 2 - 20:20
In the application or when you run.

Speaker 4 - 20:22
When you AWS environment, do you have one or do you have 15 dynamic?
Do you give one policy or you have several?

Speaker 2 - 20:30
We have several, and I'd say no.

Speaker 4 - 20:32
But for the same application, for the same container, for the same sort of
execution environment, for example.

Speaker 2 - 20:38
So, first of all, it depends if we're talking about the infrastructure level
there, we try to minimize the amount of policy enforcement, or we're
talking about the application level where you have more complexity. And
there I also talk about customers that we have. There you have policies
and rules in the thousands and even tens of thousands.

Speaker 4 - 20:59
Yeah. Okay, well, the infrastructure ones, if you think about it again, I'm
just playing with devil's advocate here, but your application, when he runs,
doesn't need all the privileges that he's been given to, right?

Speaker 2 - 21:14
Right.

Speaker 4 - 21:14
So if you look at the intersection of every single privilege that you have in
an Im policy, just for this example, right? So in principle, you should have
lots of policies, right? In fact, your policy should almost change depending
on the application is doing. But the complexity level of doing that today is
too great because we don't fully understand all those permutations.

Speaker 2 - 21:34
I think one of the main points that I'm trying to surface here is that if
you're trying to do it through the cloud IAM, you're going to have a bad
time because it's not meant for that. It's meant for how you connect the
building blocks that you have, how you connect a database to your elastic
computing, how you connect your lambdas to your buckets. That's the
level of sophistication that the IAM policies in AWS were meant to solve.
They're not solving for application level roles. They're not solving for
quotas and behaviors.

Speaker 4 - 22:09
But here's the thing, right? If you don't have a solution that addresses that
too, right. Where you went to have let me phrase what you're saying is
that at that level, you don't have enough context, right. The application to
give you context, because the application is where the action is, right? So
by design, you are over provisioning the infrastructure because you don't
have enough context, because by design, you need to have as much
privileges as the maximum of what you need once you provide application
layer on top.

Speaker 2 - 22:37
Right? So you need to at each level. So first of all, you can improve that
by breaking into small more microservices, but there's a point where it
loses efficiency or efficacy. But yeah, you are right. In the end of the day,
there will be things that you won't be able to enforce with the right
granularity outside of the application layer. Only in the application layer,
you'll have the full context. And then that's why I start with saying with
cloud native applications, to actually be secure, you have to go into the
code, you have to understand it, and you have to absolutely in the first
place to enable the level of security that you need. And building your
authentication and authorization correctly into your application code as
time progresses is becoming the most critical front that you have to
protecting.

Speaker 4 - 23:34
I agree. And actually I'm doubling down on that because I'm saying that
my application decisions or my application aware or even user context
aware decisions that I'm making need to trickle all the way down. Right?
And if they trickle all the way down across those layers, you get a huge
amount of defense in death. Because it means that even a blind spot over
here on code doesn't cause a huge amount of problem. Because the
problem is if you don't take the application specific knowledge that you're
just describing from the zero trust who you are, where you come from,
what you want to do, all that knowledge that you can have and you trickle
down to all the roles and policies across your stack, you end up over
provisioning. So you almost end up with a pyramid right of permissions.
Right?

Speaker 4 - 24:22
Where the reality is it should be like that. In fact, it should be like this.
Right? But my point is that Gen AI can help us to solve that problem
because the reason why you don't want to go to IAM policies is because
it's a fucking shit show, right? Because you hardly understand what's
going on in there. Right? And then we limit it to some of the big primitives
just because of the level of complexity. But it's still massively
overprivileged, right? So if you look at access to S three buckets, you go, I
give S three bucket access to this part. But actually the user only needs
access to that little bit over there. Right? Why does he have access to the
whole bucket? Why does he have access to all of Kubernetes? Right?

Speaker 4 - 25:01
I think the stuff you guys do is great because I think we need to push that
down. But also we need to start explaining the intent of the rules and we
need to explaining reality in a language that makes sense to the multiple
operators all the way to the business owners. In fact, all the way I agree.

Speaker 2 - 25:21
With that, but I think we shouldn't trust or expect AI to do it for us. I think
as engineers and as security practitioners, we should put in the effort to
design those understandings into what we're building in the first.

Speaker 4 - 25:39
No, no, but again, I'm not saying that you let AI build the whole thing.
This is like Jarvis, right? It's like a copilot. It's like the ability to have
augmented reality understanding.

Speaker 5 - 25:50
This reminds me a lot about the talks between developers about clean
code, against documenting the code. Yeah, you can take a really complex
code and document it really good or ask AI to document it for you. And
then you probably understand 90% of what this code is doing. This is one
way to work. It works. AI know how to explain code. It may mistake a bit
for 10%. Those 10% may be really critical. But mostly it will do know
what this code going to do, the other way to do it and I think that we at
permit pushing to this way is like clean code. Let's do with no
documentation a little bit. When the code explains itself, when the
permissions and the policy explain itself, you don't get into the IAM shit
show and you need Jarvis to explain it to you.

Speaker 5 - 26:59
You can write it in a way that it will be so understandable. You don't want
the AI, you just read it and you understand it.

Speaker 4 - 27:07
For example.

Speaker 5 - 27:11
You said you have a lot of machines. You need to get access only to one
machine. So if you are using ArbAC, it is very difficult because you need to
have a lot of rules for each and every machines and it's very complex. But
if you are using REBAC or ABAC, you can have a new attribute. This is my
machine. You have access only to it because you created it, because the
admin gave you permission to this machine. And then it's really simple.
You don't need AI, you don't need Jarvis. You just read your permissions.
You know what you.

Speaker 4 - 27:57
So interesting thing. And look, this is the same thing with Agile, right? No
documentation, right? So let me ask the question here. If you had clean
code and I gave you really good documentation, really good architecture
diagrams, I will give you visual representations of what that code is doing,
right? In fact, I will give you a visual representation of what that code is
doing plus the code that he calls and he calls it. Would you want it?

Speaker 5 - 28:22
It can be nice.

Speaker 4 - 28:24
No, that's a simple question. Would you like it or you would not like it?
Would you add value or not add value to have that?

Speaker 2 - 28:29
It depends on what your current situation is. If you already have those
things, you don't need more of them.

Speaker 4 - 28:35
Not saying you don't, I'm saying you have clean code, you have a really
nice architecture code that is you can argue that is easy to understand,
right?

Speaker 2 - 28:43
Yeah.

Speaker 5 - 28:43
For the big picture, a diagram is.

Speaker 4 - 28:45
Always nice, but even about that function, right? Like that function, about
that function as.

Speaker 5 - 28:50
A developer, I want to see for myself if it's a function, a small piece and it's
clean and I would love to see for myself this is me.

Speaker 4 - 29:02
That function doesn't work in isolation, right? That function is called by
other functions, is integrated as a flow here, right.

Speaker 5 - 29:08
So for the big picture, give me what you have for the small picture, as a
security person, I want to see for myself.

Speaker 4 - 29:17
Sure. My point here is that the reason why you're rationalizing that you
don't need or you don't want the documentation, the architecture diagram
right, is because at the moment it's really hard to do, it's really hard to
maintain, it's really hard to keep in sync, it's really hard to version control.
It actually takes away from a lot of the work you do. Right, but I'll give
you an example from a security point of view. When we do code reviews,
right? So you guys ship code, right? Let's say you release ten times a day,
five times a day, whatever number that every five minutes, right? Amazing,
right? Pretty cool, right. By the way, it's not practical to have a security
person review every line of code that you ship, right? It's not practical.
Right. Unless you have one to one developers. Right, not practical. Right.

Speaker 5 - 30:11
The developer is the security person.

Speaker 4 - 30:14
Exactly. Developers, security person, right, basically. So how do you know
which ones to look at?

Speaker 2 - 30:21
So I think here, maybe I don't want to make this into a permit pitch, but I
think it'd be worthwhile to give a little bit more color about what we do.
So with permit, we're providing you a couple of things. First of all, we're
providing policy as code. So you don't work with arbitrary code that you
write, you work with dedicated policy engines with languages that are
meant like Regal for OPA and Cedar for WS Cedar. So you manage your
policies in code in ways that are also easy to manage and easy to test and
benchmark. So first of all, you don't have to have a security person go
about checking all that code because you can have tests that check that
code when it changes and you can have tests that check the application
against that code when the application changes.

Speaker 2 - 31:13
And then we take it another step up and we provide low code, no code
interfaces. So when you write policy as code with us, you don't need to
write it as code directly. You use simplified interfaces. Think about a table
with checkboxes for permissions, think about connecting points to
describe relationships. So these are really simple interfaces that I like to
say a monkey can use, or even a product manager, if they're smart
enough. Ironically, by the way, product managers are the ones that like the
joke the most. In the end of the day, when you. Look at the interfaces
themselves. They're so simple that everyone around the team can use them
and they become part of the documentation. So you have the code itself
that's maintained in Git and that's your single source of truth.

Speaker 2 - 31:58
But simplified interfaces on top that make the conversation easier, make
the investigating, exploring easier. And we think that in the end of the day,
there are two points here. A, you have to go into the code if you want to
have any protection and B, you need to work with the right tools and the
right abstractions. So it'd be simple for everyone around the table to work
with this. And I'm not saying that AI can't come into the mix. It definitely
can. But I wouldn't go so fast to rely on it completely.

Speaker 4 - 32:31
But I never said that you jumped to an extreme. Right. I'm not saying that
we're going to let AI write the code, write the policies.

Speaker 2 - 32:38
You sure you're not saying that? Because that's a great debate.

Speaker 4 - 32:41
No. Well, I think that's wrong. Right. And that's never going to work
because we don't allow that anywhere. We don't allow a super genius
engineer to have uncontrolled access to production just because he can. In
fact, we now know that backfires because although the person can do
certain things, in a way I'm a massive fan of clean code, right? In fact, I'm
a massive fan of code that you can argue is redundant, but is easy to read,
easy to understand, easy to process. So I would always prefer to have code
that might be more verbose, but is actually simpler to maintain, simpler to
do than code. That is freaking crazy optimized. Like, if you ever do some
stuff in Scala, you can write shit in Scala that is like, what the hell is going
on here? Right? Even the guys or perl.

Speaker 4 - 33:26
Okay, but I think the readability understanding of code is very important.
Look, what I really like about what you guys are in permit IO is that
you're raising the like you basically bring a whole level of abstractions.
And in fact, what you're doing is really cool is that you are starting to
allow the role base to be maintained by the people who understand the
intent of the application. Right? So you allow the business owner to start
to own almost the role base. And the stuff that's happening in there, which
I think is really powerful. My key points here is that but even that is still a
big layer of abstraction, right? There's still a layer of analysis that you
need to put on top of it. You make it easier.

Speaker 4 - 34:09
So the reality is that any system that uses equivalent of technology that
you guys are building is always going to be easier to analyze, easier to
process, easier to do, versus a system that authorization is sprinkled
throughout the whole thing and is a massive mess to understand.

Speaker 2 - 34:24
Yeah.

Speaker 5 - 34:25
Usually what I like about it that usually when you make things more
secure, it's harder to maintain because security adds guidelines and walls
that prevent you doing things that are not secure enough. And in permit
we are trying to do it simpler and more secure in.

Speaker 4 - 34:51
The same and I think this is value, right? And that's something you guys
need to run with. That's how I position security as a CISO. I said the
things that we want to do in security is to allow the business to go faster,
right? Is to allow the business to be more optimized. So it's almost like
security becomes an enabler. So you don't have this complexity, right? You
basically now have these building blocks which I think going back to the
point here, cloud native security tools that has a big advantage, right? In
that model.

Speaker 3 - 35:23
I want to get to a point you said I don't want a junior developer get
uncontrolled access to production. I think one of the point that cloud
native and light is what does that mean uncontrolled access to
production? Because non developers should have direct access to our
cloud environment, it's irrelevant for them in cloud native. They should
have access to deploy code maybe, but they should never get access to S
three bucket, right? This bucket is supposed to have changed access from
the application level permission, right? So if we are keeping the pillar
separately to each other, every function can make sure that they are
securing what.

Speaker 4 - 36:12
They need to now. Okay, but here's a question. Can that developer write
code that then access the S three bucket directly?

Speaker 3 - 36:18
They can.

Speaker 4 - 36:20
They can. Of course they can. But how do you prevent that from
happening?

Speaker 3 - 36:26
Because in cloud native environments, usually all the deployment part, all
the chain that taking this code from repository to the cloud environment is
something that's controlled not by developer.

Speaker 4 - 36:40
Okay? But when the code arrives there, if I'm the developer, can I write
code that gets nicely deployed and when C heads gives the final container
access the S three bucket directly?

Speaker 3 - 36:52
Yeah, exactly. So that's the point of separation of concern in this pillar of
security, right? So developer is writing code, the code specifically that
getting access or accessing S three bucket is secure, right? It's secure if
it's fit with the application level security, which again in a good word is
something that's controlled by responsible for that.

Speaker 4 - 37:17
So that code is going to run in a lambda function or it's going to run in a
container.

Speaker 3 - 37:22
Just a second now. So we are securing the pillar of the code. We know that
the code that are trying to get access to an S three bucket is code that is
safe. We check that with let's say static analysis, security, maybe even with
some infrastructure as code analysis, right? So for example, tools like
Kicks and Checkoff can tell us hey, here is an infrastructure that not looks
good and then you as a CISO do not need to have code review on all the
code. You can have a code review where is sensitive as a CISO. So in that
example, the infrastructure, right? So we're securing the first filler the
code, then we are going to the container itself, the container as a
container, again, does not have access to the S three bucket.

Speaker 3 - 38:12
The configuration of this container as an access of S three bucket. And
again, this is something that you know where you are securing this level of
separation of concern. When you are getting to the cloud environment,
you only need to take a look on the previous section of configuration and
in a cloud native way where everything is declarative. You always have an
insight who has an access in the point that is relevant to you as a CISO.
Right? And if you need to do some code review for the developer, you
know, potentially hypothetically, right, with the cloud native helpful of
everything being declarative, everything declared as code, you know
where to open the incident.

Speaker 4 - 39:01
But if you go back to the when I joined you guys were talking about the
fact that one of the things you need to protect is the fact that the
container itself might have access to a lot of resources.

Speaker 3 - 39:09
Exactly. And this is exactly the trend in cloud native. So for example, I
want to take a look on the trend, the eBPF, have you heard on eBPF?

Speaker 4 - 39:19
No.

Speaker 3 - 39:20
So eBPF is a tool that is very trending in cloud native.

Speaker 2 - 39:23
Now you probably heard of Isolvent and some other companies that are
using that for service mesh and other level of cloud native introspection
into software.

Speaker 4 - 39:38
How do you spell it? EBPs.

Speaker 2 - 39:40
Ebpf.

Speaker 4 - 39:42
Okay.

Speaker 2 - 39:43
Extended Berkeley packet filters, I think I heard that.

Speaker 3 - 39:52
So if you think about traditional application they were mixing or
complexing the way you as a CISO can get an access on permissions on
things that happened. The cloud native way is helping you to separate
what you need to inspect, what you need to analyze, what you need to the
incident you need to open for the very relevant concern that you have now.
Right. So you don't have to worry anymore on all your runtime security or
on the kernel that you are running on. You can make sure that everything
is secure there. You don't have to worry about because the version is
secure and then you have to worry on the piece of code that have this most
sensitive part of what you need to do. Right?

Speaker 3 - 40:42
And in my opinion, this is the way that CISOs should start look at the
cloud native way with new eyes, with eyes that helping developers use
cloud native to help them. If security engineers will continue to look on
software as one manolite piece with one backlog of endless findings or
endless incidents or endless areas to inspect, they will lose the benefits of
cloud native software.

Speaker 4 - 41:15
Yeah, but by the way, just a very important point. Everything you're
describing there, if it's the security team that is driving that, it's already a
losing battle, right? Like everything you talk about there from going that
cloud native journey is a journey that the dev teams have to do. We have to
support them from a security point of view. But it's not the security team
that is going to do that because it's the dev teams that need to do that.
And this is why sometimes I'll argue with some of my peers, I say, if you
don't have a good CI pipeline, for example, if your engineer team is not
doing that, then don't fund tools. Fund that. Help them. If you have a
budget, help them to build proper pipelines. Help them to go proper cloud
native, because that's the hard part.

Speaker 4 - 42:02
Securing it becomes it's almost like these are tools for developers, right?
These are tools for them. We making their lives easier. Right.

Speaker 2 - 42:12
And I think a next step there maybe to also kind of simplify the things that
Gabriel said. So the idea is that as a security, as a team, as a CISO, you
want to enable and empower your developers. You want to encourage
them to work with security and don't want to slow them down. And you
then you enable security to plug in via the right tools and by applying
decoupling. So, for example, if a developer is now setting enforcement into
their code, into their app, so they'll use policy as code and they'll have
enforcement points in their code that will check if, for example, that
application can talk to that s three bucket. For example, the example used
before, can that application in this context, behalf of this user, is it allowed
to go to that s three bucket?

Speaker 2 - 43:04
And initially, you let the developers set the policies themselves. So what the
developer is responsible for is setting the enforcement and connecting it to
the correct tools and mechanisms. Once those are in place, the security
team can come in with their own interfaces and say, oh, this is the policy
we've been using so far. It's not good enough. I want to add more rules,
more limitations, more capabilities on top you're missing without asking
the developer to change everything.

Speaker 4 - 43:32
Yeah, but the thing about this is you actually are so close. This is why I'm
going to nudge the geni. You're so close because the real decision has to
be done by the product people, by the business people, right. Because
that's the key. And what you have is now this is what I'm saying, that the
power of the gen AI is that allows you to translate all these layers based
on reality to the wide audiences. Because the thing you described in a
weird way, it's not what the developer wants or cares. It's not what the
technical manager is doing is what the business owner who owns the
project, who owns the risk, who owns the development, right? In a way,
they're the person who controls the pipeline, they control the roadmap.

Speaker 4 - 44:17
They are the ones that in fact, I'm trying to intersect my world now. So,
for example, you need to bring now the risk analysis and say, hey, if in this
development environment you have this policy and you do this, you do this,
you have these risks and you're going to have to accept these risks. And
it's when we can give the business risks to the business owners that things
change. And in a weird way, you guys have made such a great stride there
because you're now starting to describe roles and permissions as business
functions, right? Which is really freaking cool, right.

Speaker 4 - 44:51
And I bet that some of your customers are actually on the tech teams, are
actually the business teams, because they're the ones who get lots of
benefit from it, which is the big challenge I always give to security tools
because I say the only people buying your tool are the security guys, then
you're already missing a chunk of the market. But the thing now is to
connect that with the risk, right? Because if you really want to and this is
where going back to the cloud native right. The risk profiles of running
stuff in cloud native environments with good designs, with good
architectures, with good mappings is very different from the risk profile of
running on an EC two instance that needs to be maintained or something
in your data center or a lambda function or XYZ over there. Right.

Speaker 4 - 45:33
That connection is really interesting because we finally have the ability to
make the business owners and here's the interesting thing, the ability to
make the clients aware of it. See, what I don't like as a buyer is I don't
have access to that data from the tools that, let's say my stakeholders,
right, which is the whole freaking business, right? I buy it and I want to
start pushing those standards down. So in a way, I want to reward the
market that does a good job versus the market that doesn't do a good job.

Speaker 4 - 46:06
If we're doing an evaluation of a day of the business of three companies, I
would love if the company that does good role based security has a really
good grip on their permissions and roles, we should be able to reward that
company with a sell versus a company who's not doing anything. But from
a marketing, it looks great. It might even be ISO compliant and have every
freaking compliance in the book, but it's not actually doing it properly. So
if you guys can go that extra mile up and then start connect with the
owners, the problem you have is the message is different almost every time
because the message is now context specific. And that's the bit that in the
past didn't scale.

Speaker 2 - 46:49
Go ahead, Gabriel.

Speaker 3 - 46:50
I think that at the end, although as developers we want to develop for fun
and develop software for software at the end we need to do business,
right? Of course we develop software for business and the more we can
closer to deliver business value faster, we're getting better software, right?
And I think that's one of the main points that drives the cloud native
trends. We can deliver software much faster. We can deliver it because we
separate the concern of infrastructure and code. We can deliver it because
we declare everything and deploying it in second and all that. We just
make all the functions closer. That's our main goal.

Speaker 4 - 47:35
Do you still see clients that question that?

Speaker 2 - 47:41
We see a lot of people that don't necessarily understand that fully. Most
people are still and most companies are still struggling just to do the.

Speaker 4 - 47:50
Basics, most bigger problems, right? Then it's like they're not even ready
to talk about role based security because they can't even connect the dots,
right?

Speaker 2 - 48:03
When they come to us, they're ready to talk about role based because
that's often why they come to us.

Speaker 4 - 48:10
And by then surely they are on a path to understanding cloud native,
right? Because one maturity surely leads the other.

Speaker 2 - 48:17
So I think there are different roles around the space here. So I think we
need to specialize, we need developers to focus on building good software
and meeting the standards that are required by them. We need the security
people to set the policies, set the workflow and connect it to the business.
We need to enable the business folks to communicate what they actually
need. And we need to enable companies as a whole to be able to adopt
these concepts without having to learn too much. And that means that we
also need to simplify things. Maybe AI can help them simplify things, but I
think better is tools that have simplification baked into them.

Speaker 2 - 48:59
If the self working with the tool can understand, then he can use the AI,
but he won't be dependent on it and he'll be able to do more things than
just that little thing that the AI is doing for him.

Speaker 4 - 49:13
Man, here's the thing, you know that word you said is one of the most
important words, simplify. In fact, you should put down a homepage of
your website because there's a great vision that a friend of mine has and
he says in security, our job is to simplify the business. And I completely
agree with him. When we do security, right, we make the business simple,
we make it efficient and I think that's a great property. And yes, going to
cloud native simplifies things right at the end of the day because it
removes complexity. Although that said, you could have no idea what
you're doing, you're going to make it more complex but then you have
different problems, right? But I think that word simplify is very important,
right? Because I think that's where you add real business value.

Speaker 4 - 49:53
The interesting question is measure that, but I think you guys should run
with that.

Speaker 5 - 49:58
It made me think or do you want to finish this point?

Speaker 2 - 50:02
No, you can take it. We have just a couple of minutes left and some people
sent me.

Speaker 4 - 50:08
Yeah, there's a question from Kieran. Kieran, I made you a co host if you
want to ask that question, because that's quite a cool question.

Speaker 6 - 50:15
Yeah, it was around the bit with regards to when you were saying around
ensuring that from a developer point of view that you're baking in, that
you build it, you own it kind of concept, that agile methodology. So it's
kind of almost agreeing what Dennis was saying around it, to say, how do
you enforce that? How do you enable that to make sure that cultural shift
actually happens and the developers do own it.

Speaker 2 - 50:52
Yeah. So I think in the end of the day, it's separation of responsibilities and
it's about enabling one another. And you want your developers to be able
to focus on being good developers. And if you have the ability to plug in
the security capabilities either baked into their work or it's things that you
can connect later in a decoupled way, then that shift motion happens more
easily. If you go to your developers and tell them, oh, you need to manage
everything, you need to bake all of the security, then some of them would
take you off on that and do it, but for most of them, it will be a lot of
friction. It's really hard to telescope and cover both areas at the same
time.

Speaker 2 - 51:38
Like a developer, in the end of the day, needs to be able to zoom into their
code, really get into the zone and build it right. And it's hard for them to
think about all the macro things that happen, but if you tell them, oh, this
is how you connect to the macro picture when you're doing, for example,
with what we do when you're building permissions, don't put the policy
into the code, don't have anything regarding that. There just set points
where you're describing what's happening and connect that to another
service that will bring in the policy. Suddenly the developer has the ability
to cognitively contain this. They say, oh, I know, I want to build this suffix
secure, so I'll make sure I'll set all the enforcement points correctly and fill
them with all the context that they need.

Speaker 2 - 52:25
But they don't need to start extending their mind and thinking about the
macro picture of what all the different policies may be that will be applied
to this application later. That's something that will be impossible. So by
simplifying it for both sides, like making it focused enough for the
developers, making it approachable enough for the CISO suite and for the
other and the business owners, we can have everyone chime in together
and build this without slowing down each other. But it really starts by
understanding the focus point for each one on the team and how we
connect these things in the right way with the best practices.

Speaker 4 - 53:05
I think you're going to say something.

Speaker 5 - 53:09
No, I can say that we are almost done.

Speaker 4 - 53:13
I'll give you a couple of minutes more if you guys could. The only thing I
would say, Kieran, and just to ora's point, I think it's very important to
understand who's making what decision because I sometimes think in
these conversations we talk about the developer as an abstraction concept
and the developers have very little power in most places, right? The
developers are executing on a roadmap. So you need to understand who is
providing the technical leadership. Because for example, even or when
you're saying if you go to developer and you say that they go of course I
would love to be able to manage my permissions in this way. But he needs
to be given that brief. It's a non functional requirement.

Speaker 4 - 53:50
A lot of the times that needs to be in a roadmap for that to be in a
roadmap that needs to be mapped to the business person. Now, sometimes
whoever controls the roadmap has enough power to push you through.
But I think in this case we need to find who is the person that's making
those decisions. A who's making the technical decision and who's making
the business decision because those are the ones that will drive it. The
person making the technical decision is the one need to say the way we do
permissions is ridiculous. We need something that scales.

Speaker 4 - 54:15
Here's a model, here's a pattern, go evaluate it, figure out the best one to
do it and by the way, I'm giving you time to do that and the person making
the business decision need to go yes, I support that because without that
the developer won't have the time, right? And that's why sometimes it
happens, right? My point is that I want to start to influence those
developers to have the time by being able to reward the companies who
are doing it right. Because a lot of the times that business person is
connected to somebody who says do the clients care? Do the clients
understand? Are we losing sales, are we losing market share? Are we
delivering what we need for our stakeholders? So you need to influence
that, right? So that the developer are giving the time to basically then
implement those solutions.

Speaker 2 - 55:02
I definitely agree. I think you can create a virtuous cycle from that. Once
developers are empowered, they'll empower back the security and vice
versa. And that's why we actually started when we started was talking
about the different levels, the different zones of protection that you have
and why you need to care about the code, especially in cloud native. And if
you do that means that you care about your developers and empowering
them.

Speaker 4 - 55:27
So I want to give you one more idea before we finish. One of the things
that we start to talk about, and there's a great podcast I heard recently
where Gary McGraw was saying that one of the biggest challenges that
we have is we need to scale threat modeling. And I couldn't agree more.
And I think you guys and this world that we talk about can play a big part
of it because at the moment when we do threat models, people go, let me
design the system. Right. See, that's the problem. It's all nice having no
diagrams in your clinic code, but if I want to do a thread modeling system,
I need to understand how it works. Right? I think you guys are sitting on
something because you start to have an understanding of how the app
works, how they behave.

Speaker 4 - 56:08
So I think you can be a key piece of the puzzle in the ability to scale threat
modeling. And threat modeling is one of those practices that we won the
battle. Nobody will argue that threat modeling is not healthy. Threat
modeling should not be done. The problem is how to do it at scale, how to
do it in a way that scales is consistent, that we leverage, that we don't
require everybody in the team to be a security expert. Right. That doesn't
scale. And role based security, by the way, is where threat model tends to
fail, because by then, we can't really understand a lot of the things. Right?
So a clean role based environment is what allows you to then start
understanding the threats of the system and ask really good questions and
understand the side effects and then put countermeasures.

Speaker 4 - 56:53
So I think threat modeling is definitely an area that going back just to the
cloud native, right? Like the thread model of a cloud native application
looks very different than the thread model of a non cloud native
application. Right. So the threads are different, the things are different, et
cetera. So, yeah, just dropping the idea to you guys because I think you're
going to see a lot of innovation in that world in the next six months to a
year.

Speaker 2 - 57:16
Yeah, for sure. It's actually, some of this is our features that we're already
working on. So it's part of our audit log system. So one of the cool things
about our product is we generate audit logs automatically.

Speaker 4 - 57:26
Yeah, it's like in gold, right.

Speaker 2 - 57:28
And we also have the ability to in anonymized way to understand the
behavior of each of the users through those audit logs so you can generate
behavioral analytics and anomaly detection and other capabilities. These
are already things that we're looking to bring.

Speaker 4 - 57:44
You know, who's going to pay for that? The business guys, for sure.

Speaker 2 - 57:49
And who's going to enjoy it? The developer guys.

Speaker 4 - 57:53
But here's the sweet spot, right? So one of the things I say a lot these days
is that the security team is one of the few teams sometimes that can make
this happen because we sometimes the only ones intersection. The sweet
spot for security is to find these added values. So you can drive decisions
and you can get people on the table that otherwise maybe wouldn't be on
the same table. Because it's almost like one of those a lot of the players
would like it, but they don't feel the pain or they don't see how it could be
done, where, from a security point of view, we can see the path. Right.

Speaker 4 - 58:20
The key is to have those benefits, to say, look, if I do this and I get the
security that I need, because that's my mandate, the developers get a
much better life. The business analysts get a better way. And we're able to
give these business insights to these dudes over there, which, by the way,
are usually the ones that have a lot of budget because they tend to be very
connected to the outside world. I e the places where the business generates
that's. And again, that's where I think Genai will collect a lot of those dots
that in the past were very hard to scale again at an organization.

Speaker 3 - 58:51
Cool.

Speaker 4 - 58:52
All right, guys, any final thoughts on comments on this session?

Speaker 2 - 58:58
Not for me. I really enjoyed the conversation. I think we delved into some
really interesting points and things that are relevant now and become also
even more relevant down the road. And I thank you for inviting me.

Speaker 4 - 59:12
Cool. All right, guys. One ask for you guys is like we now have done a
couple of these. One of my frustration is that the Open Security Summit
has such an amazing set of content for some of these things. And for
example, some of the sessions you guys done also are like a master class,
for example, of how to think about this. We need to find a way to package
that up. I need to find a way that sometimes I can go to an engineer or a
business analyst or somebody from my team or somebody from other part
of the business and say, look, just go there and read that and see that. The
question is, how do we package it up? Right. In a nice roadmap. So let's
see how we can collaborate on that.

Speaker 2 - 59:53
For sure.

Speaker 4 - 59:54
Because I think the space you guys in is very important. Right. It's the key
way to scale security. Yeah.

Speaker 3 - 01:00:00
By the way, Dennis, we just released two blog posts that is result from our
last conversation.

Speaker 4 - 01:00:06
Oh, cool.

Speaker 3 - 01:00:08
Yeah, I'll send you the link.

Speaker 4 - 01:00:09
Yeah, tag me on LinkedIn, man. My inbox, just for the record, is a shit
show.

Speaker 3 - 01:00:19
You manage your policy.

Speaker 4 - 01:00:21
Exactly. I need a bot for that. Brilliant, guys. Good stuff.

Speaker 2 - 01:00:25
Absolutely.

Speaker 4 - 01:00:26
I'll see you in the next one.

Speaker 2 - 01:00:28
Thank you.
