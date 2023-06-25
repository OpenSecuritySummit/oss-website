---
title        : Threat Modeling Kata Part 2
track        : Threat Modeling
project      : Threat Modeling
type         : working-session
topics       : 
featured     :
event        : mini-summit
when_year    : 2023
when_month   : Jun
when_day     : Mon
when_time    : WS-17-18
hey_summit   : https://us06web.zoom.us/meeting/register/tZErdOGtqj8iEtHB21i_tRD1pMsafhX7D_ZT
banner       : https://media.licdn.com/dms/image/D4D22AQGEJJE2qO-9Yg/feedshare-shrink_2048_1536/0/1686167577835?e=1689206400&v=beta&t=7OlSaFokcEZwOGUGzLBT8In0iYs165QG2xjmHY3s8Lg
#status      : 
description  :
organizers   :
    - Luis Servin
    
youtube_link : https://youtu.be/NG4_UIziVD4
zoom_link    : https://us06web.zoom.us/meeting/register/tZErdOGtqj8iEtHB21i_tRD1pMsafhX7D_ZT
session_slides:
---
    
## Summary of the session:
Louis, a security architect and platform security lead, gives an in-depth analysis of threat
modeling and introduces the concept of kata for software architectural catas. He explains
the four-step model for threat modeling and suggests using a structured approach from
system architecture instead of relying on threat modeling tools. Louis then discusses a
SaaS solution that supports grading systems in one state of the United States as their
target for evaluation and identifes potential threats from students and teachers.
The transcript discusses the potential risks of cheating in an exam system and suggests
ways to prevent it. They discuss adding an admin to connect with the grading system and
creating architecture diagrams to understand where vulnerabilities may lie. The group also
talks about different components involved in the testing process, such as a Node JS API for
displaying questions and a teacher UI for submitting them. They mention that short answer
and essay questions will be manually graded by teachers before being added to the
system's reporting feature.
The speaker discusses creating documentation with dev teams and the value it adds to
security teams. They also discuss the Python Fast API, node JS UI, and student
authentication for a test-taking system. They emphasize the importance of not giving
admin rights to everything and improving readability in code by aligning arrows and
grouping related items together. The diagram serves as a basis for threat modeling.
Two individuals discuss the potential of creating graphs programmatically to scale their
work. They prefer the simplicity of graphics and want to create relationships between text
and code bases that are created programmatically. The need for change is acknowledged,
but people often resist it due to time constraints. The speakers plan on making connections
between UI and API less wide while acknowledging there is room for innovation in this area.

### Outline:
I'm sorry, but based on the transcript provided, I cannot create an outline with chapters and
timestamps. The transcript appears to be a conversation between two individuals
discussing a security summit and a grading system. It lacks clear breaks or chapter
headings, making it difcult to discern when one topic ends and another begins.
Additionally, there are no timestamps provided in the transcript.
Notes:
The speaker discusses how to reach a desired defensive state by analyzing vulnerabilities
and threat scenarios, and validating the outcome.
The speaker introduces the term 'Kata' and explains its practice to create muscle memory.
The speaker provides instructions on how to use a JSON fle to follow an example.
The speaker advises to label data fows and elements to prepare for analysis.
The speaker discusses the target of analysis, which is the grading system.
The speaker identifes potential threats to the system, such as spoofng and cheating.
The speaker introduces the idea of a 'bad student' and how they might attempt to cheat the
system.
The speaker discusses the teacher's role in the grading system and identifes potential
actions they might take.
The speaker discusses the different interfaces available to users, including the test UI,
teacher UI, test API, and teacher API.
The speaker identifes the need for a way to onboard students into the system.
The speaker identifes the different data stored in the system, such as questions, answers,
grades, and statistics.
The speaker emphasizes the importance of creating readable diagrams and suggests
aligning arrows and grouping elements.
The speaker describes the benefts of diagramming as code.

### Action items:
Add the admin function that connects to the grading system in diagrams.
Work with developers or system architects to create container diagram and threat modeling
on fy as they start creating the system.
###Follow-ups:
How to onboard students for authentication?
How does the user authenticate?
Should the test UI be inside the DMZ?
What is node JS actually doing that an NGINX can't do?
Can they even be in the same segment?

### Action items:
Add UID for authentication
Enhance context diagram with how this person gets authentication code
Label sends grades and queries questions from Teacher API to grading system
Refactor HTML code for better diff on actual code
Align arrows and labels for improved readability in context diagram.
### Follow-ups:
1. Investigate and fnd a system that can create those text programmatically from reality
2. Predify the diagram by making invisible connections between UI and API
Action Items:
1. Work on creating relationships programmatically added to version control
2. Predify the diagram for better visualization

## Transcript:
00:00
It.
00:02
Hi, welcome to this open security summit session in June 2023, and we
have another great exploration on security caters and the second session
on this topic that we have here. And Luis is going to walk us through a
more in depth analysis of this great technique and this great practice,
which is actually brings a lot of science to this process. So, Louis, over to
you.
00:30
Thank you very much. So.
00:34
We're going to continue the threat modeling Kata we did last time. So me,
I am a security architect, platform security lead in my current role. I have
been doing threat modeling of many different things since the early 2010s.
Airplane systems, It systems, OT systems, automotive systems, some IoT
got in the way.
00:57
These are my social media.
01:01
And let's get started. So I know there are plenty of definitions of threat
modeling. My favorite one is the one from Brooke Schunfield. Threat
modeling is a technique to identify the attacks the system must resist and
the defenses that will bring the system.

