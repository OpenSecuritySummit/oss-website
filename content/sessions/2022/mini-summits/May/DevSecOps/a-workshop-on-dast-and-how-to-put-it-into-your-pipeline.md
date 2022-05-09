---
title        : A workshop on DAST and how to put it into your pipeline
track        : DevSecOps
project      : DevSecOps
type         : working-session
topics       : DAST
featured     :
event        : mini-summit
when_year    : 2022
when_month   : May
when_day     : Mon
when_time    : WS-16-17
hey_summit   : https://post-summit-sessions.heysummit.com/talks/a-workshop-on-dast-and-how-to-put-it-into-your-pipeline/
banner       : https://pbs.twimg.com/media/FQvY-8pXEAk0mND.png
session_slack:
#status      : 
description  :
organizers   :
    - Tanya Janca        
youtube_link :  https://youtu.be/NxSspDGZunk
zoom_link    :  https://us06web.zoom.us/j/82108372136?pwd=WllGL1ZScjIyTFh6TWd5SUhyK3VnZz09
---

## About this session
Adding DAST to CI/CD, Without Any Losing Friends

Everyone wants to put tests into the release pipeline, but no one wants to wait hours for them to finish. In this talk we will discuss multiple options for adding dynamic application security testing (DAST) to your CI/CD, in ways that won’t compromise speed or results, such as limiting scope, using HAR files, using test subsets, etc. Then we will do it! Learn to setup a CI/CD in GitHub using Actions, create a Bright Sec DAST account, and scan BrokenCrystals.com to find many, many vulnerabilities.  

Requirements: Users will need a laptop with wifi and admin access to install a repeater tool on their laptops in order to participate. They will also create a GitHub and Bright Sec account, which are both free. They can run the repeater using windows, npm or docker for the workshop. 


Outline:

-State problems

-insecure software is a serious, industry-wide issue

-Need for accuracy

-Need for speed

-Need to test from several angles, and we are zeroing in on Dynamic but will cover other options at a high level

-Need to keep a good relationship with devs, or our sec tools will be turned off/circumvented

-earlier we do security feedback, the cheaper and faster it is to fix

-Define DAST and explain how it works, including proxying. Briefly, this is hopefully review.

-Define CI/CD, how it works and its benefits. Again, this is hopefully a review.

-Strategies for DAST in a pipeline

-Run it on full blast, lose all of your (dev) friends - explain all reasons why this is a sub-optimal approach

-HAR files - pre-defined scope and eliminate need for crawling

-Sub sets of tests (for instance, search injection in all pipelines one week, then XSS the next, etc, eliminating as you go)

-Technology-specific tests only (if an App is Wordpress, only run word-press related tests, Mongo tests, noSQL tests, AWS tests,etc. 

-APIs and Swagger files - How to automate API DSAT scanning + tips

-Strategies for DAST NOT in a pipeline

-automated/scheduled scans

-Manual 1-off

-pentests

-When each makes sense, strategies and tips

-WORKSHOP STARTS

-Set up of GitHub account

-Clone GitHub Repo

-Setup BrightSec account

-Install Repeater

-Setup a scan using the CI/CD

-See the build break when the scanner finds a LOT of vulnerabilities

-Review vulnerabilities, discuss potential fixes

-Summarize/conclusion

-Q&A
	
