---
title        : DevSecOps Maturity Model Updates
track        : DevSecOps
project      : DevSecOps
type         : working-session
topics       : 
featured     :
event        : mini-summit
when_year    : 2023
when_month   : Oct
when_day     : Fri
when_time    : WS-15-16
hey_summit   : https://us06web.zoom.us/meeting/register/tZMpdeyhpj0sH9z34Xu-JPwt1KGX9nR4poPD
banner       : https://media.licdn.com/dms/image/D4D22AQHit37Im1TJVA/feedshare-shrink_1280/0/1694787751472?e=1700092800&v=beta&t=EREICYht0859-bWjMuek-edFKVSZtTRsncK_4pkqiaE
#status      : 
description  :
organizers   :
    - Timo Pagel
    - Prakarsh Gupta
    
youtube_link : https://youtu.be/ZbNQ-A-bzw8
zoom_link    : https://us06web.zoom.us/meeting/register/tZMpdeyhpj0sH9z34Xu-JPwt1KGX9nR4poPD
session_slides:
---

{{< gslides id="2PACX-1vQW2T7KbVZcRtPF9pgqT5hSWeemVd8EgwLklmMGNwHp7ggfaWHq_jE7xntJAsuklA/embed?slide=id.p" >}}

## About the session
DevSecOps assessments are performed often only quarterly/yearly/by-yearly. If you want to provide fast feedback to your teams about their maturity, this is for you!

Agenda
- New Features from GSoC
- New Features (e.g. team assessments)
- Outlook of the _Metric Collector and Analyzer_

## Transcript:

Dinis Cruz - 00:05
Welcome to the open security summit session where we have Timo, a
longtime participant in Prakash, also participating here amazingly. And
they're going to be talking about DevSecOps maturity model. So over to
sorry, it is DevSecOps, right? Or is this yeah, it's DevSecOps with TT
model. Sorry, I flipped for a second. Off you go.

Timo Pagel - 00:33
Cool. Hey everyone. So I am Prakash Gupta, and I'll be walking you
through the DSOM updates. And we'll also talk about the new features as
well as the outlook of our DSOM. We have Prakash Gupta as well as team
of pages for this whole presentation. So before we begin, let me just give
you a brief introduction about myself. I have been working on DSOM for
the past three to four months as part of my Google Summer of code
contributions. Apart from this, I am also a software engineer at Expedia
Group. Well, about Timo pagel, I think you already know he's a well
known speaker at OSS. So we can move on. So let's talk about the agenda
which we have over for our DSOM presentation.

Timo Pagel - 01:20
We'll start with the new features from Google summer of code which is
going to be covered by Prakash which is me. And then we have new
features apart from Google summer of code as well as the outlook of our
DSOM which is going to be covered by demo. So let's start with our new
features from Google summer of code. So on the first list we have activity
tag filter. Now before explaining to you the slide, let me just give you a
brief demo about it. So this is our newly revamped DSO. And as you can
see here, we have a sub dimension filter which was previously present and
which used to have deletable chips before. So you can see we have
refreshed this chip set. We have now toggle switches which can be turned
on and off depending on the user choice.

Timo Pagel - 02:10
And we have now included a tag section under an activity. So as you can
see inside our matrix we have process as a tag for an activity. We have
artifacts, we have components. We also have none for different activities.
Now here you can see that we have now integrated an activity tag filter
which is dependent on these tags which we have now defined. So these
tags for example, if a user if I am the user and I just want to see the
activities which does not have artifacts, so I can just click on artifacts and
all the activities which does not have artifacts are going to be removed
and I can only see the activities which are turned on in the activity tag
filter. Now having all these chips can be a cumbersome approach.

Timo Pagel - 03:02
So we have also added a reset button so that user can directly see the
default view of the matrix. So this is about the activity tag filter. I'm sorry,
if anyone has any doubt, please feel free to interrupt me in between and
we can take that out right here. So instead of having deletable chips, we
have implemented our toggle switches. We have also added tags into our
activities and we have now created another activity tag filter which you
can see right here. We don't need to see the demo here. Move on. So this is
the second part of our GSA contributions. So overlay for activity view.
Now previously into our implementation levels we used to have all these
activities.

