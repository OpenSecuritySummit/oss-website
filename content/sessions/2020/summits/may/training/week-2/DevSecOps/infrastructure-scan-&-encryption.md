---
title        : Infrastructure scan & Encryption
type         : training-session
track        : DevSecOps
topics       : 
when_week    : two
when_day     : 11th - Thursday
when_time    : WS-2
hey_summit   : https://pre-summit-training-sessions.heysummit.com/talks/infrastructure-scan-encryption/
session_slack:
status       :            # draft, review-content, done
description  : TBD
youtube_link : X1VsceDfntc
organizers   : Barak Schoster
---


### Notable logs from the chat during the session 

14:35:52	 From evanjones : Q.) What about Pulumi in regards to being used a IaC?   \
14:47:25	 From Barak Schoster : https://github.com/bridgecrewio/terragoat    \
14:50:33	 From Corcoran Smith : Checkov is The Answer   \
14:51:04	 From Barak Schoster : https://github.com/bridgecrewio/checkov  \
14:51:10	 From Barak Schoster : brew tap bridgecrewio/checkov https://github.com/bridgecrewio/checkov  
brew update   \
brew install checkov  \
14:51:13	 From Corcoran Smith : Checkov even works on Windows :wink:  \
14:59:52	 From Corcoran Smith : Secrets in TF state are a massive headache, for sure. Sops, Hashi Vault both help here.
15:07:10	 From Didar Gelici : can you show how to exit vim?  \
15:07:12	 From Didar Gelici : lol   \
15:07:38	 From evanjones : Or :wq if you want to save   \
15:11:33	 From Didar Gelici : https://www.checkov.io/   \
15:11:34	 From Didar Gelici : https://www.checkov.io/documentation   \
15:12:06	 From Corcoran Smith : Custom rules and store them in a GitHub repo? :wink:  \
15:36:21	 From evanjones : Twitter handle?   \
15:36:31	 From Barak Schoster : @BarakSchoster 


### About this talk:
Planning, provisioning, and changing infrastructure are becoming vital to rapid cloud application development. Incorporating infrastructure-as-code into software development promotes transparency and immutability and helps prevent bad configurations upstream.

In this talk:

- We'll cover the current state of infrastructure security in the open source registries.

- From there we will continue to discuss best practices for writing, testing, and maintaining infrastructure at scale, keeping the infrastructure code secured using open source scanners. 

- We will cover infrastructure security use cases like encryption, public facing data entities and plain text secrets, And will show how to find those using policy as code.

### Session Contents

{{< pdf src="https://github.com/OpenSecuritySummit/oss2020/raw/master/content/outcomes/presentation/11%20Jun%20-%20Infrastructure%20encryption%20by%20Barak%20Schoster.pdf" >}}
