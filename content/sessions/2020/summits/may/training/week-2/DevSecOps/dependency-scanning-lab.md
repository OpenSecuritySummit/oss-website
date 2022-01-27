---
title        : Dependency scanning lab
type         : training-session
track        : DevSecOps
topics       : 
when_week    : two
when_day     : 11th - Thursday
when_time    : WS-1
hey_summit   : https://pre-summit-training-sessions.heysummit.com/talks/dependency-scanning-lab/
session_slack:
status       :            # draft, review-content, done
description  : TBD
youtube_link : j184Av-LJvI
organizers   : Mohammed A. Imran
youtube_link : j184Av-LJvI
---


### Notable logs from the chat during the session 

11:45:20	 From John : do all tools also check for dependencies that have been directly checked in - ie not in a package manifest (a problem with large old codebases)   \
12:00:50	 From Imran Mohammed : https://portal.practical-devsecops.training/courses/sca-using-safety \
12:01:41	 From N/A : Imran, one problem I have is Time. If I put all this tools on the pipeline I would have a developers rebelion on the company xD  \
We spent alot of time reducing the time a pipeline runs, how can we add security tools to the pipeline without increasing pipeline running times  \
12:05:20	 From Jing : Hi Imran, which OAST tool can we use for .net and C++?  \
12:06:58	 From Raghav Rao : Flawfinder can be used for C++  \
12:07:57	 From Raghav Rao : https://security-code-scan.github.io/ —> .Net  \
12:11:06	 From Didar Gelici : OWASP DevSlop project : https://owasp.org/www-project-devslop/  \
12:11:36	 From Didar Gelici : Their meet-up page: https://www.meetup.com/OWASP-DevSlop-Project/  \
12:12:10	 From Didar Gelici : and their youtube: https://www.youtube.com/c/OWASP_DevSlop   \
12:13:20	 From Franziska : And: https://devslop.co/   \
12:19:39	 From Manav : hey Imran, I didn't provide any input file for retire, how does it know what's the input file  \
12:23:44	 From Manav : I remember when I integrated dependency it downloaded NVD db  \
12:24:20	 From Manav : does retire does kind of same? or does it check in the fly making outbound internet connections?  \
12:27:11	 From N/A : Imran, I saw you are running tools like, nmap and nikto before deploying.  \
You are running those tools against a staging/dev server? Before deploying?  \
12:28:41	 From N/A : So, some tools like retirejs are run before a deploy and nmap/nikto are run after deploying?  \
12:28:58	 From Manav : when we run SAST.. with tools like checkmarks or Fortify.. I guess the library files aren't included right?
12:29:27	 From Didar Gelici : https://www.youtube.com/playlist?list=PLxLweN1tBkoS4y73tJwWupuVsfgTQo-oV  \
12:29:36	 From Imran Mohammed : https://portal.practical-devsecops.training/courses/sca-using-retirejs   \
12:51:13	 From Imran Mohammed : https://pastebin.com/tN5Vtv7G  \
12:53:15	 From N/A : Imran, where should we install the tools (retirees, niko, etc) in the machine that runs the runner?  \
12:58:11	 From Manav : we should ask for root account.. never problem with permission ;)  


### About this talk

Lab attendance is first come first served for 30 people due to platform restrictions. 
Later participants can still join and watch as a demo.
