---

title        : AppSec Threats Deserve Their Own Incident Response Plan
track        : DevSecOps
project      : DevSecOps
type         : working-session
topics       :
featured     :
event        : mini-summit
when_year    : 2023
when_month   : Oct
when_day     : Tue
when_time    : WS-15-16
hey_summit   : https://www.linkedin.com/events/7109694688676241408
session_slack:
#status       : draft
description  :
banner       : https://github.com/OpenSecuritySummit/oss-website/blob/main/content/sessions/2023/mini-summits/Oct/banners/appsec%20(1).jpg?raw=true
organizers   :
   - Omer Yaron
  
youtube_link : https://youtu.be/KqU1ZurRqnU
zoom_link    : https://us06web.zoom.us/j/84564562148?pwd=ajN5aHFROG9JNlowT1NjcUViZXArdz09
---


## About this session

Despite the popularity of AppSec related incidents, most organizations do not have an incident response plan in place. Those that do have an IR playbook, often prepare to respond to infra-related attacks such as ransomware, rather than app. Attacks. Given the prevalence of these attacks, this presentation will provide a quick response playbook and review the characteristics that make AppSec IR deserving of its own plan. 

Publications:
https://www.darkreading.com/application-security/appsec-threats-deserve-their-own-incident-response-plan

## TRanscript:
Alona - 00:03
All right, good afternoon, everyone. My name is Alona, and I'm the host
for today. So we're going to talk today about AbSec threats deserve their
own incident response plan. And our speaker for today is the head of
research for security, and his name is Omar Yaran. So over to you, Omar.

Omer Yaron - 00:30
Yeah, hi. So I've just shared my slides with you. I also want to mention
that in the last few months we have been acquired Enzo by SNCC. So now
we are part of yeah, but this relates to research that I performed at Enzo.
So basically I'm going to try and persuade you or convince you that one of
the main things that you should be doing if you're managing a security
team or application security team is probably take a look at your incident
response plan for the supply chain because this is basically the biggest
growing attack surface currently today. And there are a lot of small things
that you would probably want to do today and not on the day that you
have an incident.

Omer Yaron - 01:40
Because a lot of the field of supply chain in open source especially, is a bit
confusing and a bit filled with terminology that is just recently been added,
and it could be under stress, too much to handle, and there's a lot of
things that you can do to prepare for that. And part of the things that we
encountered that drove us to this research was the fact that a lot of
customers were coming to us with questions that we thought they should
have known their answers by themselves before. Okay, so I'm Omar, senior
security engineer at Sneak. I previously was the head of research at
Endoseecurity. And previous to that, I was doing quite a lot of incident
response and forensics in that regard.

Omer Yaron - 02:45
And later I had the privilege for working@wix.com and had a lot of kind
of two sided view of attacks and what a company looks like during
routine. Okay, so looking at the agenda, so I'm going to go over it. I'm not
going to spend so much time explaining it here. So first a bit about the
attack vector of supply chain. So I like to go over historically a bit what
upsec is or was in the past and what it is today. And historically, I think
that application security was generally the domain that used to protect a
deployed application, meaning that you go into every part of its
development lifecycle from the beginning to end. This is like the secure
development lifecycle. And then you perform operations during that time.
And then there is a PT usually that is performed over the deployed
application.

Omer Yaron - 03:58
It could be on a demo environment, a QA environment. And the supply
chain in all of those kind of risks was mitigated by a static build of
materials, a bomb file, which in recent years, we hear more and more
about it, including, like, the biden order that recently came into effect that
specifies specifically which specific fields and contractor needs to require
to have a bill of material. So this was again what we did historically with
application security and It security was very much in the realms and
responsibilities of all the developer workstations for incident response like
EDR tools and tools like that or Antiviruses and all that.

Omer Yaron - 04:59
Of course updates and also servers like server stations and servers in
general was incident Response was the It kind of realm and they were the
one that would require everything to be updated in terms of workstations
and server. Okay, so that's how historically it has been looked like the
realm of application security looks like. And then in the recent years with
the introduction of Agile Shift, left development, DevOps and agile
development and all of that changes that brought a lot of productivity
capabilities to applications and also shifted the way application security
kind of what was under its realm and what it needs to address these days
kind of grew over it at times. It security. So we're talking changes, all are
written here. We will focus a lot about CI and CD pipelines, mostly the
continuous integration.

