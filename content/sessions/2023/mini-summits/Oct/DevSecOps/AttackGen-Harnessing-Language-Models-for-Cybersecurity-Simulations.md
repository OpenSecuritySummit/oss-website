---
title        : "AttackGen: Harnessing Language Models for Cybersecurity Simulations"
track        : DevSecOps
project      : DevSecOps
type         : working-session
topics       :
featured     :
event        : mini-summit
when_year    : 2023
when_month   : Oct
when_day     : Mon
when_time    : WS-18-19
hey_summit   : https://www.linkedin.com/events/7117866669871382529
banner       : https://github.com/OpenSecuritySummit/oss-website/blob/main/content/sessions/2023/mini-summits/Oct/banners/attack%20gen.png?raw=true
session_slack:
#status      : 
description  :
organizers   :
    - Matthew Adams       
youtube_link : https://youtu.be/B4kLg0FaUKA
zoom_link    : https://us06web.zoom.us/j/85889254932
---

## About this session
In an era where cyber threats evolve at an unprecedented pace, traditional methods of incident response testing often fall short. This presentation introduces "AttackGen", a groundbreaking tool that seamlessly integrates the MITRE ATT&CK framework with state-of-the-art Large Language Models (LLMs). Attendees will be taken on a journey from a live demonstration of AttackGen's capabilities to a deeper exploration of its mechanics. The talk will culminate with a broader discussion on the transformative potential of LLMs in cybersecurity, exploring how they can be harnessed for tasks ranging from threat intelligence to code scanning.

### Publication:
AttackGen announcement post - https://www.linkedin.com/feed/update/urn:li:activity:7099276471826817025/

Previous OWASP talk on use cases for LLMs in cybersecurity - https://www.youtube.com/watch?v=4cP-Z1iyNyY

## Transcript:
Matthew Adams - 00:00
You.

Dinis Cruz - 00:02
Hi, welcome to the last session of Monday on the Open Security Summit
session in October 2023. And we have Matt Adams, who I'm going to kick
start one of our a lot of our sessions we have dedicated to LLMs and this
is going to be on the Attack Gen, which is a really cool tool and
technology he's been working on how to actually start creating
simulations. And I'll just mention it I think is the kind of tool and the kind
of use of LLMs that I think is super useful and we can add a lot of value
these moments with the LLMs that we have. So Matt, over to you.

Matthew Adams - 00:38
Thanks very much and good afternoon. Good evening. Good morning
everyone. Thanks for joining wherever you happen to be watching. So, just
to introduce myself, my name is Matt Adams. I'm a security architect at
Santander UK. I've worked in cybersecurity for almost 20 years. So I
started out as a big four consultant with one of the big cybersecurity
practices. I then became an independent contractor working across
government and financial services sectors. And then in recent years, I've
taken up permanent security architecture roles with Costcoffee, part of
the Coca Cola Group, and latterly with Santander. And when I'm not at
work, I've got a few quite varied hobbies. So I live on a small holding in
the North Buckinghamshire countryside in England, which is where I'm
joining you from this evening.

Matthew Adams - 01:42
And when I'm not out in the fields looking after sheep and chickens, I've
got my own home lab. And I enjoy coding my own projects, which is where
a lot of this experimentation with large language models has come from,
really? As I've looked for ways to take problems that I come across in my
day job and in my personal life and look to see how I can apply those
models to make myself and my colleagues and others more efficient and
more productive. So our agenda for the talk, just going to try and bring
everybody up to speed on what I think is the current position with incident
response testing. We'll then take a dive into the architecture and building
blocks of this tool that I've developed called Attack Gen. I'll then give you
a couple of demos of the tool we'll look at.

Matthew Adams - 02:37
The well roadmap is perhaps slightly too grand the term, but the next
things that I'm thinking of for building on version 0.2 of the tool that's
there at the moment and then I'll wrap up with some of my thoughts on
how do you ideate use cases for language models and what are some of
what I would consider to be the best practices when it comes to
implementing these types of tools in an organization? And if we got some
time, I'm happy to take questions at the end. So, incident response testing
for me, again, I'm a security architect. This isn't my sort of day in and day
out job. But I have participated and run incident response exercises in the
past. For me, incident response is a skill.

Matthew Adams - 03:37
And like any skill, the more you practice, the more you refine, the better
you're going to be at it. And so you'll see that those teams that exercise
more and have more practical experience of live responses are
understandably, more efficient and better at responding when it. So I
really like the following quote from Alan Iverson who has nothing to do
with cybersecurity or incident response. He's a former NBA basketball
player. But I like it because it captures a couple of different aspects of
incident response testing. And his thought is that when you're not
practicing, someone else is getting better. And I think of this from two
perspectives. One, this could be your competitors, other organizations who
are hardening their defenses, getting better at mitigating attacks sooner
within the lifecycle of an attack. But it also applies to the bad guys, to our
adversaries.

