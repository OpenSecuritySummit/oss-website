---
title        : Threat Modeling Kata
track        : Threat Modeling
project      : Threat Modeling
type         : working-session
topics       : 
featured     :
event        : mini-summit
when_year    : 2023
when_month   : Apr
when_day     : Wed
when_time    : WS-18-19
hey_summit   : https://us06web.zoom.us/meeting/register/tZUqcuCprj4tH9yRnYyJJvgd6ifx-mOZuGSQ
banner       : https://pbs.twimg.com/media/FtHAzi0WwAE1n6o?format=jpg&name=medium
#status      : 
description  :
organizers   :
    - Luis Servin
 
 
youtube_link : https://youtu.be/a5-YPrWcW4A
zoom_link    : https://us06web.zoom.us/meeting/register/tZUqcuCprj4tH9yRnYyJJvgd6ifx-mOZuGSQ
session_slides:
---

{{< gslides id="2PACX-1vQvzMeuzm1mvMLqYteUcjC5PZ6v6Gya8KMDBY2RZh0H1BqYIP5MjEQ_s6MpbQNvyQ/embed?slide=id.p" >}}

## About this session
Katas are great ways to practice the movements of martial arts. They allow the practitioners to gain muscle knowledge to get more fluid movements. The same principle has been proposed by Neal Ford and others for System architecture. 
In this session we will 
a) Take a kata excercise from https://nealford.com/katas/list.html
b) Create an architecture to satisfy the requirements
c) Threat model this architecture and rate findings.
This will be a working session open to newbies and experienced practitioners, where we will work together  in creating the architecture and the threat model.

## Session Transcript:

Dinis Cruz - 00:02
Hi, welcome to this open security summit session in April 2023. We have
Lewis who is going to talk about a really cool concept and a really
interesting merging of different practices where he's going to take us over
on how to use the CATA concepts around threat modeling.

Luis Servin - 00:19
So, Louis, over to you. Thank you very much, Dennis.

Luis Servin - 00:23
So.

Luis Servin - 00:24
Yes.

Luis Servin - 00:25
My name is Louis Serving. I'm a cybersecurity architect, and since
Monday I may call myself platform security lead at a company in
Hamburg, Germany. In this case I'm talking about things. In my
experience, my employer knows nothing about it, and I'm not saying they
endorse me in any way. This is just flexing our threat modeling muscles
between friends, and I hope everyone in the meeting is willing to
participate. I don't want to make a presentation as such. I want to have a
working dialogue with anyone in the call that feels like participating. Of
course, me, I have been doing threat modeling for nowadays about over
ten years. I have no idea when exactly I started, but it was around 2011,
2012. I've looked at the aerospace systems, automotive systems, It
systems, OT systems, IoT and yeah, I don't tweet that often, but still I have
a Twitter account, I mastered an account.

Luis Servin - 01:40
I'm all in for infotech, information and exchanging information. I will be
referring to my GitHub account. There's a repo there which you can clone
and from there we can.

Luis Servin - 01:58
Just take it away.

Luis Servin - 01:59
Okay, so to get started, what is threat modeling? I like this definition the
most from Brooke Schunfield. Threat modeling is a technique to identify
the attacks a system must resist and the defenses that will bring the system
to its higher defensive state. As you see in the definition, there's nothing
saying it has to be, and it is about understanding the system. We have
understanding situation and understanding its particular threat exposure.
As usual, threat modeling is a four step process. You model the system,
that is, you try to understand scope and understand scope, and then model
the system, which means you basically draw a nice diagram. You analyze
the threats, trying to identify and document vulnerabilities and threat
scenarios that affect these vulnerabilities. Of course, the most important
aspect of all of this is mitigation and validating the outcome. So that's all I
have to say.

Luis Servin - 03:08
Threat modeling, kata, are we going to apply it? Feel free to make any
comments, any questions on the chat. I'll ask Dennis to maybe open the
session in a second for everyone to participate freely.

Dinis Cruz - 03:29
Yeah, I'll keep an eye on the chat and anybody asks questions and I'll
bring people in.

Luis Servin - 03:34
Thank you.

Luis Servin - 03:36
So kata is very nice symbol. Well, there's actually two symbols, but I'd.

Luis Servin - 03:40
Like to one more.

Luis Servin - 03:41
It's a Japanese word which means form. There's like several words that
are pronounced kata, but this candy in particular refers to form and it's
basically, if you have ever done karate or other martial arts, it's a
repetition of movements. It's the choreography, if you want to call it that
way, of movements. You can do the kata by yourself or you can do the
kata in a group. The idea is that you train your body to move in a certain
way. You train your muscle to create what is called muscle memory, so that
the movements feel natural. I was doing karate many years ago, when I
was doing karate many years ago as a child, I remember spending about
half the time of the karate lesson doing qatar. There's a question by
console where does the concept of risk comes in as we perform threat
modeling?

Luis Servin - 04:44
It could be around here. When you analyze the threat, so when you
analyze the threats, you have a vulnerability, you have a actually, I have.

Luis Servin - 04:54
A presentation on that topic.

Luis Servin - 04:56
I was not planning on showing you.

Luis Servin - 04:59
That slide, but I can show it, of course. Give me 1 second, if I can very
quickly open it.

Luis Servin - 05:10
That will make the concept threat modeling kata.

Luis Servin - 05:13
A lot easier to understand. Give me 1 second and I'll have it ready for you.
Okay.

