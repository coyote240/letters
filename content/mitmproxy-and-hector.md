Title: Generate Swagger with mitmproxy and Hector
Date: 2019-06-22
Category: programming
Tags: mitmproxy, swagger, pentesting

A local proxy is a commonly found arrow in an engineer or penetration tester's
quiver.  Whether it be a paid, commercial proxy like
[BurpSuite](https://portswigger.net/burp) or an open source (and fabulous) proxy
like the OWASP [Zed Attack
Proxy](https://www.owasp.org/index.php/OWASP_Zed_Attack_Proxy_Project), the tool
is a ubiquitous, critical part of an app-sec toolkit. If you're not familiar, a
local proxy, or an _attack_ proxy allows you to route local traffic from your
browser or perhaps another application to allow you to observe, record and alter
the traffic to and from that application. You may do this to test an application
for bugs or evaluate it for security.

During my own development, or particularly when I'm evaluating a mobile
application for my own use, I've grown fond of
[mitmproxy](https://mitmproxy.org/), an open source, console based HTTPS proxy.
`mitmproxy` offers a nice, interactive console interface as well as a web
interface and an excellent Python API, which is what we're here to talk about
today.

Recently I was evaluating a mobile application that I like to use. It's a
simple, social application for language learners that is developed by what I
feel is a trustworthy source. But, as the Soviets would have said, "Trust but
verify." I decided to point the application at `mitmproxy` and see how it
worked. As I expected, the mobile app is a basic UI in front of a REST API. At
first glance I see that the app uses TLS (good!), has what looks like adequate
authentication (we'll see about authorization later) and some limited ad
traffic. A cursory view looks like a prudently built application. However,
that's not what this post is about.

As I tinkered with the app, I'd keep an eye on the `mitmproxy` console
interface, occasionally clicking into a request to get a closer look. This is
fine, but its a bit of a manual process. Each request and response are displayed
in isolation and I need to look at each call and manually take notes about what
I see. This got me to thinking: what if I could have `mitmproxy` output API
documentation in the background as I messed with the app, something that would
group similar calls together, that I could review later at my leisure.

Well, `mitmproxy` has an excellent Python API! I decided I could add this
functionality as an add-on. It also occurred to me that generating swagger would
be an ideal documentation output, and as I'd not yet messed with swagger very
much, this would be a good opportunity to give it a try. So, that's what I did.

The ongoing results of my experiment may be found on GitHub in a small project
called [hector](https://github.com/coyote240/hector). It's a simple project,
basically focusing on capturing observed application traffic as swagger yaml,
grouping like calls together and capturing the names and types of parameters
passed to and received from each API call. At the end of a `mitmproxy` session,
yaml is output to your specified target, each observed host being separated out
into yaml document within the same file.

Setup is documented on the project site. Once you've created your python virtual
environment and pulled `hector.py`, you can run the add-on with `mitmdump` and a
few arguments:

```shell
$ mitmdump -s ./hector.py --set hector_output=mySessionOutput.yaml
```

As `hector` is a fairly simple plug-in, you may choose to write something similar
for yourself. Otherwise, this project will be ongoing as there are a few more
things I'd like from the plug-in, such as filtering by host, optionally output to
a separate file per host, live updating, etc. If you'd like to contribute, pull
requests are welcome!

Ĝis la revido, kaj feliĉa kodumado!
