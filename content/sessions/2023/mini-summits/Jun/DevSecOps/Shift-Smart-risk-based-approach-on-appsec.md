---
title        : "Shift Smart - risk based approach on appsec"
track        : DevSecOps
type         : working-session
topics       :
featured     :
event        : mini-summit
when_year    : 2023
when_month   : Jun
when_day     : Mon
when_time    : WS-16-17
hey_summit   : https://us06web.zoom.us/meeting/register/tZMpcu2opzIuE9OWSFEtXBTALTeDEvq6IWSl
session_slack:
#status       : draft
description  :
banner       : https://pbs.twimg.com/media/FxKsQ28WcAABJmX?format=jpg&name=medium
organizers   :
   - Francesco Cipollone
  
youtube_link : https://youtu.be/TYScog1oEeQ
zoom_link    : https://us06web.zoom.us/meeting/register/tZMpcu2opzIuE9OWSFEtXBTALTeDEvq6IWSl
---


## About this session
Shifting left had success, shifting right and adding context is hot as the number of vulnerabilities pre-flight in an SDLC is piling up. Find your path in this modern, challenging.  The talk walks through a new approach on risk base approach on vulnerabilities called shift smart. 
We will explore the difference between a vulnerability base approach and resolution first vs a risk-based approach and success from real case scenarios 

Publication: 
https://phoenix.security/shift-smart-risk-based/

## Transcipt
00:00
Shakespeare. I almost make it into Shakespeare mode. But then AppSec
and Sonnets maybe ask us, I'll ask ChatGPT to actually create a version of
this with Sonnets.
00:17
And on that note, here we go, Francesco for another master class on
AppSec and today he's going to talk about.
00:23
To fix or not to fix.
00:24
This is the question as it always comes down to context, making sure we
have context and you do some amazing work on this.
00:31
So over to you.
00:33
Thank you very much, Denis and everyone. Welcome to another master
class of session. We'll keep it live, we'll keep it interesting and we've been
discussing a lot about application security, vulnerability management,
cloud security, on whether to fix something or not to fix. We got in the
recent news a lot of example where specific thread feeds were more
interesting versus others. So there is a lot of question around what do I
use as a North Star to actually fix?
01:04
And I wish I had a better answer. It depends.

01:08
But we will as a silver lining, we will explore all the feeds and cases and
scenario where this is which feed to use, where just a little bit of
background. I'm Francesco Sipolonia, I'm the CEO and founder of
Phoenix Security. We do this day in and day out and analyze and spend a
lot of time looking at different data analytics.
01:31
Speed and how to make life easier, close bracket.
01:36
And this is what we called ship smart. So focusing on what really matters
in the context and scenario where it matters because certain things
matters most, certain things matters less in a particular scenario versus
the other. I'll have to apologize, or not apologize. Maybe this slide deck
and this presentation is a little bit lighter on memes. Usually I do an insane
amount of memes, but there is a reason for it. Security, application
security is really heavy. Sometimes it's a battle. We are in the trenches,
fighting to protect our organization day in and day out. And if we don't
have a jokes here and there, if we don't have a little bit of banter for my.
02:19
British folks, it becomes heavy, becomes dramatic.
02:25
And if we approach this problem with a little bit of a smile, with a little bit
of banter, then it's a little bit lighter. And that's my mission on this
presentation.
02:34
To make it interesting, but also lighter.

02:38
I've been doing vulnerability management at scale in several organization,
from finance to telco to international organization. And I've seen it, I've
done it all.
02:48
And I think my mission to actually.
02:51
Continue doing this and prioritizing and focusing.
02:54
On what really matters was preventing burnout.
02:58
Because doing things manually, focusing on everything, focusing on the
latest superstar vulnerability is not really helping anybody and is burning
us all.
03:09
So can we scale and make it.
03:12
More enjoyable and available to everybody? The answer is yes.
03:17
So what we're going to talk today.

03:19
We'Re going to talk about security, development, the human cost of triage,
the SDLC approach and what to fix immediately, what not to fix. And then
we're going to explore a.
03:29
Lot of terms that have been going.
03:32
Around and I think they need a little bit of contextualization, reachability
context and exploitability. They are not interchangeable and they need a
little bit more knowledge. And also how and where we use this, in which
area and how complex is to measure and use all of this.
03:48
Because vulnerability management is all about what.
03:53
Information and feed I use, where and how complex is to use. If I spend
more time actually measuring and trying to identify the best approach.
04:02
To prioritizing and I don't have time.
04:06
To actually go and fix it, then it's pointless. So which tool do you use,
where and which one, deliver the best ROI or return on investment to us?
And that is where we focus really a lot today. And then of course, all of this
get captured in the risk. As I say, the risk is the great unifier from the great
divide that is vulnerability and this deliver, really we.

