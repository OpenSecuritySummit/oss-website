---

title        : Zero Trust Database Access Using OpenZiti and JDBC
track        : DevSecOps
project      : DevSecOps
type         : working-session
topics       :
featured     :
event        : mini-summit
when_year    : 2023
when_month   : Apr
when_day     : Thu
when_time    : WS-17-18
hey_summit   : https://us06web.zoom.us/meeting/register/tZcpduyvqD8pG9wxMb4TNIDS9oAuuGMJTK5g
session_slack:
#status       : draft
description  :
banner       : https://pbs.twimg.com/media/FuqkAqLWAAAqttk?format=jpg&name=medium
organizers   :
   - Marcos Schejtman
 
youtube_link : https://youtu.be/URmbXSrMccs
zoom_link    : https://us06web.zoom.us/meeting/register/tZcpduyvqD8pG9wxMb4TNIDS9oAuuGMJTK5g

---

## About the session:
Securing your database is incredibly important and easy to get wrong. We can't go a week without hearing about another database leak. What if we could access these databases using strong identities and zero-trust principles?

That's exactly what you can do quickly and easily using OpenZiti's zero trust JDBC. Not only can you add the OpenZiti JDBC directly to your app for zero-trust access, but you can also add it to your favorite SQL editors and access the DB over a zero-trust overlay network with no VPN. Who wants to turn on the VPN just to run a query?

## Session Transcript:

Dinis Cruz - 00:02
Hi. Welcome to this open security summit session in April 23. Here we have
Marco that we're going to talk about zero Trust database access using
Open ZT and the PVC. Over to you Marco.

Marcos Schejtman - 00:15
Thank you very much and welcome everybody to this small presentation.
Basically the idea here is show you how you can start hub more control
about connectivity, how more control about security and basically start
accessing the different assets in a securely fashioned way, right? In order
to get started, I'm going to introduce myself. My name is Marco Shekman.
I've been over 15 years experience in basically cybersecurity most likely
and on infrastructure. I'm super paranoid and I'm actually a video game
amateur player, right. I love playing StarCraft Overwatch, although I'm
terrible playing, I do like it, right? Most likely right now I'm focusing on
evangelist and basically everything related to sock building, zero Trust,
OT security, IoT security, et cetera. Right? Let's get started to this topic
which is at least for me something really interesting in order to make it
happen, in order to get any idea of what we are going to discuss.

Marcos Schejtman - 01:27
Let's see the regular basic deployment production we as a developer used
to do for different companies, right? We do have basically what it's called,
our application. On top of the application, whatever we're building on the
application, we always put our firewall and of course we can put also the
web application firewall, we can put the load balancing on top of it, right?
Any other different things that we are basically those different layers that
we are using in order to make it secure. Right? What is the big problem
about this scope that we are basically regularly taking every single day?
Well, we have our attackers, right? The attacker may try to reach out to
different services just basically using the gateway. The web application
firewall most likely will work using signatures. These guys are especially
known because they only find a way to basically avoid the signature that
there could be currently on top.

Marcos Schejtman - 02:29
Of course we can basically exploit any zero day vulnerability that they can
have or they have discovered at that time, making it so difficult for us to
basically being able to protect effectively speaking or solutions or
application that we are actually exposing to everybody. Right? The future
is scary, right. Day after day we find out that different breaches, different
basically vulnerabilities, different exploitation they're currently doing. And
yeah, that happened recently. People can actually get scared and people is
actually getting still every single day it's coming. Right? On the security
perspective, that's not the only thing to keep in mind, right? We as a
developer, so when we need to collaborate with somebody else, what is the
other thing? We're using VPN right? VPN, it's coming with lots and lots of
other issues, right. How to solve it. IP overlapping all the kind of stuff that
just making it so complex to do, right?

Marcos Schejtman - 03:36
Finally, as developers, you probably have heard not only as a developers,
but basically as every person probably have heard the lattice about the
chain, right? How they can or how hackers attackers can actually get into
one company in order to basically being able to populate or to send their
attacks to any others, right? The way they do it right now, the new target
they're basically reaching out are basically the DevOps team, right?
Everything related to the CI, CD tools, monitoring, data Warehouse
Configuration Manager, basically everything that the DevOps is using. It's
a goal mining for the attacker because the attacker can just start
embedding their own bad code on top of it to basically being able to
spread their ransomware, right? So it's hard. And what can we do about
it? Well, in first place, we need to recognize what is the current model of
the networking that we are currently using, right.

Marcos Schejtman - 04:42
That is important in order to understand how can we avoid all this kind of
stuff that probably may be happening right now. In the regular network,
what we are going to have is or attacker, right? The attacker basically is
going to have or it's going to try to move laterally to any different servers,
right? Probably the attacker is not going to be able to reach out or Castle
or assets, right, in a direct way. What is going to try to do, or what the
attacker is going to try to do? Well, basically he's going to try to send
communication to any other endpoint that may have that access, that may
have basically the keys of the kingdom, right? That's the easy way they
can do it because basically they move from there and they can start right
now from this machine. They can just now move laterally and basically
reach out any other service as they basically need, right?

Marcos Schejtman - 05:37
The first thing we need to do is first recognize that the perimeter has
evolved, right? I recall when I start working in this basically space, right,
we used to say this is the physical perimeter, right. We used to protect our
data centers. That's probably one of the reason that when you go to the
data center, you need to present any number of credentials and basically
you need any number of bureaucratic processes. Don't get me wrong,
those are perfectly fine. The only issue is that we recognize how to protect
them in a physical way, right. We move into the network and then we start
saying, okay, in order to protect the network, probably we need to put the
firewall in there and then probably web application firewall as well, and
the DMC, et cetera. Basically we are promoting this physical mode into
our networking, creating these virtual barriers between each one of the
different stages of network, right?

