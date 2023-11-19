---
title        : "Let’s go on a DATA with vulnerabilities"
track        : Governance
project      : Risk and Governance
type         : working-session
topics       :
featured     :
event        : mini-summit
when_year    : 2023
when_month   : Oct
when_day     : Fri
when_time    : WS-16-17
hey_summit   : https://www.linkedin.com/events/7112485965855649793/
session_slack:
#status      : draft
description  :
banner       : https://github.com/OpenSecuritySummit/oss-website/blob/main/content/sessions/2023/mini-summits/Oct/banners/data%20vulnerabilities.jpg?raw=true
organizers   :
     - Francesco Cipollone
     
youtube_link : https://youtu.be/tkztNVDI44A
zoom_link    : https://us06web.zoom.us/meeting/register/tZEvd--oqD0rG9wap-L9TtyRW6N1RjaA3W2M
---

## About this session
Posture and Data don’t lie - risk and fact-driven approach on posture management with deep dive into exploitability, reliability and the likelihood of exploitation.

### Abstract
Posture is the art of representing complex problems in simple risk-based visualization. Risk posture had a lot of hidden measurements and data and was treated like esoteric art. In this talk, we explore various concepts like Exploitation, the likelihood of exploitability, Context and location of an asset and how it influences the exploitability, business impact and how to involve business with risk-based driven metrics.
The talk focus on data-driven research and visualisation techniques analysing what’s more exploitable from different data sources.
We will explore the difference between a vulnerability base approach and resolution first vs a risk-based approach and success from real case scenarios.
Find your path in this modern, challenging.
Writeup on exploitability data: https://phoenix.security/exploitability-data-visualization/
Writeup on CISA KEV: https://phoenix.security/cisa-kev-visualization/

### Audience
application security
Vulnerability management
head of application security
product security
security engineers
CISO
GRC

### Take away:
Learning how to start measuring a posture management program in application security and vulnerability management leveraging risk
metrics for an application security program
how to create a narrative around security with product security
how to involve management/business on the heartbeat of application security
Understand the concept of the product.
Understand and apply how to involve the business and insert business criticality.
Understanding the concept of prioritization and the data behind it
Understand and leverage exploitability, probability of exploitation, and likelihood of exploitation.
Understand and apply contextual elements to application security and vulnerability management.
Understand which Threat feed is actually valid and how to automate CTI.

## Transcript:
00:03
Hello everyone. My name is Francesco Sipolone. I'm the CEO and founder
of Phoenix Security and today I want to bring you on a date with me and
on a journey on vulnerability. I've been in vulnerability management across
application security, cloud security and traditional infrastructure for most
of my life and I have one thing to share with all of you I never actually fix
a critical vulnerability or a vulnerability at all for what it concerns. I only
focus on risk and I want to bring you on a journey to actually explain why
risk is really the king of decision making from an engineering perspective,
but also from a business perspective.
00:45
Business tend to say we need to act securely but what that practically
means is ephemera and it tend to convert into lip service of yes, we are a
secure business but what that actually mean in terms from an engineering
perspective is always fuzzy. And I want to take you today on a story and
on a journey on how to make that message and that risk profile really
actionable. And we can only do that with automation, with data and with
risk. Security is heavy enough and in order to make it lighter we need to
use meme. And that's the benefit of being in security, I guess. So I hope
you tolerate memes because this presentation makes quite a use of it.
01:40
And security, as I said, is heavy enough that if we approach it with a laugh
and with a joke then the message goes through in a bit easier way. So as I
mentioned, every presentation need to have the speaker slide me, big face
and smiling. So you can see it here, you can see it there. But I've been in
the industry for the past 1520 years working across cloud security,
application security and vulnerability management. I'm passionate about
this field, as you can feel and see. I've been speaking about how to
approach vulnerability in a better approach and avoiding burnout of
security professionals. One of the challenge that I always had is everybody
seems to have an opinion around vulnerability and risk. But it's really hard
when you have data that backs you up.