Matthew Adams - 04:41
They're constantly improving and trying out new attack techniques. And
so it's important that we continue to practice, we continue to improve our
own games when it comes to incident response. And for organizations that
are testing and exercising at the moment, they are taking account of this
increasing complexity. But it is becoming challenging to capture within an
incident response scenario. So what you'll see is that leading
organizations have moved to quite complex and threat driven testing
scenarios. So probably one of the best cases or best examples of this is the
Cvest scheme that's sponsored by the bank of England here in the UK. And
that takes threat intelligence from leading threat intelligence companies.

Matthew Adams - 05:41
It combines that with assessments from intelligence services and other
very advanced threat intelligence sources and they then use that to
produce a realistic testing scenario based on an adversary or adversaries
that they wish to simulate during that exercise. Clearly that's not
achievable for all companies. And those companies that aren't large
financial services institutions or critical national infrastructure, they're not
really able to replicate both the specificity of those scenarios or also the
complexity simply because they lack the time and financial resources to
achieve that same depth of testing. So what we kind of see at the moment
then is in more generic incident response scenarios being used by smaller
organizations. And the reason why I'm not a particular fan of those is
because they don't really account for the organizational context that is
relevant to those particular companies.

Matthew Adams - 06:57
And it may be that you're picking up a very standard phishing based
incident response test, but you may have really good email fences and
actually you get quite few phishing attacks that hit end users and you'd
better testing something that was more relevant to your organization. If
you did want to develop more tailored and specific scenarios, well, that
tends to come with a longer lead time and cost to produce those scenarios.
So some of the testing and exercising that I've been involved in the past.
I've spent sort of end to end, maybe three, four months working with a
consultancy to go from the sort of inception of an idea for a scenario that
we want to test all the way through to developing that.

Matthew Adams - 07:51
Scenario, creating new injects and content to put into that exercise and
then finally getting people round the table to go through and exercise that
properly because of that lead time. My experience is that there's a bias
towards larger scale tests with the side effect that tests tend to become
less frequent. So you might have scope to do one of those a year, which I
think is less than ideal, and more teams would benefit from being able to
focus on doing smaller tests more frequently to supplement those large
scale tests. And that was really where the idea for Attack Gen came from.
And what Attack Gen is it's a combination of the Mitra Attack framework.
So the data from the Mitra Attack framework combined with an OpenAI
LLM, so in this case GPT 3.5 Turbo.

Matthew Adams - 09:04
And I'm also then using a framework called Lang Chain, which is I think
quite a few people are aware of it now, but it's a framework for working
with language models like the GPT series. And it just makes it easier to
handle some of the prompt formatting. And that's really where I'm using it
for in this tool. And lastly, there's a simple but fairly effective UI delivered
through Streamlit, which is a Python library, which I use for quite a few of
my POC tools.

Dinis Cruz - 09:42
Matt, can I ask you a question? Have you experimented with Four or with
Cloud Two or Lama Two, the other sort of GPT models?

Matthew Adams - 09:52
I have, yeah. When you're using different models though, and Langchain
does try to compensate for this because the models have been trained and
fine tuned on different data sets and different prompt structures. The way
that Claude, for example, will deal with a user and AI response that
prefers, I think, XML, it does really well with sort of XML structured
documents and you've got quite a particular structure that you need to
give it to get the best out of the prompts. Whereas OpenAI is a bit more
transparent, you don't have to have as much work going into telling it.
This is the user section, this is the assistant section.

Matthew Adams - 10:50
And so trying to switch between, for example, GPT 3.5 and Claw Two in
this tool, I have tried to do it, there's quite a lot of work that needs to go
into reengineering the prompts to get consistent results. And so for the
time being, I've left it just as OpenAI only tool at the moment.

Dinis Cruz - 11:12
What about GPT Four?

Matthew Adams - 11:15
So GPT Four would do a really good job because of the length of the
responses. I favor 3.5 Turbo just because it's quicker and because of
things that you'll see later on in the presentation, I can work with the
slightly less capable model and still get, I think, good results from it.

Dinis Cruz - 11:39
Yeah, that was going to be my next question because I found also that 3.5
can actually be really good. And there's an interesting trend here which
sometimes we don't need very powerful models if we can prompt it quite
effectively, isn't it?

Matthew Adams - 11:51
Yeah, absolutely. I think there's a lot you can do with fine tuning and
prompt engineering to get really good results from 3.5.

Dinis Cruz - 12:00
Brilliant.

Matthew Adams - 12:05
So just to check that we're all on the same page when it comes to Mitre
Attack, because that's a fairly key part of this tool. Attack is a knowledge
base of adversary tactics and techniques. And the key to it is that it's
based on real world observations from security analysts around the world
where they're monitoring different threat actor groups and they see these
different behaviors and techniques used by them. Attack is a really good
way of cataloging those observations and then subsequently using them to
develop threat models that we can use downstream. And probably the
most important feature, I think, of Attack is that it gives us a standardized
framework to be able to understand and communicate threats.

Matthew Adams - 12:53
So that I know if I'm in a security architecture team and I'm talking to a
problem that's been detected by our incident responders, when we say
lateral movement, we're both talking about the same technique that was
used to move laterally from host to host. And so it takes away a lot of the
potential for confusion that could otherwise result. And so what you can
see in the image here at the bottom is a heat map that's produced by a
tool called Attack Navigator. And this is a mapping of some different
techniques that are used by two different threat actor groups. So apt three
and apt 29. And you can sort of see the power of being able to map on
those different techniques because it tells you where you should probably
focus your efforts in terms of defending against them.