Marcos Schejtman - 06:37
However, right now we know that not necessarily the network is what we
are working on, right? We also know that there is something else and this
is the application, right? The Pandemics actually taught us those
companies that probably were not ready at the beginning. The Pandemics
just show us how we can actually start working anywhere, just using
applications, right? Assess applications, just mobile applications,
whatever. Basically right now we cannot protect just basically physically,
right? We cannot protect just using just a firewall. Because I'm working
from home, I don't have a firewall who can protect me. I can probably
start working from the beach or I can start working from a coffee shop, et
cetera. There is not actually an easy way to identify right now what is the
perimeter that is surrounding us, right? We need to recognize the new
perimeter is the edge. It's the application right now.

Marcos Schejtman - 07:37
Right? This came with lots of benefits, right. When we start talking about
distinguish or basically acknowledge that the application is a real
perimeter, well, we're going to be able to create something that is called
microparameters and that is going to help us because we are going to
start reducing the surface of attack that the attackers may have, right? We
are going to dissolve legacy technology. VPNs for starting a couple of days
ago, the US government just released a new document about how to make
it happen, right? Security by default is the new model, right? Trying to
dissolve all these legacy technologies and be more aware of basically the
new time we are approaching to and we are living too, right? It's also
going to help us to basically do a breach mitigation, right? It is not the
same saying oh gosh, this ransomware has to spread across all our
computers and servers.

Marcos Schejtman - 08:42
They just say yeah, well, unfortunately we're going to hit on just one
server, right. Because basically it cannot move laterally, right? Because we
have done this micro segmentation, we have done this microperimeter
across the different application, et cetera, et cetera. Basically this kind of
stuff is not going to be catastrophic when we start doing that, right? That
is an immediate benefit of just recognize that the application is the new
edge and basically we need to start protecting around these applications,
right? In order to do that and before getting into what is the CDBC and
how we can do it is important to understand what is Open City. Open City
is just basically an overlay network. It's an overlay network that is going
to work on top of the Internet. What internet? Your internet? My internet.
Anybody's internet, right? The 5G, whatever, right. They're not using or
it's not going to use any specifics.

Marcos Schejtman - 09:39
It's just only going to use the regular internet no matter where we're
located onto. Right? In order to protect this, we are going to start working
with different solution or with different sites or different parts of it. Right.
The first one is the controller. The controller, as you can imagine, the
control plane is the one that is going to authenticate us, is going to tell us
if we are authorized to consume any different service that might be
located on top of our overlay network. Right? On top of that we're going
to have the routers and we can say that we have two different type of
routers. The first router we are going to discover is this one which is the
edge router and those routers are the only ones that are going to have a
public IP available. The reason behind that is that somebody or any other
customers may be able to connect to those if the controller says that I can
actually do it.

Marcos Schejtman - 10:39
Right. Of course we're going to have some other routers and those routers
might be on the fabric on their overlay network that we can start creating
or at the same time they can be on somebody else, right. Where they can
be well they can be in our own infrastructure, it can be on the data center,
et cetera. The reason behind those routers is that they can work as a mesh
healing factory, right. When we start putting more and more routers we
are going to find all this solution is going to find the closest path basically
to that, right? Of course after we have our routers we are going to have
full mutual communication between each one of those, right? Finally of
course we have the applications. The applications are going to have
completely outbound communication to the public routers or the edge
routers that we are actually putting on top of it, right.

Marcos Schejtman - 11:37
That's the way we're going to have a full communication. Something to
keep in mind is that this information might be coming from the endpoint
or might be coming from a full application that has communication to
each other. Right. The beauty of this is because everything is outbound,
there is no single port I need to open on this side and there is not a single
port I need to open on this side. Right. Everything could be and can be on
closest ports, right? No listening ports, nobody. The only one who is going
to decide who can actually have access to consume this service or this
service that's living here is the controller, right? The controller is going to
tell me oh yeah, you can move on, oh no, you don't even know what is this.
Right? So there is no possibility. I can basically do expectation because
there is nothing that could be exposed for me in the first place, right.

Marcos Schejtman - 12:38
Just for the static. With that we need to understand that this solution, open
City is going to provide us different way to access our applications. The
first way is going to provide us is something that is called cDNA and
basically that's the regular use case that probably most of us are used to,
right? There is basically some kind of VPN site to site communication and
basically on the zero trust network access, what is going to happen is that
we're going to have a router located in probably our data center and then
we're going to have another router located probably in a cloud provider.
What is going to happen is that I'm going to say all everything that is
coming from this router can be able to reach out everything that is located
into this other router, providing that probably all my users right in this
data center can actually have communication to all the services, all the
hosts located on the OCI or the cloud provider or whatever is my cloud
provider location.

Marcos Schejtman - 13:45
Right. It is completely possible to do it. Of course we can also extend this
more what happened when I don't want to allow that every single
customer or every single my user may have access to the other side.
Probably I just want to have one to one communication right from my own
computer to basically the production server to the database, et cetera. So
how can I do it? How is that possible to do it? Well we can have something
called Zero Trust host access and where basically we're doing host access
is that meaning that basically we're going to install a tunnel or a client on
each other site and basically we're going to provide full communication
between these two sites. Which means is that nobody internally is going to
be able to see the traffic because everything is going to be completely
encrypted and of course we are going to reach out the other party in a
secure fashion way, right?