04:29
Wrap up everything into risk.
04:31
So the first time you start a security scanner of any sort across any
organization, or the first time you enter an organization that hasn't done
vulnerability management, this is a scenario you are faced with lot of red,
lot of critical, lot of burning. And the more important question is who
should fix what and when? And if you work in a development.
04:55
Environment well, you have a lot of.
04:58
Things to do and then you have the security engineers, the development
engineers, the cloud engineers, security engineers and so on and so forth,
that open tickets for you and very quickly you find yourself in a sea of red
or backlog.
05:14
What we don't usually answer is who.
05:19
Is in charge of actually doing and continue working on the stuff that keeps
the business running, right? Because having a lot of tickets in a backlog
doesn't mean security. And doing triage and doing triage manually is
extremely complicated on both sides of the dev divide. So in your dev team
or in your security team is the same level of challenge of actually triaging
and identifying what to fix next.

05:48
And doing this all manually is the road of burnout.
05:51
Because traditionally an organization has at least two or three of these
tools. You have web testing, either open source or non open source. You
might have security static analysis, you might have dust autonomic
application security testing, a cloud security product, an infrastructure
product. Looking on all of these information is challenging and on top of
that you have Pen testing and on top of that you actually have threat
speed and the latest vulnerability and the latest panic that happens from
management, that happens from everyone.
06:26
This is not a right and a.
06:28
Good way to go and it's not.
06:30
Scalable because our attention gets pulled in.
06:33
Every direction and we don't unfortunately have.
06:35
Infinite mental resource time and infinite time.

06:40
And this is not news hopefully I'm talking and I'm preaching to the choir
because this is what we face every day.
06:48
And if you're a small organization that.
06:51
Has less than 1000 employees, hundred devs, you can probably still kind of
handle all this manually with different level of expertise. But the surface is
not insane. You can still dedicate enough amount of time to each team.
And the more you know each team, the more you know each application,
the faster you become in analyzing a vulnerability. And 48 minutes per
team per week.
07:15
Is actually not that bad numbers.
07:19
You have roughly two or three security teams or one to 50 security to dev.
Probably not an incentive amount, it's still a lot of work but it's not an
incentive amount to manage. Probably you will face it when it becomes at
scale and challenging when you have the superstar vulnerability homes
like Log for Shell or Spring for Shell or the OpenSSL and we start seeing
those more and more but it's still kind of manageable. Where this becomes
really challenging is probably when you get to a mid size to enterprise
level or to larger organization where you have roughly 3000 and more
employees you have 1000 devs and much less security team. So if you see
the security team do not scale at the same time.
08:09
With the development team and that's one.

08:11
Of the reason why we keep on saying security is everybody's responsibility
because we don't have enough resource to actually put our hands onto the
problem.
08:20
And if you see here the amount.
08:22
Of time it takes us to get through the vulnerability for a specific team is
much less. So we have less time to triage, less time to identify the
vulnerabilities and we really need to focus on the vulnerability that really
matters. So this is where risk management and vulnerability management
at scale really deliver the best benefit because we get time to.
08:44
Actually focus on what really matters. And we should remember that the
job.
08:50
Of security is not to fix everything, it's not to fix all the vulnerability.
08:56
We should help the business fix the.
08:59
Vulnerability that are in line with the risk expectation. So we should just
operate to the level of risk that the organization is comfortable with. And
sometimes in security we get kind.

09:11
Of wrap up especially if we're in.
09:14
Pain testing, especially if we identify a problem. We identify a problem
atomically outside the context of where that problem happens and outside
the likelihood of where that problem happens. Can somebody exploit a
specific vulnerability?
09:29
Yes, probably with some level of effort.
09:32
And some level of expertise.
09:34
But if that vulnerability is buried down.
09:37
The stack and if very little chance that vulnerability is going to get access
or if that vulnerability is web facing and everybody's looking at that
vulnerability, those are very two different critical and it might be the same
level of vulnerability, might be the same lockboard j.
09:52
The same critical vulnerability, but in two.

09:55
Different leveling context and with two different level of likelihood. And
expressing that to the business, we enable the business to actually make a
decision. Do we fix, do we don't fix?
10:08
Because ultimately the only people that will.
10:11
Authorize our dev team to actually go.
10:13
And work and focus on fixing vulnerability.
10:17
Through the backlog and prioritizing those things through the backlog is
going to be the business. So how do we involve the business into making
the right decision? Well, we tend to focus on shift.
10:29
Left and shift right, that is, moving.
10:32
Things early in the development cycle or focusing on production.
10:38
And we've been focusing as an industry.