Dinis Cruz - 13:50
Have you tried reverse engineering an attack into the Mitre framework?
So you basically say, here's my Attack, here's a scenario, now give me this
path.

Matthew Adams - 14:05
Remind me about that when we come to Hallucinations, because yes was
an example I wanted to give. So if Attack is that good, and I'm sure lots of
you have heard many things about the Attack framework, why do you
need a tool like Attack Gen in addition to it? In my experience, there's
quite a learning curve to Attack. So people get the concept very quickly of
the knowledge base and being able to have a common language for
discussing different techniques and threat actor groups. But when you get
down and use it at a practical level, you quickly come across these long
lists of techniques that are associated with each threat actor group.

Matthew Adams - 14:57
And that, in my experience, is where people sort of tend to get a bit
bogged down because trying to get those then into something that's useful
beyond just the basic understanding that Threat Actor group uses
technique A, B and C, actually getting something of value out of that is a
bit more difficult. And it takes time to learn how to use Attack Navigator,
how to create different layers, all of those sorts of things. And what Attack
Gen does is it tries to flatten that learning curve and reduce the time for
people to get value from the attack framework.

Matthew Adams - 15:42
So what you'll see is that we can quickly select a specific Threat Actor
group and then within a minute or two create a realistic testing scenario
that we could give to our security management or our Incident response
function and ask them to build a response exercise around that. And then
there's a bit of an overview of how Attack Gen works. And you'll see this
in the demo in a few minutes. But first off, we just asked the user to
provide an API key for OpenAI and to provide some very high level
information about their chosen industry and the size of their organization.
And that's just to provide a bit of additional context to the model.

Matthew Adams - 16:35
They then select whether they want to run a Threat group scenario, which
is the example we've just covered, which is you select a threat group and
you then get a list of associated attack techniques back from the tool,
which is then used to generate a scenario. Or recently in version 0.2 of the
tool, I introduced this feature of custom scenarios where really the idea
was that for organizations that have got quite advanced threat
intelligence capabilities, there may be threat actors that they're tracking
that aren't in the attack framework at the moment. And so they need a
way to select specific techniques and then build a scenario around those
particular techniques. Again, quite quickly, but quite realistically once the
data has been selected so those particular techniques have been pulled
from the attack framework, they then go into a Lang chain prompt
template.

Matthew Adams - 17:46
So as I've talked about, Langchain is that framework that we use for
working with LLMs and it then allows all of that context in terms of the
industry, company size, the relevant techniques, all to be passed to the
LLM in one go with a request that says you are an expert Cyber Incident
Responder. Please produce a scenario that incorporates all of this
information and context that we've provided. When that run occurs,
there's an option to log that to a tool called Langsmith. And I'll go into a
bit more detail about what that does in Slide or two. And I've also recently
introduced the ability for users to provide feedback on each generation.

Matthew Adams - 18:41
And that's really just something that I'm using to understand how well the
tool is performing and whether it's producing the desired scenarios or if
there's some issues that I need to delve into in a bit more detail. So this
seems like a lot of work. Right? So when you can ask Chat GPT to
produce an incident response testing scenario and it will produce
something like you see on the left hand side of the slide, why don't we just
use that? Well, as you can see, just stepping through this, I asked Chat
GPT to give me a scenario for Apt 41, also known as Wicked Panda, and I
tried to make the prompt that I submitted as close to the prompt templates
that Attackgen uses to make this a representative test.

Matthew Adams - 19:38
So you can see that we're passing in this information that it's a large
organization and that in this case it operates in the insurance industry.
And then Chat GPT starts to generate the Threat Actor profile and the
techniques associated with that Threat Actor group. And this is all looking
very credible, very reasonable as a means of explaining what this Threat
Actor is doing in their processes. So spear phishing attachments to gain
initial access, execution of PowerShell scripts, establishing persistence
through scheduled tasks, exploiting vulnerabilities to get privilege
escalation, all very credible. But when you go and map this back to the
actual listing for Apt 41 on the Mitreattack website, you'll find that several
of these are actually not relevant for this Threat Actor group, which is a
real problem if you're trying to produce realistic scenarios specifically for
a given Threat Actor group.

Matthew Adams - 20:48
So, as we can see, GPT 3.5 and even GPT Four will hallucinate the names
of techniques and most commonly the Attack IDs. It seems to really
struggle with matching the specific Attack IDs to the name of the
technique. Do get quite a number of variances there. So having mentioned
hallucinations, I thought it was probably apt to talk in a bit more detail
about what a hallucination is. Probably most people have heard about it
who've looked at LLMs and it's one of the key weaknesses of these
probabilistic models. And so I thought, well, what better option than to
ask Chat GPT what a hallucination is? And in the response it says that
they're a phenomenon where a machine learning model, particularly a
language model like GPT Four, produces outputs that seem plausible but
are actually incorrect or nonsensical.

