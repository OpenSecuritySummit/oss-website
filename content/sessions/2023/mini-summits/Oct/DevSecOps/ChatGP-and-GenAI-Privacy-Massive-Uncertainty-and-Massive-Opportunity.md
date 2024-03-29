---
title        : "ChatGPT and GenAI Privacy - Massive Uncertainty and Massive Opportunity"
track        : DevSecOps
project      : DevSecOps
type         : working-session
topics       :
featured     :
event        : mini-summit
when_year    : 2023
when_month   : Oct
when_day     : Wed
when_time    : WS-18-19
hey_summit   : https://www.linkedin.com/events/7116101480998182912
banner       : https://pbs.twimg.com/media/F7xXwtKX0AAbLxn?format=jpg&name=medium
session_slack:
#status      : 
description  :
organizers   :
    -  Dinis Cruz   
    -  Sarah Clarke
youtube_link : https://youtu.be/WjDRkiFGfNA
zoom_link    : https://us06web.zoom.us/meeting/register/tZclc-Ggpj8jGdGKNJoRA2YdYHvoNNL98b3u
---

## About this session

Exploring governance challenges with GenAI usage and the opportunities created, that could fix key parts of cyber security and privacy ecosystems that have been fundamentally broken forever. 

### Massive Uncertainty

 - How can we responsibly grasp opportunities and live with uncertainty? 
 - Where do you start?
 - How do you upskill?
 - How do we bring in new talent and increase Neurodiversity in our industry?
 - How can you manage risk for rapid dev, acquisition, and deployment?
 - How do we protect user's Privacy?
 - How do understand AI bias and prejudices?
 - How to regulate it?
 - Prompt injections and data leakage
 - Impact on User's identity, user's trust on web content and the need for 'trustworthy identity/content providers'

### Massive Opportunity

 - How to use GenAI to understand system's Privacy implications
 - Leveraging the Privacy and Isolation of private or own hosted LLM models
 - Scaling 3rd party security assessments
 - Leveraging GenAI agents to understand GenAI agents
 - Improving human's productivity by 10x (namely Risk and Privacy professionals)
 - Scaling Threat Modeling and DPIAs
 - Scaling Data randomisation and Data minimisation
 - Real time compliance dashboards (with interconnected Risks and Privacy mappings)
 - Scaling indident response that is focused on "Privacy and Trust"
 - Empowering users/customers to make fact-based and risk-based decisions

## Transcript:
Sarah Clarke - 00:00
You.

Dinis Cruz - 00:02
Hi. Welcome to this, I think, very exciting session in October, 2023, maybe
in the future, this is going to be solved. But where we are today, this is a
very interesting topic, where we're going to be talking about the gen AI
and privacy, but looking at it from the point of it's a massive opportunity
for privacy, but also it's massive uncertainty. Right. So there's a lot of
areas here and Sarah take because you got some slides to guide us
through it, and now we rock from sure.

Sarah Clarke - 00:31
I mean, this is what you get when you chat with Dinis. He asked you to do
a talk about it. So this is why, I mean, I've been trying to get across what
the governance challenges might be of this, involving myself in not for
profits and doing an awful lot of reading. There was no way just reading
was going to do it. I needed to speak to people who knew their stuff could
get under the technical hood and look across the piece to feel around the
edges. So this is where this is coming from. It's not a desperately technical
talk. There's lots of individual aspects you can look up, like, what's the
current technical standard for bias assessment? That's not where I'm
coming from.

Sarah Clarke - 01:05
I'm coming from a place of how can your average business get across this,
grasp the opportunities and deal with the uncertainties when they are not
an AI specialist company? So, first of all, I wanted to put up what Dennis
had suggested we talk about. Bear in mind he gave us half an hour. So the
man is nothing but ambitious.

Dinis Cruz - 01:27
We're going to go a bit longer, though.

Sarah Clarke - 01:29
Yeah, we'll see how we, you know, we're going to get across some of this.
I'm going to wrap it into some of the stuff that I'm going to cover. I know
Dennis will be interrupting and then I'll rein him in and then we'll get
through some more slides and we'll do fine. First of all, I wanted to just
define some terms. So I'm looking at this from data protection point of
view rather than privacy. The distinction is that privacy is one of the rights
that data protection looks to protect. It's actually about any potential
harms to the rights and freedoms of people that can come from any aspect
of data processing.

Sarah Clarke - 02:00
So it's not simply about retaining secrecy or confidentiality, it is about is
data being used in a way that could cause you harm, could cause you a
risk to any of your rights. Perhaps it might be your right to vote, your right
to life, your right to nondiscrimination. So all of those things come into it.
I generated these images with Dali just for fun and being a child at heart. I
had to have the one on the right as an example. I asked it to produce an
example of most of the current use cases, common use cases for
generative AI and the kind of prevalent models at the moment. And the
one reason I selected this one is because it's put AI fart instead of AI art.

Dinis Cruz - 02:40
I was reading.

Sarah Clarke - 02:41
It was definitely a keeper. It really sort of underlines one aspect of this
that there are a lot of limitations. There are edges around what it can and
can't do. There are amazing things it's doing like picking up flow
diagrams, translating those into code, which is opening the door to a lot
more accessible plain language coding, no code solutions. But I couldn't
get it to remove the text elements of this no matter how hard I tried. It
doesn't do it. Once they're treated as vectors, then you're done. It won't
take them out again. So it's just a little indication of where I'm coming
from in terms of generative AI. Most people have a broadish
understanding of it who are likely to be on this kind of call.

Sarah Clarke - 03:21
We know it's a predictive text edge engine, but we also know that it's
producing capabilities that are far beyond just that simple interpretation
of it. It feels like a really solid iteration of Search where you have a
marketing advantage, a market advantage from being accurate and
complete. So it's moving in the direction that we would like it to be able to
access a lot of deep data. And of course there's the bespoke versions of it
where you can train with your own data. Of course I'm talking about Chat
GPT because it's blown the lid off this. But there are about thousands and
thousands of large language models and other multimodal models out
there and a lot of them are more fit for one purpose or another. This is
from a risk management point of view. My background is risk
management.

Sarah Clarke - 04:12
I'm looking at how can I get across this rapidly defensibly to make space
to get into it, look at it, explore the potential of it, but also not open the
door to Gotchas moving forward. And the baseline truth is, you cannot
start to assess risk to get some kind of pragmatic bead on required
controls until you understand the use case context, until you understand
the data set and model that you're using, whether it's embedded and
integrated with other models whether it's integrated into another solution
where in the business it's going to impact you, where in society it might
impact which user bases it's going to impact is that going to be
approximate and urgent impact? Is it just surfacing something that's going
to help you do your job better? Or is it making a benefits entitlement
decision?