02:34
It's really hard to argue with data and when you are approached on I
think this is exploitable versus there is an exploit available. This machine is
actually externally facing the likelihood of exploitation is x. It's really hard
to argue with that information unless you're a data scientist. And we have
the session coming up next where we can discuss and debate around data
science and which data set do you choose as a reference to use? So on
today's presentation, I want to walk you through the scenario, the current
landscape and the data that sits behind the current landscape and the
current approach that is usually based on SLA and how do we take that
approach into the next generation, into the next level? And that is using
risk.
03:27
And I say the risk is the great unifier, because unify a lot of this data
element and help us driving a data driven approach on vulnerability and
risk. And to do so, I'm going to explore all the data sets that sits behind
our research as Phoenix between criticality of vulnerability and the
traditional data set that we have from MVD. The popularity of Unexploit,
the new addition of Ransomware and CVE use in the Ransomware, EPSs
and Edge cases where some of this data might not work. So caveats and
gotcha where some of these data don't work. And as I mentioned, I've
been in this journey, I feel your pain.

04:11
And every organization that starts in the vulnerability management space
across cloud security or application security or container security is
usually presented with a panel of red and critical alert and sometimes
false positive that is difficult to explore. And usually we tend to believe the
scanner data as the scanner has spoken, the oracle has spoken. And
whatever the scanner says, it tend to be taken seriously. But the more we
dig into the data, the more we find that some of this information is
actually not properly relevant for us, or actually might not be applicable
or might be a false positive, or might be less critical than what an scanner
say. If we take the example of log four J, a scanner has a specific limited
view of what a critical is critical. And the other aspect is a security
professional.
05:10
We don't have the empathy with how engineering works and we tend to
flood all this problem into the engineering backlog that have a lot of other
piece of work to actually continue working because that's their day job.
It's not fixing vulnerability day in and day out, despite the fact a security
professional that we hope that will be their job, or we have a dedicated
person to actually do so. And usually that's the challenge with security
champion, but we're going touch on that later. The challenge is of security.
We think security is a business problem, but business doesn't recognize
security as a business problem or as a product problem. And we as a
security professional don't recognize our element as part of the workflow
and the lifecycle.

05:54
So we end up in this situation where here there's a vulnerability report or
there's a pen test report, you're going to fix all of it right, you're going to
at least focus on all, at least the critical. And that's what usually happened
is business tends to wave off risk, tends to wave off criticality tend to
accept the risk in a blindfolded way because they don't have a way to
understand what is the impact for them in their own world. And then that
leads into GRC and into vulnerability table that are completely
disconnected and risk acceptance table that are completely disconnected
with the reality.
06:34
And we're going to have a meeting with a talk next week with the head of
GRC and Star program from Netflix exactly on these topics to actually
dive deeper on the connection between risk management, GRC and
engineering and how we can make this alive and based on data. There's a
very new approach for this, but ultimately our goal as security
professional and as an engineers and as engineers inside a piece of work
or inside an organization is identifying what to fix first. That is probably
not very easy and is actually not very easy as a job. And the bigger the
organization grows, the more challenging this becomes.
07:18
Because when you have an organization like an SME with 1000
employees, 100 developers that work throughout and two security
professionals that probably need to balance a lot of things, but at least
those security professionals have a lot of time or have an X amount of time
to actually deal with security engineers everybody knows with each other.
So you have that personal relationship. It still takes a lot of time to
actually analyze a vulnerability, but you can coordinate that approach in a
bit easier way. Now when you get to a mid size or a large enterprise, the
disconnection between security business and engineering becomes wider
and the time you have to actually look at the vulnerability become less and
less.

08:04
And what I like to focus on is, and we're going to see the data on it, we
have tons of vulnerability but only 10% are actually, the vulnerabilities are
really exploitable, it's actually less and 5% of the total number of the
vulnerability are actually reachable and 1% are, the vulnerabilities have
been targeted now. So let's see some of these data. And this is part of a
Ghana research that was looking at out of a sample set of vulnerability
that we consider, how many of them, how many of the 20,000 are actually
exploitable. And this is just one of the factor that we can consider and we
will consider in this presentation. Just one of these factor will reduce
drastically the amount of vulnerability that you have to look at, up to 1%
almost or 10% of that number.
08:57
The challenge is even with that percentage is a lot of vulnerability. And if
we look at how we approach vulnerability right now across application
security and vulnerability management in the cloud and on premises, we
tend to focus on SLA. And SLA is inherently a bad number because it's flat
and it doesn't consider the risk level of a specific organization or a risk
level of a specific team or application. So what that result is that SLA get
missed all the time because they're flat across the board. So even if you
focus on the top critical vulnerability, you will not be able to focus on the
medium vulnerability and the low vulnerability and the ticket time start
ticking as soon as the vulnerability get discovered.