10:40
A lot in that.
10:41
We hope that DevSecOps and I'm sorry.
10:44
For using all the terms you can use the security bingo. And trying to
identify how many keywords do I hit?
10:55
But we've been focusing as an industry.
10:57
On these two terms and going left to right and right to left and left to
right. And security has been kind of in the middle trying to help both
options. But the third option and the third kind of key players that we
forgot was the business. And it's the business that fundamentally set the
risk level where we should operate. And that is going to be the only one
who is responsible on actually driving the business and fixing
vulnerabilities. The only one who has the right.
11:25
To say I'm going to spend X.
11:26
Amount of development time in cycle on that problem versus the other
problem.

11:32
The challenge that we have is that.
11:35
We tend to speak vulnerability to executive into the business. We say
10,000 critical, millions of vulnerabilities.
11:43
And if you're in any situation like me in the past you get very.
11:47
Awkward look, very awkward feeling from management.
11:51
Team where they say what do you.
11:53
Want me to do with this? Fix them all, how bad they are. We were
surviving with this yesterday. It's not something they can make
uninformed.
12:01
Decision because anybody from a business perspective think in risk and we
need to contextualize vulnerability for them and on the.
12:13
Opposite side if we go to an engineering process.

12:15
I have a quick comment there. I think you just touched on something
which I found that more and more I think is important is that especially
when you talk to executives, I think it's very important that we have a
coherent story, for example, of why it hasn't been exploited. And I think
because it's a bit like imagine you walk into a building and say, hey, this
whole has massive gaps.
12:40
And the people in the building going.
12:41
Yeah, but the building's been here for 100 years and we haven't had a
breach. No, it doesn't mean that you cannot say luck, I think luck is a
valid reason or you can say we haven't had attackers who are
sophisticated enough or we happen to have somebody who'd done some
heroic actions. But I think especially at an executive, I think as you put
context they're going to drive you to have a rational reason for why not in
six months from now, why not in twelve months from now, or what's
changing in order for this to now be a problem. Which is the kind of
questions that the context will drive and I think that makes a lot of
difference.
13:22
As you talk to executives and you.

13:25
Give them kind of the Nostat as you're rightfully saying is the probability.
You give a sense of probability, it's not an atomic value. This is not bad
atomically it might be. Lockpoj is a very good example where a
vulnerability was discovered ages ago that all of a sudden got attacked at
scale now becomes a really important problem. Another good example is
movie transfer. We had this vulnerability exploited eight months for eight
months on a specific attack. It wasn't important before, it's super
important now. Now depending on I brought recently an article on that
depending on which.
14:00
Thread speed you look at, the probability.
14:03
And the exploit at scale is very low right now on the Movie transfer, but
the threat actors that are actually exploiting that are very targeted. So
debts in itself require that level of context and a story around that
vulnerability. Yes, that vulnerability exploitation is very low. But if
somebody attacked us with that vulnerability then we're going to face the
same level of challenge that we had in Boots, we had with British Airways
and so on and so forth. So the magnitude that is the second aspect of risk
is really important and the narrative that you build around the
vulnerability is really important for the level up. But then we need a
connection from level up to level down. Because if we tell that story to
engineering team engineers, don't bloody cares about all this story, they
just want to know what do I need to fix in the next print?
14:52
And if we tell that narrative that's great.
14:55
But ultimately we need to give them.

14:58
A number of story points that they need to allocate in a sprint. And as a
security team, we sometimes.
15:03
Forget that's our job to give them.
15:07
A visibility on what to do next and the week after and how important it is,
and then let the business manage at Scrum with existing process. Not
reinventing the will on new process, but giving them a consistent stream of
things to fix that are contextualized and important for the business. Not
reinventing the will, very boring, but that's what get things done. Not
talking about risk, but talking about what needs to be solved next in line
with risk expectation and everything else.
15:36
You know, one of the words I found myself using a lot when I talk first of
my more technical teams, I say your responsibility if they're on a security
team is to produce highly defensible analysis that when somebody with
knowledge about that really looks at it, they go I get it, I understand. It's
almost like you're also forcing us on the security team to actually produce
really good materials for.
16:02
Sometimes it's a hit and miss, but giving consistent list of things and
giving an ability to actually challenge those things and adding context.
16:11
And having that discussion give much better.

