---
title        : Threat Modeling Kata Part 3
track        : Threat Modeling
project      : Threat Modeling
type         : working-session
topics       : Serverless architecture, threat model
featured     :
event        : mini-summit
when_year    : 2023
when_month   : Oct
when_day     : Thu
when_time    : WS-15-16
hey_summit   : https://www.linkedin.com/events/7110646330049359872
banner       : https://github.com/OpenSecuritySummit/oss-website/blob/main/content/sessions/2023/mini-summits/Oct/banners/threat%20medling%20kata3.jpg?raw=true


#status      : 
description  : Starting a threat model can be challenging if you have never done it or if you face new technologies. Practice helps you understand how to improve your threat modeling skills. A Kata refers to a common practice in martial arts to practice choreographed movements to memorize and perfection them. Join this session to flex your threat modeling muscles on a serverless application for managing an online bookstore.
organizers   :
    - Luis Servin
    
youtube_link : https://youtu.be/hvDK7DXkJp4
zoom_link    : https://us06web.zoom.us/meeting/register/tZEud-uuqTMsHteI35A24ntllhP4AdzGekzO
session_slides:
---

## Transcript:
Dinis Cruz - 00:00
You.

Luis Servin - 00:02
Hi.

Dinis Cruz - 00:03
Welcome to this open Security Summit in October 2023. And we have
Lewis for the part three or Thread Modeling Qatar, which is a really
amazing concept that a lot of people should be following because it's all
about practicing, trying these things and getting a lot of amazing
momentum. So, Louis, over to you.

Luis Servin - 00:24
Thank you very much, Denis. So this is Louis Servin. I'm an application
security expert, have been working in this area of knowledge for a long
time now, over ten years, 15 years almost. Yeah, probably more 15 than
ten. I have been doing threat models for such a long time. Oh, I should
change the title. Sorry for that. I promise not to. Okay, wait, it's just a title
that I need to change. So again, I have been in threat modeling since two
thousand and ten s. I have been threat modeling many different systems as
a consultant, as an in house expert across different fields.

Luis Servin - 01:12
I worked for a long time for an automotive company, and I had the
pleasure of being the first person to create a security assessment, a threat
model of factory shop floor look at automotive systems, bridge over
knowledge for threat modeling from it into the automotive domain. But
we're not discussing that. So that's just a bit of background. What we're
discussing is threat modeling. And because the topic of this session or this
round of the Security Summit was serverless architectures, I decided to,
hey, let's do a serverless architecture threat model. Why not? And as I was
preparing this, and I had already chosen the case and I was doing
everything, I had a very interesting conversation with Dennis yesterday on
a panel were sharing, discussing how to enhance our threat modeling
capabilities through something like Chat GPT.

Luis Servin - 02:14
So I took the bait and I decided to try to do some threat modeling on a
serverless architecture and enhance my superpowers or my abilities. No,
superpowers enhance my ability to become a superpower by using Chat
GPT. So I hope Chat GPT doesn't make me look like a fool. I did try a very
simple rudimentary prompt, but I want to have the real prompt with you.
But first of all, let's discuss what we're doing. So feel free to interject with
a comment or something. I'll try to keep them open. Let me see, how can I
open the comments? Chat here. So if you have any questions, drop a
question into the chat and I'll make sure to answer as fast as I can. All
right.

Luis Servin - 03:15
So threat modeling, I like Brooke Schoenfield's definition the most, is a
technique to identify attacks a system must resist and defenses that will
bring it to a desired defensive state. So no chances. Based on business
value, we defend more, we defend less. And I chose the title of Kata based
on this martial arts practice of performing a set of choreographed
movements. If you ever took karate, for example, katas are part of your
examination to move from one belt to the other. And the higher up you go
in the rank, the more complex the movements are. And catas give you a
way to perfect or construct this so called muscle memory. So I'm not
inventing the term of CATA for doing technical work. Actually there's a lot
of previous work.

Luis Servin - 04:17
I like to take the architectural catas from Neil Ford and I think he took
the concept from someone doing development catas as well. So I could say
at least ten years of catas as a concept for It systems. So I could advise
you to look into that if you want to test or flex your engineering muscles.
Was I showing the right presentation? So kata. Is this symbol from
Japanese? It could be actually two symbols and it means form. Okay, let's
move to the next one threat modeling, just in case no one knows about it
or someone doesn't know about it, is basically a four step process. The
first one being understanding what we're building, modeling the system,
the second analyzing the threats, identifying what could go wrong.

Luis Servin - 05:14
And the most important step is actually the third one, which is mitigation
the requirements, the things that need to be added on top to solve the
threats that we identified or the vulnerabilities and threats. So one
common concept that we see is difficult for many people is to differentiate
between a vulnerability and a threat. And I would like to use the
opportunity to say a vulnerability is a characteristic of the system. It's
perhaps a negative characteristic, but it's something that belongs to the
system. And a threat vector, an attack is something that exploits this
vulnerability for malicious purposes. And cross site scripting is an attack
vector, not a vulnerability. Just out of principle, it's an attack technique.
The vulnerability is taking input from an untrusted source and presenting
it to the user where it can be interpreted as code.

Luis Servin - 06:15
And the fourth step, which is validating the outcome, so is the
architecture. Is my understanding of the model in step one correct? Are
the threats I identified and the vulnerabilities present and reachable? Is
the mitigation correct, complete or should I add more or take some? And
for this session I took a system from a Tweet. So someone was let me see
if I can find the Tweet. Give me 1 second to see if I have I had it open. Let
me see if I have the Tweet here. Yeah, I have it here.

Dinis Cruz - 07:01
Can you just quickly paste that content in the chat?

Luis Servin - 07:05
Of course I can. So I will put it in the slides as fantastic. Yes, it's there in
the chat. Of course. So I took from Raul Hunko this definition of a Qatar.
So he's giving a Qatar for development and he's saying OK, I need a
system to manage books. And he goes on to describe it and it looks very
simple like that. So basically I took his definition and made a couple of
slides just to have it more present. So what are we building? What is our
target of analysis? It's a bookshop. The bookshop will have books, we'll
have customers, we'll have orders and payments. Not too difficult. Only
authenticated users can make orders. A customer can have many orders,
an order can have many order items. An order has one payment, an order
item is one book. Easy peasy, right?