Timo Pagel - 03:58
We used to have all these activities and when a user wanted to know about
the activity and they used to click on it, a different page used to open up
right here which used to kind of break the user workflow. So instead of
that we have defined an I icon here. So when the user clicks on that I icon
they can see the details of the activity as part of an overlay. It's just right
there. It does not break the user workflow. It's already present in the top
you can see it's, the dimension of that activity. We have the subdimension
and then we have the activity name and we have all these parameters of
these activities. We have also included the tags. If the user want to know
which all tags fall under that activity, we have also done that.

Timo Pagel - 04:46
So these are all the activities which are here. This is the part of overlay. To
open the overlay we can click on the I icon which is going to be present
along all the activities. The right hand side. Cool. So this is about overlay.
Let's move on. Move on to the teams is. I think this is going to be the
major part of the Google summar of code contributions. We have included
two different concepts, team and team groups. So previously the whole
DSOM was created on a single user approach. Now we have included
teams and team groups into this. So into the menu bar when you can see a
teams title here, when we click over it we have a list of teams. So these are
all the teams which are present by default. The user can change it in the
YAML file here.

Timo Pagel - 05:46
So we have three teams right now default, B and C. So these are all the
team list. Now about the team groups can have multiple teams under
them. So it works like a department for them. So we have three team
groups here. We have group A, we have group B and we have group C. So
in the group A we have default and B. In the group B we have team B and
team C. And then in the group C we have team Default and team C. So
this is teams component. I'm going to show you what this actually makes
sense. Why I don't think that without even having to be able to utilize
teams it is going to make any sense. So this is the part team based
assessment. Now, when we go over to the implementation levels we have
multiple things.

Timo Pagel - 06:37
Here we have on the right hand side you can see Team Filter here, default
PNC. And for all the activities we can define which all teams have to
complete that particular task. So for example, if I open up in the level one
of build, we have this defined build across this activity. Now this particular
activity needs to be completed by all the teams A and teams A, B and C.
Now only Team C has completed it. So this particular cell has been
colored 33%, which is one by three. So for example, if a team B decides to
complete the particular task, they can click on it and the color is going to
depend on that. Now we have default B and C as a team filter. So for
example, I only want to see the progress of B and C.

Timo Pagel - 07:29
So this is the second part of our team based assessment. We have included
team filters into our implementation levels. So now if the user wants to see
the progress of only Team B and Team C, they can easily see that by
deselecting default. So now only team B and C, the progress of Team B
and C is visible here. If I deselect this, if I deselect A, B and C it is going to
get colorless and even if I select A it's not going to make any difference
because we are only viewing the progress of Team B and Team C. Now
this is the team filter. Now we also introduced team groups here in the
teams component. So what team group means is we can preselect
different teams here. So for example, we have default and B in the group
A.

Timo Pagel - 08:25
If I want to see the progress of B and C I can go for group B and similarly
for group C we have default and C. So now these groups can be
predefined by the user depending on what is the size of their department,
what all members are working on under them. So it makes it very easier
for the user to see the progress of particular departments rather than
seeing the progress as a whole of the company. In a team based
assessment you can see that for every activity we have multiple teams,
team A, B and C. We have all the checkboxes. The user can click on these
checkboxes to mark that this particular team has completed this
particular task. As I discussed, we have integrated team filter as well as
team Group Filter into this.

Timo Pagel - 09:14
So this marks the information about Team Pace assessment. If anyone has
any doubts under it, we can discuss it right here. Else we can move on to
the new features apart from GSOC. Timo, would you like to take the
stage?

Prakarsh Gupta - 09:40
Give me a second to do so. Maybe you can stop. I can take over. So now
you should see my screen and I go on. I will quickly present new features
which we have in addition to the features from Prakash. And afterwards
we will have an outlook. That outlook will be a bit longer because I will
tell you the architecture of Metrica and afterwards we will hear about
enhancing vulnerability management. Yeah. So actually Denise last year
requested that we have IDs for the activities in the DevSec optimal duty
model to be able to reference to these IDs. And that is now implemented.
What is missing is that it's part of the Ul. In the Ul, it's still the name of an
activity which you could implement but that will come one day. We have
also other model changes.

Prakarsh Gupta - 10:57
For example, a big break is that we move from four levels to five levels. We
have new either 2001 mappings and we have a fix of spelling errors. Now
I would like to move on to Metrica. So a problem which I often see is that
assessments are done from time to time. Maybe once in a year, maybe only
every two years. And as a product team I want fast feedback. So I get the
feedback. I haven't implemented something and when I implement it I
want to see the changes reflected in the maturity model. And that is so far
very hard to reach. And I saw that in a lot of organizations that I think
that will enhance security contributions. Because when the next audit is
next year, so that's far away until it's there and then there's not enough
time to fix something.