01:16
To a desired defensive state, which informs.
01:21
Us why we're doing threat modeling.
01:22
Right.
01:23
We want our system to resist the level of attack for which we design it, and
that is based on the criticality of the system and the value.
01:32
Of the data that we're processing.
01:35
Now threat modeling. Regardless of which methodology you take, I think
the whole world has settled down into one, into this four step model,
which is understand the system model it.
01:46
Analyze what could go wrong, identify and.

01:50
Document vulnerabilities and threat scenarios, do mitigation analysis or
risk treatment, if you prefer to call it that way, and then validate the
outcome. Make sure that you analyze the right resources and didn't start
too late or didn't do too much or too little. Kata is a word that comes from
the Japanese. There are two different kanji symbols for that. I don't really
know enough to tell the difference between either, but I chose this one,
and it means form.
02:27
So if you know the word kata.
02:30
From martial arts, it means basically choreographing your movements to
make them be fluid and make them flow on unitan. And it is practiced to
memorize or to create muscle memory.
02:47
In that sense.
02:48
Many years ago, Dave Thomas was visiting his son during karate practice,
saw what a CATA was, and he said, hey, we know we should be doing this
for coding. Dev NEWART took it further and said, okay, let's do software,
architectural catas, and there's a repository with catas in GitHub, and
there's a website where you can look at them.
03:16
And basically I'm extending that idea, taking.

03:19
It further and saying, okay, let's take one of these architectural catas, let's
figure out what could go wrong, and then.
03:27
Get started with it.
03:30
So to set up your environment.
03:35
Give.
03:35
Me just a second to make my screen a little bit smaller so that I can see
you in the center. So to set up your environment. I am working with Vs
code. I am working with a graphics plugin. And in this repository,
GitHub.com lfservingosthreadmodeling, you will find a file that you can
import directly into your Vs code. So if you open Vs code and.
04:12
You open the OSS threat modeling repository.
04:18
Directory, you will see a JSON file. This JSON file, you need to put it in
preferences, user snippets, choose dot and you should paste it in here. So
replace the existing file and paste yours. That will be all you need to be
able to follow this example as it is. So give me a second.

04:46
All right, so that's basically all you have to do. And the plugin I am using is
that one here.
05:11
I have two plugins installed. You can choose to install them both as well
from fans and from your AlPinto.
05:19
These are good places to start so.
05:20
That you can follow along. Now, as to the threat modeling part, so the
first step is modeling. Perhaps you have seen threat modeling diagrams
done with a threat modeling tool. So data flow diagrams created with a
threat modeling tool from Microsoft.
05:45
I don't love creating my threat models.

05:48
With a threat modeling tool because sometimes the level of detail is not
clear, sometimes there's too much detail, sometimes there's too little
detail. And the tool is incredibly verbose. So you can have hundreds of
potential findings that you need to validate. And it's incredibly noisy. So I
would suggest not to get too deep into that, I rather use a more structured
approach from system architecture. I like the model, the diagramming
model from Simon Brown. It's called C four model because every layer
starts with a C context the system and its users and third party systems,
container components and code containers are deployable units, not
docker containers. And the most important thing, and this is where the
threat modeling tool fails horribly, is that everything has to be labeled. You
labeled your data flows, you labeled your elements. And you are consistent
in the usage of colors.
06:52
For example, blue for in scope, gray for out of scope. And you tell what
every element is there for both the nodes and the edges. So meaning the
lines connecting the notes. Once that is done, basically you can imagine it
as being some sort of Google Maps where you can zoom in. So you have
your system, your target of evaluation in context of its users. You zoom in,
see the deployable units that make up the system, you zoom in to one of
them, you see the code libraries or whatever you have. And then you can
zoom into one and you can see individual functions. I hardly ever have
come so far down except when I ask for a demonstration of a particular
way of an implementation of, for example, authentication authorization.
So there's a.
07:53
This is the system.

07:54
We'Re gonna do the analysis. Someone rang the door. I need to open the
door for a second. I'm extremely sorry. I'll be back in 30 seconds, but in
the meantime, you can look at the system requirements.
08:08
Yes, no worries.
08:09
I'll pause the recording meanwhile.
08:11
Yes, thank you. Sorry. All right, so back from a very short break. So again,
this will be in the show notes and in the slides. This is the repo where you
can find the exercise and the diagrams.
08:30
And this is our target of analysis.
08:33
So our target of analysis is a SaaS solution that supports grading systems.
So statewide grading systems in one of the states of the United States, but
there's nothing saying we couldn't do this in other states or in other
countries. I know Germany has the same kind of because I live in
Germany, I know it has the same kind of nationwide tests that every
student has to go through when they want to graduate from high school.
So that could be a system that we could sell overseas.
09:09
So if we're flexible towards the future.

09:13
We could add these requirements.
09:15
And the idea is that students will.
09:19
Only be used the application in testing centers, and most of these will be
schools. But not all students are able to take the test. And the results are
consolidated into a single location representing all of the test scores
across the state, by school, by teacher, by student. Tests will be multiple
choice, short answer, and essay. So we have three types of.
09:47
Answers or test.
09:49
Well, test will have different types of questions, and the questions will be
either multiple choice, short answer, and essay. So I suppose for math you
might have multiple choice, whereas for literature or language of choice,
it will be an essay or a short answer. There would be some reporting to
know which students took the tests and the scores they received. So I
suppose that is especially useful for the directors of every school or the
teachers. Short answers and essay questions will be graded by teachers
and they will add the estate grades to the system.
10:33
And last but not least, any changes.

