---
title        : Threat Modeling Manifesto
track        : Threat Modeling
type         : working-session
topics       :
featured     :
event        : mini-summit
when_month   : Dec
when_day     : Wed
when_time    : WS-6
hey_summit   : https://post-summit-sessions.heysummit.com/talks/threat-modeling-manifesto/
session_slack:
#status       : 
description  :
organizers   :
    - Avi Douglen
    - Jonathan Marcil
    - Chris Romeo
    - Izar Tarandach
    - Kim Wuyts
    - Brook S.E. Schoenfield
    - Matthew Coles
youtube_link : CZxPZ-G3Gys
zoom_link    : https://zoom.us/j/91470027729?pwd=NXFxTW0yMW1Banh3bDBteGxyZXc1UT09
---

https://www.threatmodelingmanifesto.org/

15 OWASP authors have come up with the Manifesto, excited to have a number of them joining us in this session.
We will start with an overview of what the manifesto is and continue discussing how can this be used by security people and devs together.
What are you most interested about it? Come and share you opinion and questions. All are welcome!
{{< img src="https://pbs.twimg.com/media/Eov1SKgWMAEp7hI?format=jpg&name=4096x4096" >}}


## chat output from the session:

18:35:25	 From Brook Schoenfield : Don’t pay attention to that: Avi contributed quite a lot to the manifesto, as did everyone <br>
18:36:47	 From Avi D : :-) <br>
18:39:22	 From Brook Schoenfield : Also, because threat modelling includes “art” grounded in experience, approaches tend to be aesthetic and stylistic <br>
18:40:05	 From Avi D : 100% Brook. “Artisanal science” ;-)<br>
18:40:39	 From David Greer : I wholly agree Brook. I've had co-workers make threat models that were fully different from what I would have done that were perfectly correct. <br>
18:41:58	 From Jonathan : https://www.threatmodelingmanifesto.org/ <br>
18:47:26	 From Brook Schoenfield : For me, it was Izar and Matthew Coles who coalesced this now <br>
18:48:20	 From Brook Schoenfield : OTH, I thought that practitioners needed to get together not  as presenters, but as contributors since about 2011. There have been a few other attempts along the way <br>
18:53:31	 From Charles Weir : I had a slightly different question: who do each of the experts here see as the clients for their TM? Who’s the customer? <br>
18:57:42	 From Adam "surprise guest" Shostack : Charles, I prefer to ask “who are the participants” rather than clients <br>
18:58:23	 From Avi D : +100 Brook - and not just about security aspects either <br>
18:58:53	 From Adam "surprise guest" Shostack : And there, the participants are the people who are making decisions about the system <br>
19:01:26	 From Charles Weir : Adam, So the purpose is the learning, not a receiver of the ‘output’? <br>
19:02:18	 From Brook Schoenfield : these are both important, IMHO <br>
19:03:21	 From Brook Schoenfield : Learning: because most organizations are developing their skills and IMHO, all activity taken up during development must offer observable (and hopefully measurable) value <br>
19:03:23	 From Adam "surprise guest" Shostack : Learning is a great value, not the only one. sometimes the output is important, sometimes the journey is important. <br>
19:04:24	 From Izar Tarandach : Charles, I'd offer that learning is a great value and a by-product of the process. As Adam points out, the journey is important. Eventually we find out that more comes out  of the threat mpodel than just a list of threats and mitigations. <br>
19:06:50	 From Charles Weir : I was wondering too about the ‘what could go wrong?’ question. Does(n’t) TM put a restriction on the kind of what’s we’re looking for? <br>
19:08:16	 From Avi D : Charles, not necessarily, it depends on the model you want to use, and on your scope. <br>
19:08:20	 From Izar Tarandach : what kind of restriction do you have in mind? <br>
19:08:42	 From Avi D : There can be restrictions, but its not inherent to the doing of threat modeling.<br>
19:09:01	 From Adam "surprise guest" Shostack : TM™ doesn’t have an Official Answer to that. You can use STRIDE, LINDDUN, Kill Chain and be really specific or you can go beyond.<br>
19:09:23	 From Didar Gelici : shall we discuss this in the second half, live?   Otherwise the audience won’t have visibility on video<br>
19:09:44	 From Charles Weir : Avi, distinguishing TM and normal test design, I was thinking.<br>
19:09:56	 From Adam "surprise guest" Shostack : Sure! Can we also capture the chat and post it as an accessory?<br>
19:10:07	 From Didar Gelici : can do <br>
19:10:21	 From André Ferreira : I’m still a fan of “multi-dimensions model” after a brainstorm session based on STRIDE, wondering that the panel thinks of it <br>
19:11:45	 From Adam "surprise guest" Shostack : I wonder if some folks are intimidated by the idea of ‘multi-dimensional models’?<br>
19:12:11	 From Brook Schoenfield : In my experience, answer to Adam: unqualified “yes”<br>
19:12:53	 From Didar Gelici : good analogies !<br>
19:13:03	 From Jonathan : If you just joined us, manifesto is on https://www.threatmodelingmanifesto.org/ <br>
19:14:39	 From André Ferreira : It was a paper by Jouini, Rabai and Aissa, 2014 which claimed to offer a richer taxonomy than STRIDE following principles of mutual exclusivity, exhaustiveness, repeatability, acceptability and usefulness. I believed that it would benefit from further sub-classficaitions, but noted that is very similar to PASTA. <br>
19:15:42	 From Charles Weir : Cardboard consultant?<br>
19:16:30	 From Adam "surprise guest" Shostack : “A Security Framework for Secure Cloud Computing Environments”?<br>
19:17:37	 From Adam "surprise guest" Shostack : Based entirely on the abstract, I think that models which try to integrate cost are harder to adopt than ones that don’t.<br>
19:18:21	 From Avi D : … unless cost as a factor is optional?<br>
19:18:22	 From Dinis Cruz : Question: Although onsite threat modelling session have lots of advantages, remote sessions (aka zoom ) have the advantage of allowing much more (key) talent to participante. What best practices can you share on how to run those virtual sessions (maybe backed with a couple participants in a meeting room)? <br>
19:18:55	 From André Ferreira : On what can go wrong?<br>
19:19:58	 From André Ferreira : On what can go wrong? What would be looking there? Would you sub divide it in to: entry/exit points, external dependencies? Would there be a common set for guidance? <br>
19:20:26	 From Adam "surprise guest" Shostack : Dinis, 99% of the answer is how do you run effective remote collaboration, and 1% is threat model specific.<br>
19:21:16	 From Adam "surprise guest" Shostack : André, entry/exit is one way of looking at ‘what are we working on’, and dependencies are also part of that.<br>
19:21:29	 From Jakub Kaluzny : Remote collaboration that does not store sensitive data (threats) in the 3rd party cloud app :)<br>
19:21:55	 From Robert Hurlbut : +Adam’s answer<br>
19:22:48	 From Izar Tarandach : Andre, on "what can go wrong", I like to think about it in two parts - "what are the possible modes of failure",  meaning, how would I know the system is misbehaving, and then, what can lead to those modes. <br>
19:22:49	 From Dinis Cruz : Ok Adam, do you have good tips on to run effective remove collaboration?  :)<br>
19:23:01	 From Adam "surprise guest" Shostack : Also, to the 1% remote TM specific, Agile Stationery has a card-dealing tool https://croupier.agilestationery.co.uk/ <br>
19:23:05	 From Tate Crumbley : What are folks thoughts on threat modeling features as compared to systems?<br>
19:23:32	 From Didar Gelici : the croupier still requires each player to have deck of physical cards<br>
19:23:32	 From Adam "surprise guest" Shostack : Dinis, lots of retrospectives :)<br>
19:23:37	 From Brook Schoenfield : Hey, Chris, Robert joined!<br>
19:23:50	 From André Ferreira : Thanks Adam, on that point, guidance for common points on “what are we working on”. I was wondering if you guys considered further subdividing the 4 points as to offer more guidance. <br>
19:24:54	 From Jakub Kaluzny : Actually finding an offline whiteboard/diagraming that is currently maintained is not that easy. All Miro/Creatly/Mural etc. synch with the cloud.<br>
19:25:05	 From Dinis Cruz : Question: what can we do at the next onsite summit to make it work for onsite and remote participants?<br>
19:25:41	 From Brook Schoenfield : Wise words, Adam!<br>
19:25:49	 From Didar Gelici : cheeky @Dinis<br>
19:28:27	 From Adam "surprise guest" Shostack : André, we chose not to for the manifesto, but tools like STRIDE, LINDDUN help answer ‘what can go wrong.’ My (very quick) take on that paper is that they’re thinking they need a ‘complete’ methodology, and that fits the ‘perfect representation’ anti-pattern.<br>
19:29:08	 From André Ferreira : To tackle the limitations in know-how from the modellers (memory included), what are in your opinion the best resources? I recall having a very hard time trying to figure out vulnerabilties DBs while learning TM <br>
19:29:46	 From André Ferreira : Adam, thank you for that<br>
19:31:13	 From André Ferreira : Makes a lot sense. Make iterative and deep dive only where needed, I guess<br>
19:33:36	 From Jakub Kaluzny : Fully agree - TM as a metric for pentest (and vice-versa).<br>
19:34:38	 From Grant Ongers (rewtd) : 100% Brook. Security is a part of software quality... one of many NFRs.<br>
19:35:41	 From Brook Schoenfield : Apologies for going on.<br>
19:36:03	 From Grant Ongers (rewtd) : Threat Modelling is how we scope our (security) tests... Especially if we do TDD in building software.<br>
19:37:14	 From Jakub Kaluzny : Without TM, a pentest would be more bounty hunting :)<br>
19:37:32	 From Avi D : Jakub, or running scanners ;-)<br>
19:38:49	 From Izar Tarandach : it is important, i think, to call out that testers usually test "to spec", while security tests (should) focus on "to break". These are very different mindsets, and the TM helps bridge between them.<br>
19:39:01	 From Grant Ongers (rewtd) : Heh... Avi, that's what they mostly look like.<br>
19:39:54	 From Tate Crumbley : Thanks!<br>
19:40:07	 From Grant Ongers (rewtd) : But that the security equivilent of fuzz testing for functional tests...<br>
19:40:37	 From Adam "surprise guest" Shostack : Threat modeling swag store: https://agilestationery.co.uk/pages/threat-modeling-tools<br>
19:40:40	 From Jonathan : Tendency to Overfocus<br>
https://www.threatmodelingmanifesto.org/#principles<br>
19:41:02	 From Charles Weir : I wonder if the question might be ‘What might go wrong related to security and privacy?’<br>
19:41:23	 From Grant Ongers (rewtd) : Adam: yup. Needs more t-shirts / hoodies. will you tell Devika?<br>
19:42:05	 From Avi D : @Izar that’s what ASVS is for :-)<br>
19:42:17	 From Izar Tarandach : +1 on ASVS<br>
19:42:38	 From Jakub Kaluzny : TM-ing a full system or each story has a cost (mostly time), and it's pretty easy to overcomplicate. I often advise to decide first which stories are worth to model.<br>
19:42:48	 From Avi D : That is pretty much “pentesting to spec” :-)<br>
19:44:21	 From Izar Tarandach : @Jakub with the realization that at first we might not know what stories are out there. They emerge as the system progresses. That's why I push CTM with a decision by the developer of "is there security value in this particular story" <br>
19:44:36	 From Jakub Kaluzny : "Thumbs up"<br>
19:45:14	 From Avi D : +1 Izar<br>
19:46:16	 From Charles Weir : @Jonathan - how do you approach the ‘TM without the expert?’ problem?<br>
19:46:43	 From Brook Schoenfield : if a threat model identifies 1200, then you’re being paid for vulnerabilities by the pound!<br>
19:46:52	 From Grant Ongers (rewtd) : Expert in what @Charles? THe system? What can go wrong?<br>
19:46:56	 From Tate Crumbley : Looking at a feature without the context of the overall system threat model sometimes leaves us wanting, looking at it bottom up. I do like looking at it top down. Getting a model that devs can reference (ala Brooke) is a holy grail for me.<br>
19:46:59	 From Brook Schoenfield : Out of 1200, your customer will do absolutely nothing<br>
19:47:17	 From Grant Ongers (rewtd) : /registers domain...<br>
19:47:35	 From Jakub Kaluzny : That's what base threat models are for. You have 30mins budget? Draw a diagram, mark "web apps" "mobile apps" , "AWS " etc. and use BTMs, best practices, ASVS, etc.<br>
19:47:35	 From Jonathan : rofl :)<br>
19:47:42	 From Brook Schoenfield : @Avi: I do that all the time. But do they buy? ahem<br>
19:49:46	 From Avi D : Heh. Make the “not buy” more expensive ;-)<br>
19:50:04	 From Avi D : (Not that I am such a sales expert lol )<br>
19:50:17	 From Didar Gelici : OWASP Slack?<br>
19:50:22	 From Dinis Cruz : Question: What are good topics for next month’s OpenSecuritySummit (2nd week in January)<br>
19:51:15	 From Avi D : Didar a lot of folks are there, so can catch us there but not really an “official” channel<br>
19:51:22	 From Grant Ongers (rewtd) : @Dinis: "How to make sherpas of your developers for the TM journey"<br>
19:51:25	 From André Ferreira : It would be great to see “Threats categorization”, pitfalls, different ways of applying it in practise<br>
19:51:39	 From Didar Gelici : you can create a twitter account for the Manifesto<br>
19:51:40	 From Jonathan : https://www.threatmodelingmanifesto.org/#principles
use this to challenge yourself and people (it will get you in trouble but it's going to help)<br>
19:51:54	 From Jonathan : (this=patterns/antipatterns)<br>
19:52:10	 From Jonathan : PODCAST https://podcast.securityjourney.com/the-threat-modeling-manifesto-part-1/<br>
19:52:20	 From Jonathan : PODCAST Part 2 https://podcast.securityjourney.com/the-threat-modeling-manifesto-part-2/<br>
19:52:26	 From Didar Gelici : yoda cameo -most fun session <br>
19:52:32	 From Jakub Kaluzny : The thing is to get this to a wider audience. I hope that all people on this call, or all that follow OWASP already model the threats :)<br>
19:54:15	 From Grant Ongers (rewtd) : Treat all sessions as remote - and still pay for the venue?<br>
19:54:24	 From Jakub Kaluzny : Thanks a lot!<br>
19:54:33	 From Avi D : Grant that’s just for the beers<br>
19:54:35	 From Grant Ongers (rewtd) : Ooops...<br>
19:54:36	 From Mel Drews : Thanks all!<br>
19:54:45	 From Grant Ongers (rewtd) : +1 Avi!<br>
19:54:47	 From Nissim H : Thank you all<br>
19:54:49	 From Avi D : lol<br>