16:14
Result than just flooding a backlog with 2000 tickets. Because that will
never get done even ten on a sprint when you have to produce other 15
features. It's an imbalance approach like one, two, maybe per sprint.
That's the level of bug fixing that you can foresee and forecast and
sometimes as a security team we miss that.
16:37
And maybe we have one, two, three.
16:42
Shot idea when we have the superstar vulnerability like lockpoj that we all
focus on, where we can all hands on deck focus on fixing a specific
problem. But we don't have a lot of chances like that and they are
expensive in the most cycles. So even in those superstar vulnerability,
focusing on the one that are more likely to be exploited and forgetting
about the other one that can be fixed, maybe even not fixed in a normal
cycle of fixed versus building and keeping those measurements is really
important. And I'm going to stop a specific point with questions so that
we'll have time. Otherwise I'll get into rabbit hole with these things.
17:24
But I want to say that on.

17:27
The other hand, we tend to oversimplify why security is complex. And
application security, I've talked to it extensively, is complex, is variegated. I
don't want to oversimplify with this explanation and with this presentation
that it's just risk or it's just a list of things. Context and vulnerability and
risk are extremely nuanced and I'm going to focus on application security
specifically for this case and focusing on the central part of application
security or an SDLC at a very high level. That is the process of designing,
building a test and operating. And I'm going to even narrow it down to
build and test and operate where a mature SDLC nowadays look like that
because we have a lot of moving component. We have code, we have
testing in build, testing in operation. We have things that are being
deployed and there are time in place when to fix and when to make
decisions.
18:26
And sometimes making a decision in an IDE in a rapid mode is actually
much more valuable than looking at all the context in the word.
18:36
So there are time in place when.
18:39
To look at contextualization and when to look at fix it now because it is
visible and you're going to spend the minimum amount of cycle. Of course
there needs to be a balance because we can't fix all the.
18:49
Vulnerability as soon as they appear, because.

18:52
Maybe it's a major upgrade of a framework, maybe there is a better way
to fix a vulnerability. And those are the things that I call fast triage when
you decide at IDE points or when you are developing.
19:05
Something, whether to fix a vulnerability or not.
19:08
But then there is the rest and the remaining part of the vulnerability
backlog. That is everything else. And as soon as you turn on the
vulnerability, a vulnerability management solution, you will find a Seal
vulnerability. So adults vulnerability needs to be prioritized.
19:23
And they need to be decided.
19:24
And as well you might find something that operates at development cycle.
But a lot of the vulnerability, like log for J, spring for shell, movie transfer.
And things like that happens at operational level. So we need to keep a
balance of Prioritized backlog on the right and things that we fix on the
left and having a single approach on either one of these will not work
because there are two different speed, methodology and approaches.
19:52
And as I said, as soon as.

19:54
You join the point of vulnerability management is identifying who should
picks what and what's most urgent and giving them in the backlog in a
prioritized way. Because flooding a backlog with all the vulnerability in
the work will reach to burnout will result in development team not.
20:13
Listening to security at all and it's.
20:17
Not the way to go. Plotting a development team with this is.
20:24
The equivalent of asking the security team to develop features for them
because security.
20:30
Is everybody responsibility but what is the responsibility of somebody else
in terms of developing into delivering feature to the business? So we need
to empower the business to make the right decision with the.
20:41
Right tools at the right time and.
20:45
We are in this situation because Mano Triage doesn't scale as a security
team we tend to flood and delegate but it's almost like finding a needle in
the haystack. But the haystack is on fire, everything is screaming. And this
is what normally happen as.

21:00
Soon as you turn a vulnerability scanner at any point.
21:03
And the rationale for this is that we are completely unbalanced between
the number of security researcher and the number of development. So
there will be always an imbalance in this and we'll need to find a way to
actually scale vulnerability management. But the good news is that not
everything is.
21:24
Exploitable in that particular point in time.
21:28
10% of the vulnerability accordingly to the latest research is actually
exploitable, 5% of those are actually reachable and 1% vulnerability are
the one that are target.
21:38
Now that you should really focus, and.

21:41
I'll use this term interchangeably here, but actually I'll explore them much
more and expand them much more. But just for few statistics, CVSS is
actually reaching the 20,000 or 200,000 vulnerability, right? Now of which
just very little percent are actually exploitable and the speed of fixing is
actually increasing over time. And if we just use SLA. First of all we are
late because attacker are actually attacking things faster than we can
actually exploit because we focus on all the vulnerability an SLA or a
service level agreement or how long should we fix and how quickly should
we fix things are actually too simple metrics to use and deliver no results
like there is. There have been a Ghana, few Ghana studies that have
identified that using an SLA based approach doesn't work 100% of the
time.
22:43
Like it never worked.
22:46
And the reason why it doesn't work is that the triage is nuanced and you
can use different things in an automated versus an automated way. So I
want to spend a little.
23:00
Bit of time on this because I've.
23:02
Been doing a lot of research on this and I think there have been a lot of
assumption that triage is straightforward. So I want to break this and I
want to break the triage in easy as automatable. We have data source, we
have things that we can identify or very hard where things are really hard
to automate. Hence we rather spend time doing things minor.

