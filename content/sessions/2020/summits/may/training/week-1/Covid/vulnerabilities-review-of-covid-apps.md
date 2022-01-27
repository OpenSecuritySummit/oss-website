---
title        : Vulnerabilities review of an Covid Application
track        : Covid
type         : user-session
topics       : Hacking & Defending
featured     : yes
when_week    : one
when_day     : 3rd - Wednesday
when_time    : WS-3
hey_summit   : https://pre-summit-training-sessions.heysummit.com/talks/covid-apps/
session_slack:
status       : done
description  : We will look at the vulnerabilities of one of the COVID tracing apps
youtube_link : mg1rnioktxk
organizers   :
         - Mike Minchinton
youtube_link : mg1rnioktxk           
---


### Notable logs from the chat during the session

https://twitter.com/matthewsgould             \
https://github.com/nhsx/COVID-19-app-Android-BETA     \
https://github.com/nhsx/COVID-19-app-iOS-BETA     \
https://github.com/nhsx/COVID-19-app-Documentation-BETA   \
https://hackerone.com/nhscovid19app    \
hackerone can give a little feel of what has been found already...  \
Also, we can get an idea of what is being looked for and what isn't.   \
https://labs.play-with-docker.com/?stack=https://raw.githubusercontent.com/MobSF/Mobile-Security-Framework-MobSF/master/scripts/stack/docker-compose.yml   \
sudo docker run -it --name mobsf2 -p 8000:8000  opensecurity/mobile-security-framework-mobsf:latest  \
adb shell am start -n uk.nhs.nhsx.colocate/uk.nhs.nhsx.sonar.android.app.debug.TesterActivity   

### This is section two of a three part exercise:
- **PART 1** - [covid apps analysis](https://pre-summit-training-sessions.heysummit.com/talks/covid-apps-analysis) 1st June 5pm UK
We will talk about the privacy and security concerns of three implementations of tracking apps.
- **PART 2** - THIS SESSION
We will look at the vulnerabilities of one of the COVID tracing apps
- **PART 3** - [covid apps threat modeling] {https://open-security-summit-2020.heysummit.com/talks/covid-apps-threat-modeling-user-session/) 18th June 8pm UK
We will do a threat modeling exercise on contact tracing apps