10:37
Involves three governmental agencies to make sure that the data is secure.
The state does not own the hosting center, everything is outsourced. And
every project, the project must fight for its budget every year. So without
further ado, we can start. Any questions as to the use case?
10:57
No. Cool.
10:58
Nice to meet you.
10:59
On.
11:00
All right, so we started doing this last session and this is what we had. So
our target of evaluation is a software as a service solution. And of course,
these are all the.
11:27
Details that we decided and we came.
11:30
Out with this diagram. So let me show the diagram again.
11:33
And then we can start working on.

11:35
The next version of the diagram.
11:39
So I create the diagram, make it small. Now, there it is.
11:48
Do you need to do something to open it in graph vis or should you open
directly.
11:56
You might need to have graphics installed. So I'm working on.
12:04
If you go.
12:04
To your terminal, if you run dot.
12:08
It gives me answer.
12:10
Yes.
12:10
If I go to the terminal and.

12:11
I write dot, it minus H, it tells me something. Got it?
12:18
Yeah, I think I need that.
12:19
So you have to have that installed. That's the last requirement.
12:24
Of course. Sorry for that. So, .
12:32
Based on what we just read so we have testing centers which could be
schools. We have testing centers which are not schools. So different
network zones, different scenarios, different threat actors.
12:45
We have students in both, we have teachers, we have a grading system.
12:54
And this is our target of evaluation.
12:56
The grading system, find IDs to these things. So, for example, a lot of stuff
in my world we end up in jira, but it could be something else. But I think
there's a need to connect this to other systems, right, to wider things. If
you have an ID, you would put it here, correct?

13:19
Of course.
13:20
Now the question is, do you have an ID for the environment it should be
running or for the user?
13:26
Right.
13:26
Because in this case, it could be both the same user. But one year the same
user does it in his high school and the other year the high school is not
lending the lab and they have to go to a testing center.
13:39
No, I meant almost the ID for the node. See what you have here. When I
look at it, these are nodes.
13:44
Right.
13:45
You got a node represents the student, the PC in a computer, PC and
protector, and then the teacher and even the grading system. All of those
are, if you think about nodes, of actually a wider graph. And then part of
my thinking here is eventually to start to create this programmatically
using a graph database. Because at the moment, the data for this is in the
diagram, correct?

14:13
Yes.
14:14
I think in a medium term, we almost want this diagram to be created
almost from a graph. Do you know what I mean?
14:24
Exactly.
14:25
So, yes, you could add that. I'm not exactly sure where to put it. So it
could be some metadata for the node.
14:34
Yeah, you will be metadata. You will be one of those.
14:40
I'm not sure how much metadata is supported in the graphics format. To
be honest. I haven't tried that. So that's something we definitely could try.
14:47
Cool.
14:48
So basically what I'm doing when I create a node, I'll make the diagram a
bit smaller is.

14:57
Make it a.
14:58
Bit prettier than it usually is by default. So I create a node that has no
shape, so all the shapes are plain text, so that I can do some HTML inside.
So I'm basically creating a table, an HTML table that has images. And if I
turn the table on.
15:22
The cell borders to one, so you could see here how the table looks like.
Cool.
15:32
So that's pretty much easy to read, isn't it?
15:36
And the advantage this has to draw I O and other formats is you're
actually able to see the commit message or in the diff kit div what changed
in the diagram?
15:49
Yeah.
15:51
Draw.
15:51
I o.

15:52
It's fantastic. You can also have the plugin here. Now the problem is all
visual and it's all a bunch of XML in the background. And it's so huge,
there's no way to know what change.
16:02
Exactly.
16:03
That's why we almost want another level of abstraction, isn't it, where you
could start almost as diff the behavior right, almost the content, and then
have a way to create some of these. So even that table is powerful, but I
wouldn't need to see the diff. I guess you're saying that if you're only
making a couple of changes on the content, that's what you see on the diff
in GitHub.
16:30
Yes, exactly.
16:31
So if I change the description, if I change a connection between nodes.
16:40
Correct.

16:41
That's incredibly powerful. And I can just replicate this to do the
component diagram. Right. So we have the context diagram. Based on the
context diagram, we created a list of findings last time when were
discussing this. So we have Spoofing take an examiner on behalf of
someone else selling the questions. So we had taking pictures of the
questions for selling, for cheating, for memorizing the questions, attending
different locations for the exam repudiation. I wasn't there. Tell me that I
was. Those are not my answers. So how do you make sure that there's no
repudiation on the answers, on the content? Spoofing get the teacher
access to the system and grade myself. So if teachers are grading answers,
there are competing interests here to get access to the system. So these
are all things that students could be trying out.
17:49
Isn't it amazing how fast things have moved that now we should add one
which is GPT take the exam on.
17:54
Behalf of the student, isn't it? Of course.
17:56
I mean, we could add that one here and basically is well, not selling the
questions, but basically cheating. Right. So cheating couldn't be classical.
18:12
And you could even add an interesting thread, which is how to do that
without being detected. Do you mean? And that's going to be an
interesting thing. It's a bit like if you are a student that has 56% out of
100, if you then get an exam submitted, that or you get 99 or 98, you
almost need now a cheat that actually almost gives your score.

18:39
Exactly.
18:40
I just added that one. So what did I do wrong? Cheating.
18:49
Why is it not taking?
18:57
You might need an enter about okay, one more level. I know something
happened there with the levels. Oh, it's the space.
19:05
It will have a space too many. No, it's not.
19:09
It might have a tab actually.
19:13
That's okay, now it's working.