Matthew Adams - 21:55
So exactly what we saw in the previous slide, and I think a really good
answer. What then caught me by surprise was then the hallucination that
it follows with by saying that an LLM stands for low level Mistake, which,
if you're not familiar with this space, again, you could find completely
credible and quite difficult to spot. But it sort of highlights that you
continue to need this subject matter expertise to know what you're looking
for or otherwise be prepared to be caught out when it comes to this type
of generation.

Dinis Cruz - 22:34
So that's a meta hallucination, right? Hallucination only explanation of
hallucinations.

Matthew Adams - 22:39
Yeah, I did wonder if I was being trolled by the model at that point. If it
just thought it would throw that in there. And that was the first question. I
didn't do this repeatedly. That was the first time I answered it. I thought it
was too good not to.

Dinis Cruz - 22:53
Yeah, that's definitely a keeper. I agree with Sarah.

Matthew Adams - 23:00
So to Dennis's question earlier about reverse engineering attacks, that
was one of the first ideas I had when I looked at the GPT models was the
idea that if you could take a news article or maybe just a very brief threat
intelligence bulletin that had been produced. Perhaps you could pass that
to a language model and say, identify all of the relevant attack techniques
in this article and give me the references for them, the attack IDs for them
according to the Mitreattack framework. And while again it looked very
credible, I soon found that when I started to check a number of these,
what you saw a couple of slides ago happened with great regularity in that
it just wouldn't nail the Attack IDs to the technique names.

Matthew Adams - 24:08
There was always some variation and so when I was coming to think
about Attack gen, I decided to take different approach and not rely on the
language model to produce that important mapping which is really critical
to the integrity of the scenarios. So there's a bit of a fairly complex
sequence diagram here, but the bit that we care about is in the first steps.
So after we've logged into the streamlit app and we've set things like the
API key and our industry and company size, the user then selects a threat
actor group. And at that point, I'm using a very useful Python library to
just load in the Mitreattack framework in its Stix data format stix. And it's
then filtered again using just a bit of Python.

Matthew Adams - 25:10
It filters out all of the relevant techniques for that selected Threat Actor
group and then it's returned back to the Streamlit UI at the point the user
clicks generate scenario. That's when the selection of those techniques and
their associated IDs is made from the application and then passed to the
model. So I'm not really giving it much of a chance to hallucinate those.
I'm not saying it's never going to do it, but by including those in the
human input prompt for the model, I found it to be very effective at
managing hallucinations. I've not come across an instance where I've sent
it list of techniques and Attack IDs and found that in the response the
model has hallucinated something different. So from my experience at
least, it looks to be very reliable.

Matthew Adams - 26:15
When were walking through the block diagram earlier, I did touch on
Langsmith and I wanted to include this because I think this topic of
observability and feedback capture from LLMs is going to be increasingly
important as we go from this phase when everybody's got incredibly
excited about language model applications and running various POCs. But
when you take them to production. And quite rightly so, we get increasing
challenge from stakeholders to say, can you explain to me how this model
works? And the models are probabilistic. You can only go so far, but I
think tools like Langsmith are very useful in at least providing some level
of visibility into the inner workings of the model. And so that's why I
wanted to include support for it with version zero two of Attack gen.

Matthew Adams - 27:16
And so it allows that greater level of monitoring and the ability to capture
user feedback as well. So you can see on the right here, we get visibility of
the system prompt that's being passed to the model as part of the
generation request. You can also then see all of the populated prompt
template that's then being given to the model. So that data, all of those
techniques that we filtered through for this particular threat actor group,
that is where those appear, and then they're submitted to the model as
part of that generation.

Dinis Cruz - 27:56
All this code is open source, right? This is all an open source project?

Matthew Adams - 28:00
Yeah.

Dinis Cruz - 28:01
Very cool.

Matthew Adams - 28:06
And then, interestingly, then when you're using Langsmith, you can also
see the responses back from the AI. So if you're developing in house tools
in an organization and you want to have a look at what types of requests
are being submitted and how the AI has responded, if you got a bit of poor
feedback from a user. You can then go back and look at the log of the
actual output that was generated to see potentially what went wrong, and
maybe tune your prompts or even look at fine tuning the model to get
some better responses. Okay, so time for a demo. So this is the attack gen
StreamNet UI. I've already pre populated the API key that I'm using, and
we'll just select an industry at random. We'll be a media company. We'll
say we're a large ish media company.

Matthew Adams - 29:14
And then this is where we split into choosing a threat group scenario.
We've then got all of the Threat Actor groups that are currently logged in
the Mitre attack framework. So let's pick carbonate. They're reasonably
high profile. You can always look at the listing for Carbonac or the given
Threat Act group on the attack framework that's linked to Dynamically.
When you select it. You can also then see the different techniques that are
being loaded in. So behind the scenes, what's happening is we're using
that Attack Python library that I mentioned to pull data from the Styx
data and then load that into a Pandas data frame. And then just a bit of
formatting occurs just to make it a bit more presentable to the user.