Sarah Clarke - 05:02
You have things along a big continuum here and I think with the
existential risk discussions it has really masked the everyday rolling out of
automation that we really need to be paying attention to where we're
perhaps standardizing. And removing post implementation redress at quite
a rate, as well as looking at the advantages to improve day jobs that are
moving in a positive direction. So I can't stress it enough that we need to
look at some of the good categorizations that are out there and
understand where generative AI can be a positive bonus and where we
need to still keep an eye on what's happening with broader automation
that's impacting people right now. So this is just a wall of text, my
apologies. It's part of the not having an awful lot of time to prepare.

Sarah Clarke - 05:57
This is just some of the elements of privacy risk that I have on my radar.
Can we extract personal data out of training sets? Is there a risk of model
inversion? Is just whoever's got the training data because training data
has been acquired handover fist by all sorts of people to feed models, are
they controlling it prior to training and post training? That point about
further automation without redress for errors, are we innovating in the
post market monitoring as well as we're innovating in the automation and
workflow automation space? People aren't really grasping that if you are
feeding data to models that it'll be ingested and the clarity of purposes
that will be used for later for publicly available or open source models.
Open source models isn't perhaps desperately transparent.

Sarah Clarke - 06:52
Bias is going to continue to be an issue and it's a philosophical issue as
much as a technical and data issue. Against what ground truth baseline do
we want to moderate for bias? Are we trying to better than the society we
are in terms of balance and equity? Or are we operating to an imperfect
ground truth that we're dealing with right now? That's before you start to
get into the technical aspects of bias and I've got a link further on that
takes you into the weeds of looking at bias through different lenses for you
to look at in your own time, we know that it's amplifying the capabilities
of attackers.

Sarah Clarke - 07:28
I'm going to watch a great talk next week at the Mitre conference from
somebody who's using both two types of models but generative AI in the
Foreground to map all the different attack vectors from beginning to end
to identify pinch points, to better prioritize remediation. So it's on both the
attacker optimization and the defender optimization side. Something that
hasn't really been looked at in depth yet, but it's maybe brought back to
the Fore. With Microsoft now placing ads with their search enhanced
generative AI implementation, it's now going to be back to the old days of
potentially optimizing for responses based on what your ad tech profile is,
based on how you're interacting with a generative AI.

Sarah Clarke - 08:27
And there's also an element of even if it's not spitting out obviously
personally identifiable data, there is a long continuum of working out how
much inference can be gained from what it might spit out in response to a
query about a personal situation. Can you single someone out? The US
definition of personal data is PII, is it first name, last name, et cetera.
Because it's easier for developers to have a list of fields that they can
suppress and call it anonymous. In the UK, under GDPR, personal data is
either directly identifiable or by inference to single someone out. So those
things have to be borne in mind. And also I'm very conscious when I'm
using all these models to try them out, that somebody's looking at the
aggregate of my prompts and somebody's looking at me as a user profile
for somebody with AIS.

Sarah Clarke - 09:15
And that will also be part of my online persona that may be of utility for
marketing, et cetera. We know that it's going to enhance surveillance
because it allows you to pass an incredible amount more data and look at
inference and correlation for sentiment analysis, for instance, or for more
creative facial recognition implementations. I was looking at the I can't
remember exactly what it's called, but the Forever pendant that's
recording everything you see, say, and everybody, you encounter their
trust, trying to work out how they can put some privacy protection around
that. And the fact it's being thought about now when the hardware is in
prototype is an interesting way around to have it, but we'll see how that
goes. And a big discussion that's going on in the data protection space is
the erranding point of consent anymore.

Sarah Clarke - 10:15
Because how can anybody without technical understanding or the
ambition to read thousands of lines of terms and references going to
understand what their consent means at the point of collection?

Dinis Cruz - 10:26
That's the opportunity.

Sarah Clarke - 10:28
Yes, it's an opportunity. I mean, so there's massive amounts of
conversation about things like data trusts, like not just watermarking, but
indelibly encoding within data for some definable subset of your identity
that gets carried through for any purpose that would be traceable. And
you would be able to have someone interpret that with some model
visualization to where you're appearing, what you're being used for, what
revenue you're being used to generate. And I think that's going to become
to the fore even more dramatically as we leverage AI enhanced versions of
ourselves, perhaps digital twins of ourselves, we are going to want to see
return on that investment for our inputs and that creeps into the
conversations about copyright and IP that was broken already. But we
have a chance to reinvent and think about these things.

Sarah Clarke - 11:29
So this is quite a technical definition of bias, but it's really just breaking it
down into equality of outcome and equality of opportunity. The Holistic AI
site is very good via that link. I can share the slides if they're of interest to
anyone, but that takes you through steps to assess and surface bias at
different points in the process of utilizing models and AI. It's not simply
about protected groups, it's also about socioeconomic inequality and
potentially bias towards one group or another on that basis too. And as I
said, that concept of ground truth is up for grabs. I think I've never seen
so many people who are deeply embedded in the tech world take a sudden
interest in philosophy and psychology, because this is where a lot of the
answers lie.

Sarah Clarke - 12:26
They lie in our collective societal memory and our traditions and our
conventions. And there is no single truth here. So ground truth is a
misnomer. Are we trying to engineer for better than we are? Are we trying
to engineer to one cultural norm? Are we trying to engineer for a
situational ideal? These are all things that are still up for grabs and
evolving. So this is the Dennis bit, and we can go a bit deeper under this. I
have people who are absolute geniuses at mapping across different
governance requirements. I have my own database. I've been trying to
wrestle to get Obsidian to do what I wanted to.

Sarah Clarke - 13:10
I think I probably need to work out what it does rather than try and make
it do what I want it to do, to try and map across all of the different
surfacing AI governance requirements. But it's the same feeling I've had
coming up through Cybersecurity. Then data protection. I'm getting told to
assess things and make sure there's no bias and have some governance in
place and do some accountability and be trustworthy. I have by contrast to
that, I have papers coming out of places like IEEE where I've got really in
the weeds, deep seated code interrogation techniques to look for bias.

Sarah Clarke - 13:47
What I don't have in the middle, I have a bit of with things like the NIST
AI framework and some isolated guidance, some in there'll be codes of
conduct coming with the EU AI act to something that looks like a control
set that I can assess against. Now, that isn't what developers and
technicians necessarily need to hear. They want to know those as
guardrails and benchmarks for where they can't operate outside of. But
from my point of view, I've always had two hats on. I've had to work in
highly regulated industries to evidence that the right thing is trying to be
done, to work out where the edges are, and then to pragmatically assess
actual risk and actual operational effectiveness that's going on in the
control space while we're trying to make money, innovate and do great
things. So maybe it's three hats.

