---
title        : DATA Driven approach on vulnerabilities Appsec vs Infra (Panel)
track        : Governance
project      : Risk and Governance
type         : working-session
topics       : Recruitment, Talent Acquisition
featured     :
event        : mini-summit
when_year    : 2023
when_month   : Oct
when_day     : Fri
when_time    : WS-17-18
hey_summit   : https://www.linkedin.com/events/datadrivenapproachonvulnerabili7118644187322888194/
session_slack:
#status      : draft
description  :
banner       : https://github.com/OpenSecuritySummit/oss-website/blob/main/content/sessions/2023/mini-summits/Oct/banners/data%20driven.jpg?raw=true
organizers   :
     - Francesco Cipollone
     - Jay Jacobs 
     - John Kinsella 
     - Mike Shema 
     - Chris Madden 
     - Marius Poskus
      
youtube_link : https://youtu.be/BaETCQTnr8k
zoom_link    : https://us06web.zoom.us/meeting/register/tZclf-qprzIoH9V84Td6Tz77XiYPlxGmr7vv
---

## About this session
Navigating through the pulsating neural networks of cybersecurity, this session brings to the fore a meticulously crafted exploration into a DATA-Driven Approach towards understanding and mitigating vulnerabilities in both AppSec and Infrastructural security spheres.

Vulnerabilities are more than mere code anomalies; they are the conduits that can potentially unchain a cascade of unwanted cyber events. In this awe-inspiring panel, join a squadron of cybersecurity mavens who will steer you through an introspective journey deep into the core of vulnerability complexity, reachability, exploitability, and the dense fog of contextual risk.

## 🚀 Key Takeaways:

Unveiling Complexity: Dissecting vulnerabilities to comprehend their intrinsic and extrinsic complexity.
Psychology of Risk: Unmasking the psychological underpinning that influences stakeholders and drives critical security decisions.
Diverse Vulnerabilities: Traversing the variegated landscape of vulnerabilities, exploring their diverse nature, and approaching mitigation with perspicacity.
Dimension of Risk: Engaging in a riveting discourse on deployment amidst diverse risks, and tactfully managing them in the volatile cyberspace.
The session promulgates an enriched discussion that intends to shift your perspective from merely dealing with vulnerabilities to strategically navigating through them, with a DATA-driven compass guiding the way. Whether you're an Application Security expert, an Infrastructure Security professional, or a cyber enthusiast keen to expand your knowledge horizons, this session promises a blend of expert insights, tangible takeaways, and a forward-looking perspective on dealing with vulnerabilities.

Prepare to launch into a session where data meets depth, and experts decode the enigmatic realms of vulnerabilities in Appsec and Infra. It's not just a session; it's an expedition into the future of secure, savvy, and strategic cybersecurity.

## Transcript:
Francesco Cipollone - 00:02
Denis, do you want to do the honor of introduction or shall I kick it off?
I'll do the honor, everyone. Thank you, everyone. For a very long session
on Summit, I've been talking about data and data driven approach. So we
have a fantastic panel that probably span and cover every possible aspect
that you want of an organization, from application security to cloud
security, to vulnerability management, to data driven approach to data
science and CISO. So we have the best representative in here to discuss
around the table on how to best approach vulnerability management from
application security, cloud security infrastructure and traditional
vulnerability management across the board and a data driven approach
on this.

Francesco Cipollone - 00:52
Before further ado, I want to start and ask all the panelists to do an
introduction so that for the very few people that don't know you guys and
I'm going to go in order, they're going to know who you are and what
contribution have you done so far. And you will, Mike, you're the first in
the list. Thank you so much for coming. Welcome.

Mike Shema - 01:15
Thank you, Francesco. This is exciting. To be real quick right now, I work
at Block on their product security team and I'm also co host of the
Application Security Weekly podcast where we talk about all types of
things, vulnerabilities, and hopefully more than just vulnerabilities, which I
think we'll explore a bit more in this session.

Francesco Cipollone - 01:34
Brilliant. Jay, up to you.

Jay Jacobs - 01:38
Jay Jacobs. I am the co founder and data scientist at Scienti Institute,
doing a lot of research and publications in the security space. Also the co
creator of EPSs, the exploit prediction scoring system. And I think I'll just
leave it.

Mike Shema - 01:54
There.

Francesco Cipollone - 01:57
Just a tiny bit things that was Epssed in the last year. Thank you, Jay. John.

John Kinsella - 02:05
Good to be here. John Kinsella. I am doing a whole bunch of different
things right now. I spent this year doing a bunch of independent work for
startups, application security, working with some VCs and private equity
more historically. My background is in application security, container
security, cloud security, most recently as VP of Engineering at Qualis for
their container security products.

Francesco Cipollone - 02:27
Happy to be here.

John Kinsella - 02:28
Also, I'm the other co host for Application Security Weekly.

Francesco Cipollone - 02:33
Radiant. Thank you very much, John. Chris, after you.

Chris Madden - 02:37
Hey, Frank, it's an honor to be here. I heard they kept the best session
until the second last. Rumor has it you may be able to confirm that. Yeah,
I work at Yahoo Product Security. My name is Chris Madden and my
overall existence, or point of existence, is to optimize the flow of software
to our pipelines versus security risks. So I have a deep interest in all of the
things that we'll be talking about here as a practitioner.

Francesco Cipollone - 03:08
Brilliant. Thank you very much. Marius, over to you. Hi, guys.

Marius Poskus - 03:13
Good to be here. So, my name is Marius. I'm global vice president of
Cybersecurity for Go Financial Services.

Francesco Cipollone - 03:21
Brilliant. All right, so we're going to structure the panel, start discussing
around different area and aspect of how modern organization works. And
I think what I've seen so far is organization works either in silo way, so
application security, infrastructure and cloud security. We want to break
this meat and bring across the panel today all these aspects and connect it
with risk and executive view and the metrics that matter. So we're going
to start on this very easy topic between application security and
traditional vulnerability management, between Mike and John. What is
your opinion on how we've been attacking the problem so far and how is
this problem evolving in this modern age? That is a data driven modern
age.

John Kinsella - 04:14
You want to go first?