Luis Servin - 05:32
In terms of risk management or risk assessment, threat modeling fits in
this way. We speak of systems which are our assets. Assets have value I can
either assume.

Luis Servin - 05:51
Or use the pen.

Luis Servin - 05:53
I'm very sorry for that. An asset has the value, the more value you have,
the higher the risk. Because of the impact, assets might exhibit
vulnerabilities. The more critical vulnerability, the higher your risk. Or
even the presence of a critical vulnerability might lead to an increased
risk. In an attempt to curtail risk, companies induce policies to try to
reduce the risk exposure, which basically mandate controls, at least the
technical policies. The controls might help protect, detect, respond, or
recover from a given threat scenario. For threat scenarios elicitation
within threat modeling, we can speak of stripe, linden, attack trees,
attachment, pasta, whatever you want to do, but these are usual threat
scenarios. The question for me for creating a credible attack vector is
there has to be a threat agent attached to a threat scenario which is in
contact with a vulnerability for there to be a risk.

Luis Servin - 07:09
Just having a vulnerability with no way to exploit it basically means there
is a very low risk because of the chances of it happening. I hope controller,
I'm not sure how to pronounce your name, sorry. That answers your
question.

Dinis Cruz - 07:32
Actually, can you post that question? Because I think he sent it directly to
you, right?

Luis Servin - 07:37
Yes, directly to me. So sorry for that. Let me copy paste it.

Luis Servin - 07:44
To everyone in the chat.

Luis Servin - 07:46
So that was the question.

Dinis Cruz - 07:50
Console, right?

Luis Servin - 07:51
Yes, console, I'll make you co host.

Dinis Cruz - 07:55
Oh, michael is here. Hey, Michael, I also made you a co host. Feel free to
chip in right. Cassell, you can unmute if you want.

Michael - 08:06
Yeah, thanks reason why I asked that question is I think a lot of times
when you walk within 1st, 2nd, 3rd line the conversation of risk becomes a
problem. We are coming from third line perspective without really
understanding the threats right? Because a lot of times from a first line
perspective, the folks on first line, they implement the controls and all that
stuff. You come to them and tell them there is a risk itself without really
being able to articulate what the threats are, what the trade scenarios are,
becomes a problem to drive that need to remediation. That's kind of the
reason why I was asking that question though.

Luis Servin - 08:45
Definitely. That's one of the reasons I tried to do threat modeling in a bit
different way than Shostek has made famous or Microsoft before. Shostak
has made famous with Stripe. Actually, I'm more of the Church of
schunfield, if you want to think of it that way. Or the philosophy branch of
Schunfield rather than Schustuck, in which he speaks of the concept of the
credible attack vector, which is basically the same thing I just mentioned.
It's just explained in a different way.

Luis Servin - 09:20
Which is.

Luis Servin - 09:21
You have a threat agent with skilled motivation, resources, risk tolerance,
an exploit so an active action, then a path that puts the vulnerability in
contact with the exploit and the threat agent. That leads to a cradle attack
vector, which then you can measure in money impact and probability of
occurrence based on all these three or four elements existing. In the past I
have tried to match this within the automotive company I was working I
could not call it risk management but I did create a likelihood assessment
based on these things and then an impact assessment based on the
technical impact, not the monetary impact. The impact to the mission that
was a cheap way to get out of the political conundrum that makes of who
owns the Isms in the company. I'm not sure if that helps answer your
question console?

Michael - 10:26
No, sure it does. Thanks.

Dinis Cruz - 10:28
On this graph Louis is also a case where for example before or after an
exploit or even the thread agents there's a direct correlation with the risk
right? Because like you said there so the higher the threat agents that you
see, the higher the risk goes. Right, but also once they exploit also the risk
increases, isn't it?

Luis Servin - 10:52
Yeah, I would say so having more threat agents who are in the capacity of
exploiting generating this threat scenario increases your exposure because
the probability increases. If we split the world in three or four categories
we have amateurs that work on by their own then you have a consortium
of amateurs that might help each other and then you have the NSA, right,
or the Mossad or the nation state. If your only attack agent, threat agent
is the Mossad or nation state, it depends on what you're building. Right. If
you're building weapon systems, you have to protect against them. If you
maybe not, but if my 13 year old nephew can hack your system, you're
really in trouble.

Dinis Cruz - 11:48
That's important because it allows you to start focus more on the risks
that are exploitable by the threat agents.

Luis Servin - 11:54
Right.

Dinis Cruz - 11:55
That's the ones that you should be priced. That's the ones I really want to
make sure they're hard to exploit or that you have enough visibility right
into what's going on.

Luis Servin - 12:02
Of course, you cannot take the threat agents away. What you can do is
basically cut this exploitation. If you're able to take away the vulnerability,
it's fantastic. If you're able to get them not to be in contact with the
vulnerability anymore and you can just cut this access, they can still be
there, they can still try to exploit it, they just won't be able to reach it.

Dinis Cruz - 12:31
Exactly.

Luis Servin - 12:34
Not everything in the security controls that you propose is about cutting
access to or impeding the vulnerability from succeeding. Sometimes you
can just cut the weight to the vulnerability and you can buy yourself some
time to patch or do something else about.

Luis Servin - 12:51
Okay.

Luis Servin - 12:54
Right?

Luis Servin - 12:56
Yeah.

