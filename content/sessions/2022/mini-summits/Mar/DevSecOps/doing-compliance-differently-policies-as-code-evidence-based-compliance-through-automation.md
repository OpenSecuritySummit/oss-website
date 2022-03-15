---
title        : "Doing Compliance Differently: Policies as Code, Evidence-based compliance through automation"
track        : DevSecOps
project      : DevSecOps
type         : working-session
topics       :
featured     :
event        : mini-summit
when_year    : 2022
when_month   : Mar
when_day     : Mon
when_time    : WS-20-21
hey_summit   : https://post-summit-sessions.heysummit.com/talks/doing-compliance-differently-policies-as-code-evidence-based-compliance-through-automation
banner       : https://pbs.twimg.com/media/FL0_tNtX0AMPO8p.png
session_slack:
#status      : 
description  :
organizers   :
    - Luis Servin       
youtube_link : kEp61G1jgO0
zoom_link    : https://us06web.zoom.us/j/82833290290?pwd=M3BXRGpIR2EzSG11cFBoOGx4QlJRQT09
---

## About this session
Compliance today has at least three different disjoint activities:
1. Creation of policies, and making them available within the company
2. Reading policies and choosing requirements
3. Demonstrating compliance to a governance body or an auditor

How the first item is done has an influence on how well the second and third can take place. If we move away from text editors, like MS word, and develop policies as code, including version control in git, there is a possibility to have a win-win situation for all stakeholders:
a) ISMS: policies are easy to maintain, changes can be audited, discussions about changes kept as issues or items in the change board (if using gitlab or github), proof reading and comments are easier to merge.
b) Policies can be treated as data, different versions can be created for different audiences: pdfs for the policy storage website, checklists for auditors, requirements for developers or implementers
c) Policy data can be fed to an "intelligent" system which can then integrate via an API to the ticketing engine, e.g. Jira, Azure DevOps Boards, or Service now, and create tickets
d) Tickets created can then be analyzed directly from the ticketing engine to see in real time how every team is doing, thus avoiding "surprises" close to a quality gate or release.