Marcos Schejtman - 14:44
Finally you may say, what Marcus, if a hacker has control of my computer
is going to be able to try to reach out anything else just trying to install
any Rat application or that. Well you can have something else and you can
have an application embedded or something that is called Zero Trust
application access. What it means is that you can actually embed the SDK
in the application on the client side or the server side and basically provide
full communication. No need at all to basically expose anything. No need
at all that if I are ransomware connecting to my computer it's not going to
be able to reach out anything else because the only one that has
authorization to communicate to probably the database is going to be my
client and that's it. That's the only way I can basically start doing that.
That it's an easy way to basically provide security to our applications.

Marcos Schejtman - 15:44
If we already know what is the overlay and we already know that can help
us. What are the superpowers or what are those powers that we can
actually get when we start implementing basically Open City? Well, we're
going to start seeing it now. The first one is addressability. Basically you're
going to be in control of your own DNS and your own networking, right?
This is huge if you are providing like MSSP solutions or that. You know
that EIP Overlapping is constantly happening all the time, right? And it is
normal, right, I recall. Basically even when we do have a lot of segment or
the private segments in the IP, before space, we used to choose always the
timer, right? The 192, 168, ten one, or the 192, 168, 100 or the one 7216,
16, et cetera. Right. It is always on regular speaking, it's just the same
networks, right.

Marcos Schejtman - 16:45
So IP Overlapping is constantly right. Well, Open City is going to allow us
to basically move from that to create our own space. We can use any kind
of IP addresses or we can just use a private DNS and start talking about
we are going to talk about the naming of the endpoints connecting to the
services. I do need to, right? In this particular case, I'm going to allow the
cleaned workstation to communicate to the Jenkins service, not the Jenkins
host, right. He's not going to have access to probably the SSH, just the
Jenkins service, right. And that's it. Of course this implies that I can also
change the port, right? I can just decide that probably every single service
is going to listen on the same port, the four, three or the port 80 or
whatever port are actually required to. That means that I can also start
working with security by obfuscation in this particular case and start
connecting to each one of those, right.

Marcos Schejtman - 17:47
It is not going to be super standard super compliance, but it's going to
help us to start protecting our solution. Keep in mind again, this is an
overlay network, so I can modify every time I need to, right up embedded
on the server side. Yes, as you can imagine, that means that we can put
something in front of our application, the SDK on top of the application,
and basically no need to opening the port. Is that a Kubernetes application
running in? Well, don't worry, you don't need to expose it, right? You don't
need to expose basically you don't need to tell the cluster that you're
actually listening on something. Just basically you can use our solution to
reach out the service completely in an automatic fashion way, right? This
also works because it's going to be able to protect for basically anything. I
don't know if you recall two years ago, the lot for Yay stuff, right?

Marcos Schejtman - 18:41
It was a big cows we need to patch at that time probably like three times
because the first one was the current lot for yay, but then it had another
vulnerability with a Dos and then another and another, et cetera. It was a
mess, right? Well, what happened when the attacker can exploit that,
especially on a zero day, we don't have time, right, or meantime to detect,
basically reduce a lot and we need to act faster. If we are putting our
solution on top of it doesn't matter that we actually have the vulnerability.
Of course, we need to fix it as soon as possible, but we're going to have
more time to basically do those changes to test if it's not going to affect
because basically only authorized services, only authorized identities are
going to be able to reach out or solution or application and the attacker
who maybe is going to try once and whence and see if that happens, well,
he's not going to be enrolled or he's not going to be entitled to basically
being able to reach out the service and access it.

Marcos Schejtman - 19:46
Right. Of course it means that we can also certify the client as well, right?
Being able to access different ways to the different services no matter
where I located at on the browser, on an SQL client, et cetera, right? To
be honest, using the SDK, it's super easy, like two or three lines easy, right?
As you can see on the screen right now, it's just a job example, right?
Super simple. You can see this is the regular stuff we used to do, right? We
basically say I need to open a socket channel and basically I'm going to
put the listening in this particular port, right, in this particular host that
I'm getting it, right? I'm going to get and accept everything that I'm just
basically processing as I need to, right, the city way. Super easy, right?
We're going to initiate the communication, right? That's basically us
communicating with the controller and say, hey, can I raise a server, can I
put this or that, et cetera.

Marcos Schejtman - 20:53
That's something, that's the only thing that we're going to do. After that
we're going to say, what, I'm going to bind, but not on this particular IP or
this particular port, no, I'm going to bind with this service and that service
is going to have its own information. That service probably is going to put
me into the port 80 or the port 20 or the port whatever, right? It's going to
give me some way to accessing it. I don't know that at code time. That's
the beauty because I don't need to mess with it. It's going to be super
secure and everything is going to work as expected, just as easy as that,
right? Basically I don't need to know the IP, I don't need to know the port,
I don't need to know anything on this particular way. That means that it's
going to help us.

Marcos Schejtman - 21:40
Because if you recall the original model of the network, what happened in
that the attacker may move laterally in order to access it. Because
basically he's going to for the endpoint, he is going directly to try to put
something in the endpoint so he can have access into. If I embedded the
application, that means that he should know how to accessing the
application. He should know how to basically start, but he cannot exploit
beyond that application because I have put everything on my own solution.
Basically the attacker needs to know that the SCCP is only going to be
able to send SSCP information. The SQL is only going to be able to send
SQL information. If the hacker is trying to do basically an SQL and FTP
or whatever in a different port as we configure, it's going to be completely
impossible. That also means the solution that's Nmap et cetera are not
going to work because basically this is only entitled for the solution for the
application that we are just building at this particular moment, right?