Prakarsh Gupta - 12:09
So I think it's very good. When you did something, you get the fast
feedback like you want to have in DevOps. I have two steps. One is to have
manual assessments which you can place in YAMLs. And then in addition
to automate the collection from different sources here we see an overview
of the architecture. You see on the bottom are YAML. So you have
activities where you can fill out. As a product owner I did this activity, or
as a team member I did this activity. For this application. For example, we
can for example have threat modelings performed. So we document in
YAML we have performed the threat modeling for that and that
application. And then Metrica can process that and show it in the Grafana
dashboard. And if you want, you can also send out alerts.

Prakarsh Gupta - 13:14
For example, if your threshold is two thread more links in a year, but
there's only one for a specific application, then you can send out an alert
with the Grafana tools. All I'm telling you right now is just the draft so
everything can be changed. We're in the design phase. So in case you
recognize something where you say that I would do different, please tell
me. So right now it's very easy to change everything. But we will actually
start next week to code. Right now is the time to give feedback. And the
alternative to YAMLs for threat modeling feels a bit like extra work
because what you do in threat modeling normally is to document it. You
document and confluence parts of the threat modeling. The diagram, for
example.

Prakarsh Gupta - 14:07
So there is the source which you can ask is the threat modeling performed
to a very specific team in case you do it in a structured way. For example,
you have a header where you say team members and you have a header
where you say for which application ID or deployment ID or whatever IDs
you use to identify your applications. And when you have it in a bit
structured format, you can ask Confluence or any other wiki. Is there, is
threat modeling documented already? And then the collector can pick it up
through the API in terms of Confluence and then you can check thresholds
again and put it in Grafana security dashboards. So that is the main idea
here. I don't see any questions. Let me see if I can open the chat so that
yeah, so no, so far no questions.

Prakarsh Gupta - 15:05
So I will now dig a bit deeper so you get a better understanding of it. So
this is how I envision what I also have seen already in different companies,
that you have an application YAML for example, and a teams YAML for
application specific activities. And then you have a team YAML in a folder,
in the teams folder in Git, and all activities from the team inherit to the
application. So an activity which is team based is, for example, a security
champion. Does this team has a security champion? And in case, yes, it
inherits to all applications of that team. So let us stick to the threat
modeling example. So the product owner right now changes the
application YAML adds threat modeling, adds a link to the threat
modeling in this case because it's currently not automated.

Prakarsh Gupta - 16:09
Then the product owner pushes the changes to a Git repository under the
control of the executive team of that organization, and then the product
owner creates a PL for this change. Afterwards the security architect can
review this and approves or denies, for example, the security architect
could perform a check if the link to that documentation is accessible for
the security architect, or he or she can review the threat modeling if it's
sufficient. And then you can show the changes on a security dashboard.
Now we dig a bit more in the architecture and in order to be able to zoom,
I use draw I over here directly. So in Git we use GitHub as our source
repository and our build platform. And in GitHub, let us start in the
middle.

Prakarsh Gupta - 17:23
Here we will build the needed components like a statistic generation
module, the collector and Grafana dashboard. I will tell you afterwards
why that is needed. And then in addition to GitHub.com, we have the
organizational space that is all this here in the middle, where the
organization might want to overwrite the default activities or the maturity
model definition, which activities are 1 second, I need to go back. It all
happens here in this right part, what I said so far, you define the activities
for your maturity model and on the left you see what activities has been
implemented by the teams for which application. Then you combine these
data and then you can check thresholds as an alternative to the YAMLs.
We can also use the collector. One example might be your security
vulnerability scanners which you might utilize.

Prakarsh Gupta - 18:24
And there, for example, you use contrast security checkmarks veracode,
the defect ojo, whatever you use from that we can grab the meantime to
resolve, for example. And then we can later show it in the dashboard here.
As I said, we think about here on the right to utilize Grafana. A problem
with grafana which I see is that we would need to create a Grafana
default dashboard which will not fit to the thresholds which you have
defined here beforehand. So we thought about how can we utilize that.
And so far the idea is to use templating. So we have here a grafana
dashboard application, which we use to create in the end grafana
dashboards out of the data we have defined here for the activities, and
then we can populate this dashboard to grafana.

