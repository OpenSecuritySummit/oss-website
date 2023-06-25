---

title        : "Web application's language negotiation in 2023"
track        : Governance
project      : Risk and Governance
type         : working-session
topics       :
featured     :
event        : mini-summit
when_year    : 2023
when_month   : Jun
when_day     : Mon
when_time    : WS-15-16
hey_summit   : https://us06web.zoom.us/meeting/register/tZ0kcumtrzIqGdGU901Tm6DPqcl7usquqWYi 
session_slack:
#status       : draft
description  :
banner       : https://pbs.twimg.com/media/FxF-OsLWcAAHwp1?format=jpg&name=medium
organizers   :
   - André Ferreira
youtube_link : https://youtu.be/t_mgpLhXAgI
zoom_link    : https://us06web.zoom.us/meeting/register/tZ0kcumtrzIqGdGU901Tm6DPqcl7usquqWYi 
---


## About this session
LCN is a process of selecting the language and content that a web server will respond to a client's request with. It is essential for websites to provide appropriate content in the user's preferred language to enhance their user experience. However, this process can be exploited by attackers, leading to various security vulnerabilities.

This session will discuss the current state of LCN and its future direction. The session will also cover the potential security risks and best practices to mitigate them. The speaker will share their experience and insights on how organizations can implement effective LCN strategies to enhance their web application security.

## Transcript:

Dinis Cruz - 00:02
Hi. Welcome to this open security Summit in June 2023. And we have
Andrea, one of our heavyweights in application security, expanding on his
thoughts on actually a very interesting area of security, which is the
applications language negotiation, and he's going to give us a bit of a run
through on where we are. And then we're talking about maybe doing a
panel in one of the next summits. But this is a great introduction of this
quite interesting topic that it was mentioned that there's some interesting
ways to exploit it. So, Andrea, over to you.

André Ferreira - 00:32
Cheers. Definitely heavyweight. That's a good one. I'm actually quite
heavy at the moment. It's pretty accurate. Thank you for that. So I'll start.
So if you ever wondered why you get bombarded by a particular type of
advertisement in your own language when you're browsing the World
Wide Web, or if you're just curious of how websites function in different
languages, or you just want to understand a bit better what happens and
what are the consequences of specifying your language preferences? This
talk might be for you. And I will only require that you have used the
internet before, most specifically the word my web. And since you're
probably seeing this online later, if you're not here, you will qualify and I
hope you find it interesting. So, during the Pandemic, me and the wife,
were living in a north facing apartment in London, in Dublin, actually,
sorry.

André Ferreira - 01:26
And we passed a lot of our time watching TV series. And being that we are
from opposite ends, opposite seat edges of Europe, we communicate
mostly in English, despite the fact that we manage quite a bunch of
different languages altogether. I managed to speak Portuguese, English,
French and Spanish, and she speaks Lithuanian, Russian, English, and she
understands a bit of Spanish as well. But regarding what we can watch
together, we are somewhat restricted to English. So one of the shows that
we used to watch was called A Place In The Sun. And if you're not familiar
with it's one of those shows that people from the UK and Ireland buy
properties in southern countries, apartments and houses, and that kept us
entertained during the Pandemic. Now, influenced somehow by the show,
and due to some other more pressing needs, we did some financial
exercises and gymnastics and we figured out a way from Ireland and it
was supposed to be temporarily, but we did have the aim of making it a bit
more permanent.

André Ferreira - 02:27
So last year we moved to Spain, and me being from Portugal and having a
similar skin tone as the Spanish in a large forehead, sometimes the local
people talk to me in their language and I've just lost my train of thought.
They speak to me in the language and mostly I understand what they are
saying and I feel very comfort when that happens because it means that I
actually fit in, I don't stand out, but when it's my turn to respond, I have to
negotiate back that conversation into Castellano. So in Spain you might
have this perspective that everybody speaks Spanish, but in reality they
speak Basque, they speak Catalan, they speak Valencian and other
languages, and castellano is what we know as Spanish. And this
negotiation is not very different from what happens on the World Wide
Web. And although there are many different ways of serving different
languages, in this talk I'm going to focus on the Http way in proactive
language negotiation.

André Ferreira - 03:32
And let me kick in. I can change the slide, which I'm not able to. It just
takes a bit. So my name is Andrea Ferreira and I hold a master's degree
information Security for Northumber University in the UK. And I've
worked in the It space for more than two decades for small and large
companies. I've worked in different markets, I've worked in different
countries, and if you need a trustworthy person that can give you a hand,
I'm currently available. A cool thing about me is that my name is common
and I share it with many other individuals. And we all have an accent, an
acute accent on the e, and the slides take a little bit to pass. We got it. So
when we think of something that we want to share, be it words spoken or
written or gestures, those are symbols for ideas, emotions or information
that we want to transmit.

André Ferreira - 04:34
And when we want to make our messages understood, preferably the way
that we thought about it, we need to have some rules, we need to follow
some rules. Now, this communication process must follow also a protocol.
When a person talks, the other one listens, and the communication has to
be done in a language known to both and preferably pre negotiated to
avoid situations like Palivu francimpa Avenue spanol no by now, or, and
this one is going to sound funny, I took Calvinia to Viskai taip Bascan bins
use Monai, which will be something like do you speak Lithuanian? Yes. Let
me call the wife, because it's a language that it's very hard for me to
learn. Now, in early life, we also found or we also learned that words are
made up of individual letters and those two are part of the overall
protocol that we required in order to communicate.

