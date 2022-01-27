---
title        : MultiJuicer Introduction
type         : training-session
track        : OWASP Juice Shop
topics       : OWASP
when_week    : one
when_day     : 2nd - Tuesday
when_time    : BK-3
hey_summit   : https://pre-summit-training-sessions.heysummit.com/talks/multijuicer-introduction/
session_slack:
status       : done          # draft, review-content, done
description  :
organizers   : 
        - Jannik Hollenbach
        - Robert Seedorff 
zoom_host    : Dinis Cruz
youtube_link : 6NMjZbfnTOU
---

### About this talk

OWASP Juice Shop is an incredible tool to learn and teach about web
application security. The Juice Shop lets people attack a real(ish) web
application - which looks like a normal eCommerce Shop - and learn step
by step about some of the most impactful vulnerabilities.

When you are running a Security Training for developers based on the
Juice Shop you have one problem: How can every developer run and access
his own Juice Shop Instance to train his skills? The Juice Shop is
basically a single user application, so every user needs to have their
own instance to train.

You basically have to options:

1. You could make the users install Juice Shop on their own machines,
   which is error prone and can easily take a big valuable chunk of your
   valuable training time.
2. Or you could host all Juice Shop instances for the users.

This is where MultiJuicer comes in, an open-source Tool to centrally
host and all Juice Shop Instances for your training on a central
kubernetes cluster.

What MultiJuicer does:

* dynamically create new Juice Shop instances when needed
* runs on a single domain, comes with a LoadBalancer sending the traffic
  to the participants Juice Shop instance
* backup and auto apply challenge progress in case of Juice Shop
  container restarts
* cleanup old & unused instances automatically

In this session you will learn:

* What MultiJuicer is
* How it works
* How you can use it for security trainings either in your org, or for
  your customers
* How you track the progress of the hackers

Audience:

* Security Educators
* Security Consultants
* Juice Shop Enthusiasts


### Session Contents

{{< pdf src="https://github.com/OpenSecuritySummit/oss2020/raw/master/content/outcomes/presentation/2%20Jun_MultiJuicer%20Intro%20by%20Jannik%20Hollenbach%20and%20Robert%20Seedorff.pdf" >}}
