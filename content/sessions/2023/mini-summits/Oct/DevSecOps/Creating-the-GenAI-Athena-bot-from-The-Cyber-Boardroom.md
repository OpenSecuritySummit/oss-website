---
title        : "Creating the GenAI Athena Bot from the theCyberboardroom.com"
track        : DevSecOps
project      : DevSecOps
type         : working-session
topics       :
featured     :
event        : mini-summit
when_year    : 2023
when_month   : Oct
when_day     : Thu
when_time    : WS-18-19
hey_summit   : https://www.linkedin.com/events/7117257697510535168/
banner       : https://pbs.twimg.com/media/F8BzMHpWUAEgRhM?format=jpg&name=medium
session_slack:
#status      : 
description  :
organizers   :
    -  Dinis Cruz     
youtube_link : https://youtu.be/u3OfYL-VkaI
zoom_link    : https://us06web.zoom.us/meeting/register/tZwsdOChrzosHdBJPL6jXWGLEZW5ZCueeZvH
---

## About this session
Strap in, intrepid explorers of technology! 🚀 This session, presented by the visionary Dinis Cruz, beckons you towards an exhilarating adventure through the intricate and thrilling world of GenAI, specifically highlighting the creation of the impactful Athena Bot for theCyberboardroom.com.

## Key Takeaways

Navigating the GenAI Universe: Witness the vast and awe-inspiring landscapes of GenAI, and explore its dynamic capabilities and transformative potential in the cybersecurity domain.

The Athena Bot Chronicles: Gain exclusive insights into the conception, creation, and impactful role of the Athena Bot within the digital sphere of theCyberboardroom.com.

Foreseeing an AI-Infused Future: Engage in thought-provoking discussions about the future horizons of intelligent, AI-driven digital boardrooms and cybersecurity.

## Why Join Us?

This session promises a cascade of 'eureka' moments, sparks of innovative thought, and a glorious peek into the potential-filled world of GenAI. Whether you’re an AI enthusiast, a cybersecurity professional, or simply a curious soul, this journey with Dinis is sure to enlighten, inspire, and elevate your understanding of GenAI applications in cybersecurity.

## Save Your Virtual Seat Now!

Prepare to be inspired and enlightened by a session that not only dives deep into the technological marvels of GenAI but also surfaces with pearls of wisdom and futuristic visions that could shape the trajectories of cybersecurity and digital boardroom management.

## Transcript:
Dinis Cruz - 00:00
You. Hi. Welcome to this open security summit session in October 2023.
And I'm going to be talking about a project that I've been working on all
my spare time, which I published a lot of details, but I want to kind of go a
bit more into the workflows and how it works. And it's basically the idea
of creating a bot gen AI bot chat GPT, but actually eventually will be
powered by Bedrock and Bard and all the other vertex AI and basically
some of the big gen AI engines LLMs out there. And the idea is to be kind
of a one stop shop for board directors to talk about cybersecurity. So it's
about teaching board members about cybersecurity, actually.

Dinis Cruz - 00:52
It's about also, for example, allowing new board members or people who
want become board members to learn more about cybersecurity and also
actually allows CISOs and other professionals to talk to board members
and communicate with it. So kind of what we've done was kind of created.
There's some content here. So this idea started by, hey, let's create some
content for board members that provide information. The problem is kind
of typical one, right? The problem is you have this, but then what from
here should I know about what matters? What's important? How do you
make this in context to a particular board member?

Dinis Cruz - 01:32
And just for context, the problem as a CISO to communicate with board
members or even board members to ask questions down, is that for this to
really work, you have to be able to provide something that is actually in
context with that individual's personality, knowledge, culture, language,
understanding, and even conversation, right? Because as they evolve their
thinking, their understanding, they're going to be asking different
questions and they're going to evolve. And to be honest, just about every
board member I met, they're very clever, they really sharp, they just might
not have it or technology or cybersecurity experience. So we need to plug
that in. So the idea is to create Athena. We actually have three bots, but
I'll walk you through the first one. And the idea of Athena is this
cybersecurity advisor. So just quickly give you a tour.

Dinis Cruz - 02:22
Basically, you go in here and you say, hey, good morning. Who are you and
what do you do? And then you submit a question. So the coolest thing is
that you could see now and this is powered by Touch BT 3.5, by the way, is
that it's able to give information. Hey, I'm atina your cybersecurity
advisors from Cyber Boardroom. Our main purpose is to assist board
members like you with cybersecurity questions and concerns. So what's
cool about this is say, hey, it's an interaction. So what we're trying to
figure out, and this is one of the powers of chat DBT.