19:16
So use chat TPT to answer the question. So these are all threats that we
have identified from the student side. This is just a recap from last month,
right? And the teachers, were saying, okay, grade your own. There's an
incentive. Teachers are graded with the students, right? So if my students
do better than average, I get a better grade, thus opening positions for
salary increases or something else. So if I know whose answer I'm
grading, I might be more lenient than if I don't know who am I grading?
Grading other students worse than necessary. I could also be making
money on the site by selling the questions. I could facilitate cheating, so
attending several locations or allowing someone to take the exam on
behalf of someone else. And of course, directors also want to have better
grades by taking the answer. So we need to figure out how we're going to
keep the findings safe from everyone.
20:31
So this is what we came up last session last month. Now it's time to go
further. So we have the admin. We don't yet know how the admin is
getting in, but we know that the admin well, the school director, right? So
we have a school director that adds teachers at students get three ports
per class, per school. So someone has to manage who will have to take the
exam, right? So we said that was the school director or someone on the
direction side of the school.
21:05
By the way, just for reference, to get this UI that we're seeing here with
Lewis, I had to go to the command palette and open the graphics open
preview and then that's the one that will then preview the what's it called?
21:26
Did you every time I have a.

21:29
Graphics diagram, I have this Open preview.
21:32
To the side activated.
21:34
There you go. That works, too.
21:36
Perfect. Yeah.
21:37
So that's a bit easier for wildly maps, they don't have it. So I do have to go
and click on Open View, but for dot I usually just yeah, that works too.
21:46
I haven't used that. Cool.
21:49
Brilliant.
21:49
Yeah, I got it. And we do so which one are you looking at the moment? Are
you looking at the great context on the root?
21:56
Yeah, I think we didn't add the admin, so basically we could add the admin
now and say, okay, the admin connects to the grading system.

22:11
Very cool.
22:12
By the way, this is crazy reference. When you do this with an audience, for
example, threat modeling session on site or remote, it's super powerful to
have it on screen and then literally be changing the code and seeing the
diagram for everybody.
22:30
It's very powerful, to be honest, even if presential, I don't use the
whiteboard that much anymore because I have to pass it in clean
afterwards. So it's a lot of work to.
22:40
Do it you might as well be creating the diagram in the session, isn't it?
22:47
I do. So basically I share the right hand side to more or less show you how
I do it.
22:56
I basically make it big and now.
23:01
Move it to the side. So basically I show that side when I'm sharing the
screen with someone and.
23:05
Work on the other side.

23:06
Of course, now I'm not doing it in that exact way because I want you to
see how I change the code. But basically here we say, okay, logs.
23:17
In, does administrative functions and that means.
23:27
We now have to open up the system and start looking at the system.
23:31
Right.
23:31
So we already identified problems at this very high level. These are usually
unhappy path scenarios that are not considered in the usual requirements.
And this is the first place where you can start looking. So you don't even
have to start doing strides at this layer. At this layer it's just abuse cases.
So what could go wrong? How can I use the functionality against the
system now? Frank Adam, do you see any other things on how you could
abuse?
24:06
So do you think it's different a.
24:09
Student taking the assessment in the testing center, which is not a school
rather than the school? Are there any difference we should consider? Raise
your hands if you think of anything that we should consider.

24:30
Doesn't seem so okay. So I mean, it depends a lot.
24:37
On who is proctoring the exam.
24:39
Right?
24:40
Are the teachers who know the students proctoring the exam for their own
students so they know and they can pass list? Or do we have people who
don't know the students and students at a young age don't have IDs. So
how do you make sure that whoever is taking the exam is actually who
this person should be?
24:57
I don't know. Right.
24:58
So if we're taking the test in not a school and the teacher is not
proctoring, I have no idea how they are identifying the students. So this is
a lot more risky. So we could add here a threat actor. So we could add
here a fake student.
25:18
Let me see if I yeah, because.
25:20
The student could even somebody could be there doing it for them, isn't it?

25:24
Yeah.
25:24
So here we could add a fake student. The short form I use is HTML and I
will call it Bad student.
25:46
Bad Student.
25:48
So if you tap through the snippet that is created, you will jump
immediately to the corresponding spaces. So I jumped from the name of
the note to the label of the note student.
26:06
That's interesting. What creates that?
26:10
The Snippet that I put the shirt remember JSON, the one you copy paste?
If you type HTML and you tap through the fields, it helps you jump from
one to the other. Cool. So I jump to the file path. I have one in images.
26:31
Hacker transparent.
26:37
PNG. No, I didn't name it that way. Give me a second.

26:46
Terminal. No, not the hackathon. Sorry.
27:00
Hacker minus transparent. Okay, sorry. For that. My mistake.
27:06
Hacker.
27:09
Minus transparent.
27:10
So here you can see I just.
27:13
Added within the picture without a lot of trouble, a nice looking hacker.
27:19
So the bad student.
27:32
So this is someone pretending to be a student. And the purpose is.
27:40
Cheater pay for the student to pass the exam.

27:52
So that the only thing with it being HTML is that you cannot really add
break lines. So I had to ask the break line, like in HTML to pass exam on
their behalf.
28:07
And this is fundamentally planned. UML, right. So basically, behind the
hood, if I'm not wrong, all graphics or graphics uses this to render it. So
graphics has some support for HTML.
28:19
Yes, this is native graphics. So this is just the reason this works is because
the node type is plain text and it just fills in within everything. So I control
every aspect of these nodes. So this is also part of the Snippets I created
and I shared it's. Just start typing, I think, diagram or degraph, and it just
fills it out for you.
28:48
Yeah, very cool.
28:52
But student cheater paid for the student to pass the exam on their behalf.
And the nice thing about this is that I can do the student out.
29:02
In a group.
29:03
So student out and bad student. So that easy it is to create new lines.