Matthew Adams - 30:18
You'll notice here that like lots of threat actor groups, this group has
sometimes multiple techniques within a given phase. And what I've decided
to do, rather than having sort of really complex or overlapping scenarios,
is that when we come to generate the scenario if there are multiple
techniques per phase, one of those techniques will just be selected at
random. So you shouldn't see more than one technique per phase. And
that's just to keep things relatively well structured. If you've got a
requirement to consider multiple techniques for, in this case, Defensive
Agent, that's where the custom scenario generation would come in. So I'll
hit generate scenario. This is a recent feature that was introduced by
Streamlit, which I quite like, which is the ability to give better visibility
into long running processes.

Matthew Adams - 31:18
So rather than just having a spinning wheel here with the user wondering
what's going on for a minute or two, we can see that the model has been
initialized successfully and the scenario generation has proceeded. It's
fairly straightforward in this case, but where you've got tools that perhaps
have multiple agents talking back and forth where the user might be
waiting for several minutes for their output, I think things like that are
really nice. UI tweaks that you can use just to give the user a bit more
insight into what's going on. And so they're not left thinking that
something's stalled somewhere. And then this is our incident Response
testing scenario. So you can see that we've picked up the relevant details
from the prompt template in terms of type of company size and the Threat
Actor group.

Matthew Adams - 32:13
It's then creating the scenario based on the techniques that we selected.
And if we then flicked over to Langsmith, which was that observability
tool I mentioned, you can see that this is our latest run here. So all of that
information will then be logged. This is only if you're using the Streamlit
Live demo app, by the way. So if you clone my repository and run it on
your own, you can use your own Langsmith API keys and set it up yourself
or remove the environment variables altogether. The reason why I tested
using Langsmith with this tool is because really there's not any
organizational identifiable information beyond it's a media company with
a couple of hundreds or a thousand employees.

Matthew Adams - 33:09
So in terms of sort demoing the capabilities of Langsmith, while not
creating too much of a headache for myself or people wanting to use the
tool, this felt like a good time to use it. And then finally, if we're happy
with that, we can submit our feedback and then that will also appear with
the run. So it's a good way of then keeping track. I could extend this so
that if a user submitted negative feedback, they could provide a comment
to explain what was wrong. It's not something I've done in the public
version of this at the moment. And then if we flick over to custom
scenarios. So just to give you an idea of how we would use this.

Matthew Adams - 34:01
So if we've got perhaps a phishing email for initial access, that might drop
some malware and we'll think about lateral movement through RDP and
maybe some exfiltration over a C two channel. Again, we can hit that
generate scenario and it will take a few seconds to generate that. So while
that's waiting, I'll just point out that you can immediately jump to the code
on GitHub to look at this. And as Dennis said, it's all open source. So
while we're waiting for that, I'll give you a look at the prompt template
that's used for the custom scenarios. So here you can see that this is our
system templates, which is pretty consistent. And then when it comes to
specifying the human template, this is where we capture the industry and
company size parameters.

Matthew Adams - 35:13
Those will then be, for want of a better term, stuffed into the prompt
template along with the techniques that the user has selected. And so once
that's all populated, that's what then gets submitted to the language
model. And so again, that's our scenario generated. And we can see that in
Langsmith. Again, so slightly different output this time because we're
asking for a custom incident response testing scenario. It's also interesting
to track some of the latency around the request. So another useful feature
of this observability platform is you can see that this is probably a
scenario where there were quite a lot of techniques that were listed. So is
this what, Apt 29? Yeah. So 13 techniques were submitted. So the model is
obviously going to take a bit more time to think about how to work with
those.

Dinis Cruz - 36:32
Okay.

Matthew Adams - 36:33
If you'd like to try attack Gen. So I've mentioned the GitHub repo already.
You can use the Streamlit Community Cloud app as well. You can
obviously clone or fork that app as well and run it on your own
infrastructure.

Dinis Cruz - 36:53
Have you tried with Azure OpenAI or somebody who tried it?

Matthew Adams - 37:02
Yeah. So Azure OpenAI is a lot closer to sort of API formats for OpenAI.
Interestingly. Not identical though. So again, it sort of suffers from the
same problem around prompt engineering. You've got to tweak the
prompt slightly in order to get representative responses, but in principle,
with a bit of coding work, it's absolutely possible.

Dinis Cruz - 37:30
Yeah, because I think the advantage of that is that it would solve that
problem of if you want to run this for your own more external sensitive
data with live incidents right. Then at least that one doesn't send.

Matthew Adams - 37:45
The data to yes. Yeah. OpenAI say that anything submitted to their API or
via the playground, they don't use to train their models. Clearly though, if
you haven't got commercial terms with OpenAI, but you do have
commercial terms with Azure, then there's obviously a clear choice into
which one you'll use. But it's not something that I've looked to integrate
into this tool yet, but I have done for other projects that I'm working on.

Dinis Cruz - 38:21
Cool.

Matthew Adams - 38:24
So just to give you an idea of what you might see next from Attack Gen,
I'd like to add some support for additional matrices from the Attack
framework. So those of you who are more familiar with Mitre Attack will
recognize that we've only been talking about the Enterprise Attack matrix
so far, but my plan is to add support for the mobile and industrial control
system matrices. Also, with an eye on making this easier to deploy in
corporate environments, I'm planning to provide a docker container image
rather than having you either run it from the Streamlit app or build it
from source each time.