André Ferreira - 05:29
So communication shouldn't still be thought about having two radios
playing music at each other, because there's no communication taking
place. Communication needs to be thought as the successful exchange of
information and perhaps it will surprise you, but there's 8324 spoken
languages and sign languages that are currently documented and in the
planet we have 7000 of those languages currently in use. And with all
those languages, having a universal translator could save us from having
to know that many languages. And we know that from Sci-fi. This will
work great when we have to communicate with aliens as to try to defend
ourselves from something stupid that we're going to do. However, there
are some devices that already exist to help us with this. When I was
preparing for this talk, I've stumbled across this is still a bit slow vasco,
which is a device from a company based in Barcelona, Spain and their
reviews in Amazon are actually quite encouraging.

André Ferreira - 06:30
I have no affiliation with the company and if you watch recently Google I
O you also saw a person being translated in real time from English to
Spanish with their limps matching what was being said. So the future
advancements in this area look quite promising and that is until of course
we meet somebody like Arturis or have our own C Three PO because then
things will get much more interesting, I think. Now, language is not only
about conveying meaning. There's an associated culture and a diverse
history behind it and details matter. And as an example, you might have
already learned this, but Portuguese words Munto Brigado do not actually
translate to thank you, although it can. But historically from Latin it
would be more closer to I recognize an obligation to return a favor to you
in the future. Mutagarit Sidu, on the other hand, would be closer to thank
you.

André Ferreira - 07:26
And these cultural juices along with slang and the detestable, acronyms
and abbreviations are all part of an identity that translations need to
accurately represent, which basically makes us think that sometimes we
need to have subtitles for some things that will be translated and diving
super fast into history. Computer history with long jumps from the time
when an American professor ran a camp a wire across campus, electrified
it and used it to rang a bell at the far end of campus to the invention of
Morse code. As a way to transmit information fast and far distances from
mechanical typewriters and teleprinters that were later adapted to
mainframe computers to the creation of Request for Commons 20 US.
ASCII. Humans have invented and discovered a lot in the last 200
centuries, in 200 years and focusing particularly on us ASCII, which has
seven bits that allow the representation of 128 cold points being that the
first 32 are control.

André Ferreira - 08:30
Codes that you will use for controlling devices, all devices, and also for
magnetic tapes and all of the other codes from that being the alphabet
and numbers and punctuation. Humans have discovered a way to use on
and off or one and zeros to represent language. Now, US ASCII has been
a great American invention but very pragmatic towards their particular
needs and very insufficient when it comes to represent more than 8000
languages. For example, if we grab my name, it can't actually be
accurately described in US. ASCII because of the lack of the acute accent
on the e. And the way that this basically works is if you look at this table
one from the first row, where you have 64, 30, 216 and so on, you have a
stream of bytes. So you have like seven bytes. And if it's a one, you will
add the value that is on the top.

André Ferreira - 09:22
And when you sum them all together with the bytes that you have on your
right, that will give you a number 65, 110, 120, and that can then map to
a character to be displayed on the screen. I stress again that the US ASCII
is not eight bits. It's not an octet, it's seven bits. And perhaps I could
forgive the Spanish department responsible for issuing my driver's license.
However, it's the second time that it comes wrong because the first time
they got the surnames order wrong. But my first name was right. It had
the acute e there, but this time around they came with the order right, but
it's missing the e.

Dinis Cruz - 10:00
So, Andrea, at least you didn't got like a SQL error or you didn't got a call
and said, hey man, why did you just crash half our database?

André Ferreira - 10:09
Yeah, the first error was actually quite interesting because in Portugal we
have first the surname of our mother and then our father, and then Spain,
they have it the other way around. So when it came, I had it corrected
because I have other documents that need to match exactly the same
order. But this one, when I saw it, I just had to laugh because I thought it
was really funny. Now, because US ASCII is limited and to be able to
represent other languages, us ASCII got extended throughout the years,
other car sets were developed and we have examples here of what they
are. But it got to a point that it was really complex because different
manufacturers had their own thing, and when they needed to translate
from one car set to another, it was messy. And this is where Unicode came
in. And Unicode allows you to map 150,000 characters, more or less.

André Ferreira - 10:57
Not so many, but almost 150,000, which is way more than 128. And it's
really pretty smart also because you can represent most characters well,
some characters with only eight bits. But if you need more, then you can
have 16, and then if you need more, you can have 32. So it's a variable
and car set. Now, when you buy a new computer, it should ask you to
specify the language that you want to use it in, unless somebody else has
already done that for you. And the operative system language will allow
you to interact better with the device. And if that device comes already, the
computer comes with, or even if it's a Mola comes with a default browser
installed, it will probably be following the language of the Operative
system. And if you go to the internet, then if you connect that device to the
internet and you go to a page and you want to download another browser,
you'll probably see that web page on the same language as you have on
your computer.