29:11
Right.
29:11
So bad student and the student try to do this, pass the thing on the exam.
So now we know who is doing.
29:22
That'S. The interesting one, because you put the brackets in there. Is that
why you create that box around it?
29:27
Yes.
29:28
No, the box around them is because they're a cluster.
29:32
Oh, because I got it. Because you got the cluster.
29:35
No, the box around them right now.
29:37
Is can I make it bigger?
29:40
No, the box around the curly brackets here is to make sure that they both
have the same line.

29:47
Yeah.
29:48
So now in this sense, I'm answer label.
29:54
First of all, label and then answer exam.
30:01
So here we have the bad student answering the exam and here we could
have the student cheating and doing all the things. But I mean, in both
cases it is different, right? So here we have someone pretending to be
someone else. So here we have the nice student and here we have the path
student paid for or whoever is the twin brother or the older brother or
whoever.
30:29
Right.
30:32
So we have the teacher and now we could start looking at the
architecture, right?
30:36
So we could say, okay.
30:39
If we.

30:40
Open the grading system, what could we expect to find? Right?
30:47
And this is the point where we have to work with an architecture. So since
this is an architectural CATA.
30:53
We don't have a given architecture, so.
30:56
We would have to create architecture. So this works great with developers
or with system architects because they could help you create this. And you
can do threat modeling on the fly as they start creating the system. So
basically we could copy so let.
31:16
Me save this file. Okay, it's saved. Now I'll just replicate the file, copy
paste, and I will rename it to container. Come on.
31:43
Why is it not working?
31:44
Come on, come on. I have no idea why I kind of changed the.
31:56
Oh, I pasted it.

31:57
In the wrong place.
31:58
Okay, I need to open the terminal.
31:59
Pardon? Great context. So move great context to create kata.
32:16
Container graphics. So now here what I can do is.
32:27
Close this thing.
32:29
I close this thing, I close this one. Now, of course, this is still the.
32:36
Same one.
32:39
But now I could start adding.
32:44
Images.

32:45
I could start adding AWS architectural elements, right?
32:50
So one thing I could expect to.
32:53
See here is some sort of WAF. Well, first of all, a network, right?
33:00
So.
33:03
I will start carving out here the network, and I will start pruning the
number of students, right? Because we don't care too much about the
students, we care about the connections and where they are connecting to.
33:21
So in terms of groupings a bit together, would it be good to, for example,
start creating folders for these scenarios? And then inside those folders
you can almost have a markdown that explains what it is. And then all the
diagrams that you create based on that particular scenario.
33:39
What I usually do, to be honest, is give me a second, I have the report
here.
33:46
So I have the report, I start.

33:50
Adding the diagrams and how I look at things. So this is the diagram I
represent whatever I start finding here. And then I start adding here the
vulnerability, the attack scenario and the outcome. So I have one
document that encompasses this. And then I add this document with a
context diagram, the container diagram. So the detailed technical view of
the cloud system in this case. So basically, I could add here. So here, of
course, we don't yet.
34:44
Have the trading system container diagram images. Well, it couldn't be
great context, but rather grave container.
35:02
And I will just print out the grave context again, give me 1 second because
we made some changes.
35:08
So.
35:12
Context. So pardon me just for 1 second while I print the great context
with the changes. Thread modeling images create context. Yes, override.
And that basically overrides. It in my diagram so I don't have to suffer too
much. And then I can start with the container diagram. And here I could
start by deleting this grading system, because now we're going to go into
the details of the grading system. So here we could say, okay, I have a
cluster, and here we have.
35:55
An.

36:01
External zone cluster, external. Here we have the.
36:07
I don't know.
36:08
Let'S call it DM set. This is the exposed. This is to the Internet. So we can
see that has changed a bit. Actually, it's not yet there because we removed
it. So it's an empty cluster right now. And here we could have different
nodes. So I will not put images right now. I'll add the images later. So here
we could have the test API.
36:53
Test API.
37:02
This is a I don't know, let's say Python. Which framework do we like in
Python for making APIs?
37:13
It's called fast API.
37:15
Fast API. Lovely.
37:17
Pretty awesome API, because it also gives you the Swagger file.

37:21
I know, I know, they're like different flavors, right? But then you can say
that. And then this one is receives answers from authenticated users. Okay,
let's see where we have it. So we can see that it's growing here,
disconnected from everything. But we can start seeing that.
37:50
Here we have the test API.
37:54
Now we have the test UI, which is hosted in a react or whatever. So let's
say this is the test UI.
38:09
No HTML?
38:12
No test UI.
38:19
Test UI.
38:22
By the way, what's cool about this is that what we're really doing is also
defining those what's it called, pressed boundaries, isn't it? Where we start
to understand exactly what's running where, and that will make a massive
difference in our threads.

38:41
Exactly, that's the idea. So the idea here is that we have Node JS that we
understand. And that's why I like the C Four modeling convention, because
you really understand.
38:52
In a very structured way who interacts.
38:56
With your system, how your system is distributed, technology choices. And
then you can add on that whatever else you need to add on that. If we
need to understand how the test API is built, the individual components.
39:10
That make up the test API, we.
39:13
Can go so far. But we don't need to go so far to see what could go wrong
in general. So here we have the Node JS interface. Let me make this word
wrap.
39:28
It's a bit easier to work with word wrap. I lost myself, sorry. Node JS.
39:34
Okay, we have a Node JS API.
39:37
And this one basically shows the questions to the students.