Dinis Cruz - 39:15
Actually, could you run it from a lambda function? I guess depends. I'm
not sure what Streamlit supports the lambda functions is.

Matthew Adams - 39:23
I've not tried to run Streamlit through a lambda. That would be
interesting. I'm not sure it might be performant enough. It does take a
little bit of time to load the initial Mitre Attack data, but it's probably
within tolerance for a lambda function. Certainly something to experiment
with.

Dinis Cruz - 39:47
Cool. Yeah.

Matthew Adams - 39:51
So I'd also like to add the ability to generate scenarios based on the
techniques associated with different campaigns. So currently the tool
focuses on the techniques that are associated with threat actor groups.
But Attack has this concept of campaigns where you might see perhaps
multiple threat actors working together targeting particular types of
organizations and they roll that up into a construct called a campaign. So
for those organizations that wanted to practice it being part of a
campaign, I think that would be a useful addition. I'm also looking to add
some options for users to provide more information about their
organization conscious that probably many won't want to, particularly in
the public version, and hence I'd make it optional, but it's something that
I've done in some of my other tools.

Matthew Adams - 40:50
So I've got a threat modeling app called Stride GPT where I just capture
some basic information about an environment and an application and then
use that to generate a threat model. I think it would be additional useful
context to help generate the scenarios for this tool as well. And lastly, you
need to tell us.

Dinis Cruz - 41:15
About the Stripe GPT. That sounds really interesting.

Matthew Adams - 41:19
Yeah. So there's a link to my GitHub repo at the end. It's another open
source project of mine. So happy for you to take a look.

Dinis Cruz - 41:29
Do another session on that.

Matthew Adams - 41:33
And lastly, if anyone's got any suggestions having watched this talk, please
raise an issue on GitHub. If you're a developer, feel free to submit a pull
request. If you're non technical and have some ideas, then just contact me
on LinkedIn. I'm hoping to make this an even more valuable tool for
organizations as it evolves. So very happy to take ideas for improvements
and then sort of having seen an example of an LLM app and I think it's a
pretty good use case for the current state of LLMs and what they're
capable of. I wanted to sort of move to wrapping up by thinking about
different use cases or how I think of different use cases for language
models and some of the tips, really that I've thought of as I've carried on
and learned things through the development process.

Matthew Adams - 42:37
So when it comes to identifying use cases, my favorite way of thinking
about this and describing it to people is imagine you had a new intern.
They're very good at written English or in fact, any language. They will
need supervision, they're not going to get everything right all of the time.
They are definitely not your best red teamer, definitely not your best
security architect, but they're very keen and eager to help. That's the type
of individual you should be thinking of when it comes to thinking about
what would be a good use case for a language model.

Dinis Cruz - 43:25
All.

Matthew Adams - 43:25
The better if the tasks that you're going to give that intern are repetitive
and or quite tedious tasks that can be easily automated. So setting aside
hallucinations and other quirks of probabilistic models, gen AI models
don't get bored or lose focus like humans do. And so if you've got a very
repetitive or tedious task like generating incident response scenarios very
quickly from a standard set of data, LLMs are really good at those types
of tasks. And at this stage I think it's really about augmentation of
capabilities rather than replacement. So as I think we touched on at the
top of the talk, it's really about, for me, making people more efficient and
helping them to work quicker than it is about entirely replacing job
functions or particular roles.

Dinis Cruz - 44:33
So one of the scenarios that I really like with this is to explore. So I think
there's two elements. I think there's post incidents to understand the other
what if scenarios, right? So basically XYZ happens so you can go, okay,
but we got lucky because they turned right instead of turning left, or they
didn't do this and didn't do that. So you can now start to see the next
steps. But also I can see that an evolution of that is almost to do this in
real time, isn't it, where you almost start to predict what could happen
next based on these possible scenarios and then you could even take into
account the existing controls of the company so it becomes super
powerful. So you almost want to start thinking a couple of steps ahead of
the attacker, start thinking, are we ready for this?

Dinis Cruz - 45:20
Are we ready for that? What happens if this happens? So I tend to do that
incidents, but this will bring a lot of science to that and also will bring you
a lot of more, I would say three dimensions to that.

Matthew Adams - 45:31
Yep, yep, absolutely agree.

Dinis Cruz - 45:34
George, I think, has the question. George, just be able to speak. I think
Hugh, I made your co host, although if he's think actually, I think his
question was, yeah, does attack gen work API keys from other genius
servers as Bar or Bing chat? I think you kind of already said that you
haven't really tweaked it for those, right?

Matthew Adams - 46:07
Yeah. So it's limited to working with the OpenAI API.

Dinis Cruz - 46:16
Cool.

Matthew Adams - 46:20
And so, finally, just on identifying use cases, starting small with a well
defined use case is really key. So lots of organizations at the moment are
just experimenting with simple use cases like chat with your security
policies. And that's a fairly low risk consequence because people should
have a reasonable understanding of security policies anyway. And they've
always got the ability to escalate to a member of the security team if
they're not sure about a particular response that they received. And it's
also very focused. It's not trying to replace the entire security team as your
first use case. It's nicely scoped and manageable. And that then helps with
meeting some of the best practices that we'll come.