Omer Yaron - 06:15
So every time a new change is introduced it can be automatically
integrated and built and that means a lot of things but also generally like
a lot of application handlers for infrastructure. So a lot of the
infrastructure has moved into code based, right, infrastructure as code
and in the hands of a developer basically. Okay, so now it constitutes as
part of the application stack, we see it as part of the application stack.
And so this is to create a lot of challenges for application security
infrastructure, incident Response because it make it a lot whole and a lot
more kind of ways to understand it. We used to look at logs and see what
was the third party doing, what was his vulnerabilities.

Omer Yaron - 07:25
But now it's a lot more than vulnerability management because there's
also an attack surface that actively use open source as a vector to get into,
to infiltrate an organization. So a bit about the software bill of material.
So again, this is the concept that what's the problem. If we take our code,
run it through one of the tools like Cyclone DX, which is a well maintained
tool, and it will go into all of that digestion. And in the end, we'll have a
full list of all the ingredients, third party ingredients of that software, and
then tomorrow there will be like a log four J kind of issue. And we all be
able to look at that file and say, okay, here we have it or we don't have it,
and we have it here and in this version and so on.

Omer Yaron - 08:27
But apparently this doesn't really work and it doesn't work as well as it
should work and a lot of organization could not easily answer that
questions do we have it or not. And so we set out to see what's missing and
write a bit of context. These are a few incidents and events relating to S
Bomb across a Google Trend timeline of searches. And we can see it trays
over the last couple of years grown significantly. And I added here ESLint
Scope incident, which is the first incident that I encountered in real time,
that we started to think, what are we doing? How should we as a
company? I was working at a company at the time as a security
application, security professional, and then we needed to come up with
answers for R D to say, are we under any threat or not?

Omer Yaron - 09:46
This was an event that someone hijacked. Very popular package, sub
package, obvious Lint, which is a very popular linting for JavaScript, NPM
based. And then we go all the way to the log four share log four J incident
of December 2021, where a lot of people were looking and trying to get a
sense of what is their software billow materials look like. Okay, so here is
an example of how an S bomb is created. This is CDX Gen, the index JS
file from GitHub, and this is how an S bomb is created for Python files.
And we can see that the instruction for the function to create the Python
bomb is actually looking for files that are either a folder with the name
Poetry Lock or Requirements TXT under any folder, or some folder that is
named Requirements. And there's a file named TXT.

Omer Yaron - 11:10
So it looks pretty simple, right? You look for Pip files, for Poetry files, and
you try to list all of those ingredients in the requirements. But when you
look at the Requirements TXT, the Requirements file format, you see that
Requirements. TXT is usually what these files are named, although this is
not a requirement. So any organization could or any convention could go
and say, I don't use Requirements TXT, I use some other file name by
whatever the project name or requirements, project Name Requirements,
environment Name like Requirements, QA Requirements, Prod
Requirements, I don't know, Stage. And then the SBOM generation would
just kind of overlook it, oversee it. It would be in its blind spot because of
the way that it works. It goes over files and it can't look over all of the
content of all the files.

Omer Yaron - 12:23
It's a CLI tool that runs over filepath, so it has to have some kind of check
for file names. And this is just an example, of course. It goes over all of a
range of basically any other technology for supply, like open source
registries, you name it, obgems go some files, or any technology basically
does that in some way relies on file names. So this is one thing that we see,
and we thought, okay, there's a lot that can be missed. And what are we
actually looking for in an SBOM. Where we're trying to find a descriptive
way to describe all the open source components and all the things that
comprise an application in context and not missing on anything?

Omer Yaron - 13:29
And also making it more not like a permanent kind of snapshot of an
application but living updated kind of always changing, always keeping
track of new changes that introduce into a modern application which
again always has integration tests and always keeps changing rapidly
changing. So we wrote a bunch of stuff and we started and we checked
which of those things we can get automatically or not, what can each
organization can do by itself and kind of put in his own customization, his
own business logic, his own uniqueness in a way into his applications, into
the metadata representation of an application. Jumping back to the show,
a bit of what we come up with but looking just from the attacker
perspective, obviously I think no one would think otherwise, that this is the
fastest growing attack surface. There's a lot of public data to harvest.

Omer Yaron - 15:05
All of those registries are public. You can easily list all of the most
downloaded dependencies for each technologies. And aside from that, you
can also list a lot of other interesting data like which has the most
maintainers, which is updated frequently, which of the public git
associated repositories, let's say, doesn't validate signatures? I don't know.
There's a lot of things that you can test which of the maintainers email has
an email that is on a domain that is no longer valid and is open for
purchasing, for registering that domain. So a lot of easily accessible public
data that can be used in a lot of ways and for attackers this is really good.