Luis Servin - 12:57
Any comments, questions on that? Let's get to the fun part. We just saw
the concept of the Qatar and then the concept of the architectural Qatar.
Now if you want the threat modeling kata, so there's new words, I don't
know when exactly, because I've been hearing about architectural Qatars
for at least like five to seven years, based himself on the work of Dave
Thomas. Dave Thomas was one day at the karate practice of his son and
saw that they were doing a kata and then decided that he should create
this to allow developers to experiment in programming languages, new
small programs that were complete. This concept was taken by Tesnor to
create architectural catas. He created a whole website around it,
architecturalcatas.com. He keeps all the architectural catas in a
repository which can be visited. Give me a second to open it. So this is the
website from Tetnor.

Dinis Cruz - 14:33
He has to give you a repo.

Luis Servin - 14:35
Yeah, this is a repo. Tetnoord, Archkatas, and here are all the catas
defined as Jason. Why are they defined as Jason? Because you can go then
to his.

Luis Servin - 14:47
Website.

Luis Servin - 14:49
Click on the Roulette and basically you get one description of Akata. The
idea is that you can make an after work party like we're doing, have
perhaps one or several groups of colleagues or friends and just give them
a CATA each and then give them an hour to build it up or design it and
then come back and show to everyone else what they did. In that sense, I
was looking for something that was taking my interest and I chose one
about the grading system. So I'll present that in a second. Just wanted to
show the site again, I am referring to my GitHub repo. This we could
gladly host the OSS repo as well or in the organization OSS if you have, if
I can. Basically what I'm trying to do is create here resources for the cat
that I'm doing. This is the second cat that I do and the most important
thing here is the setup.

Luis Servin - 16:08
If you want to follow along, I'll copy this into.

Luis Servin - 16:17
The chat.

Dinis Cruz - 16:19
This is really cool. Nice.

Luis Servin - 16:22
I just lost the chat. Where's the chat? Could anyone type hello, I'm trying
to find the chat. Oh, there's, sorry for that.

Luis Servin - 16:34
So that's the repo. I have to push the latest commits I've done to the repo.
I try to organize it so that we can have a clean slate to start right now.
Basically what I'm saying is I'm giving you instructions on how to do this.
The most important thing is install Vs code, install a graph based plugin
and if you copy paste this Jason, you can just follow along as I do it, but
you don't have to do it, you can just watch and enjoy the show.

Dinis Cruz - 17:16
So that graphics, which one is it?

Luis Servin - 17:20
Jason? Jason is called so this is just for dot files, which is the graphics
format, the shortcut, the user created settings. Give me 1 second to show
you how it looks like.

Luis Servin - 17:37
There it is.

Luis Servin - 17:41
If I go to file so you.

Dinis Cruz - 17:44
Use yes code to create the I.

Luis Servin - 17:47
Use Vs code, but it could be anything. Actually this is an idea I snapped
from Udnus long time ago you.

Luis Servin - 17:53
Talked about.

Luis Servin - 17:56
I'm not sure if everyone was able to follow So file settings or preferences.
Sorry, user snippets configure user snippets and I choose graphics for the
one I have and this opens this file here called dot JSON.

Luis Servin - 18:13
I didn't choose the name, so it's horrible. Let me close this and let me close
that.

Luis Servin - 18:21
Here basically I have templates that allow me to create nice looking
diagrams without spreading it. So it's all there. Just take it while I talk and
present the case. Maybe you can set up your environment.

Dinis Cruz - 18:37
How do you render this on the escape?

Luis Servin - 18:40
I render it with.

Luis Servin - 18:45
A second.

Luis Servin - 18:51
So, I have installed the graphics preview. This one is the one I like to use
from F and Z-H-I installed that one and I installed all the preface methods,
but I always installed them together graphics language support and that
basically allows me to create a diagram from.

Luis Servin - 19:15
The graphics second diagram.

Luis Servin - 19:23
Oh, this is from the threat model link had happened.

Luis Servin - 19:25
Okay, yeah, that's a good point.

Luis Servin - 19:26
Basically I have my graphics dot files created this way and I hit on the
magnifying glass and I get the context diagram and the container
diagram. I'll get into the details right away.

Luis Servin - 19:42
Cool.

Luis Servin - 19:43
This is just to help you set up your environment because we'll be working.

Luis Servin - 19:46
With it.

Luis Servin - 19:51
As a matter of how I like to diagram. I don't like DFDS as Microsoft and
Shastak have promoted these circles and lines with no context. I really
despise them because they are very security specific. Developers cannot
start anything with them and who owns the file, no one feels responsible
for it except for the security person, so no one updates it. Actually
documentation of the architecture is something that should happen as the
architecture is being created. I look for software architects to find a way
on how to best do it. The best I have found so far is the simple model
diagram definition or context, if you want to call it that way. From Simon
Brown. He divides the world in four C's context, container, component and
code. Meaning context is the system and the world around it. Container
deployable units, not docker containers. Component is when you zoom in
and you have different things talking within a deployable unit and then
code.

Luis Servin - 21:05
I have never had to diagram the code myself. There's always a way to
diagram the code if you ever need it.

Luis Servin - 21:10
Right?

Luis Servin - 21:11
The most important thing is everything has to have a label. The diagram,
the elements, the edges.

Luis Servin - 21:18
Be.

Luis Servin - 21:18
Consistent in the colors you use. I'm using gray for out of scope.

Luis Servin - 21:22
And blue for in scope.

