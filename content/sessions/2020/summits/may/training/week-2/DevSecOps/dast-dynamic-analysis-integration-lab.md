---
title        : DAST - Dynamic Analysis integration lab
type         : training-session
track        : DevSecOps
topics       : 
when_week    : two
when_day     : 10th - Wednesday
when_time    : WS-1
hey_summit   : https://pre-summit-training-sessions.heysummit.com/talks/dast-dynamic-analysis-integration-lab/
session_slack:
status       :         # draft, review-content, done
description  : TBD
youtube_link : mdUP1XtYTLI
organizers   : Mohammed A. Imran
youtube_link : mdUP1XtYTLI
---


### Notable logs from the chat during the session 

11:40:59	 From Sam Stepanyan : OWASP DefectDojo - open source vulnerability management tool:  https://owasp.org/www-project-defectdojo/     \
11:43:38	 From Didar Gelici : OWASP projects and content are the best friends of any devsecops person. We love you OWASP!
11:45:39	 From Shivani : what are the open source tool for DAST which companies are using?   \
11:47:22	 From Sam Stepanyan :  - OWASP ZAP is a free DAST tool from OWASP (it is like Burp Suite, but free) : https://owasp.org/www-project-zap/   \
11:48:00	 From shubham.m : Does Github also having CI/CD capabilities? Or we can achieve CICD by using Jenkins?
11:48:53	 From Raghav Rao : Github has    \
11:48:54	 From Muhammad Yuga : for GitHub it calls GitHub Actions      \
11:54:55	 From Taj : when I'm doing sast and dast in DevSecOps. am I expected to know the programing language on which the project is build? for example one project is on java other on python other on  dotnet. so am I expected to know them to do saat and dast as part of devsecops?   \
12:44:35	 From Taj : devsecops pipeline in test shouldn't be similar to production right?? then can you give a example of what should be enabled in production devsecops pipeline.?   \
12:44:57	 From Taj : and what should be disabled??   \
12:46:20	 From Rostom Zouaghi : There are some compliance requirements where it is mandatory to test production systems but there are limitations to those tests of course, given they can affect the prod env.   \
12:46:30	 From Taj : yes that answers it.   \
12:49:08	 From Taj : In test environment. while I'm implementing dast in devsecops . then how can I configure when the build should fail, can you give an example..   \
12:50:16	 From N/A : Is sslyze a good fit for a pipeline? I mean it is a tool that should be run from time to time. In my opinion not every time a pipeline runs since the server ssl configs are not constantly changing. What are your thoughts on that?  \
12:53:17	 From Raghav Rao : Do we run DAST scans for mobile apps in ci/cd pipeline as well?   \
12:53:18	 From N/A : Do you know any tool we can collect and see all pipeline results in a dashboard for example?  \
12:54:10	 From Raghav Rao : ArcherySec or Threadfix will help you do vulnerability management.  \
12:56:16	 From Didar Gelici : In test environment. while I'm implementing dast in devsecops . then how can I configure when the build should fail, can you give an example..   \
12:57:04	 From Sam Stepanyan : OWASP DefectDojo is another popular free dashboard tool for vulnerability management. You can import scan results from many calls , display on one dashboard, obtain metrics and manage each finding
12:57:17	 From Shivani : Do we run Desktop application DAST testing?   \
13:05:25	 From Taj : while implementing dast in DevSecOps , what the strategy to eliminate false positives. because human intervention is needed to get false Positives. But if everytime human intervention is there don't you think it doesn't do proper justice to dev ops.??   \
13:07:33	 From Sam Stepanyan : Re: Desktop apps - SAST tools which analyse the source code of application can provide better value from security point of view. There are commercial DAST tools which will analyse the EXE & DLL files. On the Open-Source scale the primary DAST tools are fuzzers. This is how many vulnerabilities in desktop apps like Acrobat Reader etc are discovered
13:09:06	 From Imran Mohammed : Awesome fuzzing