Marcos Schejtman - 22:47
This is the beauty and of course we are talking about CDBC and this is
more likely for Java development, but guess what, you can basically use it
anywhere. We have SDK and there is an SDK for basically anything that
could be used. This is the beauty of the open source as well, right? Being
able to basically reuse the code and put it anywhere, develop once,
develop anywhere, right? I don't need to nail, I don't need to mess with the
networking anymore. It's just as easy and that right. CDBC, let's get into
the mode, let's try to understand more on how this CDBC or what is and
how it works, right? At CDBC basically certifying CDBC well first, you
already know that JDBC, it's the standard de facto to access any
database, right? It could be a relational databases, but basically any
databases that could be self, right?

Marcos Schejtman - 23:49
At the same time, not that long ago a company found out that many
databases contain vulnerabilities and this could be related to many things,
right? First, obviously upgrades, updates, et cetera. Secondly, as we saw,
right, basically the code we need to be the VBA, the developer, everyone,
it's trying to run with the business, right? It's trying to move the business
saying we need to do this, we need to deliver this, we need to deliver that,
and these are the dates. When the new vulnerability happens, well, it just
put into the queue, right? It is hard, to be honest, it is hard to stay on top
of the vulnerabilities and then of course to stay on top of releasing the new
version with the new features, et cetera, right? If you sum up that plus
56% of the vulnerabilities on the databases are normally high or critical,
well, it trying to makes more sense, right, to defend or put the database
protected, right?

Marcos Schejtman - 24:51
Trying to put it somewhere where the attacker cannot reach it out. Plus
let's keep in mind that most of the cases the database is going to contain
information from us, right? Information from customers. It is critical to
have that information secure, right? To have that asset completely
protected. So how we can do it? Well, basically there is a way to certify
anything and that way you just start certifying the JDBC and certify the
JDBC just basically say, what, we're going to make that any JDBC
communication, it can work using basically the overlay, right? And it was
quite easily, right? It is super easy as you can see here. One of the ways
you can start doing it right before doing the CDBC for example, and it is
just basically initialization of the SDK that is connecting with Open City
and sometimes just modifying the socket sub factory that probably that
particular ddbc is using.

Marcos Schejtman - 25:54
Like this one, right? You're going to say, Marcos, that is only happening
into the code, right? How can I make it in for example, an SQL client?
Well, using the CDBC it's completely possible to do it. The only thing we
need to do is just tell right, or solution whatever it is that we are going to
use another driver. That's the driver we're going to put or driver. It's only
going to have one small modification, the first one, right? As you can see,
instead of starting our current URL with the JDBC that we currently know
and then the completed URL et cetera, we're to modify the JDBC. But just
at C, right? CDBC, that's going to be the new path, the new URL that
we're going to use. Of course we're going to use another some other
properties in order to make it happen. We're going to use the city identity
file in order to make a what, you're going to use this key and guess what?

Marcos Schejtman - 26:54
If you don't want to send the key in plain text that I think nobody will
want you, right? You can also put it into a wallet and just make it happen.
Just send the wallet and protect the wallet as you currently do right now,
right? Protect it using the application server that you probably are using
or protected in any different way, right? It's super easy to basically just
make it happen and just get started with it, right? What are the goals of
this CDBC, right? Because you may thinking, oh man, you will need to
modify basically the application for one application for the postgres, for
MySQL, for Maria, for whatever. Well, not necessarily, right? The first
goal is not modifying existing code driving, right? The reason behind that
is because they have already invested so much time and so much resources
to make it happen.

Marcos Schejtman - 27:48
To make that basically driver working in a way that is going to provide
probably more reliability and more performance. We don't want to modify
those existing things, right? We just want to make it happen to use it as a
backbone. Basically we want to make it as simple for any customer
application and for basically any third party tools that could be embedded,
right? I'm probably using DB Beaver to connect to my databases. I want
to use it here, right? To make it simple to use anywhere, wherever it is,
right? So how does it work then? What we did or what we are doing with
CDBC is just basically a wrapper, right? What is going to happen on top of
it is that we are going to deliver some shim configure and basically what is
going to provide that is that it's going to send us directly to the vendor
driver but using our solution as the transport to send that.

Marcos Schejtman - 28:51
Basically long story short is that we're going to open a city socket right, to
the other party and the database is just basically just that city socket to
communicate to the database in a secure way, in basically easy way. We
don't need to modify anything, we don't need to modify codes, we don't
need to do anything else. Just adding our solution as it is. As we saw, the
only thing we need to modify is just the starting of the line just to put the
C, it's saying it's using or stream or configuration in order to
communicate to any database, right? Plain and simple. That's it. It's the
only thing it needs to be done. What is going to happen if we don't have
the shame for it? Well, don't worry. We have added into the solution,
again, a couple other options where you can basically do the rejection of
the stream in a possible way, in a way that basically is going to be
completely possible to modify the platform and start using it for any other
driver that not necessarily can be available at this moment right now.

Marcos Schejtman - 30:08
Right. Yes, it can be used anywhere else. You can use it on your clients but
you can probably using any kind of web application server and you
probably rely on the application server pool technology to create those
things. Not necessarily you want to put it or you want to make it or only
accessible for the code, right? It is not going to be an application.
Probably is your application that it could be located on the cloud
communicating when your databases could be on prem or vice versa. The
database could be on any cloud provider and you need to have
communication there. Well don't worry, this can be done easily as well,
right? You can just basically onboard the same CDBC in your application
or web application server configuration and do the same, right? Just
adding the new identities or adding the new properties. To that one to
provide that communication easily right at that moment, no issues at all.