39:46
So now we have we call it TMZ. But I mean, this could all be running
within a Kubernetes cluster. Or this could be running wherever we wanted,
right? So that's the testing part. Now we need the testing creation part,
and we need a few more elements, right?
40:03
So we have the teacher UI. Here we have it.
40:19
So here we have another HTML node.
40:23
Teacher UI. Teacher UI. And again.
40:32
This is a python.
40:36
Fast API thingy.
40:39
And this.
40:42
Allows teachers to.
40:47
Submit questions.

40:50
Further.
40:56
It allows teachers to we could save ourselves some trouble. Allows
teachers to break here.
41:09
And then submit questions. Great.
41:26
Answers. What else could the teacher do?
41:32
Or you could also have a malicious teacher, right?
41:35
No, well, I mean, the normal right.
41:37
Now, like the normal requirements right now.
41:40
We'Re just painting the happy picture. And then we can start doing the
hacking, the bad stuff.
41:46
Right?

41:46
But first we. Need to understand what we're dealing with. So students test
will be multiple choice. The system should have a reporting system to
know which students have taken the test and what score they received.
Short answer and essay questions will be manually graded by teachers,
who will then add essay grades to the system. Change approval state does
not own project, must defend its budget.
42:14
So, yeah, that seems fair.
42:17
And also, the other thing that's interesting about up until now is ideally
this should be provided by the dev team, isn't it?
42:25
Ideally this to be honest, I usually create it with the dev team because I
have yet to see a dev team that keeps their documents up to them because
they have to go to VCO, they have to go to draw IO, they have to leave
their ID.
42:41
But that's why the developers eventually start to love this kind of stuff,
because this allows them to keep maintaining their documentation up to
date. And this is a good example where we can add a lot of value to
security teams because we need this and they also want it too.
42:57
Yes, exactly.

42:58
So in one of my previous positions, I actually gave like a class on how to
do this, and some teams.
43:07
Actually started doing it, so I couldn't.
43:11
Enforce it, but at least it won enough traction that people were willing to.
43:15
Try it out, which for me is a win, right?
43:20
Oh, no, I got it wrong.
43:21
So this is the Python Fast API.
43:25
Thing, and the UI is node JS.
43:36
Processes input from users from teachers.
43:48
Now, we could start looking at this.

43:50
And say, okay, well, actually, not everyone.
43:53
Will be talking to the same thing, right? So ideally we could have students
not talking to grading, but talking to.
44:08
What.
44:08
Do they call it? And that's the only thing you need to keep in mind always.
44:12
Like, how did you call things?
44:14
So we called it teacher API. Teacher UI.
44:17
Let's make it all look the same.
44:20
So teacher API with small and API and PS.
44:23
Teacher UIP, test UI and test API. Okay.

44:32
So with that naming convention in place, it's easier.
44:35
So the student talks to the test UI to retrieve questions from the student.
44:51
Talks to the test API. And this is a crucial thing that is often overseen by
developers, right? The UI being node JS is loaded into my browser, which
executes in my context. And the API is actually not necessary. It's optional
at the moment where it runs in my context. I can just decide to use it or
not.
45:31
But also you could argue that test UI should not be inside that DMZ.
45:36
Right? Well, you're going to serve it.
45:40
So the static file oh, God, I got it.
45:44
That's the static version of the test UI, basically.
45:47
Well, rather than retrieve the questions and send responses to disappears
from this one.

45:54
Right?
45:55
Well, to be honest, I think there's value in actually putting it on the
browser? Because if you think about it, that's what you have. Then there
it's almost just static files, isn't it?
46:07
It is, but you still have to identify that you have a node JS or not node JS
NGINX, probably, or CDN or something serving these files.
46:19
Yeah. But then isn't it better to put the test UI on the browser context?
Because he implies that the trust boundary, like you said, we need to go
how does he get the data? Because that is just almost a static server of the
provide content. Which is important because you might actually have a
node back end. Right. You might actually have. Which in this case we
actually say we don't have, because you actually say you're using Python
for it. If I saw this, I was going, why are we using node JS? But if I have a
Python past API, what is the actual node JS actually doing that an NGINX
can do? Because that would increase the attack surface.
47:17
Yes.
47:18
Well, I mean, to get here, you do need some authentication. Right. And this
is the point where I don't know how to give the so either every student
comes to school or to the test day with their password or their Identifier in
the hand that they received during class, or there's no way to onboard
them.

47:38
Right.
47:39
So there's here there's a cat in a sack that's not exactly clear how it got
there.
47:45
Yeah.
47:46
Or they can be given a UID, some token when it is lost.
47:50
You can give them something, but how do you give it to the student?
47:53
I mean, think of eleven year olds.
47:57
They might or might not have a cell phone. They might or might not have
a laptop. So you need to give them a piece of paper that they can take.
48:05
To the exam on that day or.

48:07
Receive on that day and use it to type in and identify themselves towards
the system. Right. So here at some point retrieve static content from and
then we might need to even say, hey, this is the browser running the test
UI. So now, because this is a computer.
48:25
Not a student, the browser is running.
48:28
The test UI, is sending answers to the test API, retrieving the static content
from here. So now we identify the relationships.
48:35
Yeah, got it. So in your case, the browser is the box above.
48:40
Yeah, got it.
48:41
So this is the browser running the test UI. And now we need to figure out
how does the user authenticate. Right. And that's not something that they
gave us.
48:50
So we might need to add for.
48:52
Authentication, which is something I usually add after the protocol itself,
https.