Omer Yaron - 16:13
Also you can always take a large list of maintainers, try to get that list
over, looking for combo list of username passwords and trying to see if
you can maybe find some maintainer that reuse this password. So there's
an attacker, there's a lot that can be done and also there's a lot of open
source kind of ecosystems to look for. So just the best of information that
is publicly available is really good for attackers and also there is a great
return on investment for attackers. So let's say you have invested a lot of
time, but you will manage to access a fairly popular package maintainer
account. That means that you have the ability to get into thousands,
hundreds, millions of workstations servers, CI, pipelines, if you were to use
that whenever you see right?

Omer Yaron - 17:29
And also you have a lot of ways to kind of hide yourself. You can always at
times unpublish a package, you can always kind of change the code that is
fetched from external URLs. You can change it as you want. So you can
add some package which dynamically changes its code according to, I
don't know, the IP that it comes from or timing or how you see fit on the
server side that holds your static code. So you can maintain yourself
unvisible, right? Non malicious until you want to. Also there are very little
security controls over public registries and malicious packages in public
registries. So that also gives a lot of kind of backwind to attackers.

Omer Yaron - 18:40
It is true that today there is much more that has been done by public
packages repositories but still it's very lacking like from other fields that
are more mature kind of security wise. You can see it just by recent
incidents where a single user, NPM is a very good example because it is
very publicly known and used and tested and has a lot of information and
also I code in node from time to time. But NPM suffered basically a denial
of service a few months back just because someone he wasn't per se
malicious but he was someone who registered a lot of packages so created
like an overload so there was no limits and so on.

Omer Yaron - 19:52
And again we're talking about completely anonymous user adding
whatever code he wants as many times he wants and causing real
organizations to suffer downtime for their CI, not able to fix bugs. That's
like very crucial things for NPM just to maintain their so that's bad for
everyone, right? And again, they do make some more effort. Some
maintainers are required to do two FA multiple factors. Ago we would
have never dreamed that would be like a requirement, but today it's not
enough. Okay? So that's hackers going to hack and supply chain threats.
So again, if we look at the OS top ten risks, which is highly regarded as
industry standard for the risks of web security, so we can ask ourselves
where do we see supply chain attacks? So we don't really see it.

Omer Yaron - 21:16
If I'm giving as much credit as I can probably say that it relates to
vulnerable and outdated components might be related. It also doesn't have
to be outdated or vulnerable. It could be malicious. This is like a different
kind of threat. And also security logging and monitoring failures. Again,
why? Because it relates to that, but it's not the best. Okay? It relates to
that because we are lacking a lot of the times in CI logging for data that
we need like did we build this package during this time? So it relates to it,
but it doesn't clearly has anything say specifically about this threat. And
I'm positively like my prediction would be that the next and it's pretty
close, right? 2025, it's going to be every four years, right?

Omer Yaron - 22:19
So my prediction is it's going to be probably a category by itself like
supply chain attack or vector or confusion attack or whatever, but it will
be one of those and I think it would be pretty also eye up as a risk because
it's happening in the wild with it. And again, just from the sheer volume of
this kind of vector, I think we won't see it stopping it's only going to grow
this trend of an attack vector. So just to be a bit more clear about the
terms that we use, so there are a few different kind of different risks when
we're talking about packages. So one is a malicious public package, which
is a malicious code published on a public registry. So this was like the code
was born malicious.

Omer Yaron - 23:38
It never had a single other purpose other dispackage, other than being
malicious. Okay? And then there is a rogue public package like ESLint
example that I gave, which is a legitimate code that was updated with
malicious code, right? Maintainer takeover account, takeover of the
GitHub account of whatever. Or someone just deciding that he's taking his
package and making it malicious for whichever purpose. But that's what I
call a rogue public package. Next we have dependency confusion, where
in dependency confusion, there is a public package that takes presidents
over a desired internal package, right? So this is the confusion. It's RCI or
one of our pipelines is tricked into getting a malicious package that was
added by someone malicious as a public package.

