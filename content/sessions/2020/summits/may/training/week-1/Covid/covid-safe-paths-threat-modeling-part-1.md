---
title        : Covid Safe Paths - Threat Modeling Part 1
type         : training-session
track        : Covid
topics       :
    - Covid Safe Paths
featured     : yes
when_week    : one
when_day     : 4th - Thursday
when_time    : WS-1
hey_summit   : https://pre-summit-training-sessions.heysummit.com/talks/threat-modeling-on-covid-apps/
session_slack:
status       : done           # draft, review-content, done
youtube_link : IKHZXQfDHrA
organizers   : 
    - Dinis Cruz
    - Mark Carney
    - Jay Harris
    - Adam Leon Smith
description  : 
---


### Notable logs from the chat during the session

Our central infra asset that governs approved HA's  \
The publishing of points of concern               \
The upload of data to the HA                    \
The mobile app that holds raw data 


### Covid Safe Paths

"COVID Safe Paths is a mobile app for digital contract tracing (DCT) sponsored by Path Check a nonprofit and developed by a growing global community of engineers, designers, and contributors. Safe Paths is based on research originally conducted at the MIT Media Lab."

### Threat Modeling (Part 1)

During this session we will be doing a live Threat Modeling review of the application and collaborate with key "Covid Safe Paths" contributors in helping to improve the security of this opne source innitiative

The new coronavirus pandemic has upended our lives drastically. Borders have been closed, airports, hotels and other businesses got shut, the cultural life has been suspended, schools and other educational institutions have been completely switched to remote mode. These unprecedented measures not only depress people from the phycological point of view, but they also disrupt many economies, resulting in mass job losses and raising the probability of widespread hunger.
We all want to get out of the house, to reopen the economy and to feel secure again. COVID Safe Paths is a mobile app for digital contact tracing (DCT) sponsored by nonprofit organisation Path Check and developed by a growing global community of engineers, designers, and contributors. The app is based on research originally conducted at the MIT Media Lab. It builds tools that help communities flatten the curve of COVID-19 together.
During this session we will be doing a live Threat Modeling review of the application and collaborate with key “Covid Safe Paths” contributors in helping to improve the security of this open source initiative.

### Resources

 - Main site: https://covidsafepaths.org/
 - Main GitHub org: https://github.com/Path-Check
 - Save Paths page: https://github.com/Path-Check/covid-safe-paths
 - Frontend: https://github.com/Path-Check/safeplaces-frontend
 - Backend: https://github.com/Path-Check/safeplaces-backend
 - Security and Privacy page: https://github.com/Path-Check/privacy-security 
 - [v2_upload_flow_-_safe_places_-_confluence.pdf](https://os-summit.slack.com/files/U014V5N4RLL/F014PAGSZ6X/v2_upload_flow_-_safe_places_-_confluence.pdf)

### Support documents

Document from https://github.com/OpenSecuritySummit/covid-safe-paths-security/tree/master/docs

#### Privacy for Location Data in Safe Paths

{{<pdf src="https://raw.githubusercontent.com/OpenSecuritySummit/covid-safe-paths-security/master/docs/TEST-PrivacyforLocationDatainSafePaths-030620-1535.pdf">}}


#### Safe Places Product Definition

{{<pdf src="https://github.com/OpenSecuritySummit/covid-safe-paths-security/raw/master/docs/PROD-SafePlacesProductDefinition-030620-0756.pdf" >}}

#### User types, needs, and problems in the Path Check ecosystem

{{<pdf src="https://github.com/OpenSecuritySummit/covid-safe-paths-security/raw/master/docs/PROD-Usertypes%2Cneeds%2CandproblemsinthePathCheckecosystem-030620-0757.pdf" >}}

#### SafePlaces API Architecture

{{<pdf src="https://github.com/OpenSecuritySummit/covid-safe-paths-security/raw/master/docs/SA-SafePlacesAPIArchitecture-030620-0758.pdf" >}}

#### v2 Upload Flow

{{<pdf src="https://github.com/OpenSecuritySummit/covid-safe-paths-security/raw/master/docs/v2%20Upload%20Flow%20-%20Safe%20Places%20-%20Confluence.pdf" >}}

#### Private GP trail intersection

{{<pdf src="https://github.com/PrivateKit/PrivacyDocuments/raw/master/GpsEncryption.pdf" >}}