Dinis Cruz - 47:15
On to now, actually, that's an interesting point. Is it possible to add the
scenario of what would this, for example, depending on the maturity of the
security team, what would happen? Because at the moment, you have
scenario, scenario.

Matthew Adams - 47:31
Right.

Dinis Cruz - 47:31
But how would you think of how can you add the current controls in
place, including the fact that you have a security team that should react to
some of these things?

Matthew Adams - 47:42
Yeah, and that's sort of what I'm thinking of with that additional
organizational context I mentioned in the Roadmap. That's the sort of
information that I would think of, including how capable are your security
team? Do you have a permanent security team? Are you using an
outsourced MSP to perform certain functions or all of your functions? I
think those will all have a significant bearing on your ability to respond
and how you respond to an attack. So it's something that I'd like to at
least give people the option to factor into some of the scenario
generations.

Dinis Cruz - 48:20
Yeah, that could be actually quite massive, man, because what you would
also show is the impact. For example, imagine doing that on budgets,
right? Imagine doing that on simulations because I guess it doesn't have to
be perfect, right? But if you have a team of a certain size, let's say you
have, let's say, same scenario against three teams. One doesn't exist, one
with some resources, one with mini resources, one with a lot of resources,
or one without a lot of outsourcing, one without outsourcing. Right. I
think it would be quite interesting to run those scenarios. And again, you
can do an LLM on top of the analysis of it, but I think that would be quite
useful, especially around budget times and educations. And I guess even if
you then start to have actually another valid question here.

Dinis Cruz - 49:06
Does this actually have real world scenarios on it? Like real world instead
of a scenario almost like a real world attack?

Matthew Adams - 49:17
So by virtue of the fact that the attack framework is all about real world
observed techniques and tactics that these groups are using, then yes, it
won't necessarily replicate.

Dinis Cruz - 49:35
Yeah, but they're not specific. Right? Sorry, they're not specific.

Matthew Adams - 49:40
No, but I don't think two attacks are ever identical.

Dinis Cruz - 49:46
Yeah, but that's an important narrative, especially for in certain sectors,
being funny but personalizing. Some of these, like, look, this attack just
happened with this thing with these kind of oil industry or companies. But
that could be added, right?

Matthew Adams - 50:01
I'd say it's already possible if you go through and do the custom scenario.
So if you can get a threat intel report that says for that attack, which were
the given techniques, you could build that based off that custom scenario.

Dinis Cruz - 50:20
Yeah, that's very powerful, man. Somebody worked a bit on that one and
shared or find a good way to do it because you then have real world
scenarios mapped to a particular industry and then you add on top of that,
for example, how would the current team or the react or with the impact?
That'd be really interesting. I guess the foundations are here, isn't it?

Matthew Adams - 50:47
Yes. This is only version 0.2 at the moment, so it's still very early days, but
yeah, just sort of picking up.

Dinis Cruz - 50:59
Sarah has a question now. I was literally about to say sorry, I know you
had some questions.

Speaker 3 - 51:03
Sorry, I can wait. I want to let Matt finish and then I'll pick up at the end.

Matthew Adams - 51:07
Yeah, we've got two slides to go, I think so, won't be too long. So yeah, in
terms of best practices, we sort of covered small, well defined use cases.
I'd also say non critical use cases to start with. It's really important no
matter how compelling the use case. I wouldn't start off with a model
that's making decisions about people, for example, or things of that
nature. You really need to build up the organization's familiarity with the
capabilities of the tools and where the Foibles are before you start moving
into those more potentially risky use cases. And to that end, hewn in the
loop. Reviews remain absolutely critical at this stage. I have experimented
with having sort of pairs of agents working together which does give you
that sort of chain of thought process that's been covered in some of the
papers.

Matthew Adams - 52:11
But even then, if you were sending this report off to your CISO to say I
think we should do this and you've not even looked at it, I'd be concerned
if you were doing that. It still needs somebody that understands what the
model should be producing in order to critique it and make sure that it is
hitting the mark in terms of quality. If you are looking at making decisions
during or by using a model, monitoring for bias, using things like that
Langsmith or another tracing or observability platform is really useful. I
think the major LLMs, OpenAI, Anthropic, Google have done a really good
job at trying to minimize the bias in their models.

Matthew Adams - 53:05
Some of the smaller models on, for example, Hugging Face, I think they've
not been used and tested enough for us to be clear either way that there
isn't an inherent bias in the model. So it's important to keep an eye on that
and also look at just fundamental engineering practices. So this is a
relatively new field. We're still experimenting. It's important that you
document what works, what doesn't and track the performance of that
throughout the lifecycle of the tools that you're building. I'd also say be
transparent about your use of AI. I think because we are at that early
stage, users and even customers are very accepting of the fact that tools
are experimental. But if they can see the benefits, I think they're prepared
to accept some variation to what they would get from a pure human to
human interaction.

Matthew Adams - 54:11
This is a conversation that I'm having more often. Again, as the tools move
from POCs into production is really making sure that you're addressing
that return on investment point. And so for something like Attack Gen, you
could look at metrics such as how many more exercises were you able to
run in a year by using something like that tool, as opposed to if you're
using a more conventional scenario generation route. And as you get more
familiar with the tools and use them more across more different use cases,
I think it's easy to become over reliant on them.