Marcos Schejtman - 31:08
Right? So let's see a little demo. You can see, you can feel the platform,
right? How it works, what it's doing, et cetera. I'm going to stop the
sharing right now. Well, I'm going to modify it . That what I'm sharing. I'm
just going to show you of what I'm doing here, right? What I do have is
this is the solution. This is just basically the code, how I build it, right? You
may have an idea of what we're going to present, but basically it's first
simple, right? I do have this workstation that it's called Apollo. This
workstation have access to different things for the database or for the
communication. We have created also one database server that is located
in Europe, right, in a London data center. And we also have a US one.
This is located at New York without a center. So I do basically have
different solutions.

Marcos Schejtman - 32:03
Right now I'm located at Charlotte, right, on North Carolina. Basically I
don't have access to any of those. At the same time, we do have an
application. This application is basically using a Python code, right? You
will see different things, how this basically is working, or what we can
actually achieve on this, right? Let's get started and let's see how it
working, right? The first one, as you will see, is I'm going to do basically
just a single sh. This SSH is going to be sended basically to the
application, right? I think it is okay. It was frozen for a bit. I'm going to do
an SSH to that particular server, right? You can see here I'm connecting
basically to the US database, right? I'm just going to do you I'm going to
use SSH, and the idea behind that is that I should be able to basically
reach out this server in an easy fashion way and connect to that, right?

Marcos Schejtman - 33:05
You can see here, I do have the access. This has obviously an external IP
address as well where I can communicate with it. Basically I'm just in that
server, right? Nothing fancy at this moment, just easy as that. To know
that we are not doing like anything crazy, I'm going to connect also to the
European SQL Server, right? Basically the idea is that you can see that I
have access to both of them. They are located in two different locations,
right? They do have two different IP addresses. Basically I can just do the
curl and you can see again, this is a completely different address where we
are located and how I access these servers. Well, basically I did access
those servers because my application is having access to those. If you take
a look into this, you can see that actually I'm providing the access to this
particular server via IP address.

Marcos Schejtman - 34:05
I define this particular IP address for it even when as you can see, this one
doesn't have any 172 IP, right? This is the 1066 and probably this is one
other IP. There we go. Yes, different IP is located completely different.
Basically as you can see, I'm just locating or I can have access to it in any
fashion way I do want to, right? Not just that you are going to be able to
see it also that I do have access to different services in some other way.
There is only one port I can access to this and this is the port 22 and
actually it makes sense if I disconnect from the SSH and I just say, what, I
want to do a Cellnet to the Postgres database, right, and Postgres is
listening in the 5432, right? I can use that and just say what, send me a
Cellnet on this, on the 5432.

Marcos Schejtman - 35:00
What is going to happen is that as you can see my machine doesn't have
access to that one, right? It is impossible to basically communicate to that
because the agent policy or the policy that was deployed on top of here is
just basically to provide communication to SSH, right? We are doing
segregation, it is not possible to do it. Actually you can see that the
resolution is not even close to the IPS that this server may contain. Right?
Now you may wondering, okay Marcus, so you just prove that you have
SSH access. How can I connect? Well, the easiest way to connect is using
or client. This client. This is SQL, right? Nothing crazy. You can see that
basically I do have here configure the Postgres data driver and in the
Postgres driver you're seeing that basically for the driver class path I'm
just using the Postgres, right?

Marcos Schejtman - 35:56
Nothing else, it's just the Postgres driver but I'm also using the CDBC,
right? The CDBC is located on the Open City project on GitHub at open
source Apache two license. Basically you can use it anywhere you want.
What I'm telling is, what, the class name to provide this driver into
Postgres is going to be the City driver that we just created and the URL is
going to be modified by CDBC or JDBC city Postgres. Right, so that's it. I
do have a couple of aliases you can see here, right? I can modify this alias
so you can have an idea what I'm doing. Basically you can see in here that
I'm connecting using City to this same IP or same name with the port that
I basically test that I don't have the access to communicate to, right? I can
just say, what, connect me to the US database and what is going to
happen is that the application is going to have the solution.

Marcos Schejtman - 37:00
It's going to have the proper requirement authorization to communicate to
this particular server. In here, well, you can see, right, basically I can just
show information, I can just show any tables, right? I can just basically do
whatever I want and I can see the content on it, right? I'm working on the
SQL database and my server, my workstation don't have access to it.
Whatever else I try to use is not going to work. This works using a domain
as we did in here. It's also working if I use an IP, which IP, the IP that I
basically and explicitly select, that I can use to connect. You can see this is
the same database, but in this particular case I want to reach it out just
using the IP address. Once again, I'm going to use this internal IP address
and I have exactly the same information.

Marcos Schejtman - 37:57
I am connected to the same server, running on the same deviant device
and running everywhere, right? Basically I do have the possibility to just
communicate anywhere else, right, in just using the CDBC driver that we
are setting up here, right? As you can see, this is huge because it will allow
you not only to provide a secure access to your developers, to UDBA, but
also eventually to provide a more secure access to the application by itself,
right? Any robot code exception or any robot code injection that they may
have and they probably will win access to the application server. Well, it
doesn't matter, right? The server is not going to be able to move laterally.
The application will, but not the server by itself. We are reducing basically
a scope of the surface of attacks, the surface of the threat. It's getting
reduced and reduced even more and more.

