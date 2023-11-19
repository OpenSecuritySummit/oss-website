---
title        : "Protect Your Application, Not Just the Network. Add Zero Trust Superpowers to Your Critical Applications and Systems"
track        : DevSecOps
project      : DevSecOps
type         : working-session
topics       :
featured     :
event        : mini-summit
when_year    : 2023
when_month   : Oct
when_day     : Fri
when_time    : WS-18-19
hey_summit   : https://www.linkedin.com/events/7115459074531504128
banner       : https://media.licdn.com/dms/image/D4E22AQHu-XuLoH2h9Q/feedshare-shrink_1280/0/1695683737360?e=1700092800&v=beta&t=gkUc31dH0mwo6jQOWH_5Uf__hg-n8yJYA-ufUqeQdgM
session_slack:
#status      : 
description  :
organizers   :
    - Clint Dovholuk     
youtube_link : https://youtu.be/CfGfMqBiFPY
zoom_link    : https://us06web.zoom.us/meeting/register/tZErc-Gtqj8rGtQ6FeIaPHRocTKdnvbROvb6
---

## About this session
A overview of zero trust, what it means to be application embedded zero trust and it will contain demo golang code for people to try out live if they desire.

"Applications are the new edge and zero trust is the security industry’s latest hot buzzword. 
The OpenZiti, open source project (https://openziti.github.io) is a one-stop shop for building
truly zero trust solutions. Stop trying to protect your network. Securing the network isn't enough.
Adding zero trust directly to your app is the future and the best way to keep your users safe.

OpenZiti not only provides the required zero trust overlay network but also provides numerous
SDKs for use in your favorite language. Can't go fully app-embedded? OpenZiti also provides 
clients for all major desktop/mobile operating systems.

In this session you will:
•	learn some core tenants of zero trust and how it's different from current network security
•	see what it means to embed zero trust into your app and why it's the future for application security
•	discover the superpowers your app gains by simply incorporating an OpenZiti SDK in your app"

## Transcript:
Clint Dovholuk - 00:00
You. Hi.

Dinis Cruz - 00:02
Welcome to the last session of the Open Security Summit in October 2023.
And we have Clint, who's going to talk us about the next evolution, or
natural, I would say evolution of the whole Zero Trust, which is the
application, which I completely agree that we need to do it there. And by
the way, I love that. Isolate your app. Spot on. And we might get some
language models too, here. So looking forward to it.

Clint Dovholuk - 00:30
Great. Well, thanks a lot, Denis. Yeah. Again. My name is Clint. Clint
Obloblock. I work for a company that sponsors an open source project
called Openzd. And as everybody knows, every good open source project
must have a mascot. And so down in the lower right hand corner here,
you'll see Ziggy. And Ziggy is our mascot. He is a piece of ZD for zero
trust. All right. So anyway, let's get into it. Usually in the last few years,
whenever I tell people that I work for an open source project, that is a
Zero Trust overlay Network, this is usually the response I'll get, right? A
big deep eye roll. Because in the last few years, particularly, the term zero
trust has kind of been turned into a marketing buzword. So hopefully
you've seen this presentation. You said, is it real?

Clint Dovholuk - 01:26
Is it legit, or is it not? And by the end of this presentation, I'm going to
turn you from a deep eye roll into Shaq here and that kitty cat with a little
shimmy shake shake, right? Like, give me that. Zero trust. That's my goal.
If you're watching this live, or if you're watching it on a recording and you
have Go, I invite you to participate in the demo. That's going to happen
towards the end of the presentation here. So if you're watching it on
recording, pause the video, go install Go, and you'll get to enjoy the
appetizer for our Zero Trust overlay Network. Here's what we're going to
talk about, and you'll forgive me if you have seen this sort of stuff before.
Maybe you're familiar with Openzd already. Maybe you've seen me give a
similar presentation to this.

Clint Dovholuk - 02:14
But this is the current overview. I don't want to assume anybody knows
what Zero Trust is. So we're going to start at the basics, and we're going
to go from there. So let's first start by talking about what the current
network security setup usually looks like, right? And here's what it will
usually look like. It'll be a castle and a moat motif. So this is what you
hear a lot of that castle and the moat kind of idea. And so that's what
most people think of when they think of current network security. So here
we have just a regular basic network, right? And what is a regular basic
network? Well, it's just a bunch of castles and it's a bunch of moats. And
we have individual little networks and individual little locations.

Clint Dovholuk - 02:54
And our job is to allow network to allow devices to send traffic to one
another, right? So once you get behind the walls, once you get over the
moat, all these devices can send traffic to wherever they want. And that's
what normal network security is all about. Once you're on the network,
you're considered trusted. Obviously that's not a great idea. And this was
such a bad idea way back in the day that we said, hey, http FTP, that's
maybe not the greatest idea. Let's make our network a little bit more
secure and let's put TLS or transport layer security everywhere. And so
that's what we did. We went out and we got a little lock icon and we put it
on our little individual devices, and now everybody has TLS. So instead of
FTP, now we're using SSH and SCP. Instead of Http.

Clint Dovholuk - 03:45
We're using Https. Then people said, well, you know, that's great, Https,
but it's kind of hard to get that certificate. So poof out. Popped this thing
called https everywhere. HTPs Everywhere is a project by the Electronic
Frontier Foundation, and it was so successful that they're actually phasing
it out. But what it would do is it would take your Http URL that you typed
in Google.com and upgrade you automatically to Https. So it would check
to see if your browser had access to an actual secure URL. If it did, it
would automatically upgrade you. And that was great. Less encrypt was
started because everybody was like, hey, this Https is everywhere now,
right? How do I get some Https for me? Turns out back in the Dark Ages
before let's encrypt and SSL. Zero, I think is what it is.

Clint Dovholuk - 04:39
There's another one that's similar to let's encrypt now. You would have to
pay for a certificate. So most people on their trusted network were like,
it's trusted, I don't have to bother with this HTPs stuff. Of course, that's
obviously a bad idea. We should not trust our local network. And that's a
central tenet of the term zero trust, right? Trusting that network, you're
safe, you're secure if you're on that local network. So why is it a bad
thing? Well, obviously if an attacker in this case, represented by our little
fella down here in the lower left in red, because he's dangerous, if they
attach to your network even though you have TLS, well, what are they
going to do?

Clint Dovholuk - 05:18
They're going to start sending packets, they're going to start probing your
network, and then if they find an O day or a zero day, or some sort of
vulnerability, they're going to compromise your laptop and poof. Now
you're having a bad time. So horizontally moving across a network
something that we really need to control. And if you didn't know it, this is
what VPNs are, right? When you attach to a VPN, you're basically turning
those three little castles into one giant castle that lets you get to anything,
anywhere. Most of the time, now you might have an advanced VPN that
does a little bit of segmentation, then fantastic, good for you, but lots of
people don't.

Clint Dovholuk - 05:54
And so if you are attaching to a VPN, oftentimes you're able to get to all
of those corporate resources without any worry other than having to be on
the VPN. So again, I mentioned the word segmentation. We started to do
this idea of segmenting things where maybe now we'll take our little Ziggy
and we'll put him in a little policeman's outfit and he's going to police our
traffic. So now when that nasty offender gets on our network and wants
to send those packets, we have old Ziggy there taking care of business,
stopping those. Cool, cool. Right. Everything's good? Are we done? Call it
a day? Of course not. We can't call it a day. It's never going to be good
enough. So what happens?

Clint Dovholuk - 06:32
These attackers, they are ever vigilant, they are always out there and once
they have a foothold, they're not going to give up. So they're going to keep
trying. They're going to compromise a laptop that does have access to the
target that they're looking for and then use that target as a stepping stone
to the next network where they're going to just compromise that target of
opportunity. All right, so how do we combat some of this? Enter the idea
of zero trust. Again, we're back at our basic network and I'm going to get
rid of the castles and the moats now and we're going to just look at this
diagram. But what if our network had this idea of a device identity? So
this is one of the core pillars of Zero Trust, this device identity.

Clint Dovholuk - 07:15
And what it means is every device on your network has a strong identity
that the network can use to verify the authenticity of the identity
connecting to that network. So if the identity is permitted to connect to
the network, then great, it'll connect to the network and it can send
traffic. And if it's not, then it won't be able to. And that's called device
identity. This is how Openzd bootstraps device identity. It's a little
complicated. If there's any questions, hit us up on discourse, since you'll be
watching this in a replay, but hit us up in discourse and ask about how
Openzd actually accomplishes secure enrollment. And this is just one
flavor of getting your authentication to the overlay network and we'll see
more about what enrolling means in a bit. And then there's device identity
with our attacker.

Clint Dovholuk - 08:05
So if that firewall sorry, if that network has all these little firewalls, that
understand device identity. Even if the attacker is to get on your network
and be able to start trying to send packets, well, the network is smart
enough to not permit that attacker to send these malicious packets, right?
The network knows the device identity and doesn't even let you on
oftentimes. That's called an overlay network. So what are they going to
do? Well, they're going to just go out and they're going to find themselves
an identity in a laptop that does have access. Because once they have a
laptop that has access, well, guess what? Game's over. They're able to
connect to that machine again and Zero trust been defeated, right? Call it
a day. Of course not. There's even more we can do. So what do we do
next?

Clint Dovholuk - 08:51
Next we take that idea of segmentation and we lower it even more. We
keep narrowing the segment. So instead of having a great big VPN,
instead of having a little network, instead of having one device, we keep
going further and further down to its logical end, which will be
applications. And we'll see that in a bit too. So this concept of least
privilege says every identity on the overlay network is authorized to
connect to other identities or other services on that overlay network. If it's
not authorized, you can't connect. So here we have that same attacker.
They're trying to send data over to our target of opportunity, but ha, they
can't. Because of least privilege, the network knows what services this
device can attach to.

Clint Dovholuk - 09:36
And that laptop in the lower right that it's been trying to compromise all
along is not able to connect to that laptop. So of course we're done, right?
Call it good. But as is always, if that identity is compromised and that
identity has access to the target of opportunity and to the service in
question, then you're still going to be able to be attacked. But does that
mean this is not a good approach? Of course not. We have made this
already. Just imagine how many hoops, how many extra hoops this
attacker has had to jump through just to find a machine that can even
connect to the target of opportunity. It's all about layers and layers of
security. And the more layers you add, obviously the better it is. The
smaller your attack surface, the better it is.

Clint Dovholuk - 10:22
So least privilege giving the identities only the ability to contact the things
that they're supposed to contact, narrowing that focus. Another core pillar
of zero trust is continuous authorization or posture checking. So this
would be things like am I connecting to the service from Windows? I can
only get here from Windows or from Mac or from Linux or is my patch
level of the operating system up to date? Things along those lines. So if a
new patch comes out, you can update a posture check and then suddenly
that laptop is no longer able to even attach to the network, no longer able
to send traffic. All right, and that's a little bit about zero trust. So now
we're going to get into application embedded zero trust. You heard
mention the term overlay network prior. So what exactly is an overlay
network?

Clint Dovholuk - 11:17
You might have already kind of figured it out, but here we're going to take
the Internet, right? Generally speaking, it's really convenient if the
Internet can just be your overlay network. So can we turn our Internet, the
Internet, into our overlay network with Opencd? Yeah, you can. So what
does that look like? We'll deploy a controller somewhere out in the
Internet, and this controller's job in life is to manage authorization and
authentication. So when a device comes online, it talks to the controller.
The controller says, yes, you are who you say you are, and you are now
authorized to connect to the network. Sorry, authenticated to connect to
the network. And you can actually connect. Authorization is the green
light, if you will, giving the identity the ability to actually connect to the
servicing question. So we have a controller now.

Clint Dovholuk - 12:11
We have these things we call routers, and there are different kinds of
routers, some of which can service links between other routers and some
service edge connections. These things come online and they form
connections to everything else. So Openzd is an overlay network that's
also a mesh network, which does differentiate it from other overlay
technologies, like normal VPNs, where you have one concentrator and one
input, one output kind of place. With Opencd overlay, you can have
multiple inputs and multiple outputs, and those things all go together and
they form secure Mutual TLS connections. And that's important. And this
diagram gets really busy when I add all these locks on here. But that's
important because every single edge router to edge router connection or
router to controller, that's all Mutual TLS, meaning the device attaching,
must provide a certificate to the server it's attaching to.

Clint Dovholuk - 13:04
And the authenticity of the certificate that is being presented is verified by
both the client and the server that uses public key infrastructure. If you
haven't looked that up, fun topic, deep topic, but that's what Mutual TLS
is all about. I'm going to take those lock icons away because it makes it
busy. And then the edge routers also are there, as I said before, to service
connections between edge devices or edge SDKs, and the edge router. And
that's all done for the express purpose of one thing, and that's sending
data back and forth. Obviously, the whole idea of a network is to send and
share data. Ideally, it's with identities which are only authenticated and
only authorized to send that data, like on an opencd overlay network.

Clint Dovholuk - 13:52
Here's the three basic forms of zero trust as we define zero trust, and we'll
go into each one here in a moment. Zero trust, network access. This is
what most vendors will tell you is zero trust. You trust your local network.
Wink. Not a good idea, right? You trust your local network, you trust your
remote network, and then everything in between, we will make zero trust.
And that's pretty darn good. It's actually not bad, right? It's pretty good.
That's not terrible, but we can do better. So what if we take an agent and
put the agent on their computer. Like for example, on my Windows
computer, I'm running the Windows desktop edge for Windows, which
looks like this. And so I have a little agent on my computer.

Clint Dovholuk - 14:38
And that little agent's job in life is to make sure that traffic is only trusted
on the device. And that's pretty darn good. Openzd works like this. Other
cool technologies like WireGuard works like this as well. Or your VPN,
even if you want to consider the VPN right, there's a little agent that runs
and its job is to intercept all of this traffic and then shuttle it safely over to
the other side. If it's a server, if it's a client, wherever it's going to. But
everything in between is safe. So even if you're using Http and Insecure
protocol in your device, you can successfully and safely tunnel Http to the
server. And we'll see that happen here in a minute. And then finally,
obviously, the end all be all application access.

Clint Dovholuk - 15:22
Keep reducing the attack surface all the way down as far as you can into
the application itself. No longer do I trust my host's OS stack. Let's go
back a moment. If we look at the network access, not application. Come
on, where's my build? Right there. That's host access. If we look at this,
anything on my local machine that sends Http is able to go into this
tunnel. So if I curl there, or if I have malware, or if I have the actual app
that I'm trying to use, all of which can go into this tunnel and safely
tunnel, that is what application embedded zero trust can solve. You no
longer have a listening port here, intercepting traffic. You don't have
anything that does that sort of interception. The application simply writes
into the zero trust stream by itself. That's a huge benefit.

Clint Dovholuk - 16:14
And you can even go one step further. With Openzd, you can use a
hardware route of trust, which is really cool because then you don't even
have to trust that the file is safe on your operating system. Always there's
some root of trust somewhere here. It would be a little green dongle that
you plug into your computer. All right, so all that's what our application
embedded zero trust is all about. Let's focus now and we'll just take a look
at the attacker and the client that it's trying to attach to. So what are we
going to do? We're going to take an SDK, we're going to stuff it into our
application, and then magically lock icon shows up and we have a secure
application. And that's basically what end to end embedded zero trust is
all about.

Clint Dovholuk - 16:56
Application embedded zero trust cool is no firewalls are needed. We have
application embedded zero trust already. We're good to go. What does that
look like when the attacker gets there? Well, that attacker compromises
the laptop. You have an application embedded zero trust SCP program,
SQL program, and FTP program, right? Secure protocol. SQL. You never
know if it's secure or not. Depends on how you've done it. FTP? Definitely
not. So if the SCP application wants to send traffic to SCP, it's permitted
to. If the SQL Server wants to, it's permitted to. If the FTP wants to, it's
permitted to. Obviously. So now what happens if the SCP application tries
to send traffic to that FTP application? The SCP application has no idea
how to send traffic to FTP. It doesn't even know how to get there.

Clint Dovholuk - 17:45
As they say, you can't get there from here, so it's denied. Same would be
true for SQL traffic going to FTP or for the SQL Server program to try to
send SCP. It literally cannot be done because it must go over the overlay,
and the overlay won't even permit it to. So why that's? Super powerful.
Now you have effective immunity to malware, showing up on your local
computer, compromising, one of those bad applications, super cool stuff.
And that's where Openzd comes into the picture. Now, you might be
saying to yourself, this sounds like a lot of work and it is a lot of work,
and it was a lot of work. And this slide is one of my favorites. It represents
the duration or the longest path a human can walk across the earth, right?
And this is basically the path to Zero Trust.

Clint Dovholuk - 18:37
We realize everybody's not going to go straight from Brownfield
application to application embedded Zero Trust Greenfield application. If
you can, then great. You get to start in Siberia or maybe in Africa,
depending on where your start and end is. But otherwise you're going to
have to go the whole entire path. And so we realize that it is a journey.
Open Zero Trust is a journey, and people aren't going to jump right into
Zero Trust and application embedded Zero Trust immediately. So maybe
you'll start somewhere in the middle of Asia, maybe you'll start somewhere
in the middle of Africa, and your journey might be different. But this is the
longest path a human can walk and it represents the fact that it is quite
the journey.

Clint Dovholuk - 19:20
But Openzd has you covered because we have those things I remember I
referred to before as those tunneler apps. So if you have Linux or if you
have iOS or Android or Windows like me, or whatever, your particular
operating system target is of choice, you can use one of those tunnelers to
bridge the gap between application. Embedded Zero Trust and brownfield
deployments tunnelers do have a really cool property that is worth noting
because if you have an Open ZD overlay network, you will have these
tunnelers available to you. And so suddenly you can start doing cool things
with all your brownfield apps too. So for example, one of the superpowers
from Openzd that tunnelers provide is true private DNS. You can create
fictitious DNS names that your users can then connect to.

Clint Dovholuk - 20:12
Like my ZD which is not a valid top level domain or Linux Foundation one
summit. Like I made this slide for Bodibic boat face, right? Fluffernutter.
These are all DNS entries that you can create and would be private to
your bespoke overlay network. So that's pretty cool. But not only is it
private DNS super cool, but it's authenticated DNS. It's truly private.
Right? If you deny the user and the identity, I should say access to your
overlay network poof that DNS entry goes away. And so those are some
really powerful superpowers of a tunneler, and we could get into tunnelers
someday. That sounds interesting, but what are we here for? We're here to
talk about the superpowers of application embedded zero trust. So let's
blow it up and let's get going. So what do we have here? We have two
pictures.

Clint Dovholuk - 21:06
Perhaps you're familiar with the picture on the top. That is called the
Beast. The Beast is a limousine that the United States presidents drive
around in. It is bulletproof. It is blast proof. Right? It's got all this security
built into it, not bolted on top like the Mad Max approach. Right? With the
Mad Max approach, you're like, oh, there's a chink in the armor right
there. Oh, I can shoot through here. Oh, it has regular tires, right? The
Beast. Sleek, sexy. Security built inside. Secure from day one, secure by
design. Mad Max. We'll do our best we can. Day two, security. It happens,
right? We'll just keep bolting stuff on until we make it secure because we'll
get there, I'm sure, right? So that's a key difference of application
embedded zero trust is it's built secure by default.

Clint Dovholuk - 21:59
You have zero trust security built into it right out of the gate. That's a
superpower. Another one. From a developer's point of view, I don't know if
you've ever had a service that's behind a load balancer, but all too often
when you're behind a load balancer, you as a developer, you don't even
know where this thing is going. So you're told to connect to my
application server, and then that gets turned into an IP address. And then
if you're lucky, the load balancer will forward source IP. And so you as a
developer could have a shot at understanding who is connecting to your
service before they actually connect to your service. But that's not the case
with an overlay network. Like Openzd. With Openzd, you know, Clint is
trying to connect to Prometheus. There's no question about it. Right?

Clint Dovholuk - 22:46
You know the exact identity connecting, you know the exact identity that's
being connected to that is also a superpower. On top of that superpower is
it's not just for the clients. It's also for the server side. Right. Usually we
think about zero trust. We think about security. You think about the cloud.
The cloud is safe, right? Nobody's going to get into my cloud. My VPC is
secure. I've only got 85 holes open to my VPC. That's only 85 holes. Not a
worry. Well, with a zero trust overlay like Openzed, you can have zero
open holes to your firewall. So your VPC can be truly firewalled off from
the world. No open listening ports at all on top of that, so that's the
firewall. On top of that, the server has no listening ports either.

Clint Dovholuk - 23:33
We already talked a little bit before about side channel attacks being
impervious to side channel attacks and the local computer, that goes for
the server too. So if that FTP server is listening out in VPC land, or virtual
network land, or Cloud land, wherever Kubernetes land, it'll have no
listening ports, it is not attackable by IP and port, literally not attackable.
And that's what we're going to see in our demo in a bit. Oh yeah, I guess
this is just more no inbound Firewall polls. Same exact point. I should
have looked ahead of my slides, but you get the point, right? No listening
ports, no inbound firewall rules. That is just super cool stuff. I don't know
if you are familiar, but a couple of years ago there was a CVE, a critical
vulnerability and exploit around Java and Spring called Spring Boot.

Clint Dovholuk - 24:26
And it was kind of a big deal, right? If you got a hole in that firewall, then
anybody on the open Internet can do what? Oh, they can just attach right
through that hole in the firewall, hit that Spring Boot server, and
compromise whatever they want to compromise, because that
vulnerability was of astronomical proportions. That's a good zero day.
Guess what you can't do when you have a zero trust network like Open
ZD. You can't even connect to that, what's the word? Attackable target. I
can't come up with the right word, so you can't even connect to it. So the
only people who could connect to it are people who have that strong
identity. Now of course, if one of them gets compromised, then your bets
are off.

Clint Dovholuk - 25:08
But you have reduced your attack vector from something that's on the
Open Internet to, if you're lucky, whitelisting of IP addresses. But you
don't even have to worry about that because Openzd you can just bypass
all that and secure your application directly, have no listening ports, that
attacker has no chance to get to that Spring Boot application. And so that
was also another issue that the Spring framework had, and I don't
remember exactly what CVE oh, what's this CVE? Also a 9.8. So a 9.8. If
you haven't seen the CVSS scoring, I do recommend you go check it out.
The critical Vulnerability scoring system, it's pretty neat. It has like six to
eight parameters, I don't know exactly, but the two that I focus one of
which is attack vector is Network. Permissions required none.

Clint Dovholuk - 25:58
If you have an attack vector of network with a permissions required of
none, you're already in a bad place, right? That means anybody on the
network is able to potentially attack that vulnerable target. So if it's on
the Open Internet, I don't even know how many billion devices there are
out on the Open Internet nowadays that are available to attack that
target. With Openzd, you can close all that down. And again, before I told
you, another superpower is contacting the client from the server. Usually,
if you're lucky, you know what a server side event is, or you know what a
WebSocket is, and you can open a WebSocket to your server and you can
get events that way, or you have some sort of IoT type of implementation
that allows you to do this sort of stuff too.

Clint Dovholuk - 26:44
Openzd's overlay network already allows you to do that. So if you were to
embed Zero Trust into your server, into your client, it's just another client
on the network, your server is just another client and your client is just
another client. And it's possible for your client to declare that it binds or
accepts connections from other clients on the network. So let's think of
like SSH would be one of those ones where you would define an identity as
able to SSH or RDP for example. But with Zero Trust enabled by Openzd,
you can use application embedded Zero Trust and talk from your server
straight to your client. So if you want to notify them all, not a problem.
You can just do that. You can just connect to them. But you must be
authorized.

Clint Dovholuk - 27:29
The server must be authorized to send a message or dial, and the client
must be authorized to accept a message. And then soon Openzd is going to
allow the clients to turn off that ability of listening, even so that the device
you with your tunneler could turn off the ability to listen. So you are in the
control there too. That's super cool. And we use that with Amazon
Lambda. So because it's application embedded, it doesn't matter where
you deploy it, right? This is not Kubernetes only, this is not VPCs and
Amazon only. It is literally anywhere it's application embedded. You can
run this on your local laptop, and I'm going to run my client on my local
laptop here in a minute and when I stop blathering and get to the actual
demo, right?

Clint Dovholuk - 28:15
So another killer feature, Openzd, gives you end to end encryption out of
the gate. So by adopting Zero Trust into your application and your server,
you have true end to end encryption. If you remember, before I talked
about Mutual TLS, I talked about the router and the client connecting and
forming a Mutual TLS connection. And that's great between links, but that
means when you're on the router or at the endpoint, you can see whatever
the traffic is. With end to end encryption, even if you were sending traffic
through that router has no ability to be able to read that traffic. On top of
that, even if you had. If you use a secure protocol like SSH on your other
side, on both sides, the SSH application protocol is also another layer of
encryption.

Clint Dovholuk - 29:08
Being able to obtain secrets and defeat the security of that connection is
going to be incredibly difficult. Attackers are going to have such a hard
time. It's definitely not going to be worth it. Because of course, if it's
worth it, maybe people will find a way to get through it. But it'll take
nation state actors in order to go through the amount of effort it'll take to
bypass those three layers of encryption. So don't forget application layer
end to end encryption. Mutual TLS makes it basically unhackable, and I'll
say basically because everybody who is sufficiently motivated, perhaps
they'll find a way. But as we know, of course, there's not right now. And
that uses Libsodium, which is built for small devices. So you'll see, Openzd
oftentimes is targeting IoT type devices because we have a Csdk and the
Csdk is tiny.

Clint Dovholuk - 29:58
And Chacha 20 poly 13 Five was built for tiny devices. So even if you have
a Raspberry pi or something teeny tiny, zero trust is not out of reach. Take
an SDK, stuff it in your application. Now you have zero trust available to
you. Another just amazing superpower, in my opinion, port inference. If
you go out to any network and you scan that network, you're going to find
out, oh, Clint's using MySQL clinch using VNC, right? It doesn't matter.
When you send all of your traffic through the secure zero trust overlay
every port becomes 443. So good luck figuring out what services
somebody is using just by scanning ports. You're never going to do it. It'll
just be all 443 or whatever you choose. 443 is just a common one.

Clint Dovholuk - 30:50
So all your traffic pardon me 1 second, all your traffic gets synthesized
over a single connection through the Openzd overlay, which doesn't
impact performance. So don't think of it like that. It's a big pipe. It's as
big as your network speed is. So all of your protocols travel over that pipe.
And so they all look like port 443, whether it's FTP, SQL or SSH or
whatever I mentioned before. Continuous authorization. You get that for
free with Openzd as well. Domain checking, Mac address checking,
process checking. Also, ZD supports two factor authentication out of the
box. So that's all cool stuff you get. You get a self healing mesh network,
which is also really important. So this way, if your device is sending traffic
and one of those routers goes down, no problem. Openzd will just route
the traffic from one place to the other.

Clint Dovholuk - 31:39
That's super cool. And then this is what it looks like. This is an example of
taking an actual Java application which creates a client and then sends
traffic over that client from the before to the after. Key things to pay
attention here, let me make it a little bit easier for you to see it. Let me
make it even easier for you to see it, right? So you have no need to know
the IP address anymore. You don't need to know its local host or whatever
the IP is. You don't have any need as the developer to know what port it is.
You just know you have some super secure service, and your identity is
authorized to, in this case, bind to bind that identity. So this is acting as a
server. Bind means I accept traffic. Dial means I'll send traffic.

Clint Dovholuk - 32:29
And so as a developer, you don't need to know where things are defined or
where they're hosted, et cetera. One of my favorites, maybe my favorite
embedded superpower is this thing I refer to as Implicit multifactor
authentication. So if you have a strong identity, you can't even get onto
the network. You can't even send traffic to your API. Now, presumably
your API will have some sort of authorization that's baked into it. So this
SDK on the left will talk to this API on the right, and the API will verify the
traffic in some way. The network also verifies that identity by having that
implicit identity baked into it. So, realistically, you have two factors of
authentication already. By just using a zero trust overlay network, you
have your strong identity from openzd, and you have your authentication
from your API service.

Clint Dovholuk - 33:25
And so those are the selling points about application embedded zero trust.
And I've blathered long enough. Maybe you just skipped right ahead to the
demo. Maybe they put nice little chapter marks in here for you, and you
just skipped into the good stuff. So that's cool. So here's where we
actually see all of this in action. We're going to put our money where our
mouth is. Let's take a look at what our demo is going to look like. So I've
already deployed. In fact, I won't say I did, because I didn't deploy this
network. The Net Foundry console deployed this network on my behalf.
We call it the Appetizer Network to get you to want some openzd. And
what we have is we have a network deployed, we have a controller, we
have some routers in the mix.

Clint Dovholuk - 34:03
And on the left, you'll see the Reflect client. That's my client running on
my local computer. And then on the right, you'll see Reflect server, HTP
server. And that's deployed in Amazon, Fargate. So I made an application,
I bundled it into a docker container, and then my good friend Mike
Guthrie deployed it out onto Fargate. And now we have the appetizer out
there running. This is all open source. I don't think I even mentioned this.
All of this is free and open source, right? You can go get all of this for free.
Host your own openzd network today. Go get it. And if you want to look at
the demo, you'll go to the Openzd test kitchen. ZD zero trust. ZT. ZD.
Italian pasta. So our little logo here, this little piece of ZD. So here's
Ziggy back again.

Clint Dovholuk - 34:52
He's got a chef hat on this time and he's in our Openzd test kitchen where
we basically test things out before we put them into the main repository,
which is just Openzd GitHub.com slash Openzd. All right, out there is an
appetizer repository and aptly named. We have an appetizer Openzd IO
pause right now because you can go there right now. And presumably we
haven't taken it down whenever you watch this video, who knows? But if
you're doing it right now, you'll probably have this available to you and
you can see I've gone there appetizer Openc IO. If you enter your email
address, which is what I'd ask you to do because that's a good, nice,
unique name, then fantastic. We'll get your email.

Clint Dovholuk - 35:34
Hopefully we won't solicit you, but maybe we but you can add yourself to
my Openzd overlay network and if you don't want to be bothered with it,
you can just click the don't bother with me, don't bother me right now. But
if you want to let us know that you care about Openzd, you can go ahead
and put an email in there. Once you've done that and click the button,
you're going to see, it brings you to a page that looks like this. And then
you'll see run some of the sample programs. You'll see the git clone, you'll
see where the repository is and then it'll give you the little kind of overview
that I just showed you and tell you some samples to run. Fantastic. That's
what we're going to see because I'm actually going to just go and do it.

Clint Dovholuk - 36:11
So let's just go and do it, shall we? First thing I need to do is I need to
bring up Microsoft Edge, a browser which I literally never use and with a
bunch of junk on it. So let's go to Appetizer Openzd IO and you'll see I get
the same thing that I showed you before. I'm going to enter my I'm not
gonna put my email address, but it's Clint@openzed.org. If you want to
email me, you can. But I'm not going to type it in here because who knows
who's going to look at it. So we'll just use Clint and let's do Open SEC
Summit. Let's do that. That sounds great. That's probably pretty unique.
And add me to openzd. All right, so now once I've added myself to no, I
can't click on that.

Clint Dovholuk - 36:58
Apparently once I've added myself to Openzd, then I can go and I can
clone the repository. Now I've already cloned the repository, but you can
just go ahead and copy that if you want to. And then I need to download
my token. So remember I talked about enrolling an identity. The identity
enrollment starts with a signed document, which in this case is a JWT, and
so it says, where would I like to save it? I'm going to save this thing into
my appetizer. GitHub openzdest kitchen. Where is it? It's in here
somewhere. Work GitHub openzd. Okay, let's go back up and find it.
Where is my test kitchen? That oh, it's because it's on Linux. That's right. I
am running this inside of Linux, which is why I don't remember where it is.

Clint Dovholuk - 37:58
And let's see, my username is going to be in home and CD and Git, where
is Git? In here, and here's GitHub. And here's opencd test kitchen. And
here's the appetizer. So I'm going to save this there. Now when I saved it
there, I can then just go run the application and I've already CD into that
location. So if I bring up my terminal and I PWD, you'll see I'm in the
appetizer repository, I can go ahead and just run that command that I
copied and pasted. Now when I do this, what's going to happen? What's
going to happen is the application is going to enroll that token, which you
can see it happened and that's going to connect to a server. I'm going to
bring up the diagram. Actually, I want to bring up the prettier diagram if I
can find it.

Clint Dovholuk - 38:50
Let me find it real quick, this one. So it's going to contact a service that
has no listening ports that I stood up that will do one thing and it will
reflect back to me or echo whatever I type. So if I say hi, then it'll say hi
and it'll say you sent me hi. Now, what also happens that you're not seeing
this is normal stuff. I challenge you to find this service on the open
Internet. You won't find it at appetizer openZ IO because it's all
application embedded. So this has no listening ports anywhere. But you
can try to find it, you won't. But what happened here is I've sent a
message up into the cloud, in this case an Amazon Fargate where this
thing is running.

Clint Dovholuk - 39:41
And I have a server that's running up there accepting connections on the
overlay network, not on the IP based underlay network. And it's returned
back to me, this text. And so that's what it's done. Also what it's done is
it's looked at my input and decided if the input was profanity. So I added a
Go library to check for profanity. And then we did something even cooler.
We have another service that can deploy it out there. In fact, I don't think I
was sharing my screen, so I'm sorry about that. We have another service
that Ken deployed and that service is doing language model work. It's a
text classifier. So AI being all the rage, right? Everybody needs an AI
service.

Clint Dovholuk - 40:27
We have a service that looks at my input and classifies it as to whether it's
offensive, I don't know where Ken deployed his service. Think about
microservices, right? Thinking about the what you do all day long. You got
Team A that does one thing. Team B, that does another thing. You need
team A to send traffic to team B. Team A has to say well, how do I
whitelist my IP? Here's my IP. Blah. Right. None of that with openzd. Ken
stood up a service, told me the name of the service and told me go dial it
and that's all I had to do. And so that language model is running out there
somewhere and I don't know where Ken put it.

Clint Dovholuk - 41:02
So if I do something like say I hate babies, then you're going to see, hey,
your message seems to be offensive and we are not going to relay it. Also,
if you will notice in our oh, Clint is a dingleberry. Somebody is being a
funny dude right now. That's really interesting. Who hates babies? I
wouldn't have expected that to kit through our language classifier. But
you can see somebody else is actually using this right now. I don't know
who. This honestly wasn't the plant. Hopefully it's somebody on the chat, I
don't know. So if I then say I like babies, you can see what I didn't show
you before is that the service also reflects the message back into your
screen right here. And if you wanted to have somebody else play along,
you could just send them to messages. Messages. M-E-S-S-A-G-E-S.

Clint Dovholuk - 42:00
HTML spell it wrong. Too many s's, maybe too many S's, I think. And they
can also get the messages too. Like example. So that is application
embedded zero trust working. We have sent message from my computer
here in western New York up into the cloud to a server that has no
listening ports. That server sent traffic to another server that was doing
language model identification using Python. Oh, I should mention, I wrote
it in go. Ken wrote it in Python. You can find that also on the test kitchen
GitHub account too. And then it returned a response and I printed it out
here and you can see the latency that incurs. Here is an example. If I hit
enter, you can see basically instantaneous pops up back on my screen. So
common question is what kind of latency can you expect?

Clint Dovholuk - 42:54
Humans never notice it. Now, I also did one more thing using application
embedded zero trust. I actually created a little bot in my application and
every time a message is sent to our demo application here, it actually pops
up here in mattermost and it tells me I hate babies. If were to go look at
this one, if we look at them both at the same time and see which one gets
the message and which one doesn't get the message, you'll see that the
message that's reflected publicly doesn't come through. But the message
that might be offensive is put in our chat message here. And so I can then
decide is this actually offensive? Is it not offensive?

Clint Dovholuk - 43:39
And maybe we could doesn't do this right yet because I just made this
demo literally today, but maybe someday that yes button will train our
language model so it can learn that this is offensive or that's not offensive,
and that's all entirely secure. I don't know where Ken deployed it, so just
think about multi cloud solutions now, right? If he deployed it in Azure, I
would have no clue that I deployed it in Azure while mine runs in Amazon.
And I think that's kind of mind blowing. So hopefully you think that's mind
blowing, too. Now, that's my demo. I hope you enjoyed it. You can go out
to the test kitchen. Like I said, let's skip past all of this. That was my
demo. Opencd has all kinds of other Zdefied, as we call it, apps.

Clint Dovholuk - 44:20
We have ZSS, which is neat because you can SSH here to a place without
having a port open, right? You can deny all the firewall rules like Ken did
when Ken deployed that service. Ken used Openzd to basically be the
bastion, if you would, the entry point to that server. He can only access his
server via Openzd. We use SCP as part of the ZSS package. Some
examples we have mattermost. You saw me doing mattermost. That
mattermost server that I just it's a chat app, which is equivalent to Slack
or Discord or something like that. But self hostable. That Mattermost
server that you just saw me accessing that I was messaging, can only be
messaged via Openzd because it's protected by Openzd.

Clint Dovholuk - 45:11
But it's a good example of the tunneler based approach and an
Embedding not Embedding joining an application embedded zero trust
approach with a Brownfield existing app. We send messages from GitHub
all the time to my Mattermost. So when I get a notification oh, there's Ken
right there. When I get a notification that a commit has happened or that
Clint approved a message, I'll get a notification from GitHub in my
Mattermost. But the only way to hit that Mattermost service is via
Openzd. So there's a Zdefied webhook for that. Zdbc. Actually, Marcos
has talked at a security summit in the past about me. If you haven't seen
that one, go check it out. Really good one. Great. Marcos, great job
presenting works with all your databases out there because it's not
bespoke per database. So it works with Postgres, Oracle, you name it,
right?

Clint Dovholuk - 46:10
It's just about poking the JDBC driver in the right way. Have good blog
posts about it. Cubezetle helm. I'm going to just skip all through these
because you can go out there and check them out on your own.
Prometheus actually one of my favorites here. I have a complicated
Prometheus example where we have a Prometheus server that's scraping
Kubernetes over the Openzd overlay, where the Kubernetes control plane is
entirely off the overlay before it had to be on the Open Internet. And you
have a Kubernetes ingress after you have kubernetes API. Totally hidden,
totally private kubernetes. And yet Prometheus can still scrape it from
anywhere. Cool blog post. If you're interested, let us know. Zdefi is also
neat. Very important. Every country, I believe, not just the United States, is
now issuing executive orders that secure infrastructure.

Clint Dovholuk - 47:03
Infrastructure must be secured by a Zero Trust mechanism of some flavor,
obviously why it's relevant in today's world. It's mentioned eleven times in
that document. Here are the Pillars of Zero. Trust. And you're thinking to
yourself, clint, what a great job. What a great demo. Blew my mind. Put
this in a cart. Let me bring it home. How do I go get it? Well, like I said
before, we are out on GitHub. You can go to oh my goodness. Shame on
me. Openzd GitHub. IO is no longer the URL. It is currently openzd. IO is
the URL. So I'll have to go and fix that. That's where you'll find our
documentation and GitHub. We're on GitHub at Slash Openzd so you can
find us on all our socials here. You can follow me and Ken weekly. We'll do
a ZDTV out on YouTube.

Clint Dovholuk - 47:53
We have a Twitter handle while Twitter is still around. And look at that.
Slide is so old. Still got the old bird. Who wants to go to X, right? Nobody
wants to go to X. We have a discourse group where you can hit us up in
discourse, where you can ask questions and whatnot. And if I can ask one
thing of you, it's to go to our GitHub repository openzd, and give us that
star. That star does mean a lot to us. It helps other people know that ZD is
a cool project and people should check it out. If you look at our star
progression here, you can see we're picking up some steam. So hopefully
you all who watch this can bump this up way higher. Let's see another big
spike. And yeah, give us that star. And that's the whole thing.

Clint Dovholuk - 48:35
That's application embedded. Zero Trust. I hope you've enjoyed it. Hope
the presentation was exciting. And if you have any questions, hit us up on
those socials. All right? Cheers.
