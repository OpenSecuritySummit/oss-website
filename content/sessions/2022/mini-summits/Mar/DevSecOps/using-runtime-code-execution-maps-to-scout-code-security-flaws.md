---
title        : Using runtime code execution maps to scout code security flaws
track        : DevSecOps
project      : DevSecOps
type         : working-session
topics       :
featured     :
event        : mini-summit
when_year    : 2022
when_month   : Mar
when_day     : Fri
when_time    : WS-15-16
hey_summit   : https://post-summit-sessions.heysummit.com/talks/using-runtime-code-execution-maps-to-scout-code-security-flaws/
banner       : https://pbs.twimg.com/media/FNW7URYWUAE_B2g.png
session_slack:
#status      : 
description  :
organizers   :
    - Elizabeth Lawler
    - Kevin Gilpin
youtube_link :  sJeCzDW1fXY
zoom_link    :  https://us06web.zoom.us/j/89642744228?pwd=bmtBdWdVQXJtS2M3YmV2alJFSjJxUT09
---

## About this session

Many reports, including the [SANS/CWE’s Top 25 Most Dangerous Software Errors](https://www.sans.org/top25-software-errors/), highlight the criticality of shifting secure coding practices as far left as possible. We also know from the shift-left movement that security issues can easily become technical debt when they aren’t squarely part of the feature delivery workflow. So how can we keep secure coding top of mind when it is often considered a “context switch” for developers working on features? In this talk, I’ll show how developers can use **runtime code analysis** to find security flaws as they code. Code analysis happens continually as developers work in their code editor, presenting security findings and interactive visual code maps in real time. For an additional layer of protection, code is analyzed again in CI. Examples of flaws that are detectable by runtime code analysis include: leaking customer data & secrets into log files; missing or improper authentication or authorization; unsafe data marshaling; unsafe handling of user-provided parameters. We will discuss how these specific examples of common flaws can creep into web apps, and I’ll show how runtime code analysis alerts developers to these problems while they are still in their flow and more likely to make prompt fixes. This talk will feature an open-source developer runtime analysis tool called AppMap that provides visualization and can be programmed to provide security analysis. Audience interaction and feedback is welcome!