Luis Servin - 21:25
Each node in the graph needs to have its purpose and characteristics, the
edge, the lines between the nodes demonstrate the intent and try to keep it
short, not to overburden. Basically the idea is I have the system, its users
and third party dependent system. I zoom into this green square and I
have my container, my deployable unit. Within the deployable unit, there's
usually one thing that really does magic and that's the one that maybe you
want to zoom in further. If you zoom into one of these boxes, you basically
have code. Again, I could basically make a line.

Luis Servin - 22:14
Sorry for that.

Luis Servin - 22:16
I would make a line here on the level I usually go for threat model. If I
ever have to go deeper than that, I ask directly for the code and how
they're implementing that. Usually I do this for input validation and JSON
web token validation when I want to make sure that they're really doing
what they're telling me to do. Okay.

Dinis Cruz - 22:41
I think this is also a great way to sometimes avoid mixing context and
making sure that the elements stay at the right altitude or else sometimes
you have some threat models that mix things in the middle of it.

Luis Servin - 22:54
Right?

Dinis Cruz - 22:55
This allows you to each one leads to the next one, right, which is actually
quite cool.

Luis Servin - 23:00
Well, while I was this automotive company, I had a big number of software
architects or security architects that were doing threat modeling. More
often than not, I had a network diagram that actually tells you nothing
about the application because it stops at layer four. Yeah, so that's a
problem I have with EFTs. They usually stop at layer four. If you want to
make them more detailed, you get such a big diagram, it's very confusing.
Whereas here you can basically pick every one of these containers, tear it
apart, and create a separate diagram for every one of these containers.
For every one of these components, you can still zoom in at different
layers and then you can always separate them very well. I rather have this
kind of diagramming which is created as code, which can live in the kit
repository together with the code, so that now the developers don't need
to go out of their IDE to create, enhance, or update the diagram.

Luis Servin - 24:12
There's no excuse not to do it. The problem with using Figma or Draw I O
with the web version, of course, is that you have to go outside and do it
and you have to use a Gui. Sometimes you don't want to use a Gui.
Sometimes it's just, as a developer, a lot easier to type. Fill in three things,
make a line and that's it. Right.

Dinis Cruz - 24:36
Where do you store these files? Do you put them on the GitHub repos? I
think you mentioned a bit about ownership. Where do you put them?

Luis Servin - 24:43
Usually when I engage with the developers, I try to get access to their
repo. If they have a slash docs, I put it right there. Docs images or slash
docs architectural diagram. And then the thread model. The report is a
matter of where.

Luis Servin - 25:02
You want to put it. Yeah, cool.

Luis Servin - 25:09
Michael is asking about TFT boundaries and where do you enforce the
controls? I ask you to be patient. I will show you that this is just a matter
of diagramming and agreeing on how we're going to do it. All right, so
let's start with our Qatar. The Qatar is called. Make the grade. Basically
we have, I mean, this is very US. Centric, probably, but still fun. A very
large and popular state would like a new system to support standardized
testing across public school systems, grades three through twelve. We have
40,000 plus students, 2000 graders, and 50 administrators. Okay, so far so
good. Perfect requirements.

Luis Servin - 26:03
Yes, sir.

Luis Servin - 26:05
Students will only be able to use the application within testing centers
around the state. The application will only be used within testing centers.
Most of them will be in schools, but not all of them. Students should be
able to take a test and the results eventually consolidated. Sorry, I'm not a
very good underliner. To a single location representing all of the test
scores across the state by school teacher and student. Just by looking at
this, we have perhaps a huge problem with Pai data tests will be multiple
choice, short answer and essay. The system should have reporting the
system should have a reporting system to know which students have taken
the test and what score they received. Now, the question here is, who is
seeing these reports? Who has access to these reports? Every school
director, every school teacher getting a report of which students have
taken it?

Luis Servin - 27:16
Or is the state or I have no idea how the US. Separates states into
counties. I think is the county marshal or the county education person the
one that received this report? So it's not quite clear here. Of course, it's
multiple answer questions, but there's also short answers with sentences
and essay questions that will be graded by teachers, and the teachers will
then ask the essay grades to assist. To be honest, that's a great question,
Miguel. I have no idea whether a student will be able to take a single test.
I assume that they will take a test. As standardized tests are, I suppose
they will take one math test, one English test, and one something test. I
have no idea whether they will all be put together in the same exam or
they have to show up three different days for three different exams.

Luis Servin - 28:25
I have no idea how this works, but let's assume it's one test for the subject
that needs to be assessed. This is something that we can define, right? So
these are the business requirements. We, as the system designers and then
threat modelers, basically decide all questions that are not quite here. The
last thing for context is a change approval process involving three
different government agencies is required for changes to the way student
grades are kept to ensure security. The state does not own its hosting
center, but outsources it to a third party. The project must defend its
budget every fiscal year. Basically, don't get hacked, don't make a scandal,
and you might be able to. And don't mess up records. Don't be in the news.
You would be able to keep your budget, I assume. I'll keep the
requirements at hand, and then I'll probably switch the screen so that I'm
able to see it directly so far.

Luis Servin - 29:34
Any questions, any comments to this?

Luis Servin - 29:41
Cool.

Dinis Cruz - 29:41
Nothing? All right, we lost your screen.

Luis Servin - 29:45
Are you going to show I know. I'm switching screens because I had the
secondary screen with the presentation, but I want to show my DS code on
the main screen, and for that, I.

Luis Servin - 30:00
Need to switch modeling and share my screen. How can how do I increase
the size here?

Luis Servin - 30:34
I hope you could set up your system. I will create a new file for threat
modeling.