André Ferreira - 11:53
And let's imagine that page would be this source code. This little bit of
source code that I have on the right would represent a bit of the HTML
that Web page gives back to you. So I want you to observe that there's a
little piece of text that identifies lang equals Ang, which is the abbreviation
for English. And that page is actually with a car set equal to UF eight, utf
eight. So a trick question here would be, do we really need utf eight for a
page that is in English? But if we wanted to translate this page and we
wanted to put it in Portuguese, then lang would equal PT, and the Shar set
could probably also not be utf eight. That lang is an attribute. That's what
it's called in HTML. And this particular attribute assists screen readers to
determine the language of the Web page.

André Ferreira - 12:44
And the goal of the Web is to be inclusive. And so if your company has
claims of inclusivity, this is something that you want to take care, that you
have to avoid some future brand damage or just add it as a tick box
exercise in your release checklist. Now, when you have an HTML page,
you need to save it in a hard drive in a server so that in that same
computer, you'll have a program that will serve Web pages when you get
some requests that you'll just sit and listen for when somebody wants to
talk to it. And you need to take care when you save the file with the right
encoding, because otherwise the contents on it will just displace on
Gbrush. And it's something that, throughout the years of my experience, it
would have saved me a ton of work and a ton of, well, not losing a lot of
time.

André Ferreira - 13:36
If I actually got a pop up like this one, that would actually tell me that,
hey, there are some characters here. In this case, not so much smiley faces,
that will not actually display. Also, apart from this, there's care that needs
to be taken when we use some tools, even from known sources, because
they might actually tell us that something is right or wrong and it's not the
case in this particular scenario. I tested Google.com on W three C Tool,
and he was telling me that the Google.com page was coming back in
Portuguese for some reason, and the fact is that it was coming fine in
UTFA. So I also want you to notice that there's a Translate equal yes on
the first image one, and that helps most modern browsers translate the
Web page for you. And some of them don't actually need you to install a
plugin.

André Ferreira - 14:28
You can do it just by right clicking the page. However, in some cases, you
might actually find that it's not really desirable to have that translation
taking place. You want to set that to no. And the only browser that doesn't
seem to respect. This is Safari and I have a fundamental problem with this
one, which led me to report a security issue to Apple. But I'll get into that
in a little bit later. Using the Mac OS as an example, it allows you to
specify the languages that you want and you can set one as primary and
one as secondary. In this particular image you can see that I have my
language set up to English. And when I install applications, if for some
reason the application is not available in English, then it will use my next
preference and in this case would be Portuguese.

André Ferreira - 15:16
If you're curious why I actually use English and not my native Portuguese,
it's just because out of habit of working with different operative systems
and different versions of Windows, Linux, Unix and macOS. And if you
ignore my original settings, if you look further at the bottom, you will
notice that I have some settings on particular language that I want to use
browsers in. And that works too. And it doesn't actually depend on the
languages that I specified for the operative system. That means when I
actually open Chrome, Opera or Safari, I'm going to get them in the
languages that I have specified. MacOS also allows you to do translations
offline and I use a few. However, when you get to Safari, it always uses
online translation. And I also have an objection towards this. So when I
was testing the functionality of using the global attribute to translate on
web pages to see exactly how browsers would behave, I found some bugs.

André Ferreira - 16:12
But most importantly, I got upset when I saw that Safari didn't actually
respect that. I said translate into no. And I came up with a scenario where
somebody is using an Internet intranet, not intranet web page and it's
tabled as confidential and they translate that page. And what happens is
that page has to go through the network and to a bucket that is in
Amazon owned by Apple. And the preference that I actually have of that
not happening was if I actually had it specific as a no, somebody had to go
and change the source code to yes so that no accidental translation would
take place. So a part of that I also thought, well, if this has personal
identifiable information or the sensitivity on the file is really big, we would
not be very happy to share this with Apple. So I put this to them, but they
came back and said, no, this is not a security issue, nothing to see here,
move along.

André Ferreira - 17:06
I disagree.

Dinis Cruz - 17:08
But then again, just to clarify, so you're basically saying that when you're
browsing Safari and there's a need in the text that there's a language
mismatch within who you are and what you're seeing, the Safari would
actually send the text of that page to an Apple server for translation?

André Ferreira - 17:29
No, the user will still have to do it you will have to ask for the translation
but you can claim that you did that accidentally. And it's like a defense in
depth type of thing. When you set the transition into no and just by having
it there, I will feel way more comfortable. It would be something else that I
wouldn't have to put in the procedural debt check for this traffic if it's
going to the bucket on Apple that goes over there or not.

Dinis Cruz - 17:53
Yeah, because that page, whatever you're watching could have all sorts of
confidential information.

André Ferreira - 17:57
Right. I was thinking that even not only for the military, but you might be
working on your intranet which is supposed to be kept inside on something
that is very sensitive, you're going to launch a new product, something like
that. And I'm like this shouldn't be there. And the fact that all the other
browsers actually respect all of the modern browsers that's the ones I
tested in respect to no, I was like, why are they doing something different
here? Although Apple does have differences, as we will see in next slide, is
in other things. This one upset me a bit.

Dinis Cruz - 18:24
Yeah. It is a security issue whether there's a control in place if the
behavior is different and data is executed. I agree with you, man. It's a
security issue. We can argue on the criticality of it, but we should not be
able to argue on whether it's an issue or not.