Luis Servin - 08:10
Now, connection to the database he says use an entity framework or
Hibernate. Let's say we use Java, we use Hibernate to connect to the
database and map code entities, code classes to tables. So we delegated
that and Hibernate will manage the database connections and we will
create some rest endpoints. So we have getbooks to get all books
PostBooks to add a new book which is only accessible to the admin. Delete
books and a book ID to delete a book by its ID and it's the admin get
orders, get all orders. It's something only the admin can do. Post orders is
create a new order, get orders with an order ID is to retrieve a specific
order.

Luis Servin - 09:04
So as a customer I can look at my order and see which books were
included in the order and I can post a payment process a payment for an
order. So that's what we've got. And now we say okay, we have an
authentication using JSON web tokens which means there is an identity
provider which will allow my customers and my administrators to log in,
identify themselves, gain a token to authorize themselves to make calls to
the backend system. He says configure serilog. I have no idea what Serilog
is, but I will say configure log for J in Java for logging and logs need to be
managed by Azure's AWS log management service and there will be unit
tests to test that the endpoints are working and integration tests and that's
about it. I mean, we can look into the database and all that.

Luis Servin - 10:11
So the point here to start is and the first challenge always is where do I
start? So do I jump right into the details or do I want to spend some time
looking at the database or at the case in order? And do I have all actors
represented in this solution? So what I usually do, let me stop sharing my
screen and share my well, I can share it here, so I have to work over there.
So let me share my GitHub. If you want to follow along what I will be
doing, you can follow on GitHub give me just 1 second to add the link
here, let me post it on the chat. So on GitHub LF serving OSS Threat
Modeling just lost the chat window. Where's the chat window? There's the
chat window.

Luis Servin - 11:49
So if you go to this GitHub you will find so let me put it on the slides to
make sure that everyone has it.

Dinis Cruz - 12:02
Yeah, we're only seeing your slide.

Luis Servin - 12:03
Yeah, you're still seeing my slide or not?

Dinis Cruz - 12:07
Yeah, we only seen the slide. Let's stop here.

Luis Servin - 12:10
All right, give me a second. I thought you were seeing my so let me add
one slide files. So that's the repository where you can find the exercise
we'll be doing so you can clone it. Let me share my screen then. Not just
the file. So share the whole screen. Share. Now I will put my Vs codes on
the screen. Can you see my Vs codes?

Dinis Cruz - 13:03
You can?

Luis Servin - 13:06
Was that a yes or a no?

Dinis Cruz - 13:07
Yeah, you can. All right, perfect.

Luis Servin - 13:11
Yes. So I started creating a very high level diagram in which we have a
customer, an API, and then let's make the database. So I create there are
instructions on the repository to use this JSON file that generates these
handy functions I am using. So you can use it. I will create one without
images to simplify development. So this is my DB and this is my database.
It's RDS postgresQL. And here we store and serve book and customer
data. So basically, what I'm using is the graph language to create graphs,
graphical representations of graphs. These elements you see here are
called like in any graph nodes. And the links between the nodes are called
edges. So basically what will happen is that I have also HTML.

Luis Servin - 14:38
I could enhance this with the images from AWS, but I don't want to spend
time finding out the image. So I'll do them without images. Cognito this is
my identity provider and this is let mistake, provides pardon? I couldn't
hear you. Well.

Dinis Cruz - 15:22
Just.

Luis Servin - 15:27
So I'm just trying to model so what I'm doing is I'm trying to model the
system as it was described. So I'll go back. So the first step in thread
modeling is understand the system. So model the system. So what we have
is the user, right? The customer, not the user. Sorry. So I have.

Dinis Cruz - 15:53
You pushed.

Luis Servin - 15:58
I'm developing as we speak, right? So the repository I mentioned has the
exercises from the previous iterations and has the base file to create these
images. And as we speak, I am updating the file. So this is not yet
committed. I can commit it right away so that everyone can have it. And
then from there we can start working together if you want. So give me 1
second to commit the code. I'll commit it right away. Customer talks to
cognito label equals. So this is provide username password. This goes over
Https and that's it, right? So I will receive provide username and password
so we can see that the customer is as I type, the image changes. So I have
the first relationship, provide username and password.

Luis Servin - 17:10
Now I can as a customer talk to the API and I can say label equals make
requests. And this is all again protected with Https and JSON web token.
So here we have an initial representation of the system in which we have
the customer talking to the API, the customer talking to Cognito to get the
identity. Now, this doesn't seem complete, right? There is something
missing here. I don't usually talk to an API, do I? So in order to be able to
talk to the API, I need to talk to something else that gives me the access to
the API, which sends me to Cognito to authenticate. So let's say I have a
single page application somewhere. Spa. No, not shape. Spa is my single
page application. It's react JavaScript, and this provides the UI for the
user.

Luis Servin - 18:52
So I have a single pledge application, provides a UI for the user. And
obviously, the customer needs to talk to the spa label equals get the UI.
And this is over Https, but it's not secured with JSON web token because
this is basically me going to Amazon and reaching the page before
authentication. Right. The single page application will be the one running
on my browser, which will redirect me to Cognito to authenticate if I need
to authenticate for buying a book. And then at some point, something has
to talk to the database. So the API will be talking to the database, and the
API will be talking to the database label equals, let's say, get write data.
It's unencrypted and admin user password. So that's how we're connected
with admin user and password.

Luis Servin - 20:21
I'm obviously creating a vulnerability on purpose so that we can find
something easily, right? And this is a very high level view of what could go
wrong. Now, there is something missing here. What is missing? So I can
make orders. How are books getting into this thing? So I need an admin
user, right? So now I have an admin user, or I need an admin user. So I'll
just copy the customer and paint it in a different color to make a
difference between or maybe not yet paint it in a different color. But let's
say customer. Now it's not the customer, but my admin. And now I say
admin. Admin is a person internal to the company bookstore admin. The
bookstore admin has the function of updating. So let me zoom in so that
it's visible what I'm doing.

Luis Servin - 21:47
Updating catalogs, or rather than updating updates. That just updates
catalogs, checks, orders. And what else was this person supposed to be
doing? So this person was also supposed to be doing adding books. So
managing books, deleting books, posting and deleting books, getting
orders. Those are the three specific functions. So let's see. Update the
book catalog, update book catalog, delete book and checks customer
orders. But there was something else missing, right? So what am I
missing? So I have get books, post books, delete books, get orders, post
orders from the customer, get orders. I'm missing the payment. Post
payment. So I need to add a payment provider. Now, this is an
architectural decision that's hard to undo. I can choose to do payment
transactions myself, or I can choose to use something like Stripe.