Mike Shema - 04:15
Sure, yes. I think we have been attacking the problem, I think of so many
vulners that attackers don't care about and maybe I'll kick it off like that
because we have so many SAS, dast IST sea. We have so many ways to
find vulnerabilities. It's wonderful, we've got great observability, but then
we turn that around and say cool AppSec thinks we should fix all the
vulnerables or because it's kind of one of those easy metrics to track. And
I think one of the things I'd like to especially talk with John about is
there's all sorts of volumes that are cruft clickjacking CSRF Redos, lots of
low impact or no impact XSS. I think some things that I'm kind of hinting
at that some other panelists are going to pick up later on, but all of this
comes at an opportunity cost as well.

Mike Shema - 05:07
There's so many more interesting things that could be done and I'll tease
John a little bit. I love to talk about refactoring and rewriting code, but
instead of just refactoring code, we could also actually be working on
features or focusing on the features in the software we're building rather
than all the dependencies that we're using.

John Kinsella - 05:26
There's the concept of so I'll try to address this with the engineering
management hat on and if you think about application security, a lot of
our just think about applications start there first. Frequently when we
think about features, we're thinking about what are we designing and
developing for our customers, whether that's an internal customer or a
public customer, they're paying in one way or another or we wouldn't be
here. But there's also the features we can be creating from a security point
of view and those could be something simple like how to make sure this
application is easier to check if it's secure or is it being attacked or things
like that.

John Kinsella - 06:00
So I think what we've seen, Francesco, is going from that point where
we're just purely whack a mole when back in the day there was just
enough moles in a room that we could count them and play Whack a
Mole. And I think a large portion of what we're going to be talking about
here is as that number has grown to this crazy scale. We ain't got enough
hammers, we ain't got enough people, it's not going to work. Right, so we
can't have a top ten list for everything. So how do we actually focus on
what we want to do here and narrow that down? So I think that's what
modern AppSec is about.

Francesco Cipollone - 06:32
Yeah, no, I do agree with your point. There seems to be, though, still the
affection top ten lists. We had the top ten LLM vulnerability OAS top ten
has always been top. We had the top vulnerability exploited or the top
methodology of vulnerability exploited. And when it really matters what
are a little bit from an upset perspective, the metrics in the old age, I think
Mike touched it a little bit on before and in the modern age, that matters.
And I think I want to then after later on, ask the same question to Chris
because I know he has a very good opinion on it. So it's going to make a
very good discussion point. Mike and John, over to you.

John Kinsella - 07:19
The way I think about this. And I'm not going to look at a pure metric to
start. I'm just going to look at the concept of where we're around, which is
it starts thinking about asset inventory, which we're 2030 years into
security, maybe 50, pick a number. But we still don't know what the hell
we're securing in many cases. And where I want to do is pivot that to an
application security point of view. Some of the more modern tools, which I
like out there, that you could call them scanners, are not giving me that
list of every asset and every vulnerability on it. It's what can an attacker
see and what can they actually compromise or actually have some sort of
effect on? That gives me more where I'm going.

John Kinsella - 07:58
This is I want a list which is I want a metric which is something I can
execute on, something that's manageable, something that I can make an
actual difference, not just in that number going down, but in the security
of my product. So that's the way I think about it in general, I think, is
what our listeners are going to see here as we talk through this is there's
no one metric which is going to be perfect for everybody. Depending on
where your application is, what type of end team you have, or how your
company is set up, there's going to be different metrics that will have a
better representation of the state of security of your application.

John Kinsella - 08:36
So I think Mike probably going to look at this from a slightly different
point of view, but I like to think of it just I'll leave the actual numbers and
things out and let's look at the high level and then start focusing down in
okay, what does that mean for me?

Mike Shema - 08:49
Yeah, and I want to piggyback on that by extending that aspect of what
are we trying to communicate and how are we communicating with
metrics, et cetera. Probably the only thing that bugs me a little bit more
than Top Ten lists is metrics that use pie charts. So hopefully there's no pie
charts in the rest of this panel. But the reason I picked that up is if we look
at I'm going to just pick on the top ten API. For example, it has broken
authorization in so many. It has three or four items or just broken
authorization. And there's a nuanced taxonomy. But how much of this is
actionable? And I think that's what I wanted to hit is the top Ten list giving
the developer something actionable?

Mike Shema - 09:27
Or are we just talking about the taxonomy of this is a type one cross site
scripting. This is a type two, this is the type of cross site scripting that is
blue. Developers don't care about that. They care about what is the
impact to a degree. Meaning, how should I prioritize this, but should I be
using a same site cookie? Should I be using is this actually input validation
or is it really an aspect of access control or an RBAC application? Or we
should be using encryption in a different application layer encryption. And
I'm rattling a couple of these off randomly to highlight, basically
developer activities that don't really get called out in those top Ten lists.
They get called out if a Top Ten list says Insecure Design.

Mike Shema - 10:13
That's a little too vague because if you just invert that and say you should
have secure design. Secure design doesn't mean you don't have any
volumes. It means we have to have a longer conversation probably than
we have time for now.

Francesco Cipollone - 10:26
And how do you measure that upstream and downstream? How do you
measure the effect of security design? And how do you inform security
design? But we don't want to offend the OS Top Ten 2021 with security
design making the showcase and appearance. But I really like what you
said on the actionability, and I think from a security perspective, we get
even stuck on the naming convention because we have CVE, CWE, Mitron,
Attack, CAPEC, and The Promise. A lot of these are even disconnected
from each other. So we have domain of information that sometimes don't
translate to engineering. Do I need to upgrade a cookie? Do I need to do
input validation? What do I actually need to do with this? But on that
subject, I think you're.

John Kinsella - 11:09
Working on a top ten list of metrics there.

Chris Madden - 11:14
Please don't with pie charts.

Francesco Cipollone - 11:20
Top ten pie charts that are most hated in the community. But on the metric
subject, we often debate with Chris on which metrics are actually more
measurable. And we've done fairly modern studies, and I really love the
approach that Chris has done from a pure data driven approach. And he's
speaking to several conference about his approach and the data effect
that he's seen, but without singing the praise too much. Chris, over to you.