23:22
And it's a balance.
23:24
Right now we overly balance on the right. I want us to be in a balance
between left and right. So let's say bulk. So bulk is the first cut of
vulnerabilities that we get from different scanner at different points.
23:37
And I want to say this is.
23:38
Stuff that we can automate. There are different level of nuances of what
you can automate taking different data feed, exploitability active bounties
vector, reachability in term of code we go from very easy. EPSs is
available everywhere, an attack vector is available. CVSS base, if it CWSS
base, is there an active bounty? Is there an active exploit? In the wild you
get threat feed around a specific vulnerability. All of this information are
machine readable and can be automated and can be used in an automated
and scalable way.
24:18
To remove 80% of the vulnerabilities.

24:22
Now, the deeper you go in the code with the concept of reachability and
we're going touch on the concept of reachability in a moment, the harder
it becomes to actually track this and do things at scale, it's not impossible.
But again, it's a balance between how much effort you put in the
automation part versus how much you get out of it. If it takes you hours
and millions to actually develop a technology or to actually go and scan
each single line of code and find which single line was fixable versus a
decision of ten minutes. Do we fix it? We don't fix it because it's reachable
with a team.
24:59
Decide where you spend your time, your energy and effort.
25:03
The second complexity of the second screening will be locality. Locality
gives you the concept of where things are in your environment and how
likely are they to get exploited. Again is a nuanced approach. The
likelihood derives by the intention of an attacker. But it's a good indicator
of the more external you are, the more externally facing you are, the more
likely things are to be exploited. And you can have those information in
CMDB. You can have this information in any data set. The lower you go in
the stack, the lower you go in this particular stack. Exploitability location,
reachability, attack paths, you get more nuanced in the location and the
likelihood of exploitation of a specific vulnerability and it takes you more
effort and time. So unless the vulnerability is really sophisticated, it's
probably not worth to spend so much money, energy and effort on actually
an attack vector or an attack path.
26:06
Analysis that delivers you maybe good results.

26:11
But you probably have spent enormous amount of time and effort that
could have been saved. And second, business criticality and the more we
go right, the less automatable information, the less information you have
to use in a machine readable way. Hence it's harder to get automation.
Hence why I say the left part of this triage and staging of triage is
automatable because you have widely available information at scale or
there are provided that offer you. But the more right you go, the more this
information depend on your organization, on your particular context and
not every.
26:51
Time is actually automatable. This doesn't mean that shouldn't be an.
26:57
Incentive for you to actually go and automate a lot of this stuff because
there is a lot of benefits from it and it's probably not that complicated. But
for example, in a business criticality a number from one to ten on.
27:09
An application is easy to say.

27:11
A full fair analysis is probably more complicated to implement and to even
understand. And the last bit that is where really the manual effort comes
into place is the business decision is the internal rationale is do we fix this
particular bunch of vulnerability or do we upgrade this library, this
framework? Those decision are really hard to automate and in my opinion
shouldn't be automated because it's all contextual on the particular
business initiative that you're having. Do you fix all the operating system
or do you upgrade to a new operating system? Those could be just
business reason and decision that are supported by a lot of this
information but is at the decision where actually human are really adding
value versus automation and machine. Because most of the time this
automation.
28:05
Leads you to a straight path.
28:08
Just a quick one I think on your left a good source is also.
28:12
Incidents and threat intelligence.
28:15
Yeah, I think internal incidents especially like for example, one of the
things I tend to do is we tend to run sometimes p ones, P three S and P
four S and P two S as P ones. And one of the things we get is really good
data on either what happened or what was just one degree separation
away from happening. And that again allows you to prioritize a lot of
these because in a way, in fact I would even argue that sometimes we fix a
lot of things during those incidents. But it's really good data because it's
almost like this just happened. It's not like theoretical, it's like the last
thing of is he ritual. Well it just did.