Luis Servin - 30:44
Let me create a new directory.

Luis Servin - 30:48
For this session. So I will call this session.

Luis Servin - 30:59
And.

Luis Servin - 30:59
Inside Grace data, I will create the context diagram.

Luis Servin - 31:13
Okay.

Luis Servin - 31:13
So with that, I can start using.

Luis Servin - 31:15
The.

Luis Servin - 31:25
This is part of the JSON file that I told you in.

Luis Servin - 31:28
The beginning.

Luis Servin - 31:31
I need to change the.

Luis Servin - 31:35
How do I change setting preferences?

Luis Servin - 31:38
Sorry I'll change the font to make.

Luis Servin - 31:40
It easier to read setting accelerator font make it really huge.

Luis Servin - 32:01
Is that readable anyone?

Dinis Cruz - 32:06
It's a bit small can you make it bigger?

Luis Servin - 32:08
Still a bit small okay, let me.

Luis Servin - 32:09
Make it bigger of course is it readable? Yes okay, thank you for that.

Luis Servin - 32:30
Okay, so basically I have created a graph. I will call it.

Luis Servin - 32:36
Context Title. This is the system context diagram.

Luis Servin - 32:58
I want to see how I create it.

Luis Servin - 33:01
So far so good.

Luis Servin - 33:05
And I start with the first entity. I will put my system in the center. I will put
it without an image because we don't have any icon for it. So we'll call it
grading.

Luis Servin - 33:28
Oh, come on.

Luis Servin - 33:34
As you see as I type graph is this graph is plugging is updating the
diagram it's a.

Luis Servin - 33:44
Task solution.

Luis Servin - 33:48
Description of purpose so here I would define basically what we had in the
Qatar where I have it sorry.

Luis Servin - 34:04
Mr. Kata.

Luis Servin - 34:08
So here I have.

Luis Servin - 34:12
So we have the test. It allows students to take tests trades.

Luis Servin - 34:27
Under.

Luis Servin - 34:30
Testing platform.

Luis Servin - 34:36
Since this is HTML, I have to do it this way. It's a standardized platform
setting platform.

Luis Servin - 34:55
Serves with students.

Luis Servin - 35:04
Allows teachers to grade.

Luis Servin - 35:10
Long form answers, provide results to I forgot. Provides quick results to
multiple choice.

Luis Servin - 35:45
So that's the first one. So that's my creating system. This is the first
decision that I take. I say this thing is within a.

Luis Servin - 35:54
Cluster.

Luis Servin - 35:58
I will put it in AWS. This is an AWS instance. And AWS is my cloud service
provider. Since I came to this large idea a bit late, I have to move
everything up there so give me 1 second don't discourage if it disappears.
Now, Miguel, you were asking about the context. There you have it. I have
my dotted line things in execution environment and when we think about
it. We were told that students will be taking this in test centers which
happen to be school, but not exclusively. They could be something else.
Now we have another type of diagram. So we have another cluster.

Luis Servin - 36:54
This cluster is cool. This is a system center located in a cool and here I am
going to have students.

Luis Servin - 37:18
The beauty of having this thing is that it has already predefined fields
which you can tap into them and start filling them out.

Luis Servin - 37:27
So this is a student.

Luis Servin - 37:31
The path is images person PNG so there you have it. We have our student,
it's a person.

Luis Servin - 37:43
This is a PC in computer lab.

Luis Servin - 37:53
I have no idea what kind of PCs they will be using but I assume that if
they're using schools it's because they already have an infrastructure with
a PC lab or computing lab with PCs where they will be doing the test. And
what is this person doing?

Luis Servin - 38:13
This is a student sitting to take an exam.

Luis Servin - 38:24
Okay, now we have something very similar in this case, it.

Luis Servin - 38:33
Isn'T out. I will call it in exactly same thing.

Luis Servin - 38:50
I have to move it to a different path.

Luis Servin - 38:52
Sorry for that. Images person.

Luis Servin - 39:00
And the type is.

Luis Servin - 39:06
Unspecified location.

Luis Servin - 39:10
We have no idea where this location would be. And again, this is the
student seeking.

Luis Servin - 39:16
To take.

Luis Servin - 39:20
And again, I'm sorry that.

Luis Servin - 39:22
I was too fast.

Luis Servin - 39:27
Because this should logically be another cluster.

Luis Servin - 39:31
So this is a cluster out, this.

Luis Servin - 39:37
Is another testing center.

Luis Servin - 39:42
Which is not a school. Here I want it to have this year.

Luis Servin - 39:52
Miguel, as you see I have or Michael, sorry, as you see I have now two
students, one grading system. Now I need to connect them together. So
let's say student.

Luis Servin - 40:07
Is interacting with.

Dinis Cruz - 40:11
In C four. There's ways to simplify that code, right? Because you could
convert that into functions, right with the Plant UML, isn't it?

Luis Servin - 40:20
Perhaps you could if you use Plant UML. I don't use plant. UML to be
honest, I always use graphics because it's relatively easy to read. I mean
right now it's too small and too tight and then you cannot read it but plan
your mail creating huge Java thing, it's harder to follow through what's
going on. Yeah, I find at least in my experience of course not everyone
wants to write this by hand, right?

Luis Servin - 40:48
That means the system is called Craving.

Luis Servin - 40:57
Now I have the student talking to that and then I have the.

Luis Servin - 41:01
Other type of student out who was also talking to Craving.

