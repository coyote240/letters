Title: Mid-October Rambles
Date: 2019-10-14
Category: misc
Tags: hacking, events
Status: draft


## I've let a month go by...

It's not that I haven't been writing, but I have had trouble finishing things
lately. It's been easy to get caught up in the day-to-day, and maybe that's a
good thing. I don't know if I should get caught in the industrial mindset trap
of measuring my self worth by my productivity.

I do have a couple more write-ups in the works, with a couple of minor snags
I'll need to work out before I publish them here, perhaps in an abbreviated
form. I tend to write down a lot of what I work on while I'm working, and
sometimes things don't work out the way I'd intended.


## Kali Linux Pi Zero Wifi Attack Sidecar

For example, I'd been working on a Kali Linux based, Raspberry Pi Zero W USB
Ethernet Gadget. You may have read about [turning a Pi Zero into a USB
Gadget](https://learn.adafruit.com/turning-your-raspberry-pi-zero-into-a-usb-gadget/ethernet-gadget)
as written by Lady Ada. This works very well on stock, light Raspbian, but I'm
afraid that on a Kali image, even with the [re4son
kernel](https://whitedome.com.au/re4son/download/re4son-kernel-current/),
doesn't seem to have everything you need to do the same. This means that I
haven't been able to connect privately via ssh over USB, which I felt made for a
really cool, portable gadget. I also found that the Pi Zero had trouble
delivering enough power to my external ALFA wifi adapter, which I believe is the
cause for some pretty predictable freezes of the system any time I try to
interact with, or even list, that device. When I can, I'll try to summarize what
I encountered and put it up here.


## Ĉu vi legas la Esperanton?

I've started one article a translation of another into Esperanto. My study of
the language tends to ebb and flow, and I'm ebbing right now for sure.
Translating technical articles into Esperanto proves to be an interesting
challenge, even with the help of [Komputeko](https://komputeko.net/). It's a fun
process, but time consuming. I've also enjoyed trying to get my thoughts out as
an Esperanto-first exercise. Again, put it on the to-do list. Or the drafts
folder. Whatever.


## Toys!

I haven't been totally unproductive! Lately I've been refreshing some old
hardware and giving existing systems some much needed updates.

For the last couple of years I've been running my own, home built gateway and
firewall based on OpenBSD and pf. It's been a pretty bare-metal setup with no
additional packages after the initial install. I learned to configure `pf`
myself, as well as to set up unbound as my local, caching, forwarding DNS
server that sent requests via DNS over HTTPS to 9.9.9.9 and 1.1.1.1.