Chris Madden - 11:51
Tell us frank, please, if you can keep the mic, if you're willing to sing a few
bars, then go for it. I won't steal your thunder, but no thanks, Frank. Yeah,
so let's maybe for context, I'll start by describing where we came from and
these points will probably resonate with a lot of folks in development
environment. So what we had when we started, we had a mature new
vulnerability management capability run by my rock star colleague Lisa
for many years. And it basically triages new vulnerabilities and makes
decisions about know when they should be fixed by priority.

Chris Madden - 12:29
And we use it as a first pass triage, a bit like in a kind of medical know,
there's always a first pass triage done before you get into the more details
and a second pass, and it's a first pass triage for CVEs and the things like
the asset impact, the reachability, the remediation, all of that comes in as
a second pass. All right? All those things are important. We talked about
asset inventory earlier on. All these things are important. The business and
runtime context for understanding the overall risk, that's kind of the end
determination. But when you don't have enough hammers to do the whack
a mole, you want to do a first pass triage to decide, well, okay, which ones
do we go after?

Chris Madden - 13:13
So the first pass automated triage was weren't using CVSS scores, even
though most of the tools in our desktop ops pipeline report them, we don't
use them. We use the CVSS base score parameters and other input data.
This flow was based on a flowchart. And one of the things was that
exploitation was a key decision node in the flowchart and that's what
Sysac recommends. But many practitioners don't use the whole
exploitability aspect when they're prioritizing. And the output numbers,
this basically were an SLA. It wasn't high severity. Do I need to fix it now
or later or whatever? So that was kind of what we had. In addition then,
Frank, you would have mentioned about Silos and we had a mature
DevSecOps pipeline with several tools across the stages.

Chris Madden - 14:06
But we wanted to bring the tools and the teams and the data together to
inform risk. And that's an important aspect as well. Risk doesn't exist in
isolation and there's different tools and teams involved in detecting and
remediating risk across the pipeline. So we wanted to bring all that
together and in trying to come up with a solution, we looked around about
what was out there and we know newer things like Sys, what's that, how
can we use it? EPSs that Jay will talk about and various other data
sources. And we wanted to know, okay, we have internal data, we have
about exploitability, we have our tool data and then we have external.
How do we combine all that into something that gives us that first?

Chris Madden - 14:49
Past three azure Risk so we can whack the right mold and some of the
things we wanted out of that. So we want to combine all these available
data sources to inform risk beyond the CVSS score. And as part of a B
sides presentation early in the, you know, presented this risk taxonomy,
trying to put all these elements together to give a user guide orientation to
what they do and how to use them. We wanted to share the data and the
risk based prioritization across the tools and the teams within our
company. So we standardize on that. We wanted to understand and
validate whatever solution we come up with. And this is important. Any
tool I use, whether it's for risk prioritization or for scanning source code, I
will always benchmark it and make sure I understand and validate it.

Chris Madden - 15:43
As a product security engineer, it's on me to ensure that I'm asking
developers to fix the right things. I talked about my point of existence is to
optimize the flow of software versus security risk. So it's on me to
understand these tools. So we needed something that was understandable
not just by the techies, but by the executives. If something is ranked,
whatever zero or high, what does that look like? It needs to be
immediately understandable to both the techies and non techies. So then,
given all of that, where were coming from and what we had and what we
wanted, we landed on SSVC. And the key part about SSVC it's decision
trees. The SSVC was originally developed by the smart folks at CMU Sci
and it's now been run by some of the same smart folks within CISA.

Chris Madden - 16:41
And it's a way to given different input data sources around about
exploitation and automatability and technical impact to rank
vulnerabilities and in our case, CVE. So pretty much what we had all of
the goodness of the SSVC decision trees. But it wasn't a decision tree, it
was a flowchart. And I really liked that. With a decision tree, one, it's
immediately understandable, they're super understandable versus a
complex flowchart. And two, you can validate them. You can get code to
generate decision trees or validate does your decision tree make sense, so
you can validate them automatically as well. So yeah, it wasn't a big step
for us to go from our flowcharts to our decision trees. And yeah, that's
really it.

Chris Madden - 17:35
And at the end of the day, people need to understand of all the
vulnerabilities, which ones are the most important, which ones do we need
to fix first and why? The why bit is important and understand that this
actually makes sense. It isn't some black box spitting out a number and
you have to blindly trust it. As I said, given my point of existence, I
struggle with that. So that's kind of the journey to decision trees and
SSVC for first pass triage of vulnerabilities so we can whack the molds
that we need to whack.

Francesco Cipollone - 18:14
And focus on the critical that are actually critical because not all the
critical are critical.

Chris Madden - 18:18
Indeed, absolutely. Yes. Focus on the real criticals. Would the real criticals
please stand up?

Francesco Cipollone - 18:28
As you mentioned two or three data sources because not all the data
sources can add value and sometimes can add noise and some others are
interchangeable. And we've seen that with the research data that we did.
Some others are more trustworthy. If you scrape GitHub, you might find
9998 potential POC, but of that number, just 400 actually have high
exploitation and verified exploit. And I really like your approach on SSBC
that is getting a little bit more granular and taking the various data
sources to actually go in that decision tree and making it as a framework
base so that you can insert some of these data sources that you consider
trustworthy.

Chris Madden - 19:14
Yeah. And it turns out if you look at the data sources that are the best
indicators for exploitation, and if you kind of rank them like that, if you
start off with, say, internal data, if there's something shows up in your
book, bounty or incident response, the numbers there are let's say an
order of magnitude is in one. It could be one to ten in terms of
vulnerabilities. Then you have things like Sisikev actively exploited, but not
in your organization, but in the wild population 1000. Then you get into
like EPSs and certain thresholds. The numbers become slightly bigger
depending on your threshold. But it doesn't suddenly jump to 200,000. It's
a more manageable figure. And then you have things like active
exploitation is the CVE in Nucleus or Metasploit, two k, three k
populations.

Chris Madden - 20:03
So the populations interestingly gradually increase in terms of if you walk
down the likelihood of exploit, then you get into active or sorry, exploit
available and then the populations then kind of explode. They're less
useful and there's more of them as indicators of exploitation. When Sister
says use the indicator of exploitation for your risk management.