Luis Servin - 41:09
The thing that I was saying is, okay, we need to specify here how are they
connecting, right? Here we say if we have a system that is sending so here
we basically have.

Luis Servin - 41:31
Retrieves questions from right?

Luis Servin - 41:38
This is following the C four methodology again, so here we retrieve
questions from grading system. We read it as a sentence and we also have
the case in.

Luis Servin - 41:52
Which we send responses to the creating system.

Luis Servin - 42:05
This is where the threat modeling comes in. How are we connected? Let's
assume we are connecting with Https. So the connection is kind of secure.
Now the question here is how are we going to identify so how do we
prevent spoofing? So Michael was already thinking about spoofing.
Michael, if you're still there, how could you prevent spoofing?

Speaker 5 - 42:32
Actually, a follow up question to that Louis, is I assume you can break this
down further, right? For instance, in the case of AWS, you might think of
multiple components eventually.

Luis Servin - 42:43
Let'S say you have a microservice container diagram. This is the context
diagram. We don't want to jump right into the technical stuff. We just
want right now to put the system in the context of its users, in the context
it. Lives in the world. Just like in Google Maps, you zoom in, we could
create a container diagram in which we start tearing apart our
architecture in the cloud and putting all the systems that we have and
WAF and whether we want to deploy in Kubernetes or in Lambdas or it's
all open, right?

Speaker 5 - 43:22
Yeah, that makes sense.

Luis Servin - 43:24
That is just a context. Very often I have found some developers are not
aware of the context the system operates because they're working in this
small knob inside the bowels of the beast, and they have no idea how the
context looks like. You ask them who's your client, who's using your
system? Very often they don't have answer, which means they assume
things are happening in some way, but who knows how they're really
happening. That's why I like to start with a helicopter view 10 km above
the earth and then start zooming in towards the details, rather than start
right away with the details, because then you're overwhelmed with
information. What we could start seeing here is okay, which is the first
threat that we see here. My students what is the motivation of the students
to not behave correctly? Can anyone think of any threats coming from the
students?

Luis Servin - 44:39
One thing that I was thinking about is the students, right. So let's say
threats now, those coming.

Luis Servin - 44:51
From the students.

Luis Servin - 44:54
I think you were saying it at the beginning, Michael poofing. What does
poofing mean in the context of this person sitting here?

Speaker 5 - 45:09
Yeah, like an A student attempting to make an exam on behalf of
somebody else. Let's say my brother, right. He studied, he wanted to do
the exam instead of me.

Luis Servin - 45:20
Right, exactly.

Luis Servin - 45:22
I had thought of the same one. So take an extended one else. Anything else
you can think of?

Dinis Cruz - 45:31
Can you have extra coms, like a mobile phone or a watch or something
that gives them data?

Luis Servin - 45:40
Come again? Could you repeat that?

Luis Servin - 45:41
I couldn't understand it.

Dinis Cruz - 45:43
Yeah, I think about actually categories. The students, when they take the
exams, have a mobile phone or a watch that gives them the answers.

Luis Servin - 45:49
Right.

Luis Servin - 45:50
Okay. This is the one I called like telling the questions.

Dinis Cruz - 45:56
Yeah.

Speaker 5 - 45:58
Asking charge UPT or something like that.

Dinis Cruz - 46:00
Yeah. Can you charge you PT. The thing getting to take the exam is one.

Luis Servin - 46:09
So this one actually has.

Luis Servin - 46:16
Taking pictures of questions.

Luis Servin - 46:17
Then you also have memorizing questions. It's incredible what young
minds are capable of in memorization capabilities. What else could you
think of taking pictures of questions? And here we have two things, either.

Luis Servin - 46:37
For.

Luis Servin - 46:40
Selling and the other one would.

Luis Servin - 46:42
Be taking pictures.

Luis Servin - 46:46
Of questions for cheating, which means someone or something is giving
you the right answer to their question.

Dinis Cruz - 46:55
Don't you need also to capture the receiving of the data? Right, because
that's a bit different. Right, so that's almost like having a feedback loop,
isn't it?

Luis Servin - 47:05
Yeah. This is a lot more exposure.

Luis Servin - 47:08
Right.

Luis Servin - 47:08
This is a lot easier to be cut. Whereas this one here is more tedious. Right.
Hide it. Or they take pictures all the time. They have it in the glasses, but
they're not actually communicating with anyone. They can still go and
dump the whole exam for everyone to see.

Luis Servin - 47:26
Right.

Luis Servin - 47:28
Memorizing the questions. What else do we have? Spoofing or reputation,
maybe. I don't know.

Speaker 5 - 47:35
If a student taking an exam in different locations?

Luis Servin - 47:42
Yes, why not? So I'm selling the questions.

Luis Servin - 47:49
Pending different locations for the exam.

Luis Servin - 47:56
Reputation.

Luis Servin - 48:03
Wasn'T there.

Dinis Cruz - 48:08
It wasn't them, right? Yeah.

Luis Servin - 48:10
Those are not my answers. Right.

Speaker 5 - 48:17
There was a failure during taking the exam or something like that.

Luis Servin - 48:22
Yeah, well, I mean, I wasn't there, right? I don't know. And then the other
one is Reputation. I am pretty sure I answered something else. Now they
change it. So there's a mistake in the matrix.

Luis Servin - 48:38
Right?

Luis Servin - 48:40
Yeah. So those are not my answers. Would be a reputation attack to the
system. If they don't like the grade.

Luis Servin - 48:49
How.