André Ferreira - 18:43
I actually saw that the fines were so expensive towards the respect of
GDPR that I put some numbers when I wrote the report to Apple guys, I'm
saving you this. And I thought I was going to get an incredible bounty and
go on vacation to somewhere even more exotic. But yeah, they didn't
agree with me. So if and when I have to take care of another company
and there is confidential information in an internet, this is something that
I'll definitely want to.

Dinis Cruz - 19:09
Never publish that as a finding, right. Regardless. And even get a CWE for
it because I think it's a good example of some unintended side effects,
basically of a lot of the stuff we do that we don't have a lot of visibility.

André Ferreira - 19:21
I didn't know that I could do that, to be honest with you. So let's take that
offline and we can work on that. That would be very cool. Very cool.
Thanks for that. Let me kick off because I still had a lot of stuff here. So
most browsers, including Tor, will allow users to specify your preferred
language. Safari is the one off, the odd one off. And by setting your
language preferences you're basically agreeing and stating that you want
to have those preferences shared with the websites that you're going to
navigate. And this images on the left are from Firefox and represent my
personal language preferences and the way that this reads and you
basically have these drop downs that these options that you can move up
and down to specify the order of your preferences. I prefer to receive my
information in Portuguese from Portugal but if that is not available then I
would like to get it in Portuguese.

André Ferreira - 20:12
If that's not available, I prefer British English, but if not available, give it
to me in English French from France and if that's not available, I can read
French and Spanish from Spain. But if that's not available, Spanish. And
if for some reason the server doesn't have any of those preferences, you
can pass to me a page in Chinese that I will not be able to read, or you can
send me an error code. And that's pretty much how this preference works.
Because Safari didn't actually allow for specifying my preferences and to
avoid people from having to install browsers or browser extensions or
installing proxies that might actually share information that you're not
thinking that it happens or sharing your surfing. Experience with third
parties. I thought it would be cool to share a way of living off the land, so
to say. Or so to speak, and show a way that you can actually specify your
language preferences if you're so inclined to do so.

André Ferreira - 21:09
So in this images here you can see that I've opened the developer toolbar
and under sources I specified a local override. Now and this images show
that I got Amazon.com to return to me in Portuguese when Safari is
actually set to English. Now curiously enough, you will see that they don't
have the entire website available in Portuguese as this pop up is in white,
it's in English which undoubtedly states that their default language or
their fallback language is in English. But you'll get familiar with the
details of the override a bit later in this talk. For now just rejoice that you
can get Safari to respect your language preferences even when they don't
have another way for you to do so. But the reason that Apple actually I
believe at least from the research that they actually took that off was
because of fingerprinting. And now according to the latest Http
specification browser fingerprinting is a set of techniques for identifying a
specific user agent and track that over time using its set of characteristics.

André Ferreira - 22:10
And there are a number of request headers which we'll look into that
might reveal information to servers and that will be sufficiently unique to
enable that fingerprinting to take place. And one of those headers is the
Accept Language header. So I thought that it would be interesting to see
this actually in practice. So what I've done is that I've used tool called
Cover your Trucks. If the slide will move, sorry, I don't want to click too
far.

Dinis Cruz - 22:39
There you go, I can see it.

André Ferreira - 22:42
So I've devised four tests using Cover Your Tracks and one of the I use the
four browsers in their latest version and macOS. And in the first one I used
the regular window and I specified my four language preferences I've
shared before. The second one, I used the private incognito window, and I
kept those as well. And then on the third one, I removed all of the
language preferences. And on the fourth, I use again the private window.
Now, before you say anything, I am aware that the private window is only
supposed to not store information on my website regarding the websites
that I viewed, but I've tried it nonetheless. And if we look at the table and
with the information that we have on the site, according to their website,
33 bits is all that is necessary 33 bits of identifying permission is all that is
necessary to uniquely identifiers in the world.

André Ferreira - 23:32
And the way that the browser characteristics, including the language
preferences or the amount of identifier information that is available for
trackers and for online advertising is very high. In Chrome, Firefox and
Opera, if I have my language settings specified. Now, the same happens on
the private window. But curiously, Opera was giving me a different value
and I went under the hood and I tried to figure out what was going there.
And Opera has decided that in their private window, rather than having
my four language preferences, they reduced that down to one. So in a way,
they actually made it a bit more private. And that explains why it's not
longer a unique fingerprint, but a nearly unique, so it gets a better value.
And then when I removed all of the language preferences, we can see
across all browsers that there is less amount of information available to
being unique identified.

André Ferreira - 24:28
And then I got curious and I was like, I got a security tool here installed on
my computer. I wonder if they will actually make it a bit better. And I run
the tests again and let's see if the image will pop. There you go. So I had
NordVPN. I have no affiliation with it's just a tool that I actually had. And
I enabled thread protection and I run the test again and exactly with the
same parameters, exactly the same browsers, and I got better results.
Now, I run this around 02:00, 03:00 in the morning, and I apologize for
the upper results on when I remove the language preferences, because
those values are not exactly correct. And I'll explain why. The reason
behind that is that I have two screens. I have this one and the one, when I
look to the left, I'm looking at my other screen.