09:44
There are other and specific piece of work that we've done around SLAs
time to resolve and when SLA time has started ticking. So we're not going
to go in this right now. But there are other considerations around SLA and
why SLA in itself is an inherently bad information. Now let's dive deeper
on why are we in this situation and why there is a lot of alert fatigue and
alert panning. So if you look at the raw vulnerability data from NVD, we
can see a bias of the vulnerability database that critical and high.
Vulnerability almost form the 55% and above 58% of the total number of
vulnerability available in the NVD and then the medium are actually a
huge number. There's always just 1% of vulnerability.
10:34
So there is very high chance that if we take in consideration critical and
high, we consider almost half if not more of the 270,000 vulnerabilities
that are right now available in the NBD. Now, if we explore a little bit
more on the typology of the vulnerability or the effect of a vulnerability,
we can start seeing patterns of things that are exploited at scale. Like
remote code execution is just a 30% of the vulnerability, but those are the
one most dangerous. And then if we pair this one up with the vulnerability
that are actually reachable from a network perspective and external, that
is another way to cut the vulnerability data sources and focusing just on a
percentage basic of those vulnerability that are effective. And this doesn't
require any additional technology.

11:22
This is just analysis on a classifier that you can use to actually classify the
vulnerability by typology of effect or typology of attack. Like buffer
overflow memory corruption, SQL injection and cross site scripting tend
to be more dangerous in the back end application, while cross site
scripting SSRF and openredirect input validation. While input validation
might be more widespread, the others tend to be more on a front end. So
you can also see which typology of vulnerability are there. And we've seen
over the years that the vulnerability have changed and have evolved
certain type of vulnerability, we stopped seeing them altogether. Certain
other are increasing like cross site scripting because of the web and API
usage and widespread usage.
12:15
Those vulnerabilities have stayed there while memory corruption if you
can see, has a deep dive because of the adoption of new and modern
framework that we have. But in general the web based vulnerability like
cross site Request Forgery and SSRF or CSRF, those are the two request
Forgery. Those are still very high, still today because those are
vulnerability that are exploited at scale and on the website. So because of
our interconnected word, those are still applicable and very modern. Now
let's look at a funnel and I've been talking about the 10% of vulnerability
matter, the 1% I'm going to show you and I'm going to prove you with
data on how you can reduce your vulnerability to the 0.1% of the total
number of vulnerability database.

13:10
Now at this point in time we actually push in 207,000 vulnerability in the
NVD and more being recorded. So far we've done an enormous amount of
research to actually cross reference all the vulnerabilities that are
available in GitHub and all this information are available on our website
to further review and cross reference some of these data sets. But just this
and the Bug bunty Hot vulnerability, we already reduced that 204,000
vulnerability in 9000 vulnerability, 70,000 for the one active in the Bug
bunty platform and 9000 just in the one that are potentially exploitable.
So GitHub exploit available, proven exploit available. Now, if you narrow
down on the actual Verified Exploit and you can take CISA Care, for
example, or the Non Exploited Vulnerabilities, a manually curated
database of vulnerability from CISA, part of the US government
sponsorship or GitHub.
14:18
Verified Exploited is data set that we analyze cross referencing where a
vulnerability is actually used in the wild and has a module in meta, exploit
and other exploit databases. Those vulnerability are reduced to zero point
41% to 1000 roughly vulnerability from the original 204,000 vulnerability.
So we already are targeting zero point 41% of the total landscape of
vulnerability. Now if we further narrow down and we take into
consideration things like exploit prediction scoring system or EPSs that is
basically looking at the probability of exploitation right now and in the
next 30 days of specific vulnerability coming from a series of honeynet
data. And we're going to discuss later on with one of the creator of EPSs
from Cntia.