Dinis Cruz - 48:50
Do you connect this to the individual elements? Are you going to yeah, we
could.

Luis Servin - 48:55
Add them all of them.

Luis Servin - 48:56
Right.

Luis Servin - 48:56
The idea is not to get it to burden. What I try to achieve with these
diagrams is to inherit them to the developing team. Because very often
developing teams don't have good diagrams.

Dinis Cruz - 49:12
Well, if you think about it, the ideal situation, this was created actually by
code, right?

Luis Servin - 49:19
Yes. You could use the structure actually.

Dinis Cruz - 49:24
Programmatically. Yep.

Luis Servin - 49:32
So that could help. So now we have the teacher. Right? I know we're
running almost on the hour, so I'll do the teacher quite fast.

Luis Servin - 49:50
Teacher, teacher.

Luis Servin - 50:01
Teacher, grader. So they didn't really call them teachers. They called them
graders. But I have no idea.

Luis Servin - 50:07
So grade long form answers, and then.

Luis Servin - 50:16
The teacher is in a very different context. Actually we have no idea where
this person is living.

Luis Servin - 50:21
Right.

Luis Servin - 50:21
We have the teacher, perhaps in his or her home. We have no idea where
this person is located. Could be an employee of the grading system, could
be someone else.

Luis Servin - 50:34
Teacher is talking to the grading system. Label locks into.

Luis Servin - 50:50
Locks into the grading system.

Luis Servin - 50:56
Grade answers.

Luis Servin - 51:05
What else is this person doing? I think that's all we have from the, from
the use case. We have systems should have a short answer and say
questions will be manually graded by teachers, who will then add the essay
grades to the system.

Luis Servin - 51:26
Okay.

Luis Servin - 51:27
They report the grades now locked into grades answers, and the system
consolidates grades. Okay, so we don't have to do that. Now, if we think of
the teachers, what could be the incentives of teachers to cheat? So we
have here an interesting sentence. Results eventually consolidated to
allocation representing test scores across the state by school, teacher and
student. I was thinking, what would be the intrinsic motivation for a
teacher to misbehave. Now, if I'm going to be compared to other teachers,
there could be an economic incentive. If my class has a better average
grade if my school is going to be compared to other schools in the district
and my school gets a better grade in average, the school might get more
money for the next semester, the next year, whatever period. There's a
perverse incentive here for the if the teachers are the graders, which is an
assumption I'm making because I don't know where else they would get
2000 people to create long term answers.

Luis Servin - 52:50
There's a perverse incentive to cheat on the system.

Dinis Cruz - 53:00
If you go follow that then you also probably want to put almost the head
teacher in the school right? Because they might also be involved.

Luis Servin - 53:09
Right, sure.

Luis Servin - 53:12
The problem here is I have no idea what the head teacher is doing. Right,
not necessarily mentioned. We do know that they have a reporting
capability which I suppose so they have a reporting system which I
suppose this person would be consuming. Actually when I was doing this
by hand during the day, thinking about it, I was thinking about a lot of
other people which are not mentioned but unfortunately we didn't have
the time. We can continue this next time or we can take a different cat
next time. Teachers, I just want to put this in writing and commit it to the
code, to the kids, report that everyone can read it. Teachers have the
incentive to break own students.

Dinis Cruz - 54:04
Yeah, correct.

Luis Servin - 54:07
Necessary. I would say they could also grade other students worse than
necessary.

Dinis Cruz - 54:22
Now could they share the questions?

Luis Servin - 54:25
The answers? They have the questions.

Dinis Cruz - 54:27
They could also sell yeah, sell the answers.

Luis Servin - 54:30
Right.

Luis Servin - 54:31
Or not even sell them but in the same way to prepare the students. Sell
misuse the questions to prepare students.

Luis Servin - 54:43
Right.

Luis Servin - 54:52
What else could the teacher do? Create their own students better.

Dinis Cruz - 54:59
Well are they monitoring the exam? They could facilitate some of the
actions of the students.

Luis Servin - 55:12
Yes.

Dinis Cruz - 55:16
Can you take it to the next level and spoof a teacher?

Luis Servin - 55:20
Yeah, of course. Right. They could facilitate a cheating of course in a
second to put that.

Luis Servin - 55:27
On the right hand side.

Luis Servin - 55:31
They could facilitate cheating during what is called proctoring. It
proctoring the word for this kind of exam? During the exam, right, during
the exam. Specific cheating during the exam.

Luis Servin - 55:48
Spoofing get teacher access to the system.

Dinis Cruz - 56:00
Can you spoof a teacher? The student pretends to be a teacher and then
do that?

Luis Servin - 56:07
I will try it.

Luis Servin - 56:08
Right.

Luis Servin - 56:08
I mean it depends how desperate you are. I think this is a matter of
creativity.

Dinis Cruz - 56:15
Yeah, it depends on the threat agent, right?

Luis Servin - 56:18
Yeah. Here the teacher could be losing or having his password on a post it
in the class exit or the student guesses the teacher's password based on the
car model or the reset question or whatever not students are very creative.
Since this is at the school network, students could prepare the school
network to floss the network. We could even have here does the network
level at school, of course, center B, which is not a school. We have the
other variant, which is.

Dinis Cruz - 57:07
Would you put that as a separate dos? Because you're kind of following
the stride here, right? So that could be of dos, right. Is on section, isn't it?

Luis Servin - 57:17
Sure. Oh yeah, you're right. This is here I would say network level at
school. Of course you could also have.