Matthew Adams - 54:56
And that's where things like Human in the Loop reviews being critical of
the models and not just accepting what they're telling you is really
important because we've already seen quite a few well publicized
examples of where over reliance has led people down a path that they
really didn't want to find themselves on. And lastly, I'd say it's still really
early days, particularly when it comes to productionizing these apps. And
so I think it's incredibly important that organizations keep developing
their own internal AI expertise and allow people to experiment, find out
what works and more importantly, what doesn't. That's all really valuable
experience that I think we're going to need over the next couple of years.
And so that's everything that I wanted to cover, I think. Sarah, you had a
question. I'm happy to take any others that people might have as mean.

Speaker 3 - 56:01
That was that was brilliant, matt, thank you. It's just so nice to see
something that's so concrete, practical, step by step thought through with
all the caveats. It's just what I needed right now anyway. But in terms of
your model, it did occur to me because I did in a lot of risk articulations
which need a little bit of creativity to make them hit home, especially
incident scenarios. Would it be forgivable to just plug in the generate
scenario and ask the model to compare it to any real life incidents that it
could pull out? To maybe add some of that color, that sort of newsworthy
color to it just as one idea. I don't actually see a poor impact as long as
it's true to the mapped out scenario to paint a bit of a picture for
nontechnical stakeholders.

Matthew Adams - 56:51
Yeah, providing that you're having a human review that and someone
that's capable of critiquing the output. I don't see a problem with that. I
see it as a way of being more efficient. I think as I've touched on during
the talk where people have got into difficulty is either they've completely
relied on the output and not looked at it. So the case of the lawyer in the
US that ended up submitting incorrect case studies with their submission
springs to mind immediately. But there are also cases where on a technical
side you can see things that once you go below the level of really good
general knowledge, I'd say, then you can start to find weaknesses.

Matthew Adams - 57:46
So if you ask it really technical questions or really up to date questions so
beyond the training cut off, the training dates cut off, that's when you'll
start to get a lot of hallucinations but in terms of getting work done faster
but still maintaining that quality yeah, I absolutely don't see any issue with
that.

Dinis Cruz - 58:07
Were you talking about the scenario of taking an existing situation or
existing incident and then augmenting with possible scenarios or almost
like offshoots of what could have happened?

Speaker 3 - 58:19
Potentially, yeah. Well, either way I was just talking about sort of
potentially adding some more media friendly color to the attack scenario
for if you're bringing potentially doing an executive tabletop or something
like that to bring that color to it. That was all. I'm guessing you can
extend it by sort of asking what would happen next, but with all the same
caveats that Matt brought to it, that it would need to be credible, it would
need to be a logical progression.

Speaker 3 - 58:52
And mean, the only other thing I was going to say is I mean, I'm looking at
what you pulled up, Matt, with your Python script to inject the techniques
in there, because I'm looking at scenarios for mapping regulatory and
legal compliance requirements across different frameworks where we to
try and pull out some duplication and be able to actually have a
conversation across control objectives and risk areas. To pull out
compliance requirements discreetly for types of businesses. So it's a very
similar kind of thing in some ways so that is a good caution for me to take
away.

Matthew Adams - 59:28
Yeah, and the reason for doing that is because one because to manage the
risk of the hallucinations but with a language model that had a really
large context window so like Claude, for example, you could just try
pasting in the entire attack data set with your prompt but that's got a
couple of drawbacks really. One is the token cost. So then each input that
you submit, each prompt that you submit would contain all of those tokens
for the data that you were submitting when actually you only need to
query a small subset. You might as well do that upstream before you
actually use the LLM, you also increase the risk of the hallucination or
things not being picked up.

Matthew Adams - 01:00:25
So some of the research that I've seen recently is that language models
pay more attention, probably a bit like humans, they pay more attention at
the start of a large chunk of text and at the end and then stuff in the
middle tends to get lost. Whereas if you're doing a regulatory framework,
lookup, you clearly want it to pay attention consistently so that you don't
miss relevant clauses that are specific to the query that you're asking.

Speaker 3 - 01:00:55
Yeah, I mean, it could contract language as well. There's a potential use
case for selectively based on context, putting contract language in based
on the nature of the scenario and triage questions up front. And yeah, you
really need that to be paying attention all the way through. That's good
steers.

Matthew Adams - 01:01:22
So happy to take any more questions otherwise, as I mentioned earlier on,
there are the links to my profile on LinkedIn or to my GitHub repo.
There's a number of different projects in there that use language models in
different ways. I'm really all about practical applications for language
models in cybersecurity and trying to make cybersecurity's professionals
lives a bit easier through applying these tools. So there's sort of four or
five different projects in there that you're welcome to check out and
they're all open source cool now.

Dinis Cruz - 01:02:00
Massive contributions, man. And definitely I think you're going on that
direction of augmenting and making is a lot more productive. Right. So I
feel the other tools deserve a session too. So let's sync up on that. So
brilliant. Thanks for this session and the video will be up quite quickly and
then looking forward to the next version of this.

Matthew Adams - 01:02:25
Thanks very.