Francesco Cipollone - 20:31
Brilliant. And those are all I like the fact that you end up going to a matrix
that is both understandable as priority one, two and three as a single
number that can be made a decision on and it drives away from pure SLA.
That is, I think an approach that I like originally, but it very quickly
showed a weakness in term of approach because it's flat and it doesn't
have all that contextual aspect that you mentioned. But on that subject, I
wanted to involve a little bit more Marius and what is his opinion about
the metrics from his perspective that really matters when talking about
vulnerability, risk and all these aspects? What's your think?

Marius Poskus - 21:13
You know, it obviously depends where your vulnerability program sits. But
the first and I guess the foremost and most important metrics that you
start with, as John mentioned, so obviously asset register, asset criticality.
So obviously that allows you to determine and gauge risk because
obviously crown jewels obviously will have a different risk than someone's
receptionist laptop somewhere where does not have access to critical data.
So that's an important start. Then we go into software list as well. So you
know, who owns particular parts of the software, what kind of enterprise
software do we use? So you start with two registers and then we can start
iterating and translating that into risk language. So I guess as we talk
about exploitability and all of that all comes down to the risk.

Marius Poskus - 22:03
So I normally like to split it out so you can start trends between business
units. So which business unit is carrying more risk than another one? And
I think metrics is important but as we are changing and we are rapidly
moving at this speed and agility nowadays we can't keep whacking a mo.
So I normally now change a bit the perspective and how we do things.
Obviously it starts with a top down approach and support of the
vulnerability management program to give you authority to actually
change culture within organization. Because normally the thing is culture
is not something that you can implement overnight. Anyone who started
doing DevSecOps know it takes twelve to 18 months to get it anywhere
near where you want it to be.

Marius Poskus - 22:53
But what I like is and what I talked about business units and trends
between the risk, I like to see trends in those risks because to me if one of
the business units are trending up, yes, we can do whack a mole based on
risk prioritization and solve vulnerabilities. But obviously if there is a
trending up vulnerabilities, something is broken. So we go to root cause
and analyze whether there is broken business processes, whether there is
patching that doesn't work and hopefully sometimes to get it off the
ground it's much harder and it takes much more work but I feel that over
the long term yields much more benefits. If we can fix the broken
processes, how do developers code and how can we improve their coding
practices instead of just fixing vulnerabilities and creating tickets for them
to fix them.

Francesco Cipollone - 23:46
I do agree and I like that approach on historical trends and also seeing the
thing that matters for two reasons because you can give business unity
ability to operate at specific risk level versus another risk level. So
sometime risk reward opportunity, you might want to release a bunch of
feature because you might go out of business tomorrow if you don't
release those things. And hence vulnerability and even the critical risk are
actually not the most critical things on your table and being able to adjust
your approach on a risk based perspective is really powerful. So I really
like that and I.

Marius Poskus - 24:23
Think it's very important to understand the business context because your
business context will dictate how you solve risk. Because if you look at for
example any young company who trying to grab a large market share,
they might have a much larger risk appetite because obviously they need
to grow and operationalize their product and grab as much of the market
share. When you reach a certain level of maturity, you will bring the risk
appetite down.

Francesco Cipollone - 24:54
I do agree. And in some of patterns and trending have you find any
behavior also understanding and making the business unit compete as a
driver to actually drive down risk or drive down vulnerabilities? There a
psychological aspect in making team or business unit compete with each
other.

Marius Poskus - 25:16
Yeah, and that's the thing. It depends how I guess there's a couple of
angles you can do. You can gamify a lot of it and create a sort of healthy
competition, but it's a very fine line between competition and obviously
becoming a toxic. But I guess the important part of it is create an
understanding, create a relatable training and structure of understanding
why these specific risks that we have. Why do we need to solve these
specific risks and what's the impact? And I feel that's where normally is
the disconnect between especially if we talk with development teams,
sometimes we just tell them go and fix this vulnerability. But unless they
are given the context and understanding of why do they need to fix that
vulnerability, the chances are it creates a learning curve where you might
not see that vulnerability in the future.

Marius Poskus - 26:05
Instead of just whacking a ticket and say please solve it.

Francesco Cipollone - 26:09
Most of the time it's not just one vulnerability but it's 20,000
vulnerabilities. Like can you please fix this list and randomly choose? But
on that subject, sorry, I just.

Marius Poskus - 26:22
Wanted to add on that thing. I think as well, normally when you go into
and expand into various departments, you get a pushback saying oh,
security is not a problem, but it's about how you I always try now to relate
security with quality. So security is part of the quality properties. So if you
want to build a quality code, security has to be built in. Because when I
always say to people, when you left the house this morning, did someone
lock the door for you? No, you did it yourself. So security is part of your
responsibilities in your area.

Francesco Cipollone - 26:53
I like that analogy.

John Kinsella - 26:55
I want to jump into there real quick because I think going back to what I
was talking about originally, you're asking what is application security? I
think what Marius is just saying sort of hits it. One of the things we've
seen over the last few years is application security was it used to be a part
of the security team, right? Like those dudes in the back who sort of knew
what coding was. But they're security people. And we're now seeing that
development teams are pushing the budget for application security. So a
lot of development teams out there are actually embracing that they need
to do this AppSec thing. But at the same time as they embrace it, they
want to do it in a way which makes sense to them.

John Kinsella - 27:29
So I think as we're picking these metrics or what they are, that might be
something to also keep in mind. It's like who's consuming that metric? Is it
Marius? Is his directors or is it like a manager? Or is it the dude who's
actually doing the code?

Francesco Cipollone - 27:43
I like that and I think it's changing and it depends on the maturity curve of
the organization and also the ownership. And back. On the first point, I
think we have organizations that consider upsec separately from
CLOUDSEC and infrastructure security, and then you have the more
modern organization that look at the full you build it, you own it with SRE
and Observability, where you have full control of your application security
stack all the way down to the code and the patching and the
infrastructure. So the metric that matters to one organization I found very
painfully don't matters to other organization and the threshold that
matters for one organization and the methodology don't matter for others.
But back on the vulnerability overload, I wanted to introduce Jay and the
work that they've done. They've been fascinating work that they've done
on EPSs.