Luis Servin - 23:19
In my case, I could use a payment provider not to bother with credit card
data. So in this case, I will take a system outside of Amazon, say HTML
out, so I make it gray to make it visible that it's out of scope. I will not
analyze the gray stuff. I don't care about the gray stuff. I care about how I
integrate with them, of course, but not how they do the business. It's a
different process, vendor requirement, security, whatever, but not in scope
for the threat model. So I could say stripe. Stripe. Come on, stripe. It's a
payment provider. I could think of it as a SaaS, as a software, as a service,
and it manages payments with credit card returns, a transaction ID. All
right, so I have the things that I need to be able to operate now.

Luis Servin - 25:04
I need to mix them. So I need my API to talk to Stripe and it will send
vendor ID, send. What else will I send to it from the API so we can see the
line gets generated automatically. I don't have to generate it myself. API
sends the vendor ID, what else does it do? It sends the vendor ID and the
amount. Sends a vendor ID and the amount this is an Https connection
with an API key. At least that's how in my mind it works. I have no idea
exactly how Stripe works, but I am assuming here that Stripe works this
way. Now I have a high level context diagram. I still need to put my admin
to talk to my API. And here I will use this label and this label will allow me
to manifest the intention of the connection.

Luis Servin - 26:43
So let's say the admin updates book catalog and checks orders and this
connection is done over HTPs with adjacent web token as the
authentication method. So as you can see, the diagram grows as I type the
diagram, updates as I need it to update. So I don't bother myself with
creating it in a visual way and moving things around for the reason that
it's a lot easier to have a bit of text, which I can keep in version control,
which control the creation of this file, but I can diff them. I can do a lot of
things that make life a lot easier. So I can help readability by providing a
tab here and making everyone basically use the same length. And it's a bit
easier to see the relationships here, but that's just a basic readability
linting thing.

Luis Servin - 28:05
And the diagram is relatively simple, so there's no need to do a lot of work
to understand it and we capture the whole scenario. Now, what are things
that I could worry about? I could worry about injection, I could worry
about many things. Now we can also say, well, this will be hosted in AWS.
This will be made up of lambdas. Every API endpoint is a lambda. And I'm
not sure if you know Daniel Misler. So let me put on the chat the link to
Daniel Misler's page, 1 second. So there we have it. The other browser 1
second. I'm posting it in the chat. There's the chat. So here we have the
link, and for simplicity, I have summarized what he says on how to use AI,
how to shape or what he calls prompt engineering. So he has a seven step
process.

Luis Servin - 29:44
Let me put it over here. Come on. Thank you, so helpful. But I don't need
all your help. One out. So basically he says, okay, tell chat GPT who you
are, tell the system what format it will produce, give it the task, give the
steps, tell it exactly how you want the output to look for, show it one to
five examples of ideal output and tell it what to include or not include. So I
was preparing this session by creating this step. So basically what we're
saying is you're an application security expert, threat modeling a system.
You will identify possible vulnerabilities threats in which the vulnerability
can be exploited and propose one or several countermeasures to avoid the
vulnerability or prevent or detect the malicious action.

Luis Servin - 30:49
The output will be marked on table with the following fields ID
component, Actor, Vulnerability, Threat Scenario and countermeasures.
The system is hosted in AWS. The code is managed in GitHub. GitHub
actions push the software into production. The system is a single page
application on the front end. The system consists of a single page
application which the user downloads. The single page application written
in react interacts with the rest API calls in JSON users redirected
authenticated. The single page application is stored in an S three pocket.
Requests are first landing in cloud front, then on the S three pocket we use
Cognito as the identity provider and we can do identity federation with
Google, Facebook, Office and LinkedIn so that our customers can log in
more easily. And on the cloud side, we are fronting our API with AWS's API
gateway.

Luis Servin - 31:55
Here the JSON web token will be checked and everything will be
forwarded to a lambda. The lambda is written in Java or Dell. Lambdas
plural are written in Java. They interact with the database using the
Hibernate framework RDS postgres instance is the database using what I
told you, the database admin to connect to it. We can add to that over an
unencrypted connection. The password is configured as an environment
variable in the lambda function. The connection is not oh, I already had it.
Okay, well, I can't get it. The connection is not configured to be encrypted,
so we can remove that one.

Dinis Cruz - 32:43
This is a great prompt, man. You have to share it. It's really cool.
Especially if we can abstract just a bit right. And just have the bit where I
fill this bit here.

Luis Servin - 32:51
Well, I'm following the recipe from Daniel, right?

Dinis Cruz - 32:55
I know, I know. But it's a good practice.

Luis Servin - 32:59
Let's see what comes out. So I just finished typing this thing. I have no
idea what will come out of it. So I hope Chat GPT can run it. And if not,
are you using your paid account?

Dinis Cruz - 33:12
Are you using four or 3.5?

Luis Servin - 33:14
The free one.

Dinis Cruz - 33:16
Okay, so then also put that on the Chat. Then I'll run it on or push it to
GitHub and I'll run it on four.

Luis Servin - 33:21
All right, let's see that. So I'll commit this to GitHub as well. The
application has these user groups. So we have a customer which is
external, an admin which is internal logging. We use log for J to produce
logs. Logs are captured and logs are captured and stored. Log entries are
used for monitoring and debugging purposes. We can say they're captured
and stored in an S three pocket, so disconnected from a lock processing
mechanism. So I'm introducing avalibility into the system to see if it's cut.

Dinis Cruz - 34:12
But can you see how cool it is, what you're doing right now? You are
describing the system, right?

Luis Servin - 34:17
I am. I mean, it's the same thing we already had, right?

Dinis Cruz - 34:20
I know, but it's very different because in the past, remember, even the case
were talking yesterday, what would happen is you would spend some time
with the engineers, with the developers, with the architects, and you would
have this in your head, but you had no place to capture it or persuade.
There was no place that you would capture that you get a good reward
from it, so you probably wouldn't capture it. Where now what you can do
with this is you can write this, and even if it's going to the Dev team and
architects going, hey, is this correct? There's already a lot of value in it
because we already started to map the things. And then you apply the
security analysis on it, but you could also apply performance analysis.

