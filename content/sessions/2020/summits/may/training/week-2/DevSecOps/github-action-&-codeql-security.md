---
title        : GitHub Actions & code scanning with CodeQL
type         : training-session
track        : DevSecOps
topics       : 
when_week    : two
when_day     : 9th - Tuesday
when_time    : WS-2
hey_summit   : https://pre-summit-training-sessions.heysummit.com/talks/github-actions-codeql-security/
session_slack:
status       :          # draft, review-content, done
description  : TBD
youtube_link : zgNFQY820Os
organizers   : Sasha Rosenbaum
youtube_link : zgNFQY820Os
---

### Notable logs from the chat during the session 

13:50:12	 From Sasha Rosenbaum : https://github.co/codeql-js-workshop   \
14:15:08	 From Didar Gelici : https://github.com/DivineOps/calculator   \
14:15:53	 From Sasha Rosenbaum : https://github.com/DivineOps/calculator   \
14:16:00	 From Sasha Rosenbaum : https://github.com/DivineOps/calculator-actions-demos   \
14:18:37	 From Didar Gelici : Node.js on the right   \
14:19:32	 From Name : I have question, I'm familier with cross-platform app development. What are the cases where to use it? What type of app you mean? (about the work flow thingy)   \
14:20:19	 From Björn Kimminich : Can you choose between X86 and ARM architectures in the matrix as well?   \
14:26:37	 From Name : It's like you working with containers, right?   \
14:26:43	 From Name : you are*   \
14:27:13	 From Name : when you configure .yml files?   \
14:30:45	 From Name : Does it support Linux From Scratch (building custom linux distro)?   \
14:42:17	 From Michele Chubirka : How do you integrate output into a binary repository?   \
14:42:20	 From Michele Chubirka : like ARtifactory?    \
14:42:32	 From Michele Chubirka : Or the docker container into a registry   \
14:42:55	 From Michele Chubirka : I guess the same   \
14:45:16	 From Name : Regarding Authentication, what if I'm using MFA?   \
14:47:00	 From Björn Kimminich : You can just use an access token. Works like an app password which is not using MFA.
14:48:23	 From Didar Gelici : https://lab.github.com   \
14:49:18	 From jaxley : Are actions available on GitHub enterprise?   \
14:57:34	 From Ashish : Is it possible to share a workflow between multiple projects?     \
14:58:47	 From Ashish : In a way that i do not have a duplicate workflow rather a common one that each project can use. something along the lines of Jenkins ‘shared pipeline library’   \
15:07:32	 From Michele Chubirka : Does CodeQL integrate the SAST partner tools?   \
15:07:55	 From Michele Chubirka : do you need CodeQL to integrate SAST testing into Github?   \
15:08:43	 From Michele Chubirka : Yes, it’s SEMMLE   \
15:09:00	 From Michele Chubirka : I’m familiar   \
15:09:14	 From Michele Chubirka : But trying to figure out if that’s required for the SAST integration   \
15:16:50	 From Yazid Boukerroui : Was the scan conducted on the code delta only, or was it the entire project that was scanned?
15:18:05	 From Yazid Boukerroui : Can I create my own queries with github.com beta, or is that only for future Github Enterprise?
15:20:30	 From Avi Douglen : hypothetically can I build my own support for another (or custom) language? how complicated would that be?   \
15:20:57	 From Yazid Boukerroui : What languages are on the current roadmap for CodeQL?   \
15:53:14	 From Avi Douglen : can CodeQL only be used on public repos?   \
16:00:20	 From Sasha Rosenbaum : Workshop repository (JavaScript, Java)   \
https://github.com/githubsatelliteworkshops/codeql   \
Workshop recording (JavaScript, Java)  \
https://githubsatellite.com/watch/workshops/   \
CodeQL CTF (current and past CTFs accessible)   \
https://securitylab.github.com/ctf   \
CodeQL free course   \
https://lab.github.com/githubtraining/codeql-u-boot-challenge-(cc++)   \
Contributing a query  \  
https://github.com/github/codeql/blob/master/CONTRIBUTING.md   \
16:01:59	 From Yazid Boukerroui : Are you guys using all the 1700 open source queries?   \
16:02:09	 From Yazid Boukerroui : For the public github   \
16:03:50	 From jaxley : Did OWASP SAST benchmark run to get CodeQL metrics?   