Francesco Cipollone - 28:37
And I want touch on the angle on EPSs and application security because I
think it's not a subject that we talked enough and when it works and when
it doesn't but before diving in, what is EPSs? Jay?

Jay Jacobs - 28:50
So EPSs is the exploit prediction scoring system and it basically was born
out of the concept that if what was it that Lord Kelvin quote about? If you
can't manage what you can't measure kind of a thing and basically you
don't learn unless you have feedback. If you think about trying to hit a
golf ball, if you always hit a golf ball and never looked where it went, you
probably wouldn't improve much, right? Same thing with vulnerability
management and basically anything that if you want to do better, you
have to look at what's actually being exploited and or compromised and
the impact and all the other stuff because a lot of the earlier comments
were absolutely right, it just comes down to risk. And one element of that I
thought was relatively easy to measure in vulnerability management was
that exploitation.

Jay Jacobs - 29:37
That we can actually go out and gather evidence of exploitation and I can
go into great detail about how we define that and go after it and capture
that data because that's a huge part of this. But we basically get that
evidence of exploitation and then we try to model what it takes to predict
that moving forward. And there's all sorts of interesting tricks and things
that we can do to talk about how the past can or does not inform the
future and we can measure that. And so that's largely what EPSs is. We
gather all this evidence of exploitation activity, we've got a good. List of
data partners that we're trying to grow and we use that data then to
predict future exploitation activity.

Jay Jacobs - 30:20
And so every day for all of the published CVEs, we publish a score that is
the probability that CVE will be exploited one or more days out of the next
30 days. And we've got a lot of material published on this. We're just at
our third paper, peer reviewed academic paper and a lot of stuff on the
website and some of it we have to update. But it's all out there. We've got
a lot of stuff out there on it. And so that's what EPSs is. It's all about
CVEs and the probability of exploitation.

Francesco Cipollone - 30:50
Brilliant. And there is an interesting angle in here because library has CVE
and library have a version while code is a little bit more harder to measure
because it's not static like a CVE, it's not a timestamp version. And I think
what I've seen at scale is EPSs has a fantastic effect where you can
actually measure something that is fixing a specific version while in code is
actually more challenging because it depends a lot on the context. And
you've done a lot of work on this. Tell us a little bit more about this very
interesting aspect.

Jay Jacobs - 31:27
Yeah, the difference between CVEs and what those represent and then you
have CVEs in the open source libraries and then you've got vulnerabilities
in custom code and these are fascinating area to study. First off, it's just
super fun. But the system, I think, of exploitation, when something gets a
CVE, there's so many things that happen, right? Information gets
published, we typically have something that we can start to log evidence of
exploitation for. Without that CVE, it becomes super hard to correlate.
Someone has this vulnerability. And how do you write a signature, detect it
and what do you call it at that point? And how do you bring different data
sources together? Becomes much more problematic without any sort of
common nomenclature. But when these things get published into a CVE, I
think that maybe the attackers become more aware.

Jay Jacobs - 32:22
They start to realize, hey, this is out there. And when you have a custom
piece of software that may not be widely distributed and it's only in your
one location that may not have the same exploitation landscape but when
you start talking about open source code where it is widely distributed and
it does become more like an infrastructure type of thing like a firewall or
router or something or desktop It starts to become more like that CVE
publication public distribution thing. And so there's a lot of nuances here,
but it's definitely a fascinating area to study.

Francesco Cipollone - 33:00
No, I do agree and I see that. One thing that I'm curious about though, the
more we're going to rely on EPSs, whether an attacker start looking at
the known EPSs data so the low exportability score to actually sidetrack if
everybody's using EPSs or everybody's using a score to use the negative
score. So when things get implemented at scale, then we have a big spot
and sore spot.

Jay Jacobs - 33:35
Yeah. So to answer your first question about are the attackers going to
shift and start using ups for it? And I hope so. Anything we can do that
forces the attackers to shift has got to be a good thing. But also that sort
of goes to why we need to update this stuff. This isn't like we aren't going
to build a model and be like, hey, we're done, we got it. It'll be good for
next 20 years. It won't be. We're trying to retrain these every six to twelve
months. And during those months we're measuring, how is it still
performing, how are we looking at 30 days ago we said these
probabilities, how did it perform according to the data we've collected?
But you have to keep updating.

Jay Jacobs - 34:14
So if the attackers are going to shift, and they do, and they will, we have
to keep updating our knowledge and keep updating what we expect them
to do moving forward and measuring that performance going forward.

Francesco Cipollone - 34:26
Now, that's brilliant. And I think you publish on the website several
example and I talked a lot several example where EPSs catch up with the
data source that you can see, as well as example where EPSs catch up
very quickly like log four J, I think, was the more evident one where
specific data source catched it or scored it a little bit faster than EPSs
scored it and then kind of converging. What are your thoughts on that
subject? If somebody has to use EPSs, how to optimally use EPSs? Yeah.

Jay Jacobs - 35:06
So big picture first, it does come down to risk, and EPSs is only the
exploitation, right? And so it is not an entire risk picture you want to talk
about. Okay, if exploitation activity occurs first, is this even in my
environment? If it is, do I have any compensated controls? How am I
going to resist? How am I going to detect all of those things? And then the
asset criticality and what's on the asset? What's going to happen if it is
compromised? All of that stuff. And so EPSs is one part of that entire
decision. And then the other thing, going back to sort of the timing, the
first thing you should do is always act on intelligence first. Like if you
know something is actively being exploited, don't check EPSs because
EPSs is a probability.

Jay Jacobs - 35:52
It's sort of like if I flip coin before I flip it and I say, what is the chance of
heads? And you're going to say 50%. And then I flip it and I look at it and I
said, do you want to change your opinion? Because you're wrong. You're
like, no, you don't have any other new information. But then if we show
you and it either is or isn't, you want to act on that information, right? If
you know the answer, don't go looking at an estimate of the answer, right?
So if something is being exploited, go after that. Like log for J, for
example.