Dinis Cruz - 34:52
You could also say, hey, find me usability problems, find me bottlenecks,
find me disaster recovery problems, find me performance. And let's say
fecal points of failure on the architecture from a resilience point of view.
So there's a lot of interesting other questions you can ask, not just the
security ones.

Luis Servin - 35:12
All right, sure, definitely. I agree with you. There's a lot of value here,
right? So I'm just kind of creating my prompt. So let's see, I have created
the persona, I have asked for the format, I have given task, I have given
the steps well, I have given the description of the system. I have told it how
I want it. Now it tells me it wants five examples or one to five examples.
So let's create one example. Okay, let's say again the output must be a
markdown table and skip the preamble I don't want it to blah, blah. Skip
the preamble. The ID field is a counter used to uniquely identify the fields,
vulnerabilities and scenarios. This is an example. So that means I could
create something that looks like this. I said I want ID. I want the
vulnerability.

Luis Servin - 36:54
I just mentioned it here. Oh, the component actor, of course, to know
where the vulnerability is present. So let's copy that thing and put it here,
the ID, control V, the component actor, the vulnerability, the threat
scenario, and the countermeasures. Now I say one, two, 3123-451-2345.
This is a markdown table.

Dinis Cruz - 37:34
You don't need to provide that. He's going to do it automatically. Don't
worry about it.

Luis Servin - 37:37
Pardon?

Dinis Cruz - 37:38
He's going to do the table automatically. You don't need to do that.

Luis Servin - 37:41
I know, but I'm following his recipe in which he says, give it an example of
ideal output.

Dinis Cruz - 37:46
Right.

Luis Servin - 37:46
So I'm going to create a very good credible attack vector to have it. So I
would say API, insufficient sufficient authorization checks. An attacker
abuses the lack of sufficient authorization to elevate his rights to admin
and reduce the price of an item. Countermeasures ensure authorization
checks are done at the API gateway and individual function. I'm just
quoting the ASBs by heart.

Dinis Cruz - 39:02
Yeah. The other thing we could have done eventually this is we could also
feed it a large chunk of the mean. We could also say here's all of the SVS
or the SVS that is relevant to this part. Then pick the ones that, in a way,
are relevant.

Luis Servin - 39:22
All right. So I have all of this. Now I will copy paste it into GitHub so that
Dennis can run it in parallel. So give me 1 second to put it in GitHub. So,
Dennis, here you are. So let me add the file. Explorer OSS Threat Model.

Dinis Cruz - 39:43
You're going to put that on the main branch or you're going to put.

Luis Servin - 39:45
It no, on the bookstore kata. So I have not committed yet. I will commit
everything right now.

Dinis Cruz - 39:51
Okay. Yeah. So that branch is not there. Right? So you're going to put it
up.

Luis Servin - 39:54
It'S not yet there. Yeah, exactly.

Dinis Cruz - 39:55
Cool. All right.

Luis Servin - 39:56
Good stuff. Prompt markdown. Oh, God. What did it do? What didn't it
copy the thing? All right, try again. Feel better. Control v okay? Not again.
Let me see if I can tweak it somehow. Better copy paste. Okay. I have no
idea how to copy paste it. Then I can try to put it into okay, let's see.
Control. C I'll put it into chat GPT. So here's chat GPT. I have a new
session on Chat GPT 3.5. Let's see if I can put it here. There it is. So now I
can select it from here. Post it there. Now it worked. So that means I can
now commit and paste. So give me 1 second to commit and paste. Okay, I
think I have too many things, so give me one instant to move this to the
other side.

Luis Servin - 41:35
So I will add this into the.

Dinis Cruz - 41:38
By the way, what's really brilliant about Louis, what you're doing here is I
think you're really capturing. I would call the essence of threat modeling
because I think a lot of people go, oh, threat modeling is know, it's
complicated stuff and all. Like no, like literally, this is almost the state of
the art of threat modeling. Right. We're still figuring out we're still
mapping the things, and then we're connecting the dots. Right. So this is
exactly what happens in the real world.

Luis Servin - 42:01
Yes. It shouldn't be hard, right? It has something. Yeah, it has very few
things. I could have expected a lot more. It gives me a starting point.
Right. So insecure storage and attacker gains unauthorized access to the
S Three pockets, storing the single pitch application tampering or data
theft. Implement proper s. Three pocket Controls versioning. Not bad. I
mean, easy pick. Identity provider, identity spoofing impersonate forging
authentication tokens or weaknesses. Enforce MFA. Not bad. Regularly
audit and rotate secret keys. Monitor and log authentication events for
suspicious activities.

Dinis Cruz - 42:55
Hey.

Luis Servin - 42:56
Fantastic. So far, so good. An attacker provides a forged or exponent.

Dinis Cruz - 43:00
Have you uploaded the code to your thingy?

Luis Servin - 43:03
Pardon? No.

Dinis Cruz - 43:07
Just do it quickly because then.

Luis Servin - 43:08
I was just too eager. But I'll do it right away. I was just having so much
fun. Give me 1 second to do it. So it add bookstore, qatar. All right, I have
it. Kit, omit, book push, no trouble. So you could pull now if you want.

Dinis Cruz - 44:13
Okay, well, I'm going to grab it just directly from the website.

Luis Servin - 44:20
So let's see. API, insufficient. JSON web token validation.

Dinis Cruz - 44:25
Oh, so you uploaded to Mania.

Luis Servin - 44:29
I uploaded to Mania. I just had a branch. Not a branch, but a directory for
bookstore. I'm developing it myself so I don't have to do a lot of
complicated stuff here in the and it's all text file, so it's not too bad.
Nothing will break if I corrupt my own repo. Let me export the file. 1
second.

Dinis Cruz - 44:55
No, I got it. It's already generating.

Luis Servin - 44:58
All right. I don't know if you can create a link or make a pull request to
see the output. So I'll just basically I can share my screen or you can share
your screen. Even better.

Dinis Cruz - 45:11
Yeah. So I'll share my screen. You got those. You got nine. All right, let me
share my screen. Okay, so where's mine? Sorry, I was trying to find and
what I'll also do is I'll show you some of the tricks. Okay? So you should
be able to see my screen. Chat GBT.

Luis Servin - 45:41
Yes.

Dinis Cruz - 45:42
Cool. So you got application system experts. You got this, right? So API
endpoints. So they go look. So look. Lambda database vulnerabilities,
admin accounts, and encrypted DB connection. Right. So these results
better.