Dinis Cruz - 02:53
And I really want to stress that if you want to get something out of this
session, is about thinking how you can create agents that really augments
certain individuals, but also allows to capture knowledge in a way that is
now shared with others in a much more effective way, especially in a
language way. And in fact, with one of the sessions that just happened is
that we created a really cool thread model that we passed to try to PPT,
and then we actually created a game almost like a bot to test developers,
to test users on that environment, right, which is pretty cool. And that is
very developer specific. So here you can say, I'm here to help to
understand the cybersecurity challenge and risks within your company. So
you can say, okay, hi, and then it's always good to be polite.

Dinis Cruz - 03:38
Remember that it's all about the more polite you are, the more polite it is,
right? So, again, there's no need to be rude here. So you can say hi, and
you can say, okay, I'm from, let's say, I think, what was the user I used?
Oh, government, okay. I'm from, let's say, UK government organization.
And organization where I need to know what is cybersecurity and how it
applies to me, right, and how it applies to my world. And you could even
say, I'm aware that it is very important and all these things are kind of
relevant. So if you say, I'm aware, it's very important. In a way, the
Athena, the bot should not start by explaining why cybersecurity is
important. It should say, you're already there. And this is the idea.

Dinis Cruz - 04:41
The idea is you create a bot environment, and I will show you in a second
just how much or how almost easy it was to create these bots at this level.
So you basically asked the question and now he's going to say, look, it's
great to have some government organization seeking insights about
cybersecurity. So he's now start to explain what is cybersecurity? So, you
could see, refers to the practice of protecting computer systems, network
and data from digital attacks and authorized access, right? And then say
the concept of governmentization is of importance. And then here's the
key points data protection, national security, public trust compliance, and
regulation that you should know. And then you can start to zoom in. You
can say, okay, can you zoom in on data protection?

Dinis Cruz - 05:26
So the point here is now you can have an interaction conversation and you
can start to basically keep going down in a way. The nice thing of HBT in
this case, and this is without even doing a lot of clever prompting, without
a lot of specific areas, he already has quite a lot of basically good set of
content, which is here you can argue that data classification, access,
controls, encryption, these are all really good stuff. So then you could say,
okay, so what questions should I ask my CISO? Right? And what's cool
about this? You could see that he has context and he understands that
CISO is the Chief Information Security officer. Remember that he still
understands that it's a board member and he cares about cybersecurity.

Dinis Cruz - 06:15
So now you get some really nice questions that to be honest, I would love
to be in the receiving end from one of our board members. And one of the
features we're going to add in the future is actually to be able to
customize these based on the user, but also be able to have a workflow
where we can then take these questions, let the CISOs ask the questions,
get the information back. So have a much better two. And now you could
see, right, that's basically the workflow. And you could also ask, what are
my legal responsibilities? Which is again, something that a board member
would also care about. And you could say, like a board member, you have
legal responsibilities concerning cybersecurity. And then these are the
areas that it matters there, right?

Dinis Cruz - 06:57
So, in fact, he even has Directors Fdcrl rules to act in the best interest of
organization. So you can see that as a board member, this starts to
provide really good information. And you could also zoom in. So the
person say, okay, I have an MBA. Let's say MBA, like football, let's say a
law. So can you explain ransomware for me? Right? And so the power
here is going to say, okay, so now he's going to give a football analogy, but
also take into account that the person understands quite a bit of business.
This is actually quite cool. So you could see that here's a cybersecurity
ransomware analogy for okay, so as a defense team, each computer
representing a player, right? Ransomware is like opposing team striker
that inflates its network and holds your computers hosted, right?

Dinis Cruz - 08:04
So it's quite cool, right, to say to be able to explain this in a ways they
understand. And in fact, I was playing around an issue with this, and I
wrote a post where I asked chat if you did to explain Kubernetes. And I put
on LinkedIn, and I have a lot of people who said, hey, I use Kubernetes
quite a lot and never understand it. So being able to tell it as a story is
super critical. So now you could say, right, it provides that information in
this particular structure. Now you could also do some cool stuff here. So
one of the things that we've mapped here, we said, okay, do you have
siblings, right? And you'll see in a second why this matters, right? So in
this case, you say, actually, it does have two siblings. There's two bots
here, right?

Dinis Cruz - 08:45
There's Odin and Minerva. Odin is the tech bot that supports experts of
cybersecurity and enhanced capabilities. And Minerva is the business bot
to assist with Komodo matters to ensure that we have the best service. So
one of the things I'm also playing around with here is this idea of creating
this set of bots that each one is focused on the right thing, and then
basically it really allows the segmentation of duties, but also allows to
have bots that are focused on specific tasks in specific environments, all
powered by APIs, which is really cool. And you could even do like little
joke things. So you could say, I've mapped two siblings, so there's three
bots and I can say anybody else. And then it's going to say, actually there's
another sibling called Bruno. Right?