28:54
Well, if you get hit by a vulnerability it's like there was a very good second
World War where they analyze and they reinforce the planes where they
got hit. So do you reinforce the plane that got hit or do you reinforce
where you didn't see the plane coming back? So it's a little bit unknown
approach.
29:15
I get it, but it depends how you approach it. So for example I would call a
bigger problem, for example, lack of detectability. So for example, even
for someone when a bug bounty tell us something is wrong, I view the fact
that we didn't detect it, the fact that we didn't have more visibility, et
cetera. That's the kind of stuff that again I want to make sure we
understand because actually also detectability is also quite important here
because if it's a vulnerability that you can be quite confident that it can be
detected or at least you get some warning signs before it kind of hits
critical mass. That's way more dangerous than the kind of vulnerability
that although it's a bit more esoteric, if that gets it, then.
29:56
It'S a massive problem.
29:58
Well, those are things that goes in the triage goes in the human aspect
versus the automation and it's different on any organization where you
have the richness of the data. But in general, doing this manually, all.
30:11
Of it manually, it's probably not good.
30:15
And fixing everything as soon as it.

30:16
Comes out probably not best.
30:19
So thou shalt prioritize or thy trying. That is my rules and that is my law.
But I want to say that I've seen a lot of discussion around reachability.
30:29
Exploitability in context and all of this.
30:33
Element and all of these terms are actually different from each other and
are very different from each other and they have a different level and
degrees of complexity in actually extracting and analyzing and risk can
express a lot of this. That's why I love risk because risk can express a lot
of this element with a probabilistic factor that the business understand
well if we express all of.
30:56
This atomically probably we create a very complicated narrative. But just
to demystify a lot of.

31:03
This term, I want to get to this point where we have a specific library, for
example, log for J in a specific file and then that particular library is called
in a function that is really reachability. That is where a specific library gets
reachable and that is if I call it then that particular piece of code get
called and that particular vulnerability pops up. Detecting something like
this requires a lot a. Lot of effort. We've seen some security scanner that
are doing something like this and prioritizing vulnerability with
reachability it removes the false positive, but again it's a balance between
how much cycle and money you need to spend to actually get to that point
of deciding. Yes, this vulnerability has actually been called by a function
that's being called and a lot of those in memory scanner actually can help
a little bit detecting this because really see the attack part or the cold part
of a specific function.
32:04
But getting to that level is very complicated and require a very granular
approach across all your code. So this is for me code reachability and
reachability of a vulnerability is very hard in the stack of automation. It
depends on your scanner. But in general from a vulnerability management
perspective I will classify this as hard network reachability gives you a
little bit more context where you can prioritize maybe a log for J that is
externally facing versus a log for J that is internally facing. I would say
richability and context give you 50 of complexity depending on how good
you have your asset inventory and how good you can create your asset
inventory.
32:50
So it really depends.

32:53
Exploitability is probably the easiest factors that you can use at scale.
There is plenty of information out there is Bond DB, there is EPSs, there
are plenty of source for you to understand how likely is specific things to
be exploitable and use them at scale. I would say use them with a pinch of
salt because sometimes some of these information are appropriate
especially for application security, sometimes they are not. We've done a
recent study where we screened Caesar Cav that is one good example of
exploitability backed up because everything that goes in Caesar Cav is
well documented to be fixable and to be exploitable. So those are the well
known things.
33:42
That are exploited at scale, hit and miss and then we cross reference that.
33:47
With the likelihood of exploitation at scale or the prediction of exploitation
at scale in the next 30 days that is given by EPSs. A number of
vulnerability were completely missed, other were exacerbated.
33:59
So use each threat beat in comparison with the other.
34:06
So usually at least two thread beats, not just one anatomically. And the
other element I wanted to say is Caesar Cav is very good. From a
traditional vulnerability management and infrastructure approach and
patch management versus application security is probably not the best
resource because only 3% of whatever is in the catalog is related to a
library or to a piece of code. And there is much more out there that is
actually highly exploitable. So it's a very stressed list of things that are
exploitable in the patching and infrastructure world.

34:45
But to wrap all of this up.
34:48
And to conclude fundamentally this discussion is a lot of risk because risk
is the great unifier. So you can use a lot of this information into a risk
formula. You can capture the likelihood and the exploitability of
something to get exploited, the severity of something to get exploited, and
the criticality. So how much it impacts you into a risk formula that
everybody can understand and agree on.
35:14
And it's a journey.
35:15
Risk is a journey. It's an evolution where you go from pure severity based
and CVSS CWSS to SLA base to risk.
35:25
So don't adopt.
35:27
It straightforward out of this presentation. I mean, if you want, I'd be very
happy about it that you go into your organization and we say, scrap
everything. We should do risk. Yes, we should do risk, but evolve into it.
And a number of regulator, unfortunately, still operate with CVSS and
CVSS information. But in the civil lining, you can probably add a lot of
justification if you express your wrist posture and you say I control. My
wrist posture. Hence, a lot of these CVSS that, in your opinion need to be
fixed are actually non fixable because I can't reach and they can't be
exploited at scalar in the world. Usually that conversation goes much
better with an auditor?