15:09
We are already going down to zero point 19% and then if we cross
reference the active exploit or the verified exploit in GitHub that have a
high percentage of EPSs or EPSs above 0.7. We are already a 0.1 or 0.2%
from the original 240,000 vulnerability. We narrow down the scope and
the focus to 400 vulnerability and then if we take it further on and say
okay, which one of these 400 vulnerability are actually exploited or
actually present externally or which one are these on critical asset? If you
take even these two elements into consideration we are going to be on
.0.1% or 0.1% of those original data set. This to say that we don't need to
submit to the vulnerability overload and to the scanner overload and be
flooded with all this alert fatigue and without this information.
16:18
The challenge is as a business we hear Lock for J or we hear critical
vulnerability or a zero day and the knee jerk reaction is panic. Do I have
that problem? Am I going to get hacked? As a business owner those are
the information that cause panic and the knee jerk reaction is talking to
my security professional and saying are we going to get hacked, let's fix
all this problem altogether. And we've seen this year that we had one of
these high critical alert on a weekly basis or recently we had curl and Lib
curl that was vociferated as critical vulnerability, it was actually reduced
to much less.

17:00
Lock for J, spring for Shell again last year were causing massive panic on
Updating library directly and indirectly and without this data we can't
actually sort out or we can figure out between those vulnerability and
other critical vulnerability which one are going to get us hurt. And without
data we're never going to be able to have that judgment or fight back or
discuss back with the business on saying these are our external asset, these
are the one vulnerabilities that are actually likely to be exploited because
they have an exploit available and highly likely to be exploited in the wild.
So let's focus on the external surface first and then the second line of
external surface and then all the way down to the internal in a sequenced
approach. No business person will ever fight back.
17:48
That kind of reasoning because it's logical and it's based on data. So
business and how do we communicate with the business with all of this
very technical information and how we can convert this into a business
talk? What is love or what is risk, baby doesn't hurt me. And as I said, we
need to joke a little bit on these terms because if we only talk about data,
it becomes a little bit heavier. So I want to go with you on a journey on
why I really like risk as a way to communicate with the business on these
kind of terms of likelihood of exploitation and the ability to discern on
what is more risky. What is less risky.

18:37
The challenge is when you talk to an executive or anybody on the C suite
and you start talking about vulnerability, the reaction is I don't understand
this report, I don't understand these tons of information on this executive.
I had tons of critical, which one do we focus? Are we going to get hacked?
Those are the information knee jerk reaction that we're going to get from
a business person. And if we present that on a weekly basis, we're going to
get kind of a rejection by default because if we scream continuously that
we have critical, critical problem, the reaction is maybe those critical
problem are not that critical. On the other point, if we talk about risk to
the engineering community, they talk about number of sprint stories or
number of action points that needs to be done on the next sprint.
19:33
If you're working in Scrum or Agile, those kind of terms don't
communicate and don't tell them anything that is relevant in their context.
So we need to be able to speak with the business in term of risk because
that's in their context. They can express I want to operate at this risk level
or I want to operate at this other risk level and that doesn't even tell
engineers what critical vulnerability they need to solve. But we can
translate that information from an engineering perspective on which are
the critical vulnerability or the non critical vulnerability that's going to
have the biggest impact to achieve that risk level from a business
perspective.

20:07
And that's the way to connect a risk objective that is a context of business
into engineering community, into number of action that needs to be
resolved or execute to actually meet those expectations and in order to do
so it's not rocket science, it's not ephemeral science and this is our
interpretation of risk. So we take the base severity of the vulnerability and
we use base severity for a very specific reason. We use base severity
because it's a common language across all the vulnerability that we have
available right now and it doesn't tamper with any other information.
Then we take the probability of exploitation that is derived by in an
automated fashion and in an automated way by the likelihood of
exploitation.
20:53
If there is threat intelligence that tell us that information on that
vulnerability is exploited in the wild if there is a fix available or not, or
where that particular asset located externally facing or internally facing is
and all of those information give us a good sense of what is the likelihood
of exploitation, of a specific vulnerability, then the last but not least
important element of risk is what is the business impact? How much this
particular set of risk is going to impact me as a business or how many user
or how much importance has this particular application. Now I want to
say and I want to put a caveat that I'm not going to go in detail around
several aspects but it is important to consider in further research on three
terms that is reachability.