André Ferreira - 25:13
And when you actually have a browser in a different screen, the
characteristics that are shared with that particular tool will be different.
So I believe that 1651 would be probably because I somehow had the
browser on the left side. Not very scientific and accurate to me. I
apologize for that. But nonetheless, the results, we can actually see that
the tool improves a little bit. The ability that trackers will have to
fingerprint us, but that they are still nearly unique. So in summary, if you
decide to specify language preferences, you know that your user engine
can be uniquely identified. While some online trackers may not know your
name, this allows them to have a detailed behavior profile of your online
activity, political affiliations, education level, your income brackets, your
tastes. And this means also that lifting cookies will not help. And perhaps
this is food for thought.

André Ferreira - 26:07
And you're probably thinking of testing this tool yourself and I recommend
that you do so if you have the time. But I have a story to share and I'm
going to move from here, so I'll try to keep you entertained. I had two
questions that I needed answers to and I had ruminated about them for
the best part of two weeks since I had discovered that a book existed. And
during that time I had managed to resist the temptation of getting a copy
as ahead of the priorities and my time and attention needed. It was needed
elsewhere. And not to mention that I have several books here that I've
already purchased and they are still waiting to be read. But I got to a
point that I couldn't resist anymore. I had two questions and those
questions were this moves did Tim and Ted really share a meal?

André Ferreira - 26:56
And did Tim ted tell tim. Did Ted tell Tim? It sounds funny. All this is just
FTP with lipstick. Now, I knew that Tim's parents were both academics
and in computer science. And I knew that Tim has a degree in physics, so I
was more than 100% convinced that he had to be familiar with Dad's
publications. But this was all fresh to me. I hadn't come across this before
and around 1965, if that one will come. There you go. Ted Nelson.
Professor Theodorhome Nelson had written an article or paper, a file
structure for the complex, the changing and the indeterminate policy. Now,
the paper is incredibly interesting and it details his vision of a dream file
and its design. And while I was reading the paper, I would love to know
the professor's opinion about Google Docs revision functionality, because
for me, while I was reading, it was like, yeah, they have this, yeah, they
have this, yeah they have this.

André Ferreira - 28:01
So I don't know if they actually went there and read the paper from the
1960s and achieved all of that or not. I would love to get the professor's
opinion. I thought it was really interesting. But in this paper, the professor
also coined the term hypertext in the mathematical sense of extension. And
you may not be familiar or ever heard of a project called Xanadu that also
started in the 1960s by the same professor. But it was a project that
addressed similar issues that those that Tim Bernersley had to solve in
CERN. In the in a nutshell, both men had the ambition to improve the way
that researchers. Track knowledge. And a lot of it had to do with the way
that references function and references between papers on how to link
them. And to be honest, I don't really recall if I read that paper first or if I
read an interview with the professor where he actually shares that Tim
and Ted had shared a meal and that I was curious to find out if he actually
told Tim that he thought that Http was only FTP with lipstick.

André Ferreira - 29:06
So that stayed with me for two weeks. And then I just got a copy of the
book and the book is Weaving the Web from Professor Tim Bernersley. And
when I came about the FTP with lipstick I was like say what? And I got
really intrigued. So I needed to know more. And when I read the book is
really easy to read and it's very interesting.

Dinis Cruz - 29:34
That's an amazing book, man.

André Ferreira - 29:35
That brings me it's pretty cool.

Dinis Cruz - 29:39
I remember reading that book and really understanding the web and
getting this is going to be massive.

André Ferreira - 29:45
I think the description of all the problems that he had and if you grab
Zenadu and you see when you read the book, it just starts to come
altogether. There's bits like they're really human, it tells a human story.
There's people that own money to some other people. I don't want to spoil
the book to anyone, but the answer towards did they have a lunch? Yes,
they did. But what they ate and who paid for it, you'll have to read the
book as well. The answer is there. And before talking about the Http
protocol because this is a story basically to do an introduction to that
there was a very interesting sentence I thought that professor also has in
the book and it's this one I happen to come along with the time and the
right interest and inclination after our protect and the internet have come
of age that left me was to marry them together.

André Ferreira - 30:42
And I thought this was very honest and I really enjoyed it. So when two
computers agree that they can talk, they have to find a common way to
represent that data so that they can share it. And this is also another
sentence from the book from Tim Bernersley and this is where protocols
come in. And protocols, a protocol is a set of rules and controls in the way
that computers exchange data. And this comes from the Cambridge
Dictionary. But Tim Bernardzini's book also says that the internet is a
network of networks. Its essence though is the standardized protocols, the
conventions by which computers sends data to each other. Now, in the 90s,
this in the early 90s, but before no, sorry, so in the early ninety s the
internet had already evolved from what was called in the past ARPANET
and that was a network developed by the United States Defense
Department and it was controlled by them in collaboration with some
universities.

André Ferreira - 31:41
But then other networks started to appear and those networks didn't
speak to each other. So there was the same type of a complexity that we
had to do with us ASCII of the representation of language or characters in
the screen. The same problem started to exist with networks. And this is
where the IP range of protocol or IP protocol suite comes in, as it will
enable the communication between networks that don't actually speak the
same language. So IP, the characteristic of IP, which is most interesting is
imagine that you want to visit from your browser example if the route is
not always the same. So you'll have to go from your computer to the
provider, your Internet service provider, and then they will know somehow
how to get to example. But even when they know that path, it's like when
you're driving there's other roads to get to the same place and if one of
those roads is interrupted, the protocol knows how to find another path to
get there.