36:10
It depends.
36:11
For me, security is not compliance. And the other way around and hate me
or love me for that.
36:19
It's my opinion.
36:23
We need to evolve. Regulation upscale because we still rely on a lot of stuff
that is antiquated.
36:28
But a lot of these factors that.
36:31
I discussed today can be used in.
36:34
A formula that doesn't need to be complicated.

36:38
Fundamentally, risk in a modern risk could be your CVSS, your CWSS.
Your severity. You can express the probability of exploitation in a machine
way, in an automatable way, with exploitability, with threat intelligence. If
there is a fix available, where is the particular asset located? A lot of this
information can be extracted and scaled automatically and then you can
express the impact of your business application and how much a
particular vulnerability might impact you and how many user and so on.
So that can all be expressed in a numerical form. Now you can go as
crazy as you want and I'm going to slap you with some of the element in.
37:19
Consideration of how to prioritize vulnerability and.
37:24
Where to prioritize vulnerability so you can go as crazy as you Want with
the Risk Formula. But In A Nutshell, It's Simple and help you Much More
discussing Product rather Than individual Vulnerability. Because Business
People discuss about Product don't discuss about individual Vulnerability.
And if you look at the information between left and right. If you don't
discuss about product, you see just the sea of flat vulnerability. You see a
number of critical and you focus on the number of critical. They
uncontextualize, they are not focused. On a product prospect.
38:02
But if you add the context, then.
38:04
You can see a lower priority or.
38:07
A lower impactful business application versus a.

38:12
High impactful business application, and you focus on the right versus on
the left.
38:16
Gas billing.
38:17
As soon as you see a lot of red you will focus on the critical vulnerability.
On the very long list of vulnerability chances are the one that have
probably one or two major critical vulnerability that is externally facing it
is highly attacked.
38:31
At scale is more likely to get.
38:34
Attacked and that discussion helps with the business. So shifting smart is
all what I say in trying to get the business into this kind of conversation
contextualizing. Adding the level of risk and enabling them to set really the
risk expectation for where they want to be and translating that concept
into where the engineer need to focus. Because if you unify the three
angles of business dev and ops and security, then you really reach the
nirvana. What I'm talking about that is fundamentally business driving
risk security being consulted on risk and developer having a really finite
list of things that they need to focus on and this approach has been proven
to actually reduce the noise, reduce the alert fatigues, increase the
collaboration and reduce the burnout from an application security to
vulnerability management. I'm not saying like tomorrow go out and scrub
your SLA because okay, SLA.

39:39
Have worked but they've been around for.
39:44
A while, they're not probably the best tools or if you contextualize the
SLA.
39:49
If you use specific SLAs around risk probably it's much better and you
can.
39:57
Use nuance of SLA. And we've wrote probably tons of article and a couple
of books around this on how can you evolve from pure CVSS severity
based SLA, to multi SLA based on product to risk based SLA and really to
security OKR? That is where you should aim to evolve your measurement
because those express much better a balance that the team can then
manage internally how many things you fix versus how many things you
build that could be an OKR one single security OKR you can put to your
team, to your development team and then let them manage how many
vulnerability they fix. You as a security team should provide always the
more likely vulnerability to be.
40:44
Exploited and get the business on that journey.
40:48
And if I want to leave you.
40:49
With something is acting risk and not.

40:52
Fixing vulnerability, focusing on really what really matters and this is my
mission to the world.
40:59
So conclusion today we talked, we fixed.
41:03
Security, probably not, but at least I.
41:07
Hope I've given you some foot for.
41:09
Toll, some thinking process on what to fix next. Fixing every vulnerability
shouldn't be done and it's not feasible and it's going to only lead to
burnout reachability context and exploitability can be used with different
degrees and expense in term of engineering power in terms of mental
power and talking risk and talking probability of exploitation to the
business is what delivers. I want to give some thanks to the EPSs working
group that has been absolutely fantastic to seek to produce fundamental
EPSs if you haven't used EPSs or look at it, please consider looking at
that. And then in the whole concept of richer B, there's been a fantastic
presentation by Adam Berman where Vulnerabilities not a vulnerability.
And also Timo from DSOM has been fantastic in the whole process of
vulnerability management of Wix. We have a framework available to use.
42:05
A lot of these things.