Marcos Schejtman - 38:58
Just a couple of other examples to show you, right? I'm going to show you
another one that I completely like. This is because the power of basically
this SDK that you can integrate, we focus on the CDBC, of course, but
CDBC, it is just one of the different applications that you can do with
Open City, right? The other ones are, for example, putting a server running
behind the scenes, right? In this particular server, right, you will see this is
the server again, right? You can see all these IP addresses. You can see
what is the external IP address that got assigned to it. In this particular
server, I do have a docker for a container that is running and you can see
that this container is not having any port available. Actually if I try to
reach out this particular server, I'm going to try to reach it out in here.

Marcos Schejtman - 39:55
You can see that actually I'm not able to, right? This is the way I want to
access it and basically I don't have access to it. However, we're going to
connect to the server right to the docker. Obviously I know I'm not
following docker interfaces or docker best practices to the provided right?
The idea is that you can see when I try to run my application and I'm just
going to say what, raise this server. This is going to be a flask regular
application and you need to use this internal service. This service is just
basically a service I just created into Open City, right? This is a service
that is going to provide us communication, it's a web application
communication but it's only listening into the overlay network. What is
going to happen is that after I just did that I basically have access to
access the solution in this fashion way and of course this will work if I
want to send information just using postman or any information I will
want to send is going to be able to do it.

Marcos Schejtman - 41:03
The reason behind that is because we do have the ability to basically
embed on top of the different application as I want to. Finally even one
more solution you can provide you're using Open City. I know, right? I love
it. It is a great open source solution basically. The other thing you can do
is basically start sharing, right? How many times you need to share your
basically space on a document or basically any kind of service to
somebody else and you are using basically any probably free solution on
the top to share the file or to share the service, right? How many times?
Probably a little bit right of those. Well, Open City, right, thanks to the
SDK and thanks to many other things, you can also create this type of
sharing tools and in this particular case I'm going to share with you one
simple sharing tool that has been built on top of Open City as well.

Marcos Schejtman - 42:00
This sharing tool is called the Syrac. Basically what I'm going to do is I
have put a server right, and you can see if I go to Croc test, right? There
you go. There is here a couple of files that I want to share with you. All
right? Those files, it's an easy way to share it. How can I share it with
everybody? Well, I can just basically say Sirok, what, Open City I want to
share in a public way this directory, right? I want to do it using a web
application. This is basically what we're going to show you and what is
going to happen is that I do have this query or I do have this URL that I
can basically access at any moment. Basically what is going to happen is
that right now if you're typing it now you're going to be able to reach out
my computer and have access to these two files, right?

Marcos Schejtman - 43:01
We can show you that basically I can just say that it's working. He's going
to send me the file that I just select. So basically this is just working, right?
It is just showing you just a single file. Of course, at the moment I decide
that you are no longer have access to it, I can just click it, close it and
there you go. It's going to have full or I'm going to lose communication to
it because it's no longer going to be working. Right. I can just take it
anywhere else, any other basically a browser that doesn't have like the
cache enabled, right? We can just open a private session. What is going to
happen is just that right? It's just going to remove all communication that
you used to have on it, right? Because there is no more access to it, I just
close it out.

Marcos Schejtman - 43:50
Right. Providing that basically you have full communication and you have
full access to anything you want to share. Right. In conclusion, to have
some time for probably some other questions, let's keep in mind what we
can basically do it, right? How to get Open City or what we need to. Oh, I
think there we go. Yeah, I messed it up. I just double click. All right, we are
going to share it again. So, yeah, in conclusion, what I highly recommend
is just getting Open City. It's open source, it's going to help you and there's
many ways to basically get it right. You can go to GitHub, just download
it, you can go to City Dev and start working with it. We have multiple
options. We do have the quick start. You can just put any Open City in
there, right? As you can just launch it, create your own network, start
sharing whatever you want to, whatever you need to as you did, right.

Marcos Schejtman - 44:53
Start moving with the servers, start moving to databases, start moving for
basically anything you want to. Right? So, yeah, I don't know if there is
any questions for the public right now.

Dinis Cruz - 45:05
Yeah, look, this is pretty awesome, right? I have to say I wasn't fully aware
of this tool. Now I have tons of questions. Can we start with the last
example? Right, so you're sharing some files, right, from your one service
I've used in the past is a service called Ngrok, if you know that. So is this
kind of equivalent. So what's the requirement? You need to have an agent
on your computer, which is the almost like the routing the local traffic
router, right?

Marcos Schejtman - 45:37
Well, not really. And that is the beauty. Right. The solution can work with
agents or without agents. For example, I'm going to shoot down all my
agents here, right? What is going to happen as long as I do that is that let
me close this . My machine just got slow. So what is going to happen? You
can see right now, right? I just got me disconnected from the server, right.
I no longer have access to any SSH, basically. The reason I no longer have
access to it is because I should down the client, right. You can see it did
connect me, right, completely disconnected. So I don't have the access.
Still, if I run it this is quite similar to Angry, as you said, right? The
difference is Angry is just a public available service that you use, not open
source. In here you can mount your own instance of similar scroc, right?

Marcos Schejtman - 46:33
I can just click it, I can just share it again, right? As you saw, I shoot down
my agent. The agent is not working. If you access this right, I'm going to
put it in the chat. Bear with me because it's a little.

Dinis Cruz - 46:50
Bit slow from a technical point of view. What this is doing is your
container is sending the traffic to well, that tool you built, right? This
particular one is sending the traffic to the exposed service, right? Like you
said, we can run our own or we can run a managed service on top of it,
right?