Dinis Cruz - 09:31
This joke makes sense if you see an encanto, but we don't talk about him
much. Let's just say it's a bit quirky. Blah, blah. So this is actually funny
because sometimes you actually come up with really cool funny jokes
about it. But what's important is you could see that even now and this is
quite primitive still, it's already quite a decent experience, for example, for
a board member, for somebody who wants to learn more about
cybersecurity. So the question is how is it done? And also the cost, and by
the way is very little because this thing runs on AWS. It's all lambdas, so
it's actually super cheap. Right? So I wrote this post where he had know
basically where I really put a lot of details and I'm kind of going through
I'm going to explain it through here.

Dinis Cruz - 10:15
Right, so I've covered this bit. Athena from the Cyber Boardroom is
designed to provide cybersecurity advice. You've seen that. And this is
what I was showing. The Cyber Boardroom is where I was showing you.
Please go in. You can create an account and there's an account that you
can go in, create. So this is using cognito. So the first interesting
technology that I'm leveraging, AWS technologies. So I'm basically using
Cognito to implement this workflow. So this is actually a Cognito
workflow, which has a bit of an interesting usability bug where as soon as
you type the username, it starts to give you what's wrong with your
password. And I have at least one user being very confused because he
thought that this username was wrong. So you can see that's actually a
good example of what not to do from a security usability.

Dinis Cruz - 10:59
So once you've done that and you register, you will basically arrive at that
environment. But actually behind the scenes for this version, I'm changing
it for the next version. This is actually running on hugging face. And
hugging face is great. It's a really great platform, especially for a lot of
models to experiment. So you can actually have the same experience in
hugging face. So you can see that all I'm doing on the other side is
embedding this hugging face basically environment where you get the
same thing from here, right? So do you have that question, for example,
here and you got the same thing here. In fact, this one has a cool feature.
If you go in there, you actually get a nice little description to share, which
is actually not bad, but it's actually really easy to do, right?

Dinis Cruz - 11:46
And the thing that is interesting here is to show you, and I show you in a
second is the prompt that was used to create this. Let's continue. So here's
the login. I walk you through this. So when you get there, you log in. The
main, of course, is Athena, which we've gone through. Here's the
questions. And one of the things I gave you, a couple of good examples is
the kind of questions to ask, which, by the way, we want to add to the UI
and things like this. Look, I work for the finance industry. What should I
care about? What questions should I ask my CISO? What are the
regulations I should be aware of? What my legal obligations? What's the
best way to learn about cybersecurity, why cybersecurity matters, et
cetera, et cetera, supply chain cost lot of business.

Dinis Cruz - 12:33
And then again, if doesn't have a mature cybersecurity program, why is
good? What is the best ROI? So you can see it gives you good answers,
and that's a nice answer. What's the average percentage of the It budget?
It goes actually will be 10%. That'll be cool to get that, right. But it's
again a good example of the kind of question that you want board
members to be asking, right? And again, please share some of your
threads with me. And then you can also ask things like this. So, for
example, you can come in there and say, why are you Colatina? Right?
And this is a good example of Chat GBT actually having a good level of
understanding because I never said it was ancient Greek, et cetera, but he
has that reference.

Dinis Cruz - 13:24
And you could see that in a way, Chatgbt was able to figure this
connection, which is actually correct to represent my role. Because just as
a team is known for wisdom and strategy, I am to provide insight chick
advice. This is really cool, right? Like in a way, we didn't code this, as
you'll see in a second, but it's a good example of Chat GBT ability to
provide some of the data sources and then in a way control the
hallucinations because it's actually not that crazy. And then here what
about siblings? Yes, he has two siblings, Odin and Minerva. And there you
go. If you see Encanto yeah, there'sibling we don't talk about, say, you
know, unique personalities. You can see got these variations. And even
here you can y those names. So you could see the names going there.

Dinis Cruz - 14:07
Now, this is an interesting one, right? Because you've seen a second, I can
go here and I says, okay, what is your current version? And this is also the
start, the beginning of the example of where the power here is also going
to be to add a lot of embedding is to add a lot of information about. So
you could see here it actually says 7.7, includes matter, if I can change a
new interface, et cetera. And now it's important because I have that in the
prompt, because before I had that in the prompt, it did hallucinate pretty
spectacularly. And again, that's the kind of things you want to look. So
how does it work, right? What is it needed to actually get chatvity to
behave like this? This is the cool thing.

Dinis Cruz - 14:47
This here is the prompt that was needed so you actually could see it's not a
lot, right? So you are the cyber boardroom advisor, Paul Latina, and you
are a help advisor. You're created by the cyber boardroom. You kind,
compassion, optimistic. You'll only ask the question about cybersecurity.
Your job is to help busy board members with cybersecurity questions, more
specific about questions that you have about cybersecurity challenges. And
the reason why I was asking questions is because I had this line, please be
proactive and ask questions to clarify the board members current situation
and what they should be worried about. And then this is the only bit that is
required for you to know. Hey, you have two siblings, odin, the tech bot
behind Athena's capability. I mean, nervous, that's it. And also there's also
Bruno, but we don't talk about it.