Sarah Clarke - 14:42
I think it's a hard place to navigate. We've all watched the progress over
the years as things have moved out of the security space into the It Ops
space. Things like access management are far more it ops. Things like
basic patching are far more it ops now. But this is going to have to go on
that journey. The stuff coming out of MLOps that might have security
implications or privacy implications. We're going to have people who are
experienced inserting privacy consideration and security consideration
into continuous development to surface the key things that could
potentially be automated as code but also then brought through to be able
to visualize as a risk profile for those conversations with the people who
aren't at the Tech coal phase. So the translation space is absolutely up for
grabs on that basis.

Sarah Clarke - 15:36
I hate doing data protection impact assessments because a lot of it is show
and tell writing long form stuff. There's very little you can analyze across
the piece, there's very little between one and another. You're comparing
apples to kangaroos, not apples to apples. And this has always been my
focus is trying to surface some standardized defensible risk indicators and
signals that are not too weak to push as far left in the process as possible.
Things that are going to put you in the way of more risk, things that give
you an indication of maturity, things that indicate how much uncertainty
you're going to be living with, which can aid some of this.

Sarah Clarke - 16:15
Generative AI is very good to help summarize visualize and surface
correlations you may not thought of it's not great where you need
precision and consistency as we saw in a talk earlier on, you can pull in
pre verified variables that you know will consistently be interpreted
through prompt as attack gen talk. Was it Monday or Tuesday? Dennis
was very good from Matthew Adams I used it to generate a privacy notice
and it would have looked good to the naked expert eye, but it was wrong
and it took a couple of people when I posted it a few minutes to see what
was wrong with it. We know that lawyers have had their wrist slapped by
preparing for cases, by trying to pull reference up from the bowels of the
collective memory and looking asking for references and sources.

Sarah Clarke - 17:14
This is why all the major players are now adding search for validation into
their wrapped offerings. Because I think it was Claude had three out of
four references I asked for which I knew existed. The URLs completely
wrong, the references are completely wrong. I said you've got this wrong,
correct it the next three, two were right, two were wrong, different ones.
This validation step is very important.

Dinis Cruz - 17:39
Let me introduce think so my analogy now is that you have the reference
of the AI Iron Man, Tony Stark that helped him to build that. I feel that
what we've done was we build Jarvis which is an insane helper, right? Who
can massive co helper. We ask Jarvis to sing a song and to write some
poetry and to write some things and then we criticize it because he's
getting that wrong. So I think the generative AI in a actually it's funny
because the way we're talking about there was a thing I realized here is
that I think Hallucinations are really good on gen AI, right? Because I
think they show the limitations because here's the interesting thing the ML
models that are already using society that actually probably they shouldn't
be using Society, they also elucidate, but they hallucinate in much smaller
percentages.

Dinis Cruz - 18:35
In fact, they hallucinate. And that's where we get lot of bias problems, lots
of really bad decisions being made, but they start to be on the low
percentages, so they almost get drunk to the radar. But actually, I don't
think we should be using ML for those cases. The same way that I don't
think you should be using Gemini for that. Where it's really good is if you
give you a bit of data and you can interact about that data having a bunch
of references in the past. And that's why, for example, if you look at the
attack gen, the solution that he came up with, which works really well, is
to say, okay, you might even have access to the attack tree yourself, but
don't use that version, use this version. And now I'm asking you questions.

Dinis Cruz - 19:12
So in a way, it's almost like the model learning via the main attack gen
almost gave you the understanding of what it is you need to feed it data.
And I think that's where we're going wrong. We almost asking too much of
this technology and we're almost not appreciating the fact that what's
amazing about it is you can interact, you can have dialogues. So the way I
use, for example, Chat GBT, and this is interesting, I stopped using
Google. In fact, I found annoying irritates me to use Google now because I
cannot put context. In fact, I had to search images for a talk recently and I
was really pissed off because I was so inefficient and I was like, can I just
explain what I mean? And I know that the data was there, right?

Dinis Cruz - 19:57
But my point here is that where is really valuable is that mode where you
kind of know the output, right? So I think there's two worlds here, right?
There's a world where the person who knows the output, it can make that
person ten times more productive or 100 times more productive, because
what it does, it shortcuts a lot of the steps. And this is the generative
element. It allows the recreation of the materials to be very cheap, right?
That's a big difference. So I don't think that the interesting part here. And
the interesting opportunity is to say, hey, chat GPT, give me a data impact
assessment of this without a lot of data. That's not what I'm looking for.
What I'm looking for is to say, hey, here's a bunch of data sets.

Dinis Cruz - 20:45
Consolidate this, give me analysis of it, give me a review that I can look at
and go, yes, that is really good. Now, fine tuning like this. Now what
about this data set? What about this data set? Even more interestingly,
and this is the bit I make here, is that when you talk about explainability
where I think we're going to get a crazy amount of mileage here, is to be
able to translate it to the stakeholder. So I'll give an example. I need to
brief my board, I need to brief my execs, I need to brief their direct
reports, I need to brief their teams, I need to brief the engineers.

Dinis Cruz - 21:16
Now, the only way to do this effectively is to have a personalized briefing
that takes into account who they are, what language they know, what
culture they in, what state of mind are they in, how do they like to be
communicated, what's their background, what they know. Right? If you
don't know that, your message are always going to be diluted, right?

Sarah Clarke - 21:36
Yes.

Dinis Cruz - 21:37
So I think we now have the ability to say, I want to communicate this for
this persona. Give me that bit. Even more interesting, allows that persona
to interact maybe with the bot that has been briefed to do that. So our
ability to communicate and scale is suddenly increased ten hundred fold.
And that for me, is the opportunity.

Sarah Clarke - 21:59
Yeah. Do you know, I agree with you, Dennis, and you've probably
recognized that I feel like I have a split personality when I'm dealing with
this because I'm so excited by what it can do. There was one of the
elements we talked about bringing people more neurodiversity into the
industry. And I think this is a superpower for a lot of typically neurodiverse
traits because this is going to I will apologize to anyone for generalizing,
but within my sphere of experience. But thinking to the nth degree, seeing
every extrapolation of potential outcomes is not the challenge for a lot of
my neurodiverse peers and comrades. It is finding a core to simplify down,
to bring other people into the conversation. And for that it is amazing.

Sarah Clarke - 22:53
And also it's taking a real super complexity of ideas and giving you that
plain English that gives you a starting point to work out from. And that
has been a game changer for a couple of people. I know. It keeps them on
task. It stops them having to be pulled out of rabbit holes by their ankles.
They come out of those rabbit holes with deeper, richer, broader insights
than your average person who hasn't bothered to think to that extent.
They need the rapper to then be able to communicate as hooks for that
value to other people. And for that it has proved beyond valuable in a way
I can't quantify. And I'm maybe generalizing wrongly, but this is the
feedback anglically that I'm seeing on that front.

Sarah Clarke - 23:47
Definitely with that following on from this, I've got something that kind of
speaks to that a bit, but I wanted to sort of keep it in context of potential
use cases because I think you have to use it to work out what it is and
what it's not. And I think we're trying to generalize, to regulate in such a
complex space that we are going to hobble some of the potential here. I
make my money because I can deal in regulations, but I'm a pragmatist.