Marcos Schejtman - 47:11
That is correct, yes. So basically you have that ability. My computer is
going to send the traffic or everything is going to be using that. I don't
need to open any port, right? I don't need to expose it, nothing. I can just
share that URL or any URL that the system is going to provide me at that
moment and I can just share it with you. I can just share it with anyone
and they can start accessing to it. I just finished the share, I just closed the
share and nobody else is going to be able to access it, right? Particularly
for the syrup, I think somebody else in some other session they're going to
talk about it, but we can discuss mods in different ways. Basically for the
Syria perspective, you can also share it in a private way and just say, what,
this is going to be shared, but only those that are actually part of my
overlay network.

Marcos Schejtman - 47:58
Not necessarily publicly explicit, but it's only private, basically network.
Yeah.

Dinis Cruz - 48:05
That's the kind of policies I think I saw you mentioned, right, that you can
apply almost point to point policies based on application, right, based on
identity and that kind of stuff.

Marcos Schejtman - 48:15
That is correct. Because this is an overlay. Everything is going to become
an endpoint, right. Remember, we're telling or we're trying to move this
concept that the endpoint is just a computer right now, or Endpoint or
Edge is just an application. Right now we're saying this application can
connect to the SQL. Any other application running on my machine can't,
right? For example, you saw that I shoot down the tunnel, right? My
tunnel is no longer working and I don't have access to the databases,
right. If I want to have access to the database located somewhere into the
US, for example, this database, I'll be able to connect. The reason behind
that I'm able to connect is because my machine can't. But this scroll
database, right. Client, this one can. Right.

Dinis Cruz - 49:05
It correct to say that one of the advantages of the agent is that it will
probably require in some cases less changes, right?

Marcos Schejtman - 49:15
That is correct. You have the ability to basically communicate to anything
you want to, right. You have the ability to put the agent and the agent is
going to provide the full access to your computer. But you can just certify
that. It's the word that we are using. Basically when you certify that you
are able to just provide the access to that specific application, you may
want to yeah, cool.

Dinis Cruz - 49:39
In terms of the server side, what you're creating is almost a mesh network,
right, with the agents that get installed, the server instances, right. And
then is that correct to say? For example, on the other end you have a
bunch of those deployments and they now know how to communicate
themselves so that they can find the right basically target that you want to
communicate. You build a kind of a custom DNS almost like
infrastructure on top so you can find things.

Marcos Schejtman - 50:10
That is correct.

Dinis Cruz - 50:11
Yeah, I'm just trying to get my head around it, right?

Marcos Schejtman - 50:16
Yeah. And you can put anything right. You can create your own DNS
space. I'm using my own personal DNS, but basically you can just avoid
DNS. Probably you just want to say, hey, I want that squirrel can
communicate with, I don't know, postgres DB one. Right. You're not
putting any DNS, it's just naming convention that you're using. Or
probably you want to recreate your own basically networking, right. You
work for many other companies and this is going to help you to flat that
network as well, but also.

Dinis Cruz - 50:46
To completely protect it. Right. Because for example, at the moment with
VPNs you have to give access to a huge amount of stuff, right. With this
you almost create connections right, based on what we want a particular
service or user to access.

Marcos Schejtman - 51:01
That is correct. Basically you just provide the access to those specific
services. Right. I don't want you to have access to the whole server. The
only thing you may have access is to the SQL, right, to the postgres
because you're the DBA, but you don't have to connect via SSH, it's just
DBA, that's it. I'm not going to give you access to your computer just to
the application you're using, right?

Dinis Cruz - 51:24
Yeah. Have you had use cases where you actually use this, for example,
inside a Kubernetes cluster to lock down access? Even within the cluster
you can of.

Marcos Schejtman - 51:34
Course you can do micro segmentation. You can actually allow some
specific services running on the cluster, you can actually allow that some
specific containers or some specific application running on the cluster may
have communication externally as well. Of course, if you are talking about
Kubernetes, you can also say, what, I want to manage my Kubernetes
cluster without exposing any public IP and only the administrator
Kubernetes can connect to it. Right. And yeah, that is an opportunity.

Dinis Cruz - 52:06
In that case, why are you installing the cluster? Are you installing a server
or the client?

Marcos Schejtman - 52:12
That's a good one. From the cluster perspective, you have the ability to
use all helm charts. Using the helm charts, you can basically install some
other application running the cluster that is going to work as the bridge.
Right. That is going to provide basically that communication being quite
simplistic right now.

Dinis Cruz - 52:31
Just to clarify, so by bridge you means I could call a server, right? Like the
server unit. Okay. Let's say if I have two complete separate clusters and
then a server somewhere else, what you're calling Bridge is almost the
service that runs on each of those to allow them to communicate.

Marcos Schejtman - 52:50
That is correct. If I do have two different clusters, I can make them
communicate to each other. If I do have an application running on this
cluster that needs to have communication to this database living on any
cloud provider, and I don't want to create any VPN in there, I can also put
it in there. Right. I can just put the application running in the cluster as
well. They may have communication to the database. No code
modification, no age installation, basically directly on top of the
Kubernetes as well. Basically you have the ability to put it anywhere, right.
Any to any yeah.

Dinis Cruz - 53:23
It just to make sure that those bridges can talk to each other, right?

Marcos Schejtman - 53:27
That is correct. Yeah.

Dinis Cruz - 53:32
I'm assuming that the bridge is then where we can serve authentication or
even like all sorts of key based authentication. That connection between
bridge to bridge is actually quite secure.