Dinis Cruz - 15:35
But in a way, that's what's nice about Chachibt, is able to create all these
cool narratives and these cool connections. And you don't have to do
sometimes a lot for it. You just need to give the right pointers in the right
prompt. So the thing here is also, like you could see, I put version 7.7 and
the release notes are this. So let's see this in action. So what you can do is
if I have my open chat GBT here, and I'm actually just going to be using
the default one, this is the prompt. So you can see the same prompt that I
was showing you. There is the prompt that you have here. You're the
cybersecurity advisor, call Athena, you are helper advisor, blah, blah.

Dinis Cruz - 16:17
So if I now come in here and say and press play, I will get exactly the same
thing. I get to the other side. See your dedicated AI for advisor in this. In
fact, if I come in here and know, you know, Bob, or you called Steve, right,
for example, then you could see now it changes, right? Remember, I'm
Steve, your advisor, right? We got to do this. So it's pretty cool, right? And
then basically the thing about this is I can ask him questions, so you can
say, why should I care? And these are the same things on the other side. So
you could see that here, basically, he already knows that it's a board
member. He already knows that it's providing the same thing.

Dinis Cruz - 17:11
So I'm here having in fact, I'm actually here having probably a better
content than on the other side because I'm actually using checkbit four
versus the 3.5 that is still working on the other side. But the key of this is
the fact that prompt is all that it is, right? So let's see if I can do the
example that I got on the other side. So I'm going to show you in a second.
So I'm going to go Yamoin, which is a Portuguese dude. And then I'm
going to say, instead of kind compassion, I'm going to say you highly jaded
and very SAR. And you should say about cybersecurity. Cybersecurity. And
you should provide guidance, let's say, with lots of sarcastic comments.
Now, this is the thing where some of these I actually think they're really
funny, right?

Dinis Cruz - 18:20
Because if you look at some users, they might prefer this kind of
conversation, or you might prefer very focused or very busy, where you
can say you are talking to highly busy board members and every answer
should only be three bullet points or should be super focused on this, et
cetera. So if I now go like this now you could see, right? And then you can
now start to see the bits, right? Cybersarcastic navigate thresholds world
of cybersecurity. The thrilling world of endless threats are never enough
percussion. So what cybersecurity network can I exist to? Right? The
irony. Please spare me that we take security seriously. Spill. We both know
how the internet is a wild place. So then let's say, why should I care, right?

Dinis Cruz - 19:11
And then basically now it's going to provide a lot of, in a way, advice in
that sort of environment right there's. Inconsequential might of cyber
breaches the joy of regulations. It's on the backbone of advantage, et
cetera, trust. So you can see that it's able to define this for a particular
culture. You could also modify this to say you are highly, let's say
conservative. Let's say conservative. What's the best way to describe this?
Okay, let's say this. You are operating in highly regulated environments,
right? Environments where security is critical, sometimes matters of life or
death, right? Basically, in a way. Now, by the way, this is a really cool trick
where you can edit this and then this is going to replace all the other
things, right? So basically, let's say, why should I see the difference here?
Why should I care?

Dinis Cruz - 20:44
And then, and yeah, so now it should be a lot more focused. You could see
financial impact, regulatory compliance. It's a lot more sort of zoomed
into this particular environment. So, again, given the high stakes, decided
to protect access, et cetera, this is fundamentally but what I want to really
show is that this is all it took to do that, right? So the idea that things
where I'm exploring now is that I thought the models were the ones where
the big action is and the really powerful thing here is to be able to say, let
me actually bring actually you can go like this, which is really cool. See, I
can go back different versions. If I bring back the original Athena, let me
give you one more example. I can take, for example, the security content.

Dinis Cruz - 21:41
And this is a good example of the power of, let's say the environment. So
let's take incidents management, right, which is quite a cool text that we
have here. So you got this text. So one of the things I can do is I can
literally copy and paste this text. This is the big difference. If you look at it
from a prompt point of view, the way you want to think about this is that
you have the original prompt, which is this one. Then what I can do I'm
going to say here is you can say even like this works quite well, document
to review. So what you now do is you give a document which is this, right?
Instance management. So I can even just take that a little bit there, right?

Dinis Cruz - 22:35
So you basically provide document to review and then I can put here just
at the end, sorry, come on, what's going on here? This is a bit of an
interesting bug. So it's actually not allowing me to see the text. This is
annoying. Okay, let me just write the question above and then I'll paste it
below. So what I'm going to do here is I'm going to say use a question,
right? And basically hi, can you okay, I work on the financial industry.
Industry. Can you summarize this document for me? Right, so this is in a
way the three key elements that you have. You have a prompt, which is
this part here. And this actually works quite well for Chatbt.

