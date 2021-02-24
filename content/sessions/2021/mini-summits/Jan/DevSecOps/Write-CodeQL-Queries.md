---
title        : "How Variant Analysis and CodeQL helped secure the fight against COVID-19"
track        : DevSecOps
type         : working-session
topics       :
featured     :
event        : mini-summit
when_year    : 2021
when_month   : Jan
when_day     : Fri
when_time    : WS-3
hey_summit   : https://post-summit-sessions.heysummit.com/talks/write-codeql-queries/
session_slack:
#status       : draft
description  :
organizers   :
    - Alvaro Muñoz
youtube_link : 5beYejYfhjY
zoom_link    : https://zoom.us/j/99007108913?pwd=SDRHQUcybVNrQXVXb1VGeTMwT0o3Zz0
---

## About this session
In security, ‘variant analysis’ is the process of searching for variants of known vulnerabilities.

This used to be done with grep and painstaking manual code audits, but it can be automated with a
powerful semantic query language like CodeQL.

I will show how we performed a variant analysis using CodeQL which started analyzing a vulnerability
in Nexus Repository Manager and ended up finding many other critical vulnerabilities including a
Remote Code Execution (RCE) in Germany's Corona-Warn-App (German's Contact tracing app).

Finally, I’ll explain the factors that must come together to drive the adoption, scalability,
and success of such technology.