49:01
UID for authentication.
49:07
So this person has a UID and then we could enhance this in the context
diagram saying how this person gets.
49:15
The authentication code, I don't know. Right.
49:18
So we could add that later and basically the same story happens to the
teacher. So the teacher does not log into the grading system. The teacher
talks to the teacher, UI, logs in.
49:40
Retrieves static content, and this.
49:46
Is Https, and they do have a.
49:56
User ID, clues, passwords, or some other.
50:01
Way to authenticate themselves or their single tenant, let's say.
50:05
Single tenant. Single tenant.

50:07
So they need to use the same credentials they use for school. Single
tenant. Let's make ourselves CC yeah, that's fair enough, right?
50:14
Which actually then when you go into the remote one, that might
introduce a curveball because they might not have the.
50:22
Same system, isn't it? Yeah.
50:28
So give me a second while okay, there it goes. So label, and now the label
is.
50:38
Sends grades to questions.
50:46
Retrieves at the content. Oh, well, sends and receives.
50:50
So sends grades queries questions from.
51:04
Sends grades to.
51:08
So basically the API, the teacher use.

51:12
It to query questions to and send grades to. And this is just for the long
form and short form answers. So this is the teacher and we can say here is
grading.
51:28
Grades, long.
51:29
Form answers in the browser. So little by little you can see that the
diagram starts to look differently.
51:40
And we could even say, okay, could.
51:43
They even be in the same segment?
51:45
I mean, to be honest, I couldn't.
51:48
Have these things in the same segment. I would probably want to isolate
one from the other.
51:56
And then we could.

51:58
Keep on doing this exercise. I mean, I'm running out of time now, so I'm
just going to wrap it up. Showing like the next logical step would be to
add here another cluster.
52:14
Database.
52:18
DB zone, VPC database.
52:26
HTML, DB.
52:35
I don't know what's the SQL database from AWS called.
52:39
I always refer Aurora. Believe so, I don't know, it seems good enough.
Aurora SQL database. Now we know what we're dealing with.
52:54
And then who connects to it, right? So on the one here stores, questions.
53:13
Answers, sorry, it's too small.
53:17
Stores, questions, answers.

53:21
Grades.
53:32
What else do we have here? Student.
53:37
Data, maybe? Stats, school districts, schools.
53:47
What were you mentioning?
53:48
Stats, statistics and activity data.
53:53
Depends. Right.
53:56
Statistics.
54:02
Yeah. And then of course something has to.
54:07
Connect to it because else it has no value, right?

54:09
Exactly.
54:10
This reminds you of that joke of that teacher that was doing a pen test
course and said, here's a page that has all your scores and you all failed.
Your job by the end of the semester is to pass. You have to hack into the
system and change your grade.
54:29
If you do, you pass.
54:31
So that was such a cool way to say teach your grade. At the moment,
you're all failing.
54:39
That's great. Teacher API. They both.
54:46
Read.
54:47
No, they talk to the did I just call it database? I just called it database.
55:00
Okay, so that's the only thing when.

55:03
You do this, you have to keep.
55:06
The names of the notes in your head database.
55:09
And here we could add a label in which I mean, this couldn't be all too
uncommon, in which you say.
55:18
Read, write data, two, and they connect.
55:23
As the.
55:27
So it's encrypted communication.
55:33
Whatever protocol the database speaks, but admin user. So I have found
this so often, and it's always a great discussion why.
55:45
It'S a bad idea to need, right? Yeah, because that makes a big difference.
Because what's interesting is that you have, for example, these different
UIs here, and then you can ask the question, why should the test API has
privileges to change stuff where you should be in a situation where even if
the test API has a vulnerability, you shouldn't have the privileges to change
stuff.

56:07
That's exactly what I end up in my discussions with developers. So I
usually end up here with developers saying, okay, it's a terrible idea to
have admin rights here. Oh, but we do this and we do that.
56:23
Yes.
56:23
But if by any chance any one single location, you miss something and I'm
able to say, drop tables, you lost the game.
56:31
Yeah.
56:33
And sometimes they react to that and.
56:35
Say, okay, you're right, it's a good example of saying that makes a
vulnerability in that test API ten times more toxic than otherwise, because
then you almost limit the damage that can be done.
56:50
Exactly.

56:51
So give me just 1 second, because right now it makes no difference to have
the bad student here, so I'm just going to kill them. And we do need the
admin, right? So we need the admin to be able to talk to the admin
interface. So the teachers are doing some things and the admin is doing
the same. So basically we would need to add.
57:11
The same again for admins.
57:15
But we run out of time. So this is an exercise and commit to GitHub. I
mean, I can commit to GitHub. Well, I will not do live. I'll commit to
GitHub in a few minutes after the call. And we can wrap this up next
week. Well, next Open Security Summit, in which we do compare these
against threat modeling.
57:40
Tools from Microsoft to see who gets more actionable results. For
example.
57:46
Yeah, I think it'd be really cool to see if you can refactor a little bit. For
example, that HTML code so that you don't have the complexity and you
have a better diff, isn't it, on the actual code. But the super powerful thing
is at the bottom of that file that you have there, where the relationships
are now. Easy to read, easy to map, easy to like. If you scroll down on the
left. I think the real powerful is this bit here, right? In fact, if you just
maximize that's the power, isn't it? Just a little thing. What I tend to do
here is just move it a bit to the right. Again, I tend to add spaces because I
think you can. So I try to align, for example, even the arrows so that you
can almost read them, so you can add space C, so it doesn't affect the
result.