Prakarsh Gupta - 19:41
In addition, when we have a data points, whenever something changes
might be the collector picks up daily the meantime to response from the
teams, or we have a change here in one of the activities, for example, I
performed the thread modeling, so there will be a new date for thread
modeling. Then we push through prometheus push gateway these metric
data, so we have a new time point in the time series database and then we
can utilize this data from Grafana. In addition, when we have the
definition of thresholds already here, we can also more easily export data
at this point in time. So we can, for example, use a transformation to be
able to show the activities which we have performed also in the DevSec
Optimity model per team.

Timo Pagel - 20:51
All right.

Prakarsh Gupta - 20:56
I go back. I have to add it's not a silver poop bullet, because still people
need to perform threat modelings, right? So people and processes is a
thing you really need to tackle. It just enables you to do it in a better way.
From my point of view, people still need to understand that they update
these YAML files, otherwise they will get alerts, for example. But maybe
they create a filter and route the alerts and spam box. So you need to have
work to cultural work to let people understand why they have to do it.
That is something you cannot outsource. But I think it's really helpful to
enhance your culture. Yeah, it's still a draft. It's done when it's done.
Currently we think it will be done by the end of this year.

Prakarsh Gupta - 21:57
Please contact us in Slack and the dsound Channel or contact us via
GitHub issues. Maybe I should show here that there is a Git repository for
it that you find here. That's also a change. Beforehand. The DevSecOps
Maturity model repository was under my name. Now you see, it's under
DevSecOps maturity, model, organization. And we have here Metrica. And
in Metrica currently, as you see, we only have documentation. We just have
documentations about the architecture. We have architecture decision
records here. So for the YAML we have defined here how these YAMLs are
structured. This is the one the teams fills out or the product owner fills out
for his applications. So we have here an API version, a Kind, and then
application settings. And then we start with the activities. And here's, for
example, conduction of threat rolling on technical level.

Prakarsh Gupta - 23:09
As I said, very important is that we have a date so we know when it
happens. Currently I haven't planned that we have quality criteria or
something. So you just have a title and then you might have links later. As
I said, it would be very good to automate this because in case you just
have a small structure how to document a threat model, you can grab that
information and then you have other activities here like data privacy
requirements. It's just a read confirmation or that there is Source Control
protection enabled. This is something currently we plan to have it first in
YAML files, but later obviously you can go to your version Control system
platform like GitHub, utilize the API and check the configuration of all
your repositories. So the teams don't have to do that manually in here.

Prakarsh Gupta - 24:06
But this kind of checklist is the start and then we enhance it to automate it
more and more. I should also mention the sponsors. So currently I am
building this with Access Switzerland. So they are the main driver of this.
They are also sponsoring development resources. But obviously we hope
that by making it open source that other people will join and contribute
different features. Go back to the diagram. For example. Everything I
marked blue here will likely not be sponsored by Access. So tools like
Defect Ojo for example, will likely not be sponsored by Access
Switzerland. So that is something where we could need help. Or also here
the team's communication currently is not planned or other exports.

Prakarsh Gupta - 25:08
Exports mean that when there is an alert, for example that you haven't
performed threat modeling within the last year, then you might want to
have it in your Vulnerability management system or in your incident
management system, depending what you're utilizing there and then you
have there in the finding. All right, let me go down a bit to the definition.
So this is what you document as a product owner. Now let us come to
what you document as a security architect for your maturity model. Here
is an example for production of simple threat modeling on technical level.
Then you can define components. For example that there should be an
array with a title inside with an object title which is string, a date as a
date and again an array for a title as a string and a URL as a URL.

Prakarsh Gupta - 26:09
Then you have the level so your desired level in your application security
maturity model and then the threshold. So the threshold here is a date.
There should be ten dates for the last 365 days. So that is very optimistic. I
would say ten thread warnings for one application but that is how you can
define it. You can also reduce the value here in case you think ten is too,
less or too much. Then we also want to populate that data to grafana. So
you can define the diagram type as a chart and you can add grafana
information mainly no, I think in case you have diagram chart here, you
don't need this information. This all comes from the top here. Oh, I didn't
push this. I changed it, but I didn't push. Yeah, okay.