Marcos Schejtman - 53:48
That is correct. All communication is going to be completely secure. Right.
You can work with Mitchell TLS. We also work internally with the Chacha
poly. Of course, you also have the ability to for the end users, you may say,
what, if Marcus wants to connect there, not only he's going to use his
strong identity, but also he needs to use probably an MFA right. Of his
identity might be on any basically a smart card or any strong identity
solution that I may want to use. Right.

Dinis Cruz - 54:26
Yeah. That was my next set of questions in terms of client identity. Right.
What do you support in terms of identifying the user, the network that you
in, the device that you're in, what's the options there? So this is from the
client, right. That talks to the bridge.

Marcos Schejtman - 54:48
That is correct. From the client perspective, you have the ability to put
basically MFA any TOTP solution that you want to start working on it. He
can basically use it and because it use that specific you can basically put
the identity into any hardware piece. Right. I don't know, HSMA I think it
is called. Right. In English the acronym but basically smart card, GV key,
whatever. Right. You can just put your identity there and you can just plug
it into the computer and if you have declined you may be able to connect.
Right. So basically the hardware works.

Dinis Cruz - 55:27
Yeah. Really cool. No, I see tons of really powerful adoption. I think it's
really great that you guys build it on top of an open source because it
allows a lot of more flexibility on the deployments and then providing
commercial service on top of it. I think it allows for wider adoptions in
places where sometimes you cannot have connections to the outside world
or you only want to have specific points that connect to the outside world.

Marcos Schejtman - 55:55
That is correct. Yeah, that was basically the idea to make it completely
open source. Right. It's an open source project and I invite you to use it
right. To start testing it to fork the repository, to basically download it or
just use it for your own purposes. Right. Like I said, I'm super paranoic
and I used to have these droplets located in the cloud, different ones. The
way I used to access those was basically using VPNs and to open the VPN
to those I was using like pornoking. Because super paranoid right now is
like I just connect to my client and I can reach out any server, whatever I
need to deploy it in an easy secure way. Right.

Dinis Cruz - 56:41
Let me say I could deploy this on native instance, right?

Marcos Schejtman - 56:47
Yeah.

Dinis Cruz - 56:47
Now it comes my bridge using a terminology and then that could be the
only thing that gets exposed to the outside world.

Marcos Schejtman - 56:56
That is correct.

Dinis Cruz - 56:57
That means apart from public services, okay. Something we expose here
and there, website, we publish everything else. It's almost like we can
create a jump box with this. Right? I was going to say a much nicer jump
box. Right. Because usually jump is just a freaking SSL SSH proxy. You
jump into it and you go in there. This seems to me like it's a gem box. I
guess in that case you then have policies that you can apply to. Right. It's
almost like you have a gem box but that could be connected to another
one that gives them the policy. How do you manage that? Distribution.

Marcos Schejtman - 57:38
That's correct. Yes, that is the perfect example. I couldn't say it better.

Dinis Cruz - 57:43
Yes, very cool. No, I think it would be really cool to do it's. Such a
powerful concept. I really like as a good example of zero trust networks.
Right. It seems that this is hitting a lot of those key elements. Right.
Because you now have conditional access based on who you are, what you
are, what you want to access. What I really like is the ability to almost
start to create a nice segmented, zero trust access. Right? If an app can
only connect to X resources, that's the only thing you should be able to
access, right? In terms of DevOps kind of this thing, right. In terms of
pipelines, what examples have you seen where let's say that the definition
of what needs to be accessed is actually on a repo, right? I'm just thinking
in terms of scalability. For example, you have the helm charts that already
define the ports that are open and all that jazz, right?

Dinis Cruz - 58:50
How is the logic then that you would configure that and then as you
deploy the application will configure what's required for the access. Is that
the logic?

Marcos Schejtman - 59:04
That is quite the logic. Basically we do have, in terms of perspective, we
do have everything ready so you can start using in the CI CD pipeline,
right. A communication to the different artifacts that you can probably
use. We also have the home charts that you can basically deploy and start
making it ready to start communicating your solutions. We do have also
TerraForm ways you can start doing it. On the open city site, if you go to
city dev, you also will going to find Kubernetes cluster ready. You can even
deploy the solution on top of a Kubernetes cluster and just making it
happen. Right. We have lots of examples where you can start basically
using it. We have CDFI also Kubectl, right. If you need to manage basically
your Kubernetes cluster, you don't need to install any agent. You can
basically just use Kubectl solution, your identity, do that and start
managing the cluster as well.

Marcos Schejtman - 01:00:12
Basically it has all the tools already ready so you can start working with.

Dinis Cruz - 01:00:19
Cool, man. This is really good because I think it's a great implementation.
I can see lots of really tough use cases. Let's do a couple more sessions
and I can totally see the value of and the solutions you're solving. Right.
So really cool.

Marcos Schejtman - 01:00:45
Yeah. I invite everybody to connect to fork it, use it, and giving us a star as
well. Right? If you like the project, if you trust the project, just giving us a
star that is going to encourage us to keep moving and keep working on it.

Dinis Cruz - 01:01:02
Where are you guys based? Where is everything based?

Marcos Schejtman - 01:01:04
Company is based basically in North Carolina, although we are working
across the world, basically.

Dinis Cruz - 01:01:11
Yeah. Cool. All right, man, look brilliant. Thanks a lot for doing this
session and I look forward to seeing you on the next one.

Marcos Schejtman - 01:01:19
Of course, will be my pleasure. Thank you everybody for your time. I'll see
you next time.