André Ferreira - 32:36
And the TCP on the other hand is a very reliable protocol. If it was human
stocking, it would be a bit like this I would say hi and you'd say hi back
and I would acknowledge that you'd say hi, so I know that you're listening
to me and then we can communicate. And the difference towards UDP is
that in UDP I'll just say something and I don't really know if you listen to
me or not. And that was what enabled the World Wide Web to come into
place. Now, if we look into a better way of actually thinking about this, it's
by using the OSI model. The OSI, I didn't say that correctly. Open systems
intercommunication model. And you have seven different layers. So you
have the application layer, you have the presentation session, transport
network data and physical. And this basically means that from the point
that you want to transmit some information from your browser, the
interface that you're interacting with and you are asking for example, bits
have to be converted into different meanings so that they go from all of
those until they actually get into zeros and ones and get sent throughout
the network.

André Ferreira - 33:43
And this is basically used this table or this model for coordinating the
efforts between systems intercommunications. And it basically describes
what needs to happen and which protocols need to exist. So you get a
packet out through the network. So let's focus in an Http request and it's
composed of three lines of text and the first one, it's called a request line.
And here you can see the Cat method and it's asking for examples.com.
Default resource at port 80, which is implied by the protocol used Http.
And he also informs that he would like to communicate with version 1.1 of
the protocol. And I'd like to prove that to you now, I'm not using a browser
here. Oh wow. It doesn't actually share wait, let me stop here. Or does it?
Then I can't actually see it. Can you see two other windows?

Dinis Cruz - 34:41
Yeah, I can. To text.

André Ferreira - 34:46
Cool. Thank you for that. I can't actually see it here for some reason.
Cool. All right, so I'm using a tool called Curl. I'm not using a browser, but
this will function in the browser exactly the same. In one, I'm calling http
example. In the other, I'm adding a port and I'm specifying the resource
that I want. So this is just to prove that if the first is exactly the same as
the first, but by convention, normally we don't put it there. A caveat,
though, is that sometimes that default resource is not actually index
HTML because you can specify in the server a different one. So sometimes
it's safer just to call the domain if you're after an home page. Let's read it.
That. Now, another part that happens behind the scenes, even with Curl
tool is what that first request line actually what happens.

André Ferreira - 35:38
So when the browser sees that example, it doesn't know its IP because
computers in the network, computers are known by IPS, they're not
known by name. And the browser will try to see if he already knows the IP
address of example. And if he doesn't know it, he will ask the operative
system, hey, do you know the IP of this particular domain? And the
operative system will look in its own cache. And you think about cache as
being a temporary storage of information. And then if it doesn't know it,
you will have to go into the network and ask somebody that knows it. And
that is part of the DNS protocol, which is a bit outside of this talk. But
anyway, there's negotiations to get to the IP so that the request can go
forward. And the reason that this existed, that it alleviates all the
synchronization that needed to exist in our own computer if we needed to
know and keep track of all the changes and all the domain names and
everything that keeps on changing on the Internet.

André Ferreira - 36:34
So that responsibility is delegated. Now, I'll probably mention this first
when we ask for in the example before that, I gave what I actually got
Amazon.com in Portuguese, they have their default page in English. So
different resources may have exactly the same content, and those are
called variants. The reason for that, or better yet, there's a principle that
it's actually mentioned in the book by Professor Tim is that each resource
should have its own unique Uri, that's a Uniform resource locate
Identifier, uniform Resource Identifier. The names changed, and he was
also not happy about that. So bear with me. And in this case, it's example
index HTML, being that the resource is indexhtml. Now, in principle, as
each resource should have its own URL, you don't want to call
Amazon.com and expect that URL Uri not to change, because then the
principle of uniqueness is violated.

André Ferreira - 37:48
And the reason for that is that if you want to be precise into the linking
that you have, you want to refer to the resource exactly as is. Another
example is because this doesn't happen only with language. You can have
a page in HTML, but you can also have it in PDF and those are variants of
each other and they should reference each other, but they should have
different URLs as well and the service should try to accommodate for that.
Now the other two lines here are headers. Let's see if the image changes
and it's not changing. There you go. Cool. So headers are composed of
lines and the line starts with a name, followed by a column file, followed
by a field body. In this case, example, if you look at the host one, and it has
to be terminated with a carriage return or a line feed, but it has to follow
some rules and those rules are actually you know what, I'm going to end
here, but let me finish this bit.

André Ferreira - 38:52
So the names have to follow us ASCII because Heathers use us ASCII,
which is, remember this, seven bits. And it has to have values between 33
and 126, which allows for some verification of the input, is actually
correct. And the body of the header, it follows the same, but also allows
for space and horizontal tabs, but it can break into multiple lines. And this
folding has actually been used for a lot of hacking, not particularly with
the exact language, but it's something that we will see on the second part
of this talk, because I'm going to end it here because I already see that
we're doing this for 58 minutes and yeah, that would be this for today, and
I'll follow up in the next talk. Thank you for your attention. I got a lot of
other slides, guys, so I'm going to stop it here because otherwise it's way
too much.

Dinis Cruz - 39:49
Okay.

André Ferreira - 39:52
Maria, I lost track of time.

Dinis Cruz - 39:58
So it's 44.

André Ferreira - 40:01
Oh, God. But I had 1 hour on my timer here. So if you haven't stopped, I'll
continue then.

Dinis Cruz - 40:10
Yeah, continue for more.