Omer Yaron - 24:52
And it will take and since it's the same name, there are certain flows
where the public package will take president over the internal package,
which is meant to be taken to be integrated and built. And then there's a
vulnerable package. Vulnerable package like log four J in the log for shell
CVE detected. So this is a non malicious package which was found to have
a vulnerability. Of course, the log for shell is a very extreme example
because we know that it was a very high severity and it was used in the
wild. So we know that a lot of efforts were going there. But generally
when we see any of those kind of threats, we suspect any of them, we
think any of them happen. So in our own CI. So any one of the first three
is an indication for a breach. Right.

Omer Yaron - 26:06
If a malicious code doesn't matter if it's born malicious, was changed to
malicious, or was confused to be taken over legitimate code, any one of
those incidents is basically a breach. You need to treat it like one. You
need to validate whether or not the code ran in your pipelines. But if it did,
and you have indication for that, it means that you might need to rotate
all of the keys and all of the assets that are related or affected, including
the developer station and other developers that might have ran it. But the
developer station that introduced the specific vulnerable code, vulnerable
package. Right. But in the case of a vulnerable package, by itself the only
indication that some vulnerability was introduced by a package, this is by
itself not a breach.

Omer Yaron - 27:06
You can obviously update, you can maybe decide that in some cases you
want to check the log to verify that nothing was being used as part of that
vulnerability. But this is by itself a vulnerability is not an indication for a
breach. And so this is very important. If you need to take one thing, it's
probably some of that you cannot fix a breach by updating. You cannot
just update a package and say okay, I fixed it. Unlike a vulnerable package
where you can update and say okay, the vulnerability is no longer there. In
those cases, the first three you need to go and be prepared with an
incident response because you may be breached in a very pretty sure way.
If any of these incident did happen, you need to treat it as a breach and
it's important.

Omer Yaron - 28:26
Every breach has to have some kind of incident response. You have to
assume maybe someone has some of the credentials that are available in
those environments where the code has ran and you need to validate that
or rotate and check for any activity according to your own incident
response plans. Some don't have incident response plans and they rely on
external, some organization rely on external teams so that also has
repercussions. So you might want to have, before you call someone, what
do you need to validate, what do you need to check? Maybe you can have
enough resources to address the initial triage yourself so it might be very
important.

Omer Yaron - 29:27
Okay, so if we're looking at what at stake from an incident response view
so let's say you have some indication that malicious package was used
inside your CI pipeline or inside or at a developer station was run and
maybe exfiltrated MRC file or credentials for the VPN, whatever you
suspect. So basically, you need to first try and see what the indication
means, what it relies on. What are the generally, I would always suggest to
create a timeline to try to understand, because a lot of the times you can
say. Okay? For instance, we just got a notification that some package was
taken during the last week has been updated with malicious code, and
now it's been known and it's off and whatever.

Omer Yaron - 30:45
And now we need to say okay, during this week have we or have we not
built this specific version into an application, into one of our applications?
So this might be something that you can answer or not. You need to have
logs, you need to know what you're looking for and you need to maybe
look at what would initiate build. So build could be initiated manually and
they might be initiated by a new merge request or by a new, just by a
commit to a new branch, to any branch or just commits to a specific
branch. So we want to know that basis. This is the initial triage to
understand whether or not there is anything to follow and then there is a
verdict. Basically validate or accelerate to exonerate is usually harder. To
validate that something is malicious, it's usually easier.

Omer Yaron - 31:58
But to exonerate you want to be 100% sure and then after that you want
to identify the first line of attack of assets at risk. So let's say it's an
application, then what is credentials? So it could be the CI credentials, the
environment of the deployment environment. Again, where and when and
how it was deployed well and don't forget the developer credentials, its
workstation, because today incident Response, like I said, as part of the
application, kind of the application extension right into a lot of realms.
Then today the It who will check the workstation of the developer, he
might be able to check some of the physical forensics for the computer,
but it might lack in does new git commits were entered as this developer,
would he be able to know what he's looking for?

Omer Yaron - 33:18
Would he know what logs he has in his git audit that is available for him
and what is not? This is usually more in the realm of application security
as they also a lot of the time they deal with the different development
groups, the different development teams and the GitHub code owner files.
Git code owner files. It's usually more in the domains of the application,
rather It or something. And so all of those kind of checks should be
performed for the developers that are related to this incident. Mitigation
Threat for first Line of Assets so this is what you do for the first line of
assets in case you define them and you see which of those might need to
rotate keys, might need to remove any changes that have been created
automatically.

