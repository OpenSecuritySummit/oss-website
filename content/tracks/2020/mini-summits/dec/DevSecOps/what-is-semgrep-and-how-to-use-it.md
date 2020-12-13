---
title        : Embrace Secure Defaults, Block Anti-patterns, and Kill Bug Classes with Semgrep
track        : DevSecOps
type         : working-session
topics       :
featured     :
event        : mini-summit
when_month   : Dec
when_day     : Fri
when_time    : WS-6
hey_summit   : https://post-summit-sessions.heysummit.com/talks/what-is-semgrep-and-how-to-use-it/
session_slack:
#status       : draft
description  :
organizers   :
    - Clint Gibler
youtube_link : EIjoqwT53E4
#zoom_link    : https://zoom.us/j/91592155450?pwd=cjdZVS9KcWgvWG5aQWo4YThDS2ZVUT09
slide_id      : 2PACX-1vQdAuii6O1Z45gEsb93oFjmXtCMvqiXdKrUgWWPY5wkdF8UHxNLPTCNXRKhKtLhdgU0rQWHMpbBPiyr
---

## About this session

Are you tired of seeing the same types of bugs surface again and again at your
company? Do you ever shed tears of weariness or despair at the deluge of false
positives your security tools continue sending your way?

Don’t worry, there’s another way! There’s a new approach that many
forward-thinking AppSec teams are embracing, including Microsoft, Facebook,
Google, Netflix, Dropbox, and more.

These companies are abandoning the Sisyphean task of trying to find every bug,
and are instead embracing secure defaults: services, libraries, and frameworks
that developers can use that prevent entire vulnerability classes from ever
occurring in the first place.

In this talk, we’ll present [Semgrep](https://semgrep.dev), an open source,
lightweight static analysis tool, that when combined with secure defaults can
effectively scale your company’s security by eliminating vulnerability classes.

Key Semgrep features:

* Fast - scans code in minutes, not hours or days.
* Does not require the source code you’re scanning to be buildable.
* Comes out of the box with over 1,000 rules, and supports languages including
  Python, Java, Golang, JavaScript, TypeScript, Ruby, PHP, C, and more.
* Most importantly, Semgrep makes it easy to write custom rules, no fancy DSL
  required. This empowers AppSec engineers and developers to detect and block
  company-specific security bugs and anti-patterns as well as enforce best
  practices.

We’ll demo how to easily write custom Semgrep rules tailored to your specific
code base, and how to get continuous security coverage in CI in a just a few
minutes.

This workshop will be interactive! We'll write some Semgrep rules live together
and share challenges for attendees to solve.