Dinis Cruz - 24:19
But take a step back, right. We still don't understand how it works.

Sarah Clarke - 24:24
Yes. Nor do most of the model vendors.

Dinis Cruz - 24:28
Yes, exactly. If you think about it, right? The idea that we should allow
something that we don't fully understand to be fully autonomous and
make decisions is insane. Right. And think about it, in the human world,
we don't allow that. Right. Like for example, we don't allow the genius to
use AWS expert to be running production by himself. Right. So we know
that we put guardrails in place. It doesn't matter if this person can do it all
or can provide all the answers. We put system checks and balances in our
workflows, right. We've learned that, for example, sometimes the
explainability of something is more important than somebody who can do
it sometimes, but it has a margin of error of x. So that's why also I feel
that it's these transitions that are the interesting opportunity, right.

Dinis Cruz - 25:15
But of course, people sometimes it might feel like a shortcut and I'm sure
there's a lot of team companies and stuff that will use it, but I think that
it's like the Internet. Think about the power of the Internet is that you can
send a packet from A to B in a distributed way and it arrives there. It
actually eventually arrives there. But look at what we build on top. So I
still feel that Gen AI is a bit like that. That's the capability that is really
interesting is the ability to feed it data and get analysis and then have a
dialogue in human language about those outcomes.

Sarah Clarke - 25:53
The speed at which we're moving up the stack and building things on top
of it is so rapid at the moment. That's one element of it as well compared
to the speed at which solutions were built on top of the Internet.

Dinis Cruz - 26:05
But we've always done that, right? If you think about it, we've always
done that. You can argue that the speed that we built up on top of the
Internet was massive. The speed we built up on the cloud was massive. I
think we've always done that. Right. We always build things on top of the
other. What I think is a bit different now is that we have the ability to start
to understand how the system works. We were just me and Lewis were just
in a session, we talk about threat modeling. The big elephant in the room
on threat modeling is that most organizations have no idea how their apps
work, right? Because we from the security team arrive and do a threat
model. What is the first question, Lewis, that we ask, hey, how does your
system work?

Dinis Cruz - 26:41
Can you show me some diagrams? So it's almost like we don't even
understand how our current systems work, right. And we're building more
stuff on top. But I feel that we now start to have the capability to
understand how it works or to even be able to say it's beyond
understanding. It's such a giant mess that we can understand, but then
you can ask the question, should we really be making decisions, especially
decisions that infect people at the end on top of these systems?

Sarah Clarke - 27:09
Yeah. I mean, this is where I came from. This is what drove me. I've
worked in corporate risk management for a long time. I worked in
financial services risk management for a long time, and shoehorning the
human rights and individual collective impacts elements of data protection
risk into corporate risk profiles is very difficult because it still deals in
financial risk management standards right up to board reporting.

Dinis Cruz - 27:38
And it's all spreadsheeted.

Sarah Clarke - 27:40
Yeah. And that's why I pivoted into data protection, because there was a
legal hook to hang rights and freedoms of individuals and groups off to
bring it closer to the table. That doesn't mean I'm not a pragmatist in that
space, but I was always looking for ways to integrate that into the whole
process, and this does help to do that in some ways. So give me a chance
to get a couple further on. If you think it's a waste of time, Dennis, you
can interrupt again.

Dinis Cruz - 28:02
That's lovely. I've been getting asked one, so what did I do?

Sarah Clarke - 28:08
I went and asked it a really complicated question, just to test the edges.
The Use case was a general insurer assessing customer relationship
management data to understand the risk of policy renewal, because it's
the kind of thing I think people are going to want to do. And I was reading
a CIO article recently where someone was bemoaning what the exec felt
that Generative AI should be able to do, or the suite of models that were
available should be able to do, versus what it was necessary to do to
arrange to make that happen. In terms of identifying the data set, was it
clean enough? What needed to happen to it for that to go ahead? What
were the systems requirements? What were the other non functional
requirements, how was it going to be delivered?

Sarah Clarke - 28:49
What were the implications of sharing data with a model, et cetera, et
cetera. So I asked Chat GPT, I asked It to outline what the contributory
tasks would be and the skills that were required to complete those tasks.
And I put absolutely no store by what it told me. But what it did do was
create some shape to push against. Everybody knows that having
something to push against is easier than coming up, than starting from a
blank page. So this is what it's given me at the moment. It excludes any
governance effort is what.

Dinis Cruz - 29:23
It gave or what you created.

Sarah Clarke - 29:24
On top, I've formatted the Excel table that it output after I told it what I
wanted as columns and rows for the table and what's populated into all of
the columns and rows of the table. Is what it automatically output from
the prompts that I iterated to talk about.

Dinis Cruz - 29:40
The useful that I think is useful.

Sarah Clarke - 29:43
All of these steps have been massively useful. I mean, this is adding in the
data protection effort with an estimate for the time it would take to do the
data protection task. This ignores the training amount of time that I asked
It to spit out an estimate. This is the totals that it spat out. I asked very
specifically the balance between machine and human effort in its own
estimation. So it's looking at nigh on a year of consistent, full time
available effort in a balance of this kind of proportion to get to the stage
where you can start to get some useful insights about what the risk of
attrition failing to renew policies is for an insurer. Now, we know that it
doesn't have any local knowledge.

Sarah Clarke - 30:35
I told It that it was a local and general insurer that covers pet house and
car insurance. And it was about 10,000 employees. And the prompt was
very specific about what I wanted to pull out as the different model inputs
and outputs and balancing between human and AI effort. And it is about
how far it can get you in terms of something to interrogate or push back
on. This is all the data that it spat out for my this is an Itest slide. But I
asked It about the kind of models, whether it was gen AI, whether it was a
different model, what kind of tools. So really just interrogating from my
own point of view, using it to enhance my thinking about how I might plan
out a project and manage expectations about what was achievable and
what wasn't.

Sarah Clarke - 31:28
And I thought the best use for this would be to hand it to the consultant
that they paid to come in and tell them how AI could ten x their business
and say, can you tell me how you can justify your estimates compared to
these estimates? Can you help me to interpret this? Because that felt like a
very many layered validation of the offerings that we're getting. In some
ways, I do feel that management consultants jobs are at risk more than
almost anybody else's with this.

Dinis Cruz - 31:56
They need to leverage it, right?

Sarah Clarke - 31:58
Of course they do. The Boston Consulting Group study. The Centauris and
Cyborg study training on their own data. It was really interesting and it
should be paid attention to. And the way it uplifted, probably the least
productive members of the team was pulling down to a mean and there
was thinking about that. Much like in mapping, you have your pioneers,
your town planners, and your settlers.

Dinis Cruz - 32:29
By the way, important. They call it explorers.