21:49
So if a particular vulnerability is actually reachable from a network
perspective or non network perspective or a particular line of code is
actually reachable from a library perspective, those concepts we're going
to go around those concepts we can actually build a whole presentation
around it and we've been talking in the past around this. But exploitability
is another concept that we really talk into and through and we're going to
see a little bit more because it's relevant to this particular presentation
versus context that we already discussed and there is business context as
well as system context. So where that particular vulnerability manifest
from a network perspective, from a location perspective, is it external, is it
internal the system where that particular vulnerability manifest? So let's
see the magic behind risk and risk calculation.
22:43
Now I tend to use and attend to love the use of a matrix that is easy to
harder in term of automation and in term of data accessibility. Now we
have the level one where we can take all the vulnerability in bulk and
automate using and achieving, as we've seen in the funnel before, a very
finite and a very short number of vulnerability or finite number. Of
vulnerability looking if there is an exploit available or if people are
targeting that particular vulnerability that's what we call popularity with
bug banti or if in the CVSS vector this particular vulnerability is
attackable by a network perspective. And this particular vulnerability has
a remote code execution attribute that will tell us that it's easy or to a
specific percentage to deploy a piece of code remotely to the system.

23:38
Now reachability from a code perspective and partially from a network
perspective becomes much harder to understand and calculate, where the
other factor that we explored are easier to calculate because there is data
availability already at scale on those information. And the scale between
harder and easy on this scale, on the vertical scale is a risk, reward
opportunity that I see. So the harder it is, the harder and more time and
effort we need to invest in terms of calculating this information and the
less we receive in terms of benefit from this calculation. So we like to
balance and take an approach that takes a lot of this information and
enough information that enable us to make a decision because that's the
ultimate goal we want from a triaging perspective and from a
vulnerability management perspective.
24:33
So from a location perspective we can see if something is exploitable
remotely where it is from a location perspective is it externally facing? Is it
internally facing and more harder to calculate? Is there a particular
attack chain path that this particular vulnerability or a set of
vulnerabilities can be chained together? Again from easier I mentioned the
data point from the easier point to the harder point and those needs to be
considered from a risk perspective. And lastly but not least is business
criticality. So is this particular application business critical for me? And
hence I need to focus a bit more or less. And hence we have two system
that is a business impact assessment or fair analysis that is a bit more
complex and deliver a more granular perspective on risk and business
impact.

25:25
But also it's much harder to implement at least the area that we can't
really automate. That is the manual triage. So this is the last stage where
we can determine if it's a false positive. It's something that's been raised
by the scanner that is actually not exploitable but there is an element that
we're doing right now that is we put false positive and manual triage at
the beginning of the flow, not at the end of the flow. Hence at the end of
this flow the number of vulnerability that we end up dealing with is 0.1%.
If we put the manual triage at the beginning of the flow the number of
vulnerability that we have to deal is 270,000.
26:07
So there is a scale difference in here and the likelihood and the chance in
term of risk reward perspective that something going to go amiss is very
high while in this chance in this particular environment is very low. Now if
we take the concept of exploitability we have different level of
exploitability. We have how likely is vulnerability to be exploited in the wild
by popularity? So how many people are looking at it, how many link in
GitHub are available or in packets form or how many people are targeting
that particular vulnerability. From a bug bunting perspective, from an
exploitability perspective, we have also the element of zero day where
there is no patch available. So usually those are not it's rare that we hear
a zero day, that we usually hear a zero day when it's too late and when it's
exploiting the wild.