Luis Servin - 45:56
That one was not found by this one.

Dinis Cruz - 45:57
Yeah. So you should be interested to compare both, right? Because. This
should be a little bit better, right. In these kind of things, four has a lot
more better context and understanding. So, look, use im roles for
accessing the database. Single page application, expose the blue token.
That's quite good. There you go. So we give a token look, HTP only. That's
quite good measures, right? Cognitive control over Google. So API,
gateway rate limitation, the nail of service, GitHub.

Luis Servin - 46:35
Oh, you have more things because you have GitHub actions. I didn't get
any.

Dinis Cruz - 46:38
Yeah. Access to git repository. So there's two ways you can tackle this. So
I'll show you a couple of tricks, right? Lambda, environment variables,
API, endpoints logs in S three testing CI pipeline, APIs communication.
Right. Where was that vulnerability that we put in? That was by default
that you put.

Luis Servin - 46:59
Unencrypted, unencrypted communication between the lambda and the
database. And were using admin database connection between the lambda
and the database.

Dinis Cruz - 47:13
Yeah.

Luis Servin - 47:14
And that wasn't found. Right. So it does help you get the low hanging
fruits.

Dinis Cruz - 47:22
Yeah. But for example, what you can do for here, so we could say, great,
can you focus on the connection between what was it with the two
elements?

Luis Servin - 47:32
Between the lambda and the database.

Dinis Cruz - 47:34
Between the lambda and the database. Right. So let's see. There you go.
See? So one of the things that is really worth doing is going bit by bit. So
now I picked it up, right? See, lambda to RDS connection, unencrypted
connection there in transit could be intercepted by an attacker encryption.
You seeing that?

Luis Servin - 48:06
I see it. I mean, that's the last step in the recipe from Daniel, right? So
that's why I like Daniel's recipe so much, because it gives you a very good
way to create a prompt and then a very good way to tweak the output.
Which is exactly what he's saying.

Dinis Cruz - 48:22
Right?

Luis Servin - 48:22
Tweak the output. Focus it on where you want to focus. So it gave us a
very good first pass with ten findings on something. But then we can start
focusing on the API, we can start focusing on the S three buckets on the
log collection or lack of log collection, et cetera.

Dinis Cruz - 48:38
So there's two ways you can do this, right? You can keep improving the
prompt here. One gotcha, which is a hack, is that remember that there's
still a limitation on the prompt size. So eventually, if you keep doing this,
you'll notice that the chattypt will start to lose data because the prompt
size is always the same. Right. So one trick that you can do is you can edit
this one here. See what I mean? So I'm going to edit this guy and I'm
going to say so, for example, you have countermeasures. I could also go,
let's say I'm going to go risk level probability, right? Actually, see, I don't
even need to do that, right? I could also go can you also add to the table
above? Risk level probability attack agent and let's say impact, right, to
business.

Dinis Cruz - 49:47
So what's cool about this, right, is that now it should create a wider table,
right? So you could see that expand the table. So increase that. See, look,
there you go. See what's doing?

Luis Servin - 50:06
I know, looks nice.

Dinis Cruz - 50:12
And then the thing about this, right?

Luis Servin - 50:14
No, the question here is, okay, you have a probability medium, but a high
level risk to understand the likelihood of occurrence, right? Because risk is
a vector. So it works two numbers, right? An X and a Y. So we have the
probabilities, the Y, but we are missing the X.

Dinis Cruz - 50:36
We do. But I always say that depends on the attack agent, right, or the
attack based the attacker. Right? Because whether you have that attacker
or not, because if you don't have internal attackers, then the probability of
some of that stuff is happening is quite low, right? Like, for example, this
one, not between.

Luis Servin - 50:57
The Lambda and the database, right?

Dinis Cruz - 50:58
Well, between the Lambda database, if you don't have internal attackers,
it's going to.

Luis Servin - 51:04
Have here a high attacker, right?

Dinis Cruz - 51:06
Well, the risk is high. For example, for that one, the Lambda database. By
the way, I have a trick. So I created a little let me share my screen again. I
have a little JavaScript which I'll share with you, right? But that basically
allows me to do this. Can you see that? So I have a little script that just
makes GBT bigger because it's really annoying that it's quite limited,
right? I have a little JavaScript that I can run on a page that hacks the UI,
right, and see how nice this is.

Luis Servin - 51:49
I know, yeah.

Dinis Cruz - 51:51
So you can see. So in that example, you got the Lambda database, right?
Yeah. It's high, but it's because you have external attackers inside a threat,
right? But then you got cognito. You got that. So I can now say, great,
now can you recreate the table? And this is one of the things I always find
that when I do thread models, I never like to mix external or internal, like
different type of attack agents, right? Basically who you're defending
from, because they will be different. And also your risk metrics should take
that into account. So I prefer sometimes to create the same thread model,
but from different points of view because everything becomes a lot more
realistic.

Dinis Cruz - 52:40
Because if the business is going okay, so I'm really worried about attacks
from the outside, then you go like this, because sometimes you might go,
well, the insider thread can do a whole bunch of other stuff. So this is not,
yes, you could do this, but it probably can do even more things, or it
depends where you are. So I could say, look, now can you recreate the
table only from the point of view? Right? The table only from the point of
view of external attackers with no to, I say low to mid level skills. Right.
So again, I'm not saying state actors and stuff like that. Now, it should be
able to refocus a lot of this, what's it called, the high, mediums and lows
should now be reclassified on those. Because now that's what I would
expect.

Luis Servin - 53:49
It included new things, didn't it?

Dinis Cruz - 53:51
Yeah, well, it was out there in secured direct object references. Was that
there?

Luis Servin - 53:55
No, I see either number three or four. Number two or three, yeah.

Dinis Cruz - 54:01
There you go. From an external attacker. And we can classify this. So we
can also say what is our classification for this? What's our classification
from this? So that's quite nice. Right. Because you remove actually, a
bunch of the ones that are not immediately exposed from those skills. So
it's a lot more focused. S, Cloud, Front, Cognito API, Gateway API expose
sensitive data and GitHub if it gets exposed. So this is pretty cool. Another
thing you can do here, you could say, actually we can go back to the first
one and again we can edit. So I tend to do this quite a lot sometimes edit
the original prompt and you could say here, can you map in fact, this
should actually work. Can you see what I'm asking for?

Luis Servin - 55:04
Stride category.