Sarah Clarke - 32:33
Oh, that's it.

Dinis Cruz - 32:34
Dealers and town planners.

Sarah Clarke - 32:36
There you go.

Dinis Cruz - 32:37
I asked Simon because I forgot to.

Sarah Clarke - 32:39
Yeah, I needed to change that. But we're going to need to identify those
people. We're going to need to nurture those people and work out where
they fit into this because it's never been more important to understand
that.

Dinis Cruz - 32:52
But here's the thing, if I go back to that one, all right, the way I think we
use this, I think you use in two ways. I think you can use the LLM models
to jumpstart the creation. But where I think it's very interesting is for you
or for a bunch of experts to validate this, right? They validate it, they
validate the structure. In fact, the beauty of it is you can go into detail,
right, so you can start to provide more meat behind this. And then the
sweet spot is to then say, okay, you have now a prompt which is you're
going to provide analysis of this. Here's the raw data, which is this bit.
And here's my prompt, which is for example, now review this or map this
for a company with this structure, with this thing, with that.

Dinis Cruz - 33:38
So what you're doing is you're reducing the universe of what is creating.
And the fact they can create these is already pretty cool. But there's going
to be mistakes here. There's going to be things that don't make sense. So
this doesn't need to be perfect. This just needs to better than what you
would do initially as a.

Sarah Clarke - 33:52
First or to get to this point.

Dinis Cruz - 33:53
Quicker, to get to this point quickly. And then as we learn that. So I now
find that I can already understand that I can prompt to get to here. So my
prompts now are designed to get me to this phase, so I can then analyze it,
verify it, and my bits, which has extra context. And then I use that to feed
the next question.

Sarah Clarke - 34:16
Yeah, I mean, this is why the points from Matthew Adams were really good
as well, because he had looked at when he was prompting with attack
actors to get mapped to techniques and to then produce incident scenarios
to plan exercises around. What he surfaced was that he couldn't reproduce
exactly with the same prompt with different models, say Bard or Claude or
Llama. He was having to prompt engineer to pull other generative, AI,
LLMs to the same output. So there's many layers of understanding that
they're going to go into standardization. And then there is that question of
model dependence and economics of retaining access to it over time.
Because like I do with some other things, it's recognizing that everything
we're talking about is absolutely beyond a vast amount of people right
now.

Sarah Clarke - 35:27
$20 to pay for Chat GPT access per month to have some semblance of
control over what you're doing, and access to the enhanced tools. That's a
big portion of disposable income for a whole shed load of people. And it
will be gated for a whole shed load of people who work for someone else
at the moment. It may change at some stage soon. I work for myself, so I
can pay for what I feel is needed to do my job, and no one's going to stop
me using it. But yeah. So all those things I have in mind when we talk
about democratizing AI, in terms of the benefits and the knowledge to
take advantage of it, I think that terminology has been a little bit cynically,
co opted for other purposes.

Sarah Clarke - 36:13
I really do think we have to spread the opportunities from this as widely as
feasible while growing our understanding of where the edges and
guardrails should be. But, yeah, I was just bringing in something from
Tech Target on other proposed uses for it. We both know, Dennis, as we're
exploring here today, that there will be a new use case every second
created for this with the access to the APIs and the more open access
models. And there's a lot of money being thrown at creating wrappers to
have market offerings. Though I did notice that there's a thinning of VC
funding because of the relative openness of the OpenAI APIs and others
now that people are recognizing that the layered value has more ubiquity
now. So there's less sort of unicorn potential in that space.

Dinis Cruz - 37:10
That was my big paradigm shift. My big paradigm shift when I looked at
this is I thought the models were where the action is. So I kind of started
to go deep. And then I realized, actually, the models will become a
commodity in a way, because actually we almost don't want unintended
behaviors from the models. What we want is to really understand what
you can do, is that embedding that data that we feed that becomes way
more important, allowing us to talk.

Sarah Clarke - 37:38
To the world of technology and data. This is a use case. It's very sad, but
one of my most exciting use cases is mapping legal and regulatory
requirements. I want to have an intuitive, rapidly surfaced visibility of
where somebody else is telling me my edges are and where somebody else
is telling me my controls need to be so I can navigate around that and I
can work out local relevance.

Dinis Cruz - 38:06
You see? But that's exactly when I say about translating and connective
dots. I have that problem, right? I need to be able to show the business,
the progress, give them roadmaps, give them map projects and activities.
And I got all these frameworks that I cannot connect, right? And the
frameworks are great because the frameworks allow me to go to the
granularity. What I want to be able to do is to be able to map this control
with that attack vector, with that incident, with that risk, with that
stakeholder, with that project, and be able to say, this is why we're doing
this. Right? And this is the impact of not doing this. And by the way, there's
new regulations come along. By the way, there's this new attack or this
new requirement, or we claim as a company to do ABC, guess what?

Dinis Cruz - 38:47
With this. We are in severe risk of breaking that. But at the moment I still
cannot connect the strategic directions, visions, projects with the controls,
with the actions on the ground.

Sarah Clarke - 38:58
I agree with you. I mean, that lack of connective tissue between doing
something better or right or more visibly or more reportably at the
operational level still doesn't exist to report up in terms of adjustments to
strategic, directional, strategic risk picture.

Dinis Cruz - 39:17
The top has a spreadsheet. We get in there and there's a fucking air gap.

Sarah Clarke - 39:21
Yeah, that's the gap that I try and live in and make a little bit more
connected.

Dinis Cruz - 39:27
But we kind of do that gap. But we do it almost with art. I think we now
have the ability to start to bring science to that.

Sarah Clarke - 39:35
It's risk modeling. It's risk modeling. And prior to this, absolutely what
we've got, were lacking the tailgate of things like cybersecurity and data
protection breaches and risks. We didn't have consistently standardized
enough reporting about all of this stuff. One of the promises of things like
Genai and other models is that you can bring consistency and
standardization out of unstructured data. That's a massive sea change. It
was always promised for big data and various analytics attempts, but it
was never really realized. And that could potentially produce analyzable,
effectively labeled data to enhance our understanding of risk, to build
genuine risk models for a lot more things that have more utility and have
more potential to be aggregated realistically. But I could bore you about
that forever.

Dinis Cruz - 40:32
And we don't have very but that's massive.

Sarah Clarke - 40:36
Oh, it is. It is massive.

Dinis Cruz - 40:37
It's a step change and one of the paradigm shifts I have on that one. When
I realized that Chattypt could translate from Python to JavaScript, I was
like, that's cool. But you can also go from JavaScript to cobalt, and you
can go from cobalt to PLD, assembly to assembly. And I like, whoa, this is
very different. Because then I realized, whoa, all those.

Sarah Clarke - 40:59
Own mainframe guys who they keep bringing out of retirement because
they want to do something else with that stuff.