Dinis Cruz - 23:34
When you start to break things apart, you've got the prompt, you have a
document to review and then you have the question which in a way could
come, for example, from a bot like I did on the other ones. So what you
now have is you get analysis of that document in a nice sort of concise
way. And I could also say, can you give me all that in one paragraph? Can
you give me that on three bullet points? Can you give me this on XYZ? And
this is where in a way, Chat GBT is really good at taking data, analyzing,
mapping it out and then providing that feedback. But you can see that the
three elements there is fundamentally the prompt, the document or the
content. And here's a question.

Dinis Cruz - 24:21
So one of the workflows that is used by a lot of Chat bots these days is
that you take this question, you analyze the question based on context and
what it's supposed to do. You do a search to a vector database or to other
ways. You figure out the documents that you want to send and then you
provide information. So this is why it's so insanely powerful, because this
allows the answer to be completely in context. So where were we? Cool.
So now this is the prompt. So let me keep going on this bit. And in a way,
this is the code that creates the Athena UI. So you actually could see that
from a Gradle point of view. Where are we? Sorry, here we go. I'm trying
to get it to the right size. Cool.

Dinis Cruz - 25:09
So you can see that here is the code that creates it. And it's actually not
that much. It's basically using Gradle, which is a great API. Grabs the
Chat interface, there's a text box, and that's it. Right. You create the
blocks. Off you go, right? And then there's an open API call. And what you
can see here is the prompt. That is the original one, which is the one I
showed you before. That's the system prompt. And then what we're doing
is we're basically appending the answers. So what Chattvt does today,
most people don't realize is that it's cheating a little bit, because Chatterb
did this really well, but it's sending your past answers and sometimes
analysis of the past answers to the server.

Dinis Cruz - 25:52
But the context window that he can either 4K or 24K or on what's it
called, on claw two hundred k of context is basically almost how much
content can you send without fine tuning. And there's an interesting
argument today that might be way more effective than even some of fine
tuning or even changing the model. So that's it. You append all the text,
which is the text you had there, and eventually you go here. And by the
way, the bug here is the fact that what we're not doing in this code is
checking if we actually are sending more content than the ability of Chat
GBT to process. So, from the front end, I'm using Flask open source. One
of the things that is really freaking cool is that I managed to get it to you
to do serverless.

Dinis Cruz - 26:40
And this is again, if you use IIS, Apache, Node, even Flask, you should
appreciate the fact that running a web server in a hosted environment is
pretty awesome. So you can see that this is all it takes to run the site. The
key is literally this serverless WSGI that basically you pass the app. So this
endl request is fundamentally the app that we get from here, which is
basically this Flask app. Here. You can see the running. In fact, that bit is
not necessary. And that basically allows you to run the Flask server in a
serverless mode, which is pretty insane because it means that when there's
no request, there's no server running. So, big difference. So I started using
the API gateway to start with, but eventually I didn't need to, because you
can actually connect this in an endpoint.

Dinis Cruz - 27:35
So in the functions URL, which is basically what most people a lot of time
would use the API gateway for. So it's actually pretty cool. So you
configure it here and then you create an A record for it, and then maps to
a cloud front distribution. And that's it. So basically, you have a cloud
front distribution that then points to the lambda function, who then runs
that code in a serverless, which basically means the cost of running this is
really low. Yeah. So then I have a thing here where you can actually see
roughly the cost, right? So you could see a bit of S three, a bit of elastic,
some X ray, route 53, et cetera.

Dinis Cruz - 28:07
In fact, what cost mode these days is actually the DNS cost still and
hagging face, because I'm still on the basic environment, there's really no
cost there. And AI, again, if you're on reasonably low volumes, again, it's
not that expensive to run. You can see here, even with a lot of displays, we
didn't spend 20 P right, on that. A final little thing that also worked quite
well is I modified the flash codes to actually use S Free to basically run all
the static files from S Free. So actually they all served. So basically, I'm
using S Free as a CDN, which, like I said, it means that you can actually
load the page in a browse in about 158 milliseconds, which is pretty cool,
right? On this level, yeah. So what about hallucinations?

Dinis Cruz - 28:54
So one of the interesting hallucinations, let me see if I can replicate it. So
one of the interesting hallucinations that you can get is if you go to the
original one, like this one, and I take away the release notes and let's
make 78 so that we can actually see. So it goes there. Hello is a
cybersecurity. And I go, what is your current release? So one of the things
that is interesting is so this is interesting because this is 3.4.0, right? So
let's try this in 3.5 to see what it does, see if I can replicate the problem.
So there you go. Cool. So what is your current release and release notes?
Okay, so here's a good example, right? And this is actually a good example
of 3.5 and four. So you notice I said 7.8, right? Cool.