Dinis Cruz - 55:06
Yeah. So this is where the T from the GPT part is super critical because it
should now go to Stride and it should give it look.

Luis Servin - 55:19
See.

Dinis Cruz - 55:22
How cool is that? It understands what Stride means, right?

Luis Servin - 55:30
I know, but do you know how many times I have spent half an hours of my
life discussing whether something falls within this or that category of
Stride because it's such a bad yeah, but that's a threat category that I tend
to skip it. But I see the value in this. I mean, I would rather map it to
CAPEC, which is like a lot better.

Dinis Cruz - 55:54
Okay. How do you spell that?

Luis Servin - 55:56
C-A-P-E-C. CAPEC.

Dinis Cruz - 55:58
C-A-P-E. Like that? Yeah. Okay. And by the way, the script that I was
talking about sorry, just because I got some BOOKMARKS, I don't want to
share my screen.

Luis Servin - 56:16
I'm recording while you get there, we have a cool mel drews is asking any
predictions or thoughts on how enterprises could make use of similar
techniques now or in the future? Considering with consideration to
concerns for sending organizational applications, security data to some
AI, I think that's part of the risk equation. Right. So having models in
hand.

Dinis Cruz - 56:44
But that's already addressed already. Because if you look at Open API,
Azure Open API, and if you look, for example, at Bedrock, put this way, if
your organization is not using AWS, then you have bigger problems.
Right? For example, if you're using AWS, then AWS already has a mode
where you can use Cloud Two that is locked. And if you're using Google
Cloud, it already has Vertex that is locked. And if you're using Azure also,
right?

Luis Servin - 57:12
And if you have some sort of chat internal thing.

Dinis Cruz - 57:17
I think there's a couple of variations, but it already completely addresses, I
think, Mel, that point. Right. And there's an interesting argument here
where the better we create the prompts, the better we create the
materials, the less powerful model you want. In fact, if you really want to
go private, use Llama Two, right? And llama two is already pretty good.
And again, and you can run that completely in your environment, your
data center, your local machine, and there's different models of Llama. I
haven't fully run it, but some guys I was talking to, it's about between
three and ten grand a month. So depends on what size of the enterprise.
It's already a reasonable cost and it's going to come down. Right. Again,
depends on usage. Right.

Dinis Cruz - 58:01
If you have one person using, maybe it's a lot, but if you have a lot of
developers and if you really have those requirements not to send things
very widely, then that makes a big difference. So, yeah, let me just share
my screen to see the output here.

Luis Servin - 58:15
Cool.

Dinis Cruz - 58:16
Can you see? Yeah. So there you go. Right? Is that better for you?

Luis Servin - 58:23
So KPEC is really the better mapping thing rather than strife.

Dinis Cruz - 58:28
Yeah. Now, the thing about this is that this is what the guy that was doing
the attack gen thing is that some of these sometimes JBT does get these
tend to get more the IDs wrong than these mappings here. So what you
can do is you can feed it to it, right? So you can actually feed for example.

Luis Servin - 58:44
You can ask it to put the link, right? Now, if it's linked, you can just click
and check the.

Dinis Cruz - 58:51
That'S the one, right? Common attack pants classification, right?

Luis Servin - 58:54
Yeah.

Dinis Cruz - 58:57
But the other thing you can do with this is you could also say, see, look, I
don't know if you've seen this, so I could also take this and I can basically
go a new one, right? And basically I can use the advanced data analytics,
right? And I can then say I was actually playing with this and you can
basically say, can you create a visualization right of this application from
a thread model point of view? So in principle, this is the one that has the
code, right? So basically you could see that, first of all, it's going to create
the table with probably a bunch of issues. In fact, I could have probably
given the other issues. Right, see, so it's doing that, but this is the one that
has the advanced data analytics. Have you used this before?

Luis Servin - 59:57
No, I don't have a paid subscription. Yeah, my company is not yet on Chat
GPT. I'm actually supposed to be doing the analysis for the risk
assessment, but when I'm done with that, we might be able to use it. But I
mean, right now I'm on my private account just trying things that have no
relationship to my company, right?

Dinis Cruz - 01:00:17
It's really worth doing this because this part here, it is quite impressive
and sorry, I'm just saying.

Luis Servin - 01:00:44
I assume based on the description, you could also ask it to stop right
where we told it to create a table and tell him or tell it to create mermaid
diagram.

Dinis Cruz - 01:01:00
Exactly. That's what I'm going to do now. So you see, look, see the risk
levels? Okay, so basically it's done this bit, right? You got this thing and
now you can go, great. Can you create, let's say, graph visualization of
this data, namely the data application should be able to now this is the one
that has so you can see that now he's mapping, right? He interacts single
page authentication handed to government success authentication. The
user receives a JWT token. API requests are out to the API gateway. And
my point with all this is that we should still have, you know, this should
still be verified, right? But this is the one that actually erites the code. See?
So he's using Matplotlib with network X. He's going to create a graph.
See, look, there's the nodes, there's the edges.

Dinis Cruz - 01:02:15
Can you see user, he's adding the edges. He's drawing the network, getting
some labels to it. Access request returns. And then he's drawing the
network. And then when he raises bugs like this and then sometimes it's
funny, right? He goes, oh, it doesn't exist, I should be using this one. Why
don't you do that in the first place? But the other thing that is sometimes
really cool is if you have APIs that can do this, you could also ask it for the
code to execute in your end or the functions to execute in your end. And
you could also give it code samples. But the logic is that it just gives you
that acceleration, right? It just gives you that extra mappings and there
you go, right? So there's one visualization.

Luis Servin - 01:03:03
I mean, it's something.

Dinis Cruz - 01:03:08
So you can actually map it up, right? Now, the one I was playing around
before is like, for example, you could also ask to do a plan to ML. So you
can say, hey, give me the plan to ML code for this. And in your example,
remember that you already had some of those modules. So you can say,
hey, here's the building blocks that I want. Now use those building blocks
to do it. I think once we package this a little bit more, it's going to be
super powerful. And remember that it's also about helping, let's say you or
the more expert threat model person to review the materials. Imagine you
being on the receiving end of this, but also you now communicate in
prompts.

Dinis Cruz - 01:03:48
So you can capture your knowledge in prompts, or are you making the
original prompts better, which is that much more efficient?

Luis Servin - 01:03:59
Yeah, certainly this has just so much potential, right? It's incredible what
can be achieved.