Dinis Cruz - 41:06
But is that translation and even if it's not 100% perfect, right, we can now
to put some guardrails on that. But is that built to translate, like you just
said, unstructured data to a structure? And then the power is that you can
put other bots in the mix that can give you the consistency, so you can
actually start to reverse engineer things. Right? And we know how to do
that because we can have a bot that goes from A to B to A and variations,
but that now scales because it's a one off effort to create that. And that's
why actually complexity is almost like you want simple things in a weird
way. You don't want a model that goes from here to here. Actually, I want
a model that goes from here to here.

Sarah Clarke - 41:44
There is power in the incremental changes.

Dinis Cruz - 41:47
And version controlled, right? That's the key thing. Version control all
checked in with tests, right? But that in the past was impossible to do at
any kind of scale modeling was impossible to scale. I think now we very
close to be able to start to scale it, which is really cool.

Sarah Clarke - 42:05
Well, this is the slide I'm going to have to explain because I was thinking
about that triage piece that were talking about, which is what we've got at
the moment and what we've always had to an extent is we've not just got
compliance or non compliance, if I'm thinking with my traditional audit
hat on. If we allow for the fact that some control sets make sense once
they're scoped effectively and you understand the inherent risk attached to
them, a privileged access control for your Florist isn't as important as a
privileged access control for your It outsource provider. So you need to
scale what these into context. This is me trying to get feel around the
edges and apportion the amount of uncertainty that we still have and the
amount that we can get across and test for during the normal change or
procurement timescale.

Sarah Clarke - 42:55
Because we both know that a lot of stuff ends up live or lacking the post
market monitoring it needs because of just sheer scales available. And the
inability to surface rapidly to somebody who can make a decision when
there maybe is something that calls for a pause or calls for a little bit more
to be done, a little bit more scrutiny. So I just did a very basic breaking
down across the AI supply chain. Most people are operating in the validate
and deploy space. They're not operating in the acquire train package
space. And we have It general controls, SoC, two type two audits and all
the big four who are used to doing your more traditional audits
assessment scope with traditional security controls, traditional privacy
controls, the governance level, bit of pen testing all sort of live in that
level.

Sarah Clarke - 43:45
Then the orange section is portions of controls that live sometimes
discreetly, sometimes concurrently across those portions of the supply
chain in the real technical testing space. The people who can interrogate
the data and model structure and model design and layered controls on
top of it. And that is a really scarce skill space. So what I was trying to
understand is where does most uncertainty live? And when I say
uncertainty, I don't just mean things that are unknowable. I mean things
that are not knowable. With the expertise available, with the guidance
available and with the time available. It is uncertainty if you cannot gain
clarity. So that was how I broke it down.

Dinis Cruz - 44:32
We're back once.

Sarah Clarke - 44:33
Okay, cool.

Dinis Cruz - 44:34
Stay there. I think you're missing a couple more.

Sarah Clarke - 44:37
Steps here because oh, I probably am. This was nice to make it fit on a
slide.

Dinis Cruz - 44:41
Yeah.

Sarah Clarke - 44:41
Carry on.

Dinis Cruz - 44:42
I think if you look at in the deployment in between your validate and I
think so, imagine, for example, Chat GPT or Claw two via thing, right?
They arrive in a way after the model being deployed, right? It's almost like
you get or Lama two, right? You get that thing already created. Right. But
there's still a lot that goes afterwards that has as much impact, if not
more impact in that lifecycle. I have to say, I think there's a trend where
this becomes compute. This becomes a commodity with some behavior and
the main action happens afterwards where, in a weird way, we might get
to a point where unverifiable and not understood behavior becomes even
more of a bug of the systems of the models where we start to prefer
models.

Dinis Cruz - 45:41
And you can already see this a lot of people, where they go, well, we play
with Chat GPT, but we use 3.5. We even use this smaller one, which,
although it might not be as powerful, chat GPT, the way you can see it and
the way you can give it the prompts becomes a lot more predictable, a lot
more still does the same input and output that you want, but without the
extra baggage.

Sarah Clarke - 46:01
It's interesting, the news about the Aracus, isn't it? Not releasing the
smaller models OpenAI? People are very interested in why that might be.
But, yeah, there's going to be a lot happening in terms of boundaried
models, bespoke models.

Dinis Cruz - 46:22
Open source will drive that. Right. Because now that we have enough
models and remember that a model is a bunch of numbers, right? That
sometimes a model literally is a matrix. Right? Okay. It's more complex
than that. But fundamentally is this frozen thing that you then ship, right?
It's just a bunch of mappings. I think you need to add to here is what you
do with it, right? And the prompts, but also the controls that you can put
in the middle that make a big difference in that workflow.

Sarah Clarke - 46:54
I think what I'm trying to do with this always decided to do it all by itself.
Okay, but just to put in context what you were saying, Dennis, one thing
that I've always wrestled with is persistence of accountability through
supply chains. We've always had a challenge with that. Each downstream
vendor gets about 1700 different flavors of third party assessment tracked
at them. That they more or less busk or robustly, give you an I 27,001
certificate that's just for physical controls in their canteen, for instance.
Other more diligent ones. Yeah. There is a cottage industry of conducting
running workflow to get answers back for 100, 200, 300, sometimes 1000
questions from each vendor up and downstream. Massive economies of
scale to be had in that space. There needs to be collaboration.

Dinis Cruz - 47:50
I'm going to use your analogy of asset 27,000 for the kitchen.

Sarah Clarke - 47:53
Yeah, exactly. But we're looking at trying to tackle some of this with things
like Sbomp, with the software builds of material, the evolving AI builds of
material, the model cards coming through, it's got to better than that. So I
was thinking, how could we do that if we can get a credible estimate of
the degree of uncertainty that's come to you through the supply chain,
through the portion of controls that are controllable and controlled at that
portion of the supply chain prior to you receiving it could actually
translate into contractual liability. It could translate into regulatory
enforcement of accountability. I can't think why anyone would sign up for
this, but it says potential here. And when I'm talking about levels of
compliance, I mean, we know that compliance and risk don't mean the
same thing.

Sarah Clarke - 48:44
I'm using very basic audit principles for those levels, which is you tell me
it's compliant, but I've just got your word for it. I have no idea if that
control exists or if it's working.

Dinis Cruz - 48:54
Okay, but are you talking about the third party, let's say, supply
assessment, which I think is a great thing, or are you talking about the
previous slide on the model?

Sarah Clarke - 49:03
I'm talking about taking a It's control set. Agnostic. If you took all of the
things in the codes of conduct for, say, the Euai Act, once that's finalized
and spat out, you could do a rapid assessment and it would be based on an
evidence promissory note. You're not going and trying to do an audit on
everything before you can actually make a decision about acquiring it or
rolling it out. What you're doing is you are seeking assurance about
whether they can provide evidence level of compliance. You're at.