42:06
A small takeaway, we are a security company that focus absolutely on this.
So if you want to do this at scale and automate a lot of these vulnerability
decisions, we're here for that.
42:17
Stop the pitch.
42:19
But we love OAS and we have a version available for OS. So scan the QR
code, get your Oasp edition. We want everybody to be able to not burn out
and do vulnerability management at scale. And also, if you want to know
more, we have plenty of white paper around this that explain and explore
on this. And a master book on SLA and why we consider SLA of that and
how you can evolve your organization to go from pure vulnerability
management to SLA to security. OKR, and also we discuss a lot about this
on the podcast. We discuss cloud security and application security. So I
would invite everybody to visit the CSV, it's also available on our website.
And I'm going to open the floor to question because I've been talking a lot.
Thank you everyone.
43:13
Cool, no? Great session as always, man. Yeah, if there's anything, guys,
please put it in the chat. I'll be able to I don't see anything in there, but
give it a couple of minutes.
43:23
I don't see the chat.

43:25
I'll keep an eye on it, but I think it's that evolution, right? I know we start
talking about the chat gvt in the beginning and the AI. I feel that the
biggest challenge I always had with this is a lot of this, it makes complete
sense. The question is how to scale it in a business that has that on
steroids. And not just that when you talk about context and talking to the
business is not one entity. If you think about it's multiple entities with
multiple levels of stakeholders, multiple levels of seniority, multiple levels
of priorities. And I think now we're getting to the point. Not yet, but I
think we're getting close to be able to mass customize some of the content
we have so we can really put into context, so we can get to that ten or 20
things that really matter for a particular stakeholder.
44:20
And I think with a new wave of analyzing a large set of data and of course
there's a whole thing of cleaning it up, making sure it's correct, make sure
it's well processed. But I feel that we're able to provide to do this at a
much highly scalable way once I mean, there.
44:38
Is LLM, there are language models, some of this we might find correlation
in path. But a lot of this stuff is just collecting the data that we have
already and really basic stuff, it's not like rocket science, it's just getting
everything. And as you rightfully say, Dennis is doing this at scale,
collecting all the vulnerability in one central location, grouping them by
product. That is not rocket science. You can have some MLS like we're
doing, like trying to patternize and see who is maintaining the same repo
and maybe they are all part of the same product or who is doing the same
issue. Over time you will start seeing trending and other stuff, even if you
do just basic aggregation and basic analysis and then you evolve in these
three R. So at the beginning you will do a lot of triage manually and then
you start automating some piece of it.

45:26
So, yes, AI is very exciting, but.
45:29
It'S very likely that it's very easy to throw garbage in and to get garbage
out. And I'm guilty as charged. Like I've done this because I get super
excited about the new technology and I say I don't need to use your scale
and then I get good result, bad results. So, experiment. Yes, absolutely. We
have a fantastic tool that is available out there to experiment mixed
feeling about result. Like we've been discussing with Sharif and he's done
some interesting experiment. If you haven't seen this, there've been a
fantastic presentation he has done on Chat GPT and we're fixing stuff
actually or using chat GPT for code analysis. I've used it at scale as well
myself. And sometimes it gives you the right pointer. Sometimes if you ask
them to auto fix or auto patch remove specific piece of code. So makes the
code secure because it.
46:23
Doesn'T.
46:25
Doesn'T run the thing, right?
46:27
Yeah, but it wasn't taught to be dead, it just happened to be dead because
it has a lot of language and a lot of good and bad examples. So maybe if
we train something on good and bad example, maybe we'll have some
more precise LLM.
46:42
But as everything, we still have to.

46:46
Fix the basic and we still have to fix the basic stuff because business
context, the way to talk to the business that's still on us internally.
46:55
But that's where I have to say I've already had some good success on
prompting because you can start to prompt the audience that you're going
to have. You can say I'm speaking to this person which runs this and this is
the context, this is the objectives, this is the issues, right?
47:09
And I think we're doing prompt engineering on people.
47:13
It's context, right? It's basically providing ideas. And I think if you look at
the latest stuff on Palm two and vertex and I think being able to start to
teach the models with the data that we have and then fine tune it, this is
where the worldly maps is interesting, right? Because the LLM pushed all
the stuff to the right. And now you're going to start to see these security
LLMs coming to market, and they will be very laser sharp. Focus on
certain things. The same way that you have a medicine focus. One, you
now start to have security. Imagine having a risk one having imagine
feeding the ISO, the GDPR standards, the internal policies, all the kind of
the OAS. Yes, all that stuff.
48:01
And then starting there is already somebody.
48:04
That has developed that.

48:06
It's super powerful.
48:08
GRE.
48:09
Yeah, it's crazy powerful. All right, man, look, I don't think we got
questions here, so thanks again for doing these great sessions, and I'll.
48:18
See you on the next one. See you guys.
48:21
Thank you very much.
48:22
Stay safe.