27:06
So for this there are Mitigating control and mitigation element, there is a
Google zero day project and Trend Micro zero day project that have some
of this information available and few other less more obscure sources of
information about zero day. As I mentioned before, there is an element of
automation of an exploit and hence executability by automation. That is
there a vector or a particular element in the vector that tells us that
exploit is remotely executable or requires zero authentication? Those are
the two parameters we tend to focus a lot in the vulnerability exploit or if
that particular vulnerability is a remote code execution, hence the exploit
and the payload of a vulnerability can be deployed remotely. And the other
data aspect that is really key to actually prioritize vulnerability is this
particular exploited at scale and is actively used at scale.
28:09
Now, there are caveats where the threat intelligence come into place,
where certain cases shows us from a broad cyber threat intelligence that
this vulnerability is exploited in the wild at broad scale. And then there is
targeted CTI that tells us there are specific threat actors that are targeting
this set of vulnerability at scale because of ransomware, because of your
industry, because of you. And there is an element of risk reward against in
this prospective where if your loss or the consequence of an exploit are
actually super high, you should consider targeted CTI or expensive CTI,
because it tends to be not. Cheap to implement good CTI because it's
usually manually analyzed data that needs to be put in there. But that has
an extreme value if you can identify and exploit before you get hit again.

29:07
Risk Reward Perspective the broad CTI like EPSs enabled you to jump on
a vulnerability or to reduce the noise of a vulnerability. Now, as part of the
data analysis, we did an overview of the top ten vulnerability that is either
more exploited, more critical or more exploited at scale. Now, the
popularity concept, again we can see some pattern around. It's interesting
to see that the top critical vulnerability are actually Oracle, Apache,
Debian while the more exploited vulnerability from EPSs perspective and
in terms of number of exploit available at scale is actually Microsoft. So if
you already take criticality as an element to actually decide if a
vulnerability is exploitable or not, you're really too late and you're already
doing something wrong because you're focusing on the wrong
vulnerability that people are not looking at versus you missing the
vulnerability that people are looking at.
30:09
Oracle and Log four J is popular and kind of across the board available
throughout Apache threads, debian vulnerability. These all come from the
amount of installation and we're going to see this number actually
reconfirmed from who is targeting this vulnerability at scale from a
ransomware perspective. And I have one of my favorite sentences not all
the critical are critical and not all the source are actually good source of
information. So we're going to see and compare here in the next section
source of vulnerability information. I'm going to go a little bit faster. So
on the left we're going to see the analysis from GitHub NVD database and
on the right we're going to see the Caesar cave and EPSs and compared it
to data set. If we see the first data set that is just criticality again.

31:05
Oracle, Apache, Debian, Microsoft, those are performing well while in
Cisco kev in terms number of vulnerabilities that are actually actively that
have an active exploit at scale, we can see Microsoft jumping very high up
in the score Adobe apple. So there is a big discrepancy between choosing
just the critical vulnerability or looking at the vulnerabilities that are
actually being confirmed to have an exploit. And all of this link will be
available in the PDF and in the website. So you can actually play with this
data set and see and dig a little bit more into these data sets. Now the
popularity of an exploitation, we can see the numbers of link available
throughout several platforms.
31:53
Microsoft, Oracle with Log four J, Debian, Apache, Red Hats, the top
exploited operating system are actually the one that have the majority of
vulnerability at scale across various data sets. And then if we take high
PSS and the previous data sets we can see that out of all the GitHub
exploits available, just a fraction of them are actually available and
actually exploited in the world. And if we take the same information
around EPSs and CISA Kev, we can see again a fractional, a very finite
number of those are available. The reason why we take EPSs above 0.6 or
0.7 is because those are the factors that we consider to have the
vulnerability more exploited at scale.

32:49
And then we have a certain division above, basically the 0.7 where the
majority of EPSs are at, but is even a further refinement of all the
vulnerability available. And if you can see a lot of the vulnerability, up to
94% are scoring a value that is 0.11% or 0.1% of likelihood of exploitation
in the wild. So this enable us to really focus on the vulnerabilities that
actually really matters. Now, Sisakev also has published a top routinely
exploited vulnerability. I'm going to go a little bit faster on this element
where we can. See the top twelve vulnerability exploited in the wild at
scale. And you can see again these data sets available. Recently Sisa Kev
has also crossed two projects together that is basically number of
vulnerability exploited between the sysercave entry and used by
Ransomware.
34:00
And again in here we don't see a lot of surprises. So Microsoft is the one
that has the biggest attack surface overall, hence why they're being
targeted by the exploit. Now I want to rephrase and I want to refresh the
concept that a lot of this information can be automated and can become
the probability of exploitation together with location that enables you to
focus on the 0.1% or even less if you consider business location. Business
context and location. That leads you to a 0.1% of the total number of
vulnerability that you have to consider.