Dinis Cruz - 01:04:09
Actually, the other one that you can do. Let me show you. This is while you
were doing that. Let me see if I can load it up here. I basically asked?
Yeah, it's kind of okay, give me a second. See if this works. You kind of
pause in the middle. But see, the other thing you can do, check this out, is
you can take your diagram. Look at this. So what I did is I took this one,
see where you were literally a screenshot of your stuff and say, can you
write a thread model for this application? And you wrote this, right.

Luis Servin - 01:05:00
Not bad.

Dinis Cruz - 01:05:01
Phishing attacks, denel of service attacks, API vulnerabilities, this. So it's
not bad, right? Maps the thing that you have there. Yeah, actually, the
other trick that you can do, which I also think is insanely powerful, is I
was trying to recreate the whole thing. The other thing you can do that is
also crazy powerful is we could also take that table. See, look, I think this
is really cool. So I can take this table and look, just copy this, right? So
I'm just going to copy literally this stuff and I'm going to go, okay, I'm
literally just going to paste that whole thing and say, hi, can you review
find blind spots in the thread model below. And you can literally just paste
it like that.

Dinis Cruz - 01:06:06
See how I'm not even formatting it correctly, but in a way Chat DBT can
interpret that way better than we. So this is what I think is really
interesting is when you do something and you go, hey, can you find blind
spots? Can you look at other things that we could be looking at?

Luis Servin - 01:06:28
Yeah, certainly. This has a lot of potential, right. It's basically the
beginning of how to do threat models enhanced by AI. Looking at this
from the business perspective, I am creating a security champions
community right now. And I don't have a lot of security expertise in the
company to the threat models. Brilliantly. They will get there sometime.
But this can just turbocharge everyone's abilities exactly.

Dinis Cruz - 01:07:05
Right. And also, I think you could also drive a little bit the whole thing of
thinking of and teaching and getting people to use OpenAI right. And Chat
GPT because you're also teaching them. Because look at this. So I can
now can you create a business analysis to provide to a business and
project owner to make the business case to spend time addressing these
issues? So now, look, create a compelling business analysis, right? And
there you go. Right, okay. What is actually giving me okay, so this is a
structure approach. This is cool. Look. So you could see introduction,
executive summary, introduction, analysis, financial analysis. This is not
bad. So it gives you the thing now. Great. So now can you write one
adding can you write one based on the data provider? Right? So now it
will draft a business one. Right?

Dinis Cruz - 01:08:23
See look. So now it's going to give you a text that you can rewrite and you
can basically apply. So that's blah and the grand through landscape or
threat model in five vulnerabilities, right? Look, see, bam, bang. And if you
even know better who you're going for, you can start to.

Luis Servin - 01:08:44
Really you can describe the person's role.

Dinis Cruz - 01:08:46
Describe the person, right? So you can say, Great, but that is too long.
Can you give me the same with max one paragraph? Right? Yeah. But
now.

Luis Servin - 01:09:14
This is the kind of feedback that you could give a human and be punched
for, right?

Dinis Cruz - 01:09:19
Yeah.

Luis Servin - 01:09:20
Someone could have spent hours doing this and then you say, come back
with one.

Dinis Cruz - 01:09:24
Exactly, right, but that's the thing. In the past, this is my point. My point is,
in the past, this would be really hard to do, right, because we do all this
stuff and it's super painful to do, right, and now you can go, okay, can you
write that one paragraph for somebody that has no idea what
cybersecurity is? Right? So you can now start to trick it, right? And then
you could see that the language changed, right?

Luis Servin - 01:10:03
I agree, world of Chat GPT is fantastic, but we definitely need to check the
output, right? So it is going to write for you very easily or very long text.
Now you need to check them and make sure that they actually match
what you want to say.

Dinis Cruz - 01:10:22
But that's the point. The point is that I think where people get in touch
with you wrong is that they shortcutting the last step. And the point is that
it's not about shortcutting the last step. The last step is still there, or even
the intermediate steps. The point is that the recreation of the materials is
now super easy. And like you said, you can go from big to small to change,
to multilanguages, to adding mix or say, oh, he's the language that we're
supposed to do. Or, by the way, this analysis, or he's a project report or
whatever, you can add lots of bits of data in ways that in the past would
make it very expensive. Because you have to go back and rewrite and
think about these things. Right?

Dinis Cruz - 01:11:01
So even little tweaks, you can say, oh, don't use language like this, don't
use words like this, use words like that. And then you can rewrite it. And
that's the keys. The feedback loop now of creative materials is actually a
lot more, which is really powerful. And if you look at the CATA stuff, I
think it's really worth exploring that onboarding, that practicing. I like the
fact that we can now create even games on this. In fact, look at this,
right? So actually, let me give a really cool example. If I start from here,
right? So let me take it from that guy there.

Luis Servin - 01:11:43
You're not sharing your screen, just showing something.

Dinis Cruz - 01:11:46
Sorry. So if I start from. Look at this example. I'm going to take that
example of where were actually capex, see where were, where we got that
list, right? Okay. So can you now create a game and the set of questions
and answers to teach a new developer, right. How to do thread modeling?
Threat with a t. Yeah, sorry. Yeah. Although you actually would pick it up.

Luis Servin - 01:12:22
Thread modeling, I'm not sure. Threat and thread.

Dinis Cruz - 01:12:25
Okay. But it understands the context. That's the other cool thing. There
you go. But it's fine, it's better if you spell it properly, right? But now, Silo,
can you create a game and set a question and answers to teach a new
developer how to do threat modeling for the app above, right? So give it a
cool name and use emojis. I usually go with taste, or else you can go quite
off piece, right? So call Cyberslu thread defenders to engage. Right? There
you go. Look at this. Okay, so what's cool about this is you. Okay, so it's
actually giving the answer, right?

Luis Servin - 01:13:09
Can you see?

Dinis Cruz - 01:13:10
But that's cool, right? Because it already gives you this, right? So you
have the thing. But can you see how really cool is to do a game based on
that particular application that is relevant to that particular thing? See
what kind of risks associated with storing data like DB nine passwords in
environments like lambda. Now, this is very relevant to whoever, to the
developer that wrote this.

Luis Servin - 01:13:41
Sorry, I see. What would be fantastic is I'll put the output of chat TPT 3.5
or. On the repo. If you could also add the output that you have been
generating.