Omer Yaron - 34:29
So, like, revert to a specific date, to a specific time, and then you keep on
and perform digital forensics for any kind of you broaden the lines in case
there was movement, right? Some kind of lateral movement within the
application. Then that's where you go into the less stage of trying all the
time to validate that everything was exonerated and clean. Okay, so again,
if we're looking at the challenge edge for investigative, then this is an
example again from npmjs. So packages can be unpublished. So if
someone, for instance, if it's something like dependency, confusion, attack
and someone updated public code, you might be able to remove that code
by the time you try to investigate it. So you want to know what that code
was doing.

Omer Yaron - 35:38
Unless you have that and out of the know, the indication that something
ever happened is that NPM removes a package and when it removes a
package, you get the security holding kind of you get a generic for that
version. You get a generic kind of security notice warning, but you can't
access the actual code. So for investigators, for the people who do the
incident response, they need to understand that this is part of the lifecycle.
So you might not have access to the particular code. So it might be harder
to investigate. Again, there are some ways you can go at such a challenge.
You might be able to look at mirror repositories that might have it and
might not, and might have the latest version or might not. There's a lot of
ifs, but all of those you want to kind of think ahead.

Omer Yaron - 36:48
What I've shown previously is that most of these things and this can be
basically kind of automated and enlisted in the terms of what we have and
what we don't have, like identify the line of assets. This could be easy.
Usually, you know, what an application, which databases they have access
to and so on. You can do it prehanded or you can at least do it once or
twice to a drill to understand what is missing, what logs are missing. Like
this is an example again of something that you pretty easily can find when
you start to think about it as if you're trying to investigate it and then you
find out that packages can be unpublished and unlisted. And so it makes
you think, okay, maybe I need to, whatever, put aside all the code that I
download.

Omer Yaron - 37:55
Maybe I need to have a caching mechanism. Maybe you can find your own
answers, I'm sure, but just thinking about premeditating, about the
challenges that arise, it will save a lot of time. Okay. Also a few things
about the nature of supply chain attacks. So a supply chain attack, it
might affect many organizations. Take for example, log four J, which is
again not an it was an attack in the sense that a known vulnerability was
being used in the wild, but any other ESLint care or something that causes
a lot of organizations to kind of wonder if they're related or not. So what
it creates is a surge in professional needs. Right? A lot of organizations at
the same time, let's say log four J calls their on call teams or calls whoever
professional, would they advise it at these kind of times.

Omer Yaron - 39:14
And all the advisors are overwhelmed with requests because everyone is
experiencing the same thing. So if you rely on external professionals,
because some people do in those kind of attacks, you have to have a bit of
more, I think, kind of plan, incident response plan because it might take a
while until you'll be able to be until you'll be serviced by your professional.
But also there is a bit of comfort that there's a lot of others that are in the
same boat in the same situation with you because scale breaches more
time for each of us to kind of individually respond each organization.
Why? Because usually it's not like the data that was breached, like, let's
say NPM credentials, it's not at that moment automatically being used to
exfiltrate all the data that is available. It's harder than that.

Omer Yaron - 40:48
Each one usually can be automatically except maybe getting all the
packages that are there. But if you want to do more, it would probably
require more from the side of the attackers, which at the time are being
bombarded with a lot of credentials. So it might work that you can have a
bit of more time if you need to rotate keys. In that case, the more the
merrier for each the risk reduces because it's a lot of people that are
under attack but still you don't want to be there. And a breach can be
highly targeted or widely spread, right? You have a very similar results. If
it's very targeted or widely spread, you end up with the same result of
someone might have breached this pipeline, have the credentials that are
available by the environment, let's go from here.

Omer Yaron - 41:58
So it kind of funnels everything into a very maybe similar incident
response, a lot of the scenarios. Also a dedicated attack is always more
likely to escalate quickly because someone is targeting specifically you for
instance, usually because it's name based dependency confusion attacks
would be more likely to be a dedicated attack. So if you think of generally
of dependency confusion, it's usually targeting like naming of specific
organization or premeditated knowledge of how like if the front end code
is exposing names of internal packages. So a dedicated attack, you can be
quite sure that it's more dedicated to your specific organization and then
you would want to escalate it quickly. And generally just a very general
sense that a breach cannot get fixed by an update.

Omer Yaron - 43:17
These are like two separate things when you want to fix something and
when you want to investigate and potentially have respond to a breach.
Okay, completely two different things. Need to remember that. Okay, in
my last ten minutes, but I want to give some time, I'll go over a bit of our
predictions and what you can do like what is the takeaways and where do
we see this field going? So generally I said, it's not going to stop, it's only
going to get higher, more and more, I think, being used by hackers in the
real world. And of course, I think we will see it, that we find more and
more kind of usage and targeting applications, pipelines and developers.
We see developers that are being more targeted than ever.

