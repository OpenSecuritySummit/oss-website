---
title        : Purple Teaming with OWASP PurpleTeam
track        : DevSecOps
project      : Owasp
type         : working-session
topics       : 
featured     :
event        : mini-summit
when_year    : 2022
when_month   : Mar
when_day     : Wed
when_time    : WS-20-21
hey_summit   : https://post-summit-sessions.heysummit.com/talks/purple-teaming-with-owasp-purpleteam/
banner       : https://pbs.twimg.com/media/FMSxtqIX0AAHP36.png
session_slack:
#status      : 
description  :
organizers   :
    - Kim Carter      
youtube_link : MDDsAiO_ios
zoom_link    : https://us06web.zoom.us/j/85384368101?pwd=ZkNhUlpIVFFzRndkcnNNaFBJek85QT09
---
### Session slides

{{< gslides id="2PACX-1vSLoAjIN0ElP1--ImhYPJP5W96JMxthCFYqf1SND6ichtBxj42gJL1QE3f0U4OXrQ/embed?slide=id.p" >}}

## About this session

# What is OWASP PurpleTeam?

PurpleTeam is a Developer focussed security regression testing CLI and SaaS targeting Web applications and APIs.
The CLI is specifically targeted at sitting within your build pipelines but can also be run manually.
The SaaS that does the security testing of your applications and APIs can be deployed anywhere.

Kim will briefly discuss the four year journey that has brought PurpleTeam from a proof of concept (PoC) to a production ready Developer first security regression testing CLI and SaaS.

An overview of the NodeJS micro-services with many features allowing a Build User (DevSecOps practitioner) to customise their Test Runs without having to write any tests by simply configuring a Job file.
Allowing multiple options to deal with false/true positives.
Setting alert thresholds in multiple places and for multiple testers (app-tester, tls-tester, server-tester) allowing the Build User to define what constitutes a successful or failed Test Run.

# Why would I want it in my build pipelines?

In this section Kim will discus the problems that PurpleTeam solves, such as training the Build User with advice and tips on security defects as you fix the defects that PurpleTeam highlights.
As well as the huge cost savings of finding and fixing your application and infrastructure security defects early (as you're introducing them) as opposed to late (weeks or months later with external penetration testing) or not at all.

# OK, I want it, how do we/I set it up?

Kim will walk you through all of the components and how to get them set-up and configured

# Great, but what do the work flows look like and how do I use it?

Let's walk through the different ways PurpleTeam can be run and utilised, such as:

* Running purpleteam stand-alone (with UI)
* Running purpleteam from within your pipelines as a spawned sub process (headless: without UI)
* Running all of the PurpleTeam components, including debugging each and every one of them if and when the need arises

Publications: PurpleTeam came from a PoC Kim wrote about, built, ran workshops and spoke about in my first book: https://holisticinfosecforwebdevelopers.com/

Podcasts: Top three here: https://binarymist.io/publication/