Dinis Cruz - 49:36
You talk about the AI models, I'm.

Sarah Clarke - 49:38
Talking about supply chain. There would either be answer you can get or
answer you can't get. If you can't get answer, it's unknown. If they say, we
don't have that control, it's non compliant, great, you can do that.

Dinis Cruz - 49:52
Okay. There's some same thing. You're basically saying, let's really scale
up how we understand and analyze third party vendor assessments in a
way. Okay, but that's exactly my thinking here. Right. Like, I want to use
Gen AI for that because I want to say, here's our standard, here's the stuff,
here's the questions, here's the context, now analyze that. Right. And I
think that makes this realistic. In fact, even better. In fact, I was just
talking about this with my team. Even better. We can eventually create a
bot that we can give the supplier with a freaking roadmap for what they
need to people.

Sarah Clarke - 50:30
Yeah, there's people who are doing something. There's an awareness
raising and escaping element of this as well. Obviously, there's a lot more
to this. This is my Mickey Mouse slides. In my rapid time I had available to
do it, but this has evolved from stuff that's years and years old. People like
Credo AI do a readiness assessment that produces this kind of visibility.
You've got Magda Celli with her third party risk management solution
over in Singapore. She's doing an awful lot of open source available
information to assess strategic supplier risks, stabilities financials, what's
been said about them in the news, what breaches they've heard about to
do with them, as well as the inside out staff.

Sarah Clarke - 51:10
As well, you've got people like Riskledger who are creating social
networks for vendors where they can each share a selection of their
evidence of compliance or risk management. And it means that they can
construct supply chain views. Where you're going to get 3rd, 4th, 5th party
who's connected to the first party. It doesn't mean they tell you everything
or they disclose everything, but it still gives you less to assess around the
edges. In the same way we're talking about.

Dinis Cruz - 51:40
Gen AI gains, you need to add gen AI to the mix because you go back to
the previous point is the touch points between the systems that become
really hard, that don't scale. And I think that's the problem those
companies are having is they can all get to the point. But then for that to
be actionable, for that to actually start to put into context, you need to
start to connect in the dots and ask questions in ways that are consumable
from either side.

Sarah Clarke - 52:05
Absolutely. The utility for something like this is just to really as a
provocation, everything is about managing risk. Everything is about what
you can gain visibility of promptly. Everything is about what you can
automate versus have to chase manually. And at the moment, we're
dealing with sufficient uncertainty and sufficient difficulty surfacing the
control reality for the things that we're plugging in, that we need to
acknowledge that uncertainty. Uncertainty isn't a showstopper, it's just
something that it's better to understand. And of that, 64% of controls with
either not more than a show and tell for compliance or we don't know or
it's non compliant. Where do they live in the supply chain? Do they live in
the deep detected controls or do they live in the procedures? Do they live
in the model training or do they live in the deployment?

Sarah Clarke - 52:57
Do they live in the post market world? It's really just trying to locate your
uncertainty to focus your effort for deeper assessment and focus your
effort for trying to handle your residual risk.

Dinis Cruz - 53:08
But here's where I think the opportunity lies for privacy. For example,
imagine me being able to do a privacy assessment based on my specific
requirement, based on my specific commitments and by level of privacy,
let's say understanding of the company to our suppliers where I can get
this level one to five. So I'll probably have suppliers that today have flying
collars. Marketing materials are awesome, they look really shiny. But once
we do these assessments, we realize they're not managing our business.

Sarah Clarke - 53:36
Yeah, once you keep the tires privacy.

Dinis Cruz - 53:38
Risk, but that today doesn't scale because we cannot customize.

Sarah Clarke - 53:41
No, there's no sweet spot that anybody who's done third party risk
management will know there is no sweet spot between looking someone in
the eyes and actually getting evidence put in front of you versus just taking
their word for it. There is no half verifying level. You may as well get some
honesty about how mature they are and whether they've got a control in
the first place because then you can work together to improve things.

Dinis Cruz - 54:03
But imagine a model where you can say here's the bot that has now been
trained in prompt for this specific data. We can even say, look that's fine,
the data will not leave your company, but I want the output of that. And
then I think the conversation would change very quickly because there are
elements.

Sarah Clarke - 54:19
Of this again, it's looking at the discrete pieces where you can get
defensible, reliable reproducible gains. It's always about that this is where
we want to get to. You're talking about talking to executives and boards.
If I've got a decent indication that I can surface rapidly of their capability,
maturity in terms of do they have anyone that understands the specifics of
models? Can they even start to get across it and understand their own risk
profile? And they're doing something that is going to be pointed at lots of
vulnerable people. That is a very proximate risk. It's going to lead to high
impact decisions very quickly. It's going to scale very quickly. Then as a
guide, you're going to either pause or you're going to put in a heck of a lot
of very responsive post market monitoring. So you have rapid feedback
loops.

Sarah Clarke - 55:11
If it's medium risk, if you're doing something that could potentially have
some impact, maybe it's to do with a little bit of an enhancement to
insurance claims using AI, but it's not going to move the needle massive
distance, but it could have a reasonably large impact on people in terms of
having claims rejected or approved. You could pause and get some deeper
dives for validation focusing on where you've got higher uncertainty or
higher levels of non compliance base, most likely to be uncertainty. If it's
low risk, if you're just doing something like putting together an attack gen
model, that's going to be something that you're going to refine and it
could be really useful but it won't be the only tool in the armory and it's
not going to materially affect your response to breaches, et cetera.

Sarah Clarke - 55:55
It's going to be a positive addition that you can pull out or not. Then why
would you not mature and learn about the tools and et cetera and mature
in parallel? The thing we've got at the moment though is we've got a lot of
things being viewed as ethically tolerable justifications to move forward.
Regardless of where you sit on this.

Dinis Cruz - 56:13
Picture, the business wants to take the high risk.

Sarah Clarke - 56:16
Yeah, that bothers me. So I mean this is just to close up and then we can
get into whatever you like. Is we need to know what it is and isn't. We
need to have some taxonomies ontologies categorizations so we can all
have a conversation where we're talking about the same stuff. We are
starting to surface some useful things in terms of groups of use cases that
come with more or less inherent risk. We are starting to pull out some
tasks that it's more or less suited to depending on the model and model
maturity and we're starting to get some understandable language around
model types and model function types. We need to make spaces, low
impact spaces to do high impact things potentially safely.

Sarah Clarke - 57:00
Obviously we've got regulatory sandboxes but we need to be careful that
we're learning lessons from that and it isn't simply rubber stamping those
things with greatest market potential. It has to be innovating in the
governance space as much as it's innovating in the monetization space.
And I think we've got a little bit of an imbalance there. We need to have
those feedback loops at the moment, the place where algorithms and more
sophisticated machine learning are being used that worries me the most is
things like benefits, entitlement, health care access, that kind of thing.
Where I feel that we haven't evolved to detect, monitor, log feedback
surface aggregate rapidly enough on those non standard cases, exceptions
and potential attrition out of systems when it comes to post release.