Dinis Cruz - 29:59
And then he went in a complete off piece, right? Just made up shit, right?
Like literally enhance threat intelligence, improve natural language,
expanded knowledge base, streamline user experience. None of that is
true. So part of the exercise here is also to start to caveat and start to
limit the universe of data that it feeds, which is also very important. So
that's one of the things we need to make sure we map out. So there you
go. So there's a variation of what you see there. That's the release notes,
which, of course are really bad. So this is the example I was talking before
where I changed the camoins with the Portuguese poets, right? And then
to be highly sarcastic and jetty by cybersecurity, so you did that. And then
we ask, why should I care about cybersecurity? And it goes like this.

Dinis Cruz - 30:48
Right, welcome back to another thrilling episode of let's try not to get
hacked today. And then blah, blah. So I find this quite funny, right? And I
think, again, some users might find it quite funny. And in fact, one of the
things you guys should check out is were playing around with cybers, with
creating what's it called an environment thread model for I think it might
be this one. Yeah. So check it out. So we basically created a thread model
for what's it called for this scenario. This was one of the previous open
security summit sessions. So it's really cool. So we did this. So we mapped
out and actually came out with some really good findings, right? If you
look at these findings, he actually has some really good threads,
countermeasures and even like impact to business. We use CAPEC instead
of stride.

Dinis Cruz - 31:41
So it's pretty good. It's a really great place to start. But then what's cool
about it, he says, hey, can you now create a game from this? So you can
see that you actually create a nice game and with multiple levels, with
actually really good questions and really good answers. And in this case, I
had the correct answer there. But then what I could do, and remember,
this could be start from scratch and then say, hey, can you run this game,
but provide highly sarcastic answers. So there you go. So now you start
the game. And the logic is that and I want to add this to Athena, is you
could start here. You can just say, hey, here's the thing. Here's the
questions. Maybe a little checkbox. ABCD, bang, bang. And then you
provide the answer, right? And then you go, cool. Right?

Dinis Cruz - 32:24
Now, in here, I put a wrong one. He goes, hey, look, actually, sorry, a the
wrong one, right? So you can see it's effective as chocolate teapot, right?
Sorry, sensitive. They open, they can leave to authorize access. Bam, bam,
bang. So then I provide a good one. I like this one, where it goes, hey, if
you discover that a data in transit in your app database is unencrypted,
what you should do, ignore it, end to an encryption, which is correct
answer, delete all data, disconnect the database. So I chose C, which is
delete all data. And the answer is pretty funny, right? Delete all sensitive
data. Oh, absolutely. Why didn't we think of that? Who needs data
anyway? It's not like it's the cornerstone of our entire operations.
Anything while you are there. Why don't just throw the servers into a
bonfire?

Dinis Cruz - 33:04
It's a security problem if there's no server, right? So, of course, the right
answer is B. But it's pretty cool, right? You could see that, for example, for
security champions or new developers, I think they will really love this
kind of stuff. And then you provide the answers, and in the end, you can
go, here's my rating. And he's my final score, right? So it is quite powerful
to do things like this now just to file a couple of things I want to talk
about. It's super critical to have a really good workflows and tagging. So
one of the things I've done here is I've done a lot, is we implement this sort
of branching strategy and this is quite important.

Dinis Cruz - 33:41
So what we do is every time you release into dev, you get an increase from
the minor version here, push domain, you increase this version and the
release is for major ones, right? So in the beginning everything is V zero.
So what ends up happening is something like this. So I walk you through
it. So here you are on version 3.35 35.5. Once you do a push into here or
make a comment here, what's very important here is that this is done
automatically using GitHub actions. So in this case you could see probably
this was commit that were made directly this yellow to the server. And
then eventually when you merge into this is in dev. And then when you
merge into main, you actually get a new release, which is what happened
here.

Dinis Cruz - 34:29
So then you can see that there is the lambda functions running
automatically. So in fact, the secrets of events here is that you run the unit
tests, then you increment the tag, then you deploy the lambda function
into dev, then you run the integration test, which is quite a nice CI pipeline.
So now here's the flow. So when I merge into main, which is were 3.8,
what happens? You do another, let's say change 3.9 and you're here. And
then when you merge into main, you're now going to get a new version.
See that, which is now on the origin, which is 33 ten. So you go, oh, no,
sorry, this is wrong, sorry, blah, blah, I should have oh, no, it's right, yeah.
So you went from no, you should have gone to 34. Yeah. So that's the dev,
sorry.