Jay Jacobs - 36:20
We did a write up on the website and I think in the opening paragraph I
said, if you're around and working that weekend, December 10 of 2021,
or whatever it was, and you need to check a scoring system for this
vulnerability, you're probably doing your job wrong, right? I mean, like,
the internet was on fire for it and so then to use that as a poster child to
say how good or bad EPSs was, it's sort of irrelevant at that point. But
EPSs is 100% data driven and so it's going to react to the data that it can
get its hands on. It doesn't interpret people's various connotation that
they're putting out on social media or anything like that. It may look for
like volume of posts about something and so there's some nuance there,
but it does look for other things.

Jay Jacobs - 37:07
Like one of the biggest variables that blew my mind was the number of
references in a published CVE is a huge predictor. Just the number of
URLs in a CVE is a very large predictor. And I think log for J is what, over
a few hundred at this point in that CVE? Yeah. And so the average CVE in
these years, the last few years, like two or three, so when you see
something with over 300, it's kind of a good indicator that there's
something going on there, right? And so the model has sort of figured that
out. And then there's other things, like, do we see a published exploit, all
of that stuff. So if something is published and it doesn't have any exploit
code out there, it has two references in the CVE, it's got this, it's got that.

Jay Jacobs - 37:54
It's going to be scored low, right? It's looking at the environment, the
model is looking at the data it's able to collect and it's going to score low
or towards the bottom or something. But sometimes if it's Microsoft and
it's this particular attribute and this type of vulnerability, it may jump up
without some of the huge red flags. And so, I mean, that's basically what it
is. It's going to react to the data at hand and generally it does pretty good,
but it will be wrong at times. Absolutely. And so if you have other
information, use that first. If you don't have information, like if you don't
know if it's being exploited, that's where EPSs is going to come into play.

Jay Jacobs - 38:31
It's going to help you with beyond the few hundred or a few thousand that
you may have evidence of exploitation for, how do you look at the rest of
them? And that's what that's going to be good for.

Francesco Cipollone - 38:42
Thank you so much. And I think it's risk reward opportunity. If you are a
specific national state that is going to be highly targeted at day zero of a
ground zero attack, or if you're a particular software provider that has a
chain of very critical hospital, or if your national state or if you're critical,
national infrastructure. Your risk profile is going to be entirely different
and hence the time to react will be entirely different. While 98% of other
folks out there, they just need to be a little bit better than their neighbor.
And that's where EPSs, I love EPSs because of that.

Jay Jacobs - 39:23
Yeah. And to that .1 of the pushback that we often get with EPSs is that
we don't offer categories, we don't say this is a critical, this is a high,
anything like that. We've got a score between zero and one. And the
reason is, I think someone said it before if you're a small organization, you
may have a larger risk appetite you may be more tolerant of taking more
risk on, and your threshold for what to fix might be completely different
than, say, a large, mature financial institution may consider a whole
different threshold as being critical. And we got to fix it this month or this
next two days. And those thresholds are going to vary. So for us from a
central organization to say these are critical and these are hot, I think
that's a terrible thing to do as a central organization.

Francesco Cipollone - 40:07
And I praise your effort on resisting on a top ten score or a scale of four
aspect of marketing because I like the fact that will stimulate the industry
to go to a more risk based approach and probabilistic approach and
consider other aspect that is like critical element and not all of it. And you
might want to just use EPSs to a specific bucketing system, but that's
entirely up to your risk appetite.

Jay Jacobs - 40:37
Yeah, go ahead.

Mike Shema - 40:40
I was going to say if I could add real quick, I wanted to expand one of the
things that Jay you had mentioned mentioning log for J or just like these
are probabilities in the spirit of what can AppSec do? AppSec can also
help with the idea of run a tabletop exercise before the next zero day or
the scary log for J or whatever, take a volume, say what if the EPSs score
is the magic 100%? Let's just roll that. And that type of tabletop exercise
can help you say, well, do we have an asset inventory? Even mature
organizations probably don't have one, but it can start to help you say,
well, we have a pretty good one in the cloud because AWS knows how to
bill us for our resources so we could find those resources. But maybe we're
missing.

Mike Shema - 41:24
We have these other gaps as well as it's going to get that sense of can we
fix this fast? Meaning is our CI CD pipeline, do we have tests that don't
have like a break glass capability to them? So we actually have to wait 6
hours to push through a release. And all these can be done in the much
lower stress environments when you're not over that weekend of dealing
with Log for J. So that's one of those things that AppSec, I think, can help
with and spend time on this more strategic, more helpful to the
organization than just go fix this.

Jay Jacobs - 41:57
Yeah, and think about the scramble just in Log for J, about finding where
it is exactly to your point, like the asset inventory and all that. So sorry,
Chris, go ahead, no worries.

Chris Madden - 42:07
Yeah, I was going to plus one on what Mike said is in the asset inventory is
important and the software inventory as well is what software? What
libraries have you got? The other interesting thing that where AppSec can
help but nobody uses is understanding root causes for things is in
gathering all your data, doing the data analysis, coming up with the root
causes is your software ten years old. Whatever open source dependencies
or whatever the thing is, coming up with the root causes for all your
software and data in your OpSec pipeline is a fairly simple thing to do
with the exploratory data analysis tools, but nobody does it. And it can be
done at your leisure before the next zero day critical thing drops.

Francesco Cipollone - 42:52
Maybe I'm gonna be fictitious here, I'm gonna be controversial. Shall we
stop calling it threat modeling exercise and call it business continuity
exercise? Because that's what lock for J was. We were on the brink of
being afraid to be crippled or the zealous vulnerability. And depending
who you are, which side of that data breach you wear is still business
continuity. As long as we call it security or upsetting, it's going to be really
getting in the realm of, yeah, that's a security thing. As soon as we call it,
well, let's do a business assessment of like, do we have the asset
information? If we lose this asset, what is the business impact of that? Do
we know that our third supplier or our software supplier is going to be
compromised with this? What is the impact from a business perspective on
our critical survivability?

Francesco Cipollone - 43:46
I found that calling it with different name can bring maybe different
people on the table.

Marius Poskus - 43:53
Yeah, sorry, I'm just going to add Francesco. I think it's the way I think the
whole industry is trending as well because we've been talking in the latest
San CISO networking event as well. So 2010s were all kind of us trying to
reduce the likelihood of risk, which always been done sort of at the
perimeter and edge security, whereas 2020 feels like it's inevitable that
something's going to happen. So how we can reduce the impact and we
shifted from reducing the likelihood to reducing the impact and actually,
should something happen, how do we still maintain business operations
and actually still take money? So I think that's where our industry is
moving now.