Dinis Cruz - 01:13:58
Yeah.

Luis Servin - 01:14:00
We could then create a branch on the Open Security Summit to keep these
things. Also, this is a place to start, right?

Dinis Cruz - 01:14:08
Yeah. Look at the difference. See what happens now. So look at the power,
right? See, look, see what happened. I could have gave him this, right? So
I could have say, hey, based on this, now run the game. So that will be the
prompt, right? So you could see that. Now you got this. Look. Welcome to
Cybersfluid. Your first misidentified, right? Walk, comment, blah, blah.
And then you can go like this. And then you type the answer and then he's
going to give me a response, right, based on correct answer, blah, blah,
fantastic. Identified. But the other thing you can do, which is quite funny,
right, is I can come in here, right, and I can say, can you run for me? Can
you provide highly sarcastic answers, for example, right? So it's not going
to be for everybody, right?

Dinis Cruz - 01:15:05
And comments to the user, to the player responses, right? So I think this is
not for everybody. But look, so now I'm going to say let's step to the world
of this, right, with a good attitude, right? So you can see it's going to
change a little bit, right? Oh, a new cybersecurity on this. Let's see if you
can spot a vulnerability better than it can spot the laser dot, right? So let's
say I'm doing the wrong one and now he's going to go it should provide a
nice sort of really? That's a cute guess effect. That was chocolate teapot.
But don't worry, there's more fun ahead. Do you know what I mean? But I
think that this makes a difference, right? And you can even put into
context. I'll run this from the point of view of a retailer or a finance
institution.

Luis Servin - 01:15:58
You know what, I'll try this next week. I have my Cybersecurity Champions
meeting next week. I'll provide an illustration of the system and I'll let
them play the game. Let's see what happens.

Dinis Cruz - 01:16:09
So what I'm doing with the Cyber Boardroom, right, is to try to create an
environment that wraps this so that you don't see the middle. For example,
I'm using Chat GBT behind the scenes, but I, for example, just give you the
options and it will give you ABC, and then you click know, so it's almost
like wrap a little UI from a board member point of view, but make it much
more interactive, much more kind of nicer. But the engine behind is sort of
this logic of Chat GPT, which is really cool, right?

Luis Servin - 01:16:39
It is definitely good.

Dinis Cruz - 01:16:41
All right, man, this has been great.

Luis Servin - 01:16:45
It's definitely a very different threat modeling session than I intended
yesterday. But I think after discussing on scaling threat modeling, I really
wanted to try a very good prompt for just flexing the prompt muscles and
you could see how it works.

Dinis Cruz - 01:17:08
Can you see how a lot more effective you are when you're finding blind
spots versus creating from scratch? And I always felt that the problem
with most people doing threat modeling was the start, right? It was that,
how do I start? Where do I go? What's the first? And then you go to stride,
and it's like guessing where even if jump. Hey, thanks, guys. Nice
comments there. But look, just what we're doing here, literally, me and
Lewis, is what we do in threat model. This is what we've been doing for
the last ten years, right? Literally, we've been ad living figuring this out.
Even the stuff that Louis now is already very comfortable doing. The plan
to ML, I remember when we start using that, I was like, well, this is really
cool. We can now visualize the threat model.

Dinis Cruz - 01:17:57
So I think what's nice about our industry is still there's still so much
ground to evolve, and practices like threat model are still very archaic if
you compared to what they should be. So there's great space for
innovation, which is really cool.

Luis Servin - 01:18:13
It is. It's been a fun session. I know. Next open security summit. Let's do a
different Qatar.

Dinis Cruz - 01:18:23
Oh, yeah. By then we're going to have a bot. We're going to have the Open
Security Summit bot with us, right. Providing help and enhancing things
like this. Right.

Luis Servin - 01:18:33
I mean, it took me about the same time it would have taken me to draw
the thing and walk through the case with creating the prompt. Right. So
the prompt was a lot of text and a lot of tweaking and a lot of following
the rules, but it's given us a good result. So we could perhaps next time
start with a bath prompt, improve the prompt as we go to see how it
improves.

Dinis Cruz - 01:18:59
Well, and to share it. Right.

Luis Servin - 01:19:02
The idea is obviously to share it in such a session and have the iterations
the prompts on a markdown file or something to keep it.

Dinis Cruz - 01:19:10
Yeah. And that's one of the other bits I'm really looking at also, and
playing around with the boardroom bot is I'm creating three bots, right?
So I'll go in detail the session, but I'm creating three bots, and each bot
basically contains Minerva. One is Athena, which does the board, the
advice. One is Odin, which actually does the backend stuff, and one is
Minerva, who does the business stuff. So you kind of have a mix of
multiple bots playing together, which know when it works, it's going to be
pretty cool. All right, man, this is good stuff. I think it's been a pretty good
session. Man, this has been a really nice session.

Luis Servin - 01:19:46
It was really fun. Thank you for your interaction. I mean, it was great to
see how you use it. I saw your reading list for the summer and I was like,
envious of where you find the time to read so much.

Dinis Cruz - 01:20:01
Yeah, but it's like I was telling point the point of having those books,
although I drove to Portugal so I could bring it, so my wife didn't complain
that I brought a bag just for books. Right. But I felt that I had the books I
needed to read in the sequence that I wanted to read. And what that
allowed me to do is allow me to go quite deep. And then one of the things I
realized was that the action was not in the models. The more depth I went,
the more I realized the history of it and where were and the innovations,
and the more I understood how GPT worked, the more I realized that the
action is not in the models is in the prompts, is in, maybe even be the
training of it. Right. But that's where I became quite interesting.

Dinis Cruz - 01:20:39
But I was able to almost read the book in sequence that I needed to. So I
needed the 30 books so I didn't read.

Luis Servin - 01:20:46
I mean, I remember your list was like ten books. So out of the ten, which
one was the best?

Dinis Cruz - 01:20:52
There was a couple. I think the O'Reilly GPT transformers was really
good.

Luis Servin - 01:20:56
All right, so I'll get that one.

Dinis Cruz - 01:21:00
I think it's that one. Yeah.

Luis Servin - 01:21:02
I'm using you as my chat GPT.

Dinis Cruz - 01:21:04
Yeah, you're.

Luis Servin - 01:21:06
My dean GPT. And I cut the ten books to one. That's good enough for me.

Dinis Cruz - 01:21:11
Okay, cool. All right. Take care on that. All that notes.