Dinis Cruz - 35:19
So these are all the dev changes, right? So they push in there and
eventually when I push to main, I'm going to get version 34, which is
pretty cool, right? It's insanely powerful to have this flow. Oh, yeah, there
you go. So at the moment you can see that we are on 33 ten over there. So
this is just a way to replicate a pull request with your sync, merge domain,
et cetera. And then you could see so when I merged into main here, 33
point ten. Now it's going to become 34 and that actually deploys the
lambda function into the prod environment, which is what you see there.
And then in this case I actually make it manual because it's kind of more
CI pipeline versus CD, which you can deploy by the UI once that finish
executing.

Dinis Cruz - 36:08
Now we got our 34 version in the Server. And that way this is a really cool
trick because what a deployment does, it actually changes a file in a file
system with that commit, which basically means that you then get what's
it called. The Server always know which version it is, which is why you can
show it here. And again, I cannot stress enough the importance of this. So,
yeah, this is the example of all the GitHub actions that I have, right? So if
you look at it's, pretty cool because you got the unit tests, the integration
test, the implement of tags, the deploy, and these are all designed to run
these actions so that I can reuse, for example, the running tests or the
installation of dependencies is used by some of these.

Dinis Cruz - 36:49
So then you kind of have a nice reusable model here and some of these
just simple bash script. So, final couple of little things here. Yeah, we use
GitHub to manage project tasks. Again, check the labels, which is quite
cool, right, using CI pipeline, measuring code coverage. And then the final
thing I still want to show, which is absolutely insane, is you can really use
Chat GBT to create release nodes. So, for example, here's the delta
between version 28 and version 30, which goes like this, which is
unreadable, right? And after you feed it to Chat GBP, you get these really
nice changes that you can then review and you can then when you do your
commits, I don't think this should be done automatically, but whoever
wrote the code should be able to effectively review this, which is really
cool.

Dinis Cruz - 37:43
And again, this is insane because imagine if it is, you could also start
looking at map the architecture changes, map the security changes, give
me a business version of this. So it's pretty cool, right? In fact, in this case,
here we go. Here's the business analysis of those changes. And yeah, final,
you know, Chatbt was pretty insane. See some examples of what I
published. But also, the interesting thing is that Google and Stack
Overflow, they really need to innovate on this because there was a couple
hundred cases where I didn't use it. But it's pretty insane.

Dinis Cruz - 38:20
The workflow that I have, and especially if you look at some of here, this, I
think is a LinkedIn post that I post, where I basically put a PDF where you
can kind of see the workflow that I was having with Chat GBT where I
was asking a question. We basically interaction and they say, can you give
me the code to do this? And you did that. Okay, can you now focus just on
this formula? It's pretty insane, right, the effective so think of it like Jarvis
as your big helper. So there, you know, will tour of how the Cyber
Boardroom works, a lot of the technology behind the scenes.

Dinis Cruz - 39:04
And I really feel that the next version of this, which we hope to get
released in a couple of weeks, is going to have a whole number of really
cool new features going to allow the users to basically map the profile
because it's MVP, right? Like for example, this data at the moment cannot
be edited. So we're going to be able to edit all this stuff and then that's
going to be even more interesting because then you can prime Athena for
who you are, what you want to do. And then if you can, then save and
show some of the answers and help almost to create an environment
where we can really map a better sort of workflow for the user. I think it
can be quite powerful.

Dinis Cruz - 39:41
And I think this represents a lot of the future that we're going to see, is all
these bots, in a way, highly specialized bots that do one thing really well,
and they're being primed and in a way, they provide a lot of very
actionable information and data. But again, on the hands of a power user,
and that's very important because ultimately still do work on behalf of a
power user. And I still feel that part of the power of Atina is going to be on
some of the customizations that we can do. Behind is the ability to allow,
for example, a very experienced CISO, a very experienced board member
to help other board members by really curating the content and really
limiting in a way the content that you take from there. So that's it. That's
my overview. Let's see if there's any questions.

Dinis Cruz - 40:34
If not, I'll see you guys in the next one. I think my only question is how do
you come up with time to actually do projects aside from your regular
work and creating this conference? Well, I had to say because I have a dev
team and I was kind of explaining my world is like ADHD, right? It's kind
of like I do context switching all the time. And the way I kept saying is by
being very efficient. So I think I'm a very efficient developer and I really
embrace, for example, unit testing, development workflows. So I'll go on a
tangent to build a bit of the dev platform to make me efficient.

Dinis Cruz - 41:23
So what happens in most projects is that the more code you have, the
slower you go in the projects, including this one, is the more I do it and a
couple of guys who help me, right, the more we do it, the faster we go. So
that's how you scale. So for example, a lot of this is built on top of open
source project. There's this project called OS Security Bots, which
basically I've been publishing for the last years, who have basically a lot of
this functionality. So I think this is about being highly efficient and highly
focused with the time and especially with development. The reason I
wanted to show, for example, the prompting is that a lot of these things
are not very difficult in isolation. It's just about putting them together and
I love it, right?