Omer Yaron - 44:32
Public package managers I think will be adding security controls and we
already see it, but I think it's going to grow and because it hurts basically
their own and their own kind of brand okay, their own legitimacy is very
well need to be that it is maintainable that it is safe to use a public
package. And I think we're also going to see more and more regulation for
supply chain risk management. I think we just at the start of it and the
more we understand that this field is complex, the more we're going to
understand that we need more and more risk management in this aspect
okay, and where we think this might be going. So here is some research we
did about IDE plugins. So again. Why? IDE. Plugins because first of all,
they're very common used by any developer.

Omer Yaron - 45:50
They're open source like this code is open source. They have open also
IntelliJ, but those are last of Ides but their reusage of extension is a
common thing. You probably cannot use any of those for specific language
without using some form of extensions. And then we wanted to see if we
can use all of the knowledge that we know about how our attackers use,
let's say NPM to kind of confuse developers. Can we do the same for Vs
code? So basically were able to kind of create an educational package. We
were able to use some repository that we have no relations to, very similar
to packet JSON confusion that was recently disclosed in NPM but over
starjacking types of attacks. So we could easily do that and make it
appear like our project is very being used. It's very lively.

Omer Yaron - 47:36
We were also able to add the verified publisher again on whichever eligible
domain you can think for yourself. So generally we say like okay, this is
where we're going to meet. This is one of an example of where you could
also expect those kinds of attacks to be happening in the future. Bringing
it a bit together. So I think that Upsec IR plan is really critical because it's
the biggest going attack surface. It's a huge return on investment and it
has very unique kind of characteristics like that when it happens, you
might not have proper resources available for you because it will happen
to a lot of people, to a lot of companies. And also it's a bit confusing.

Omer Yaron - 48:50
It's not our original realm where we just look at a deployed application or
in process of building an application and saying okay, what we need to fix,
it's something a bit different. And also there are always new tools to allow
organization better to handling this threat. But when it comes to incident
response, there are still a lot of gaps and you might want to create and
differentiate some of the different threats. So this is an example of what a
basic incident response plan can look like. I think you should kind of drill
and think of any uniqueness in your organization that would require
something and then go over it and see do I have CI logs in SBOM to even
start answering a question like is a specific malicious was built or not?

Omer Yaron - 50:03
Also the question of failing tests, for instance, in a dependency confusion.
Well, it's likely that a public package does not know the logic of the
internal package test will fail. And in that case a failing test is not an
indication for that everything is okay because it wasn't rent to completion
the bill. It's actually a way to indicate that something was wrong and bad
code was maybe ran and caused this entire application to fail a test. But in
the process it doesn't mean that you're safe so you need to take those into
account. So again, an example, identify the assets. Need to see if you are
lacking there in any way to identify assets that relates to some package,
what it does, what's its usage in the code. Maybe it's being built but run
without script so it's safe, maybe not.

Omer Yaron - 51:26
So all of that information, including, like, notify RND and so on, a lot of
the time we see that I've seen that the kind of security goes back and forth
with RND and asking RND questions that's not supposed to be. Like, the
security in those kind of situations probably knows a bit more of the
specific risk and it should create value and not run after RND. Okay. And
that's, I think basically it just know that it was based on two different
articles that I published. So if you want to read more and how and more
about the resource that we did. And I'm going to have two more minutes.
If anyone has any questions would be love to hear it. Okay. So if you still
might want to ask something, I'm available online on LinkedIn or
whatever. I'm sure you can reach him.

Omer Yaron - 52:53
So thank you everyone. The driver behind the sneak, so I will answer. So
what we did in Enzo and our unique kind of way of thinking was later
adopted by a lot of leading vendors. And we talked about ASPM
application security, posture management, meaning we don't care about
vulnerability management, but rather the context of what is relevant and
what is not relevant and what will bring the most security, which operation
would bring most security. And I think that's what Sneak kind of was
looking in their own product to enrich it. They do a lot of good assessment
of vulnerabilities, but they were lacking the bigger context and that's how
they're looking at it now. Like vulnerabilities is just one piece of the
puzzle. Other questions? Okay, so with that, thanks everyone and hope to
see you on other sessions. Bye.