André Ferreira - 40:12
Yeah. All right. Sorry, let me share that. Wait, how do I do this? Wow, this
is pretty slow. Let me just pull that. Bear with me. I'm just trying to get to
the same point that I was here. Okay, I'm not sure whether it's still doing
this, but let's see. Can you see it? Can I see?

Dinis Cruz - 40:58
Yeah, I can see it.

André Ferreira - 40:59
Okay, cool. Let me move on to the next one. So this is an example of some
fields that are sent by Firefox in its latest version in the macOS. And you
can see that the browser is sending information to the server and it's
telling it that he wants to go to a host. In this case, a refrain website. And
it accepts HTML and text application and XML. And he has a strong
preference around it, which is the Q Nine that I'll talk about in a different
slide, and then that it prefers a Viv images or WebP. It also is able to
understand Jzip and deflate PR and it would prefer to receive the
resources in the languages, the order of my preference. And then it
identifies its user agent with a big string that doesn't really represent a
user agent because of fingerprinting in the Mac, that Mac version for
example, they stop changing it because they wanted to stop fingerprinting.

Dinis Cruz - 42:04
That accept language is the one you say that actually creates quite unique
Identifier tracker.

André Ferreira - 42:09
Yeah, as we saw before, if you actually have it as big as mine that will
increase the way that I'm fingerprinting. But the trade off always here is
that I'm going to get exactly what I'm after. So it will be me as a user that
you have the freedom to say I don't really care that you track me or I care,
or only share that with particular websites. Because the problem with the
accept language Heather, is that if you have never visited a website before,
every single resource, and imagine that there's 150 images on the
homepage, all of them are going to get that except header. But in reality
that doesn't help. Well, it would help if the content negotiation was done
for every single image to get a representation in Portuguese. But in most
websites the images are not actually translated, it's mostly the content, the
text, so it becomes a bit wasteful.

André Ferreira - 42:57
But on the other hand, the fact that it's a proactive negotiation, it saves
you from actually having to get a page and then going through the flags
or the drop down and selecting a language so that it's actually faster. But
yeah, as soon as you specify this you'll be further tracked or your
possibilities of tracking you are superior and let's zoom into that. So in the
slide we have exactly the same headers and we can see that the first
language that I have, Ptpt, is actually called a sub tag and it's composed
of languages that are request for comments that specify what those values
are. And there's also ayana registry that keeps track of all of the ones that
are registered so that you can actually use. So validation can actually be
achieved against that registry. And let me actually read the slides here
some recipients treat okay, so regarding the order of the languages as I
have it, you might notice that Ptpt and then PT actually have a quality
value of nine because that's what it means.

André Ferreira - 44:05
And if I had other languages that had that nine, that had some bugs in,
some have had some bugs in the past where this actually existed and
passed and crashed the server. But the composition is pretty much detailed
on the specification and there are requests for comments in all of them.
There are some caveats that the forward slash privateusing grandfather
uses, not something that I personally, with my experience, I've ever seen
used, but I have not. The maximum that I had to work with was 16
languages in a single website. I never had more than that and I didn't
work in word processing or language more intensive type of applications. I
don't work in the operative system level so I'm guessing those would
actually be used there. And when you don't actually specify a quality level
so for example, you only say, I want English, then that pretty much means
that, yeah, the quality value is one.

André Ferreira - 45:07
And that breaks down to more or less something like this with the values
on the table on the left side being the specific values that I've specified
when I actually put them in order in my preferences. Now some of the
advantages of this proactive content negotiation is that it avoids the
communication to go back and forth and the server does not need to
describe how it's actually going to look at your preferences and how it's
actually going to make the choice. So the fact that I have Portuguese
specified does not mean I'm going to get a Portuguese page. If there is one
that is in French and English is also not available, they will serve that how
that happens is transparent for the client. It's logic that sits with the
server. However, the disadvantage, one of those that I've already
mentioned is that it's a bit wasteful making it a bit inefficient and there's
risk for privacy though that fingerprinting that we've discussed, it's a
matter of choice.

André Ferreira - 46:06
You'll have to decide exactly if that nearly unique fingerprint does not
actually mean unique fingerprint and you're tracked either way and you
rather get consume content the way that you want to consume. There has
been a lot of abuse with the language except feather and these are some of
the cases. There are CVEs that are open so you can actually send
something even bigger than mine. You can specify there's a limit but it's
not in the specification of 8000 bytes if I'm not mistaken, on this total size
of the Accept header. And in the first versions of Http that used to be sent
in as plain text, it became binary from Http two. So that actually meant
that anyone on the network, if you have a man in the middle, somebody
that is listening and wiretapping your connection, they actually get access
to all of those language preferences.

André Ferreira - 47:01
But then again, if they are wiretapping you, they pretty much know who
you are because otherwise they wouldn't be wiretapping you with
language preferences, you'll be sharing that and if you sent in very large
ones that would crash some servers. And the CV is that if you want to
verify it, then there was a way to craft some packages, some values that it
would create a loop on the server. You started thinking and when I saw
this one. I thought it was interesting because the details of the CV don't
actually specify exactly how this happens. But if you look at the way that
it is composed and if you start looking at the string and you want to
explode it by, say, the semicolon and if you set because we are abusing now
the accept language header. And all the values that you have is semicolons
and the computer is also parsing that you're basically consuming time and
that slows down the server.