Prakarsh Gupta - 27:12
I am currently not sure if it's the right way to do it so generic, so that you
can really combine everything you want. That makes it a bit more complex
in the development process, makes it very adjustable later for
organizations. That's why we defined it like this. But on the other hand,
sometimes it's better to just define in Java, threat modeling is like this and
don't let you define all this. But we said it's better to have this very
generic. Then we pick it up and you can define your own activities because
everyone will define these activities different. At least there will be
different names and you have different sessions, different attributes you
want to ask for.

Prakarsh Gupta - 27:58
So that's why we make it so generic and then out of this we can generate
a schema definition so that when a product owner will update the YAML,
it will directly tell you if that YAML is conformed to the schema. So far I
don't see questions in the chat so I will continue to talk. I think here we
mostly saw everything which is important. Now maybe this here is also
nice, the required level. So you saw in the definition of your maturity
activities you need to define a level and in that level you can define for
example, you want to have a pen test by yearly and a pen test yearly on
your level three. On level one you don't have a pen test because it's
internally. That's something I saw very often in different organizations.

Prakarsh Gupta - 29:06
And like that you can also because you have these pen tests two times, you
can define applications on level two should perform the pen test every two
years and on level three every year. So you have different thresholds for
these two different activities. Okay, yeah, we thought a lot about what
should be the dashboard. As I said, in the end we came up with Grafana
because we need something where we can show metric data and we
thought about creating our own dashboard using DSIM as a dashboard or
using Grafana. And Grafana is currently the best option, I would say. But
with the extension that here, we can also transform the data which we
have here and add it to our DevSec ops maturity model. All right, I think
that's all I can tell you right now.

Prakarsh Gupta - 30:30
In case you have any questions, please do not hesitate to ask. I'm also
open for calls in case you want to have an extra call. I think recurrently,
you are not allowed to talk, so you would need to write in case you want
to talk. Maybe we can enable you to talk. So just ask me here or ask me
later. Now we come to the last update, that is that we currently work on
the merge with the vulnerability management framework. Francesco
Meker is the author of this vulnerability management framework. We
performed so far a mapping. We defined what we need, so he said he
really needs five dimensions. So that was five levels. That was a kickoff
that I moved from four to five dimensions. I wanted to do this since long,
but now it's implemented.

Prakarsh Gupta - 31:28
Also we said we need different tags, so that's why. Also we implemented
the tax feature currently based on all activities, the non tag in the
production version. But we will change that soon. All right, so this is the
end of this talk. Do you have any questions? One addition maybe. Denise
in the start asked me about how can we make it more accessible that
people can ask I have this problem and see the answer, for example, from
the DevSecOps maturity model without the need to go through all the
different activities. I'm working here together with Spiros, with the Open
CRE project, which from my understanding means they will grab the data
from the YAML or from the application, and then they have an AI where
you can ask questions and it will point you to the different Ovas projects.

Prakarsh Gupta - 33:02
And one project I think in the future will be the DevSecOps maturity
model. Oh, we have a question here. First question. These are model
changes from four to five levels and some other additions. Do you expect
changes to the model from time to time? So these hard changes I don't
expect often from four to five levels, that will not happen. I assume
currently that won't happen in the next two years. That was just because
we had too many activities. In case we now get an activity boom and we
get, let's say, 50 new activities, we will have to think about more levels.
But I don't see that currently that we will get a lot more activities, that we
need more levels.

Prakarsh Gupta - 33:44
You need more levels when you have too many activities in one let me open
it so I can show it in one subdimension and level so you can see it better
when I show it. So when you have let me find something. Where we have a
lot here, for example. So infrastructure hardening we have here a lot of
activities so the maturity model is there to guide you what you have to do
as a next step. But here this field is already like a bit too much. Here this is
only here so much because I have to not only relate all the activities in this
subdimension, I also have to take a look. What? Do you do in all the other
subdimensions? And then I have to place it according to that and not
according only to this subdimension.

Prakarsh Gupta - 34:37
It's why you have so many activities here. And now you have to choose
again, right? What do I do first of all of this? Why? The objective of the
model is to give you a guideline that's why we now have five but you see
still this one here has a bit too much but all the others are looking fine,
right? So there it's acceptable only this has the match so I don't expect so
big changes in the future do you have more questions? Okay, I stopped the
recording hi at least I hope I can do that the recording now is not stopped
do you want to copy to cloud recording? If yes, you will see an email
notification when the cloud recording is ready.