Sarah Clarke - 58:06
And I do think we may be at risk of the outsourcing effect where people
are very focused on removing fragile people from the equation is going to
be one motivator in some spaces. It's very easy to understand that if you
can be far more productive maybe you need less people. And when I talk
about not overzealously offboarding your domain specialists I don't just
mean your sort of superstar rock star developer I mean your people who
really understand some of your most basic tasks inside out. They probably
know intimately why it works, why it doesn't work, what could be done to
change it.

Sarah Clarke - 58:44
I think regardless of whether or not it's AI that's used to do it, I think we
have an opportunity to learn from our people again, because I think there
are a lot of them inside organizations who could tell you tomorrow how
you could save a lot of time and effort. And I think it opens the door to
those conversations again. And that's my last word on things. I think really
we can't ask people to be accountable for things that they can't influence
or they don't have sufficient information to understand. So we need to be
having better conversations in this translation space and servicing better,
simpler information faster in these processes and really being creative
about how we bring that information to the fore.

Dinis Cruz - 59:27
That's for me is the opportunity. I think the same way that the internet
brought global connectivity and I think the same way that we can do zoom
now is all this stuff right? I think. This new transition or new technological
jump allow us to do the things that we just described in a scalable way.
Because I think the problem in the past and then even when you try to
regulate it doesn't work because the overhead to do some of those things
actually in a weird way had the perverse effect that almost rewards the
ones that can do it better. And I'll give you a simple example. There's some
ancient argument that says this means the elite is going to be even more
elite. This means that there's a lot of things that if you're really good, you
get even better.

Dinis Cruz - 01:00:14
I think it's the other way around. I really love the threads about how this
new generation can help Africa, can help underrepresented minorities and
other groups that suddenly you don't need to go to Cambridge, Oxford,
get access to a certain degree of education, certain degree of knowledge,
certain degree of information. And in fact, even better, we can now create
personalized individualized training paths. Training knowledge that
reflects an individual instead of treating our kids as freaking almost
robots, almost designed it's almost like the training the school system was
designed to deal with the inefficiency of how do you measure progress,
right? And you have exams who suits only one type of individual, right?
Which they can do really well, but the other don't, right?

Dinis Cruz - 01:01:01
So I really like this idea of spreading almost talent pool in a way of
providing knowledge that allows a whole raft of individuals to enter a
certain type of workload that before were just not possible because they
didn't had the opportunity. They were in the right place, they were born in
the right postcode all sorts of things or the right country to give those
opportunities. And I think that's very interesting. Like teachers, right? So
people said we don't need teachers. I'm going we need even more teachers
because teachers are the most important people in the education. They're
the pivot points, right? An amazing teacher makes a whole difference,
right? So suddenly we can now remove a lot of the overheads from the
teachers and allow them to teach, allow them to think about education.
And it's the same thing with teams.

Dinis Cruz - 01:01:47
I'm telling my team, if they're not spending 20 30% of their time figuring
out how to work more efficiently, whatever they do in the other 70% of the
time is actually not going to be that good. Now, I think there's a number
of individuals that are going to be resistant to change and for those I don't
think we can do a lot, right? And they're going to move and then maybe
they wait and then they move at the end. But I think there's a whole talent
pool of individuals that would love to have opportunities that don't have
today, I think can have with this new ability to learn in a much more
personalized way. And if you look at, I think, a lot of things that we see in
corporate environments.

Dinis Cruz - 01:02:26
We see lots of companies getting away with things that they shouldn't and
they only get away with it because there's no visibility, there's no ability to
scale that information out of the company. And I think we could do that
now in a way that scales a lot more, that brings a lot more transparency,
that rewards the good behavior because that's the best way to ratchet up,
right?

Sarah Clarke - 01:02:45
Well, actually, this is one of the things that I found worked when I was
building a massive vendor governance program. I was surfacing enough
information to give the accountable people for ensuring there was time,
engagement from their people because it takes a village. You know, I
needed to have legal across it, I needed to have procurement across it, I
need to have claims team across it. And they started to take pride in
having the best risk profile for their department. And they started to
resource better, they started to contribute into the budget for the vendor
governance team and they started to call us before they went to supplier
selection. I mean, as far as I'm concerned, that's the gold medal for a
governance function.

Sarah Clarke - 01:03:28
And I had know, you had the old conversations know, I delegate security
and privacy to you because it's your risk to you know, I was having
directors who piped up of their own accord and said, excuse me, Jack. No,
it's not her risk. It's your risk that she's helping you to understand so you
can manage it. And she can't do that unless you play. And that's the whole
ballgame for me. It's that understanding collaboration, it's turning critics
by careful conversations into advocates and it's enabling them to make
better decisions by having better, more prompt information to make the
decisions. That's what motivates me.

Dinis Cruz - 01:04:09
I agree and I think that's an opportunity. Right. And I think unless the
models dramatically improve at some of the end and I think some of the
flaws of it are so big that I'm not sure how that will work.

Sarah Clarke - 01:04:22
We have to balance the hype so we don't lose the promise.

Dinis Cruz - 01:04:26
Exactly. Right, but that's why it's like the internet if you think about it, the
internet, there was a massive hype, there was a crash, but underneath the
change was real. Right.

Sarah Clarke - 01:04:34
And it's making sure that we nurture those spaces and bring a really good
cross section of people into those spaces where there's consistent, level
headed, but exciting work happening. And that's, I think one of the
challenges. But I'm going to be really bad note. I have to go because I had.

Dinis Cruz - 01:04:52
Something else me too, I need to drive.

Sarah Clarke - 01:04:54
No, but I've thoroughly enjoyed and I'm glad we had a bit longer than you
suggested. It was really ambitious scope for this.

Dinis Cruz - 01:05:01
Thanks for the preparation. Really great. And let's keep now this path
because I think we feel that there's a lot of interesting work to be done
here and we can finally fulfill the privacy and risk promise of actually
allowing the business to accelerate and to make good decisions and allow
see, I want to make good privacy decisions on my supply chain. And at the
moment, I can't because I don't have the data. So I want to use our own
effort and muscle of a big supplier to go, no, we want good practices and
push security downstream. Right. Which is, by the way, it's happening. We
now have some big requirements from massive companies, which I like,
right. I go, hey, I'm going to be compliant to those guys. Right. It works
when the best players push down, push down.

Dinis Cruz - 01:05:46
You just raise the bar for everybody else.

Sarah Clarke - 01:05:48
Yes, definitely.

Dinis Cruz - 01:05:49
Brilliant. Please share the slides and we'll take you to the next one.

Sarah Clarke - 01:05:53
Okay. Thanks, Dennis. All right, bye.