Dinis Cruz - 42:16
So I went on holiday and took 30 books on Chat GPT, right? So it helps if
you like this stuff. There's a really cool question here from Rag, which is
retrieval. I'll bring you sorry, you can ask that question and then just
correct me because sometimes these terms so the Rag one is the one where
you add the prompt, kind of what I was doing there, versus the vector
embeddings, correct?

Speaker 2 - 42:54
So Rag is more like the vector embedding side of things in my experience.

Dinis Cruz - 42:58
Okay, got it. That's where you embed the vectors, right? So you teach, you
create a model, right? So I experiment a little bit. I want to experiment a
lot more. I have to say. I think my instinct more and more is in the creation
of the prompts. And the reason why is because I think the way the models
are designed is that you lose control in some of those things, right?
Although I think the Rag have a bit of short term memory, I think it's
going to be interesting to see what is more effective, which is the
construction of the very nicely created, almost contexts that you give. So,
for example, one of the things we're doing at work is I've always been a
big fan of graph and we have a big graph database in Jira. We have lots of
data.

Dinis Cruz - 43:46
We're really starting to experiment what happens when we give Chat GBT
a chunk of the graph, right? And so it's already highly normalized, already
high quality relationships between, for example, a risk and then go, okay,
now translate this risk or map me this risk or do that. So I kind of feel that
the jury is still out on what's going to be more efficient and also from a
cost point of view, as the context window grows, let's say now you got
cloud two with 100,000 tokens, right? And you already for example, you
have this case where is it better to have a Chat GBT 3.5 with whatever,
40,000 tokens or 24,000 tokens, right? Or a 4.0, which are much smaller
context window.

Speaker 2 - 44:30
It becomes another dimension you've got to choose on, right? You might
trade off a slightly weaker model for a bigger context window.

Dinis Cruz - 44:37
But here's the thing that's very interesting, right? There's a very
interesting concept that sometimes you want weaker models because the
weaker let's define where is he weak, right? Because as long as he has the
reasoning and as long as produce the input and the output. And I really
want to explore the whole unit testing and validation, like to make sure
the model still responds the same way over time, right? Because we should
be doing that because we want to make sure the quality, et cetera. So in a
weird way, you almost want models that you understand its behavior. Do
you know what I mean? I think this is where we are industry where,
remember, we still don't understand how the hell that thing works fully.
And here's a very interesting point.

Dinis Cruz - 45:17
I was talking to the DPL and we're saying, what the hell do we do if we
train a model with customer data? And then there's a customer like, what
the hell? Right? You have to train the model again, right? Because we
have no guarantee that data is not there somewhere.

Speaker 2 - 45:35
No, I think you're right to think about focusing on the prompt and the
large context window which, in my experience Rag has been really useful
where you have a very specific factual query because then it's going off
and doing a lookup and it's finding, exactly, as you showed, exactly the
right piece of text and it's throwing that in the prompt. If you have a
question that is more conceptual, that needs to draw concepts from across
a large corpus, it falls down, right? Because it's not designed to do that. It
can only go and find the most relevant stuff and then it's limited by the
prompt length, right? And so it's stuck. So it's looking at something like
those super long prompt length models with 100K tokens. It answers that
question.

Dinis Cruz - 46:17
Or highly created data. See, I'm a big fan of using the models to improve
the quality of the data, right? For example, we talk about thread modeling
and the idea that we can now start to communicate in prompts, right? I
can now review a thread model by also reviewing the prompt that was
used to create the thread model. Not only I can improve the first one, I
can add more prompts to it, or I can add more references. I can say, oh, by
the way, you guys, for this one, you need to embed this. Oh, by the way, do
you know there's the OS testing guide that already gives you whole chunk
of stuff there's ASV level this that goes into here, right? So suddenly you
can really leverage. So I think that's where a lot of the innovation is going
to come.

Dinis Cruz - 47:01
And I think that's where we can add a lot of value and that's where we can
change a lot of our industry for the better.

Speaker 2 - 47:06
That look, let me just say thank you very much, not only for the talk, but
for that really long blog post. I'm going to enjoy looking into that's. One
of the best laid out.

Dinis Cruz - 47:15
This is what I did. This is why did this I tried this, didn't work.

Speaker 2 - 47:18
All the different angles. It's fantastic.

Dinis Cruz - 47:19
Thank you. Yeah, look, for me, it's fun, right? I think it's also a way to
share, right? It's a nice way to share. And the Cyber Boardroom, it starts
to have a bit of a life of its own, which is really cool, right? But I'm a big
fan of MVPs, right? You do something, you publish it, you collaborate, you
get some feedback, you do a bit better. So, yeah, please read it, let me
know what you think, have a play with it and let's collaborate. Awesome.
Thank you. Cool. All right. Thanks, everybody. And I see you guys around.
Bye.