34:37
So to wrap it up, the data set to consider are EPSs for the probability of
exploitation, CTI against a bit more refined CTI to actually look at the
likelihood of exploitation, elements that are used in ransomware from the
CISA cave database, location of an asset for the likelihood of exploitation
and the reachability from network, as well as the type of vulnerability.
Now, how easy is to deploy an exploit? The element you should consider is
the popularity of an exploit. So how widespread is that exploit? How
likely? And how many times is this exploit used at scale? If it's widely
available, if it's been verified, or if there is a module that actually for this
particular exploit to be deployed, and again, exploit being using the wild
leveraging EPSs or your CTI data, and you can see the various module.
35:37
We did also analysis on the top twelve and the methodology of attack from
the top vulnerability exploited last year. And as you can see, remote code
execution is the one that is most used because logically those vulnerability
are easier to implement and easy to weaponize at scale, either if you use
ransomware or if you do a specific targeted attack. Now, I want to cover
in the last five minutes a couple of edge cases where some of this
information might or might not be useful. So EPSs tend to have a 16 to 30
days synchronization effect with new vulnerability at scale. So if we take
OpenSSL vulnerability that was mentioned at the beginning of this year,
temporary had a 4.5, ended up being very high for a specific amount of
period.

36:32
But EPSs code was super low for a long time, while the CTI interest for
targeted and refined CTI information was really high because of the
distribution across number of systems available. So it was something that
attacker really looked into. Another vulnerability that later on got really
attention and got really exploited at scale was VMware or QNAP systems
because those vulnerability got a lot of attention from Ransomware
perspective. Original CBS 8.8 a lot of high interest from CTI. Again EPSs
very low and it ended up catching up later stage. So those are cases and
caveat when using CTI versus EPSs that there is a little bit of a delay
between when a vulnerability get published and when a vulnerability get
exploited at scale. So to wrap it up, you can get information around
likelihood of exploitation in comparison with EPSs.
37:46
When EPSs is low, always double check if the vulnerability widespread. If
there are a number of systems, for example in Shodan or Gray Noise that
are highly exploited or highly available, or shadow servers is another good
data source of information as well as hacker one data and other bug
bounty data to see fundamentally if that vulnerability is exploited in the
wild. We have a lot of this information under exploitability and probability
of exploitation and the popularity in Phoenix Security to actually enable
you to do this at scale and the least, but not last. You can see the
methodology of attack like CWE Capex. This becomes a little bit more
complex to dig into.

38:35
So I want to conclude that vulnerability at scale tend to be a tunnel and
very hard and very heavy to explore and dig into, but there is a light at the
end of the tunnel. To summarize manual triage is not practical, it's not
effective. EPSs is a great source for prioritization context, location and
other factors can help further down refining the vulnerability exploitation
and the one you should focus on and risk enable us to talk with the
business in a better way. And if we identify the single thread of risk to
vulnerability, we can enable the business to communicate and to connect
with the majority of people. Now, I want to leave with a last comment,
that is this is what we do at scale with Phoenix Security.
39:34
We are a data driven company that use a lot of detail set to actually
contextualize, prioritize and deliver high quality feed to engineer at scale.
You can find us on Phoenix Security and a lot of these data sets are
available. We love the community. So we made available a version of
Phoenix Security with OWASP and you can get access to the Phoenix
Security edition from Oasp using this QR code that you have available in
here. A lot of these data sets and a lot of this information are actually also
available on some of the write up and the publication that we did around
vulnerability management at scale and Application Security program at
scale.

40:19
You can find them using the QR code as well as the new tool publication
that we did around the use of SLA and how to move away from SLA and
into a more data driven and risk approach. Again, the QR code will lead
you to the specific page or building a resilient application security and
cloud security program using this QR code. We also discuss around this
particular topic on the podcast CSCP or Cybersecurity and Cloud podcast
with a lot of thought leadership around the world. So I'd like to thank
everyone for your time and effort. And I want to thank all our defender for
actually defending and helping our business to get up to date and safe
every day. It's not an easy job, and we're here to help you all to get less
burnout and more focus. Thank you very much.
41:19
I'm going to open the floor to the question. I'm going to stop recording
right now.