Mike Shema - 44:41
I hear definitely the aspect in the CIA triad availability as the primary
aspect of that business continuity but in the spirit of what you're going for,
BCP sounds great. And then maybe also throw in like privacy aspect
because a lot of organizations now have a chief privacy officer or fall
under CCPA GDPR and there's a difference between log four J. Did that
just impact continuity, impact availability or was that on a system that has
customer data privacy? So I'd be happy to move on from just calling
everything threat modeling and aligning that language with the people
that are involved because a lot of BCP and privacy typically don't have
very strong AppSec presences.

Francesco Cipollone - 45:28
Brilliant. So let's move on from application security threat modeling into
business continuity and how can we use the data driven model to actually
assess hold on our asset inventory that we've been fighting for years or
our supply chain that is I don't think it's a new thing. We've been fighting
this since threats and we don't seems to learn the lesson of there is a
particular library or a particular piece of software that might impact
across the board. But what I've seen and I want to hear the opinion on the
panel is the likelihood and the perspective and the amount of time those
library got attacked made all the business shift in terms of likelihood of
those things to happen. Strats happened one point in time and then there
was quiet up until OpenSSL, Heartbeat and few others.

Francesco Cipollone - 46:26
Well right now we're seeing an exploit of a software library, open source
library on a very much more consistent basis. What's your opinion? Let's
start with Mike.

Mike Shema - 46:39
I get to talk again. I think Struts is interesting. I think there was an article,
somebody wrote a blog post this summer about Equifax pointing out that
Equifax for the most part fixed their struts, what they knew of within 48
hours. What they got caught out on was their asset inventory didn't cover
this legacy system. I think if I remember correctly, the legacy system
wasn't even exploited until roughly 30 days after the vulnerability had
been announced. So I guess I want to pull this back. My answer will come
back around to asset inventory which John started us off with and the time
to response and the metrics around time meaning perhaps time that you
can identify are you exposed to this? The time it takes to fix, but it would
hesitate to gamify that.

Mike Shema - 47:35
But also and maybe a little bit of EPSs would helps out this but the time
you're taking away from your developers, meaning you're telling them
about all these low risk vulnerabilities or you're just telling them fix this,
fix this in the sense of so many alerts that's just a distraction. So I guess
I'll throw in my time as my dimension being a Doctor Who fan.

Francesco Cipollone - 47:59
Brilliant. Chris, what's your opinion on it?

Chris Madden - 48:03
Yeah, so long time ago, I won't say which company I was working in, I
was aware of the risk associated with software and open source software.
And just because we're talking about open source software just to
highlight, that doesn't mean all the vulnerabilities are open source, it just
means that 80% of the software in our apps is open source. And we're
talking about that here. There's all the vulnerabilities in the software we
write, which is separate, right? So just to clarify that a long time ago
within a company I had put together this software supply chain risk
management value stream, which was an adjunct to our software
assurance for the software we write.

Chris Madden - 48:43
And trying to explain, look across our build pipeline, the open source
software that we intake, it's a risk and here's why and software supply
chain and all that and it was like what's all that about? And then
SolarWinds came along and then life as we knew it changed and everyone
knew what that was about. So it's kind of funny to see how the perspective
changed and it's the gift that keeps on giving. We have the Spring shells,
log for J's and shells and they're all these things. And now software supply
chain risk management, it's become a thing and everyone knows what it
is, no explanation required. And that's a good thing. It exists.

Chris Madden - 49:24
We're now interestingly, I think, at the stage where there's a lot of
standards popping up around it, and there's many in a sort of separate
recent effort, I was involved with a professor working with industry, let's
say companies. And developing a proactive software supply chain risk
management standard so people could look at it without having to read
the 20 different standards on supply chain to figure out, well, what do I
need to do? What's everyone else doing? And what do I need to do? So this
whole concept of software supply chain, it's maturing as sort of on the
back of solar winds, et cetera, but we're not there yet. You hear about S
bombs, we should all have S bombs, but in reality nobody has working S
bombs.

Chris Madden - 50:19
I think, and that's a strong statement, but they're not at the point where
everybody's using them and they're useful. My colleague DJ has a whole
podcast with the thought leaders on that is called Thebomb Show. And so
S bombs will come as well as a follow on. So it's an area that's maturing
and there's lots more to happen in this space.

Francesco Cipollone - 50:46
Brilliant. And I think with Steve Spring that we discuss about even the
evolution of bomb to P bomb and softer bill of material that is extending
away from just pure libraries to actually asset management. It seems to
joke and go back to asset management, but on that software asset
management, john, what's your opinion? Are we going to get to that point
or are we going to just circle on it?

John Kinsella - 51:15
I think software asset management, we should have a chance and the
reason I'm going down this path is more and more of what we're doing is
automated. Less and less of what we have is a developer has a mercury
repo, like underneath the desk or something like that, right? We're using
most of us are really shifting towards GitHub actions. I don't know, pick
the Amazon or de Aure version of it, but some sort of centralized code
base. S bombs, I think are and we covered on ASW earlier this year, s
bombs themselves are fairly easy to generate, lots of ways to do it. The
question is, what do you do with them? Now you've got this other thing to
track in your inventory, the tools. Are they're improving compared to
where they were a year ago?

John Kinsella - 52:01
But still, this is definitely one of the situations where the thing was made
before the things were made to do something with that thing. So inventory
is improving. I think the one interesting thing back from the earlier
comment about internal versus open source code, the internal code is just
where when you create the vulnerabilities, you keep them to yourself
versus with open source, you share the vulnerabilities with everyone else.
So you still have to do something with them. Right? You have to track
them. You have to understand where they are. They're probably going to
be harder to find since you don't have signatures or sort of more common
methods of tracking those things down. But yeah, I think a lot of this also
comes down to that maturity model. Like, where is someone like sort of
both how big is an organization?