58:43
So you kind of get them all in one line. So you could see that at the
moment you almost want to have all the arrows to the right aligned.
58:54
Yeah.
58:55
But even on the student, I would also align that with the one below. Do I
mean no, go up to line 96. On line 96, you know the arrow if you tab it?
No, tab to the left. Yeah. Now if you tab it and you align it with the arrow
on line.
59:17
98 oh, I see what you're saying.
59:20
Yeah. See, so by doing that and then it might be that you might sometimes
even allow I'm just kidding.
59:27
This one anyways, remember?
59:28
Yeah.

59:28
Or maybe if you kill that, then you maybe don't need that. But you see
what I mean? So I try to align it because it's much easier to read, right.
It's kind of like you almost go AB and yeah, so I tried to align that in code.
You might not need such a big space now that you don't have the one
below, but always add a little bit like that, a couple of extra spaces. And in
this case it's cool because graph, this doesn't matter how many spaces you
got, it still basically uses the separator. In fact, even you could see even to
the right of the arrow, just add a couple of spaces, it becomes already
much more readable.
01:00:03
Right.
01:00:04
So even there yeah, just two spaces there, see? Or a tab. See, I mean, like
even that is already much cool, you know, to read. See what I mean?
01:00:15
Like I know what you mean. So here I could basically ask admin.
01:00:24
Admin UI.
01:00:29
Admin.
01:00:37
API. Yeah, that's about the problem is once.

01:01:00
You cluster them, you lose a lot of space.
01:01:04
Right.
01:01:04
So either you don't cluster or you yeah. Break the line. I'm not sure if you
can break the line, actually.
01:01:11
Yeah, but see, this is a good example of sometimes I prefer the inefficiency
of not clustering because it improves readability.
01:01:21
Yeah. Do.
01:01:22
I mean, sometimes it's like you might get a little bit of efficiency, but
especially in the code, I always goes, well, it's not because you can
improve it or make it smaller that it actually makes you more readable.
Because I think the readability is a lot more important than sometimes
some of these clusters or some of these code optimizations that you have
there.
01:01:45
Yeah.

01:01:47
Because even here, what you can do is you can start to group them. Look
at how nice it is to have all the admins in one place, all the students in one
place.
01:01:56
Yeah, I think it improves readability a lot.
01:01:58
Absolutely. And especially once you start diffing it gets even more relevant.
01:02:03
Certainly I'm literally sending that screenshot to my team right now.
01:02:09
Check this out. This is threat modeling as code.
01:02:13
Well, it's diagramming as code, right? Threat modeling comes afterwards.
The problem is this is not even threat modeling, right? This is the basis for
threat modeling. And once you have this in place here, then you can start
doing threat modeling because it's trivial now you have all the information
you want. You don't have to consolidate or correlate diagrams with
descriptions and this other thing and this other that. Everything is one
place now. It's very easy to focus and just zoom in and you're done.

01:02:46
Yeah, and then there's so much potential here man, this is definitely
something we need to keep experiment on this. And this is also an area
where I feel the new GBT world of code pilot and things like that. I think
now again to the point where some of these will be created
programmatically so we can take it to the next level in a much more
scalable way. But this pattern would always going to be needed. It's just a
way to scale this to the next level.
01:03:11
Certainly.
01:03:15
The problem is I haven't found something that's really a lot better than
this. So I know this is a bit clunky and it's not yet perfect, but.
01:03:24
The simplicity of graphics is by far superior to me.
01:03:30
Especially when diffing to draw IO or other things that are more wishy we
what you see is what you get.

01:03:36
What I've done is in some cases I start to just throw those nodes and edges
sometimes in jira, sometimes in JSON files and then create the graph like
that using plan to ML which basically creates these graph bits, just a wrap
around graph this and to try to make it easy to understand and to
visualize it. And I want to work on a system that were already creating
those text programmatically from reality. So imagine a world where you
analyze the code base or a repo and those relationships that you have
there literally that text is also created programmatically added to a
version control. So you still have the same base because it's like you
mentioned before, draw your visio, it's all nice, but it creates works of art.
People can't maintain it and more we need things that come directly from
reality.
01:04:36
Cool. Exactly.
01:04:38
That's usually the problem I face. They've spent so much time doing one
thing and then something changes, they don't want to do it again.
01:04:49
Absolutely right. And also the worst part for me is that everybody becomes
allergic to change because in their heads they're like oh, that's going to
take me half an hour to do. So they almost start arguing why not to
change versus just saying no, that's reality. That's how he goes, that's how
he evolves. And of course you can version control it. There's lots of things
that are not.
01:05:11
Very good with it, certainly.

01:05:13
So basically, I have now made the diagram, so, of course it looks a lot
different. And we could predify this a little bit in which we make invisible
connections between the UI and the API so.
01:05:28
That it's less wide.
01:05:32
But usually screens are wider than they're taller, so I'd rather have them
going sideways than going is lengthwise.
01:05:40
Yeah, well, man brilliant.
01:05:43
That's another session. Good materials. And then for anybody watching,
right. This is real world, right? This is literally how, at the moment, we do
stuff, and still the state of the art is there's lots of great areas for
innovating here. So cool. So, Louis, thanks for doing this session and I see
you in the next one.
01:06:02
See you next time. Thanks.