André Ferreira - 47:54
If you send a ton of those you could pretty much crash the server as well.
There was also bugs where if you don't actually send any language the
system would crash in. Others that I found very interesting is if you
actually specify JavaScript as your Accept Language value, that will also
cause problems in the server others that you can also think about. So if
I'm requesting a page in Portuguese and there's one in English, and the
logic on the server side would be grab parse that string, grab the piece in
English and grab a file from the folder that is called English. That would
allow for path transversal. And I could actually say get me the etc
password file by just specifying that in the HTML in the Accept language
header. It's just a way to exploit it. Or you could also include other files
and get them displayed to you and SQL injections that you mentioned
before, they were also available there because now the server side could
actually have the languages in a database and they could do a select web
page where equals English and then it allows for SQL to be abused.

André Ferreira - 49:04
Now I'm very upset with this slide because at this point I actually wanted
to use Stride for it but I didn't get a chance and I was actually thinking
that I would manage to get to this slide today, hence the part two. But
there's a lot of things that can go wrong, and this is a big list, and I got
that one from Chat GPT, to be honest, of all of the things that can go
wrong with language. Feather and to be honest, also during my career, I
saw a lot of those and I had to deal with them and learn from all of that
experience. Now one way that we can protect service is with a tool like the
Osmot Security core rule set and when I had a look under the hood, I
actually didn't find in mod security a specific rule set to parse the Http
except language.

André Ferreira - 49:51
So I reached out to Dr. Christian on Twitter and he assured me that it
follows the standard rules applied for all of the headers. So there is
protection there. But the caveat is of course that WAFs are not application
dependent, meaning that you would still be able to craft a particular
packet, particular header in a particular way that will pass the web
application firewall and cause some damage on the server side and that's
it. Thank you for your attention. Actually managed to pass most of the
things. So I cut a lot of slides because I had more slides and I went to the
detail of specifying the differences in Http versions because now we are at
version three and there are things that are relevant, but I think that I can
do that in a different opportunity at another time.

Dinis Cruz - 50:46
Very cool. I think it's definitely one of the areas that is going to keep
showing up. And it's a good example of something that especially the
fingerprinting, I thought was really interesting. And you could see there's
so much data in there, so many independent points, that you can see how
that can then be used to actually fingerprint specifically the users right.
And how it falls to the radar on some of the detections. How more and
more you have these anonymization services which I think is already cool.
Very interesting to see how they handle that and how they proxy and they
rewrite some of those headers to try to protect you but then if they don't
allow it, then you still are highly traceable.

André Ferreira - 51:39
I got to tell you that there's one extension that you can install in the
browser that is really well known and apparently heavily used that doesn't
do a good job and actually calls home. I'm not going to name it. And that
when I actually came across the local overrides. I never thought of using it
that way. I actually thought, okay, this is something that is worth sharing
also because you can do exactly what you were talking about. So you can
have the security tool but you have to trust them or you can do it yourself.
Now the caveat there is that if you're going to do it yourself, it's going to
be a lot of work and it's going to be a lot easier for sure to do it for you.
But it's like if you're a power user you can, you don't have to delegate that
and potentially have to trust, have to share.

André Ferreira - 52:21
But yeah, it was very interesting to me to also find that information, the
changes and the experiments that and I'll mention it still. So Google, this
talk came because Google I found out that they were doing some work
changing that the way that this proactive negotiation happens and we
could make it even more efficient if I actually sent it only a header, right, a
head request. If I send a head request with my language preferences and I
don't send anything else and I get the head response back, then that
negotiation can happen at that level. But I could also make it different. I
could send a head request and the server would tell me all the languages
that he has available. I lose no privacy and I select one of them. That can
still happen. The content language can come when I get all of the index
page, but that index page can have 200 Http requests, like images, videos,
whatever, and that makes it inefficient, but the privacy of the user would
be retained.

André Ferreira - 53:21
And I started asking myself, where does that not happen? And we have
tools like Google Analytics that do a lot of tracking to improve the user
experience and so that you can improve your products as well online. And
when you specify your language preferences, those get available in
JavaScript. So if you go into the console and you type navigator
languages, if I'm not mistaken, you will also get access to all the list of
your languages preferences. So that basically will go away. And it's not all
about tracking, it's not all about evil, it's also about people being able to
improve the website stores to serve their customers better.

Dinis Cruz - 54:02
But we already have something that happens a little bit, because if you
think about it, you already have the special kind of security. You already
have the initial Get request that you can use to get a policy. You already
have the first options that actually can give you that. So there's a lot of
things that there's places where we can put that, and I agree, we will
make it because that actually goes with every request. And you might
argue that maybe that's not the best case. Cool.

André Ferreira - 54:28
Cash up. That's it exactly right.

Dinis Cruz - 54:31
Good stuff. All right, thanks for doing the session. Let's definitely do a
variation. I would like to see if we can explore it now to the idea of
adaptive content, which I think is coming to the web where you start to
dynamically create content and you're going to need to start providing
more information about who the user is. It's almost like we get to the
point where we're going to start prompting sending prompts to the server
to provide better information and that has another instant kind of worms
thread modeling. That one brilliant, man. Thanks for this, Jeff.

André Ferreira - 55:04
Thanks for having me.