John Kinsella - 52:51
How many of these cats are you trying to herd? But then also, how
sophisticated are you in your herding? Right? I don't know. What my
analogies today? Do you have a bunch of sheep hounds that are really well
trained for your whistling? Or is it like you're just sort of like throwing
rocks and hoping that the sheep go in the right direction? So there's a lot
of wherever you are on that maturity model is going to come down to
which one of these tools you're going to be using and how do you use it. I
mean, okay, imagine if I gift you like a five person shop, some hundred and
$50,000 asset inventory software inventory system that would take two or
three guys full time to run, plus the training, plus everything else. It's
useless to them. Right?

John Kinsella - 53:33
So it's not just the sophistication of the metrics, the tools, how do you find
these things, but also has to be matched with what are the capabilities of
that organization, where are they on that maturity curve?

Francesco Cipollone - 53:43
And I like the maturity curve, but we have few minutes, so I want to just
manage touch Jay and Marius. Jay, what's your opinion on are we getting
more and more mature or less mature?

Jay Jacobs - 53:57
I would love it if we can look back in five years and look at the time now
and sort of laugh at how archaic we are or something like that, like we
advance so much that this looks ridiculous, that would be awesome. But I
want touch on this automation thing that John was talking about and I
think that's so critical. I think it is absolutely critical and more from
remediation standpoint. So if you're building libraries, open source code,
anything like that, they'll have some reuse. The ability for people to put
that in place, put a new version in place without the hassle is really
critical. And so as we're studying remediation times, if anybody
remembers Microsoft from like 2000, they were terrible at security, just
absolutely terrible and pretty widespread.

Jay Jacobs - 54:44
And they would put out patches that would bring down systems and one of
the biggest things they did was made those patches more reliable and then
they started patch Tuesday and made the timing more reliable. And now
they are one of the fastest platforms to get remediated when
vulnerabilities are found and CVS are issued and getting patches out
there. They are one of the most quickest remediation things to happen on
networks. Now google is catching up with Chrome being autofix, things
like that in open source we need to be able to give people that trust that
when something needs to be updated that it can be updated if it's going to
cause hassle. One of the worst things actually slowest to be remediated is
Java.

Jay Jacobs - 55:25
It is by far one of the slowest things in any network to get updated and
remediated because I think anybody who worked with it knows that pain.
And so I think that's one of the areas that from a remediation and
robustness of resilience of code we need to work on that remediation and
fix strategy and make that a lot more painless.

Francesco Cipollone - 55:45
I like the example because I think regression testing the scare of
something to be broken and the ramification of upgrading and bumping
up a library of, God forbid, a source control or a Java virtual machine
from one version to the other that's going to break completely. The
method or even Spring Boot and the rest of the methods are still terrifying
because of the amount of regression testing that people want to do. But
we're getting better where risk reward is actually lower and lower and
reachability versus just bumping up a library is getting less rewarding on
actually decompiling that library and identifying where is the vulnerability
versus just pump up the library. Marius, what's your opinion on it?

Marius Poskus - 56:36
I think we are moving in the right direction. I think especially because we
are working now in everything's becoming interconnected, most of the
organizations moving into the cloud. So I think the way we can negate
some of the work that we do in some of the manual work is we now can
start scaling our governance policies in cloud at scale. So as long as we
set our correct governance structure and strategy. You can fix some of the
stuff just by policies of enforcing repeatable processes time and time again
of how and what you fix and then whatever you need to test. And
obviously you can again create an automated test where you just have a
person overlooking instead of actually person doing those tests. So I think
we're on the right track.

Marius Poskus - 57:23
We just obviously there's still some time to go until we get there. But I
think as technology evolves, our thinking evolves and how we address be, I
think hopefully we're going to get there soon.

Francesco Cipollone - 57:38
Brilliant. And we just time. So I want to leave everyone with the hope that
in five years, as Jay said, we're going to look at this podcast and this panel
and we see we advance so much that now all the asset management are
done, risk assessed. We have real time information about the assets. The
exportability and attacker don't have a chance anymore to bridge. But
unfortunately, I'm a pessimist and an optimist at the same time. So I think
we're going to face a different kind of challenges and we all going to have
a job tomorrow as we have it today, defending our organization. But
hopefully it's going to be a little bit less stressful and a bit more interesting
than just chasing up a library in a patch. Everyone, thank you very much
for the time that you came today.

Francesco Cipollone - 58:23
It's been a brilliant panel. I know that we're at the time, if you want to
leave with the last thoughts, I'm going to just do around and do the round
of very quick last thoughts on the subject I'm going to gain. Start with
Mike.

Mike Shema - 58:37
You don't have to fix all the talk. Have a different conversation with your
developers about anything other than just fixing a bunch of volumes. Talk
about design, something like that.

Francesco Cipollone - 58:47
Brilliant.

Jay Jacobs - 58:48
Jay, I think the biggest thing is feedback. Whatever you're doing, try to do
it in a way that you can look at the feedback from your decisions and
actions, including design and all of that stuff.

Francesco Cipollone - 59:01
Brilliant.

Chris Madden - 59:02
Chris, I think understand your data that's really understand what you have
and the data from your tools and put it together. Holistically disclaimer.
No live moles were whacked in the making of this presentation.

Francesco Cipollone - 59:18
I love that.

Chris Madden - 59:19
John.

John Kinsella - 59:22
I'm going to say think about your budget, right? So it doesn't matter if you
have 10 million things out there to fix or five, but it comes down to what is
that budget? Both monetary plus your resources, plus your skill set. And
then based off that, you have to figure out what you're going to do with it.

Francesco Cipollone - 59:37
Brilliant. Marius?

Marius Poskus - 59:40
I would say take your organization on the culture journey and how we can
collaborate between the teams and get them together. It's not operations
versus security or versus development. It's how we work together and get
that problem solved.

Francesco Cipollone - 59:56
Fantastic. And I'm going to. Leave everyone with the last thought. That is,
let's stop calling it Vulnerability management, application security, and
let's call it Business continuity and survivability. Everyone, thank you so
much. It was a beautiful panel. And stay safe out there. See ya.

Chris Madden - 01:00:16
Thanks, Frank.

Francesco Cipollone - 01:00:17
Bye bye.

Marius Poskus - 01:00:17
Thank you.