Luis Servin - 57:33
App.

Luis Servin - 57:34
Level for the grading system. They could actually try to plot the grading
system, not just the network here, but overflow these ones. One is
attacking the physical link, the other one is attacking the end of the
system. Teachers, grade students, other students. Some issues facilitate
cheating during the exam. We of course have the Admin. Within the
grading system we have an Admin. And here I was.

Luis Servin - 58:15
Admin it's admin.

Luis Servin - 58:46
Now the question here is this Admin? The admin, right? We have
information regarding the admin, almost nothing. We know there are 50
administrators, which I think it's too many for a system. I have no idea,
they're nowhere in the description. We can only guess what that means.
Which is for me, basically admin the grading system, which for me would
be maybe not a grading system Admin, but this could be the school
director or head teacher of the school. School director. This is the person
with Admin capability for the grading system, for their school. And this
person let me zoom in.

Luis Servin - 01:00:04
Because it's not visible.

Luis Servin - 01:00:08
This is the person with Admin access to the school. So this person can.

Luis Servin - 01:00:24
Teachers.

Luis Servin - 01:00:38
Reports yeah.

Dinis Cruz - 01:00:39
Manage the grades per class.

Luis Servin - 01:00:45
Cool.

Luis Servin - 01:00:48
Manages the grades. I'm not sure, but yes, sure, that would be getting the
reports. Right. So the system is going to well.

Dinis Cruz - 01:00:54
Also editing the reports. Editing the data, right. Can the admin edit the
data?

Luis Servin - 01:01:02
I think that is a different kind of admin.

Luis Servin - 01:01:05
Right.

Luis Servin - 01:01:05
This is the tenant admin, if you want. You have the real admin of the
system, the one that sets up the system and keeps it alive.

Luis Servin - 01:01:14
Right.

Luis Servin - 01:01:14
So this is the tenant admin. You could think of it like as a SaaS solution.
Every school that is on board is a tenant, should be kept separate. You
have Admin, let's call it SRE, people managing it with access to the real
data.

Dinis Cruz - 01:01:36
Compromise. They could change the grades, right?

Luis Servin - 01:01:39
Yes.

Luis Servin - 01:01:39
Those are the ones that can change the grades, the teachers. We have the
incentives for the directoradmin. Here the incentive would be to get better
grades. Could they have access to the answers? I don't know, but I mean,
they could probably try to. That leads to a very interesting question.
Everyone is talking about the grades, right? Everyone has to do with
questions. Who's putting the questions in, who's creating the question?

Dinis Cruz - 01:02:24
Yeah.

Luis Servin - 01:02:25
That question is not answered at all. Sometimes it takes me a lot longer to
do the non technical diagram than to do the technical diagram, because
there are so many unanswered questions that immediately show you
abuse.

Dinis Cruz - 01:02:41
Well, and it goes back to the idea that sometimes when we do these things,
the hard part is creating architectural diagrams, right. Getting designs of
actually how things actually work. Once you have that, it's easier to find
the vulnerabilities.

Luis Servin - 01:02:53
Yes, exactly.

Luis Servin - 01:02:56
We're already ten minutes. About time. I think we might have to close it
and then we can decide whether in the next month yeah, let's do another
one.

Dinis Cruz - 01:03:05
This is really cool, man. I think this is a great way, too. If you share the
links, then especially with the recording, because the thing sometimes we
don't do is let's add more data to the session itself, because once we share
the video, the summit session, it's quite a nice one, because the video I
need, Adam, is actually here. He adds to it, but, for example, adding the
links, adding some more examples. So, yeah, let's do that. And let's do
another session in Germany.

Luis Servin - 01:03:28
That's cool. Yes.

Luis Servin - 01:03:30
So, without further ado, we come to an abrupt end, but to extend it too
much, maybe next time we can book an hour and a half.

Dinis Cruz - 01:03:41
Yeah, absolutely. Brilliant, man. Good stuff.

Luis Servin - 01:03:44
Limit anyone in the room that wants to comment or add a question to
what has been said.

Luis Servin - 01:03:52
Sure.

Dinis Cruz - 01:03:52
I think Michael had to leave.

Michael - 01:03:54
Just a question. Do we get a copy of the.

Luis Servin - 01:04:00
Material that was presented in GitHub? I haven't yet pushed, because I'm
creating it live, but everything here, the code you see on the left side, the
image and the findings will be on GitHub.

Dinis Cruz - 01:04:14
Yeah. On that link you shared. Right.

Luis Servin - 01:04:18
This one here.

Luis Servin - 01:04:18
Right.

Dinis Cruz - 01:04:19
I just put it again. Right.

Luis Servin - 01:04:45
OSS threat modeling.

Dinis Cruz - 01:04:47
Yeah. I just put the link on the chat.

Luis Servin - 01:04:50
I have to commit, so don't be amazed if it's not yet there. Sorry for that,
but I still have to push. In the end it will be here, I promise.

Dinis Cruz - 01:05:01
Yeah, cool. Great price to collaborate.

Luis Servin - 01:05:03
Thanks.

Luis Servin - 01:05:05
So, yeah, feel free to comment. Feel free to send me. We can link on
LinkedIn or on Twitter or master them if you're in. Master them and we
can kick off the conversation or maybe see you next.

Luis Servin - 01:05:19
Time around in the morning.

Dinis Cruz - 01:05:22
Good stuff.

Luis Servin - 01:05:25
Thank you, Danny.
