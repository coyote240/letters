Title: Getting Started with O.MG's DemonSeed EDU
Date: 2020-08-01
Category: hardware
Tags: hacking, hardware


## I have good friends

It's been a lonely year, no doubt, but I'm very lucky to have a loving family
and plenty of friends to lean on. While I don't see many people in the flesh
lately, I do have frequent contact online, and my hacker friends have been
critical to my health and happiness. Thanks to the hacker and DEFCON
communities, I've even been able to make new friends along the way.

One new friend from DEFCON has made a pandemic project out of learning to cast
gaming dice. He's been sharing his progress, from buying masters to crafting his
own masters and resin printing them before casting his own masters. He's learned
some pretty stunning coloring techniques, so I had to have a set of my own. When
he posted a set that really caught my eye, I claimed it right away. He let me
pick the color for the numbers and once they were ready, he put them in the
mail. The dice are _beautiful_, and someday when we can get together again for
some dungeon hack'n'slash, I look forward to using them.

## What's in the box?

Now, when I received my package in the mail, and I was done marveling at my new
dice, I noticed a small, paper envelope at the bottom of the box, white with
black, seemingly demonic symbols on it. My friend had included an [O.MG
DemonSeed EDU](https://o.mg.lol/) kit! These were quite popular at DEFCON and
I'd seen them available at
[Hak5](https://shop.hak5.org/products/o-mg-demonseed-edu). This was a very
generous gift that I certainly did not expect! While I've done a certain amount
of hardware hacking, my workbench has been neglected this summer. I took the kit
to my bench in the basement, dusted off the soldering mat, and got to work.

I'm not going to cover my effort here. For starters, I've only gotten through
soldering the programmer and the DemonSeed into a USB connector before loading a
very basic payload. Also, I still haven't done the work I want to do to safely
load photographs onto the site without spreading even more location meta-data
about myself onto the internet. I do, though, want to put up the links I'll want
later, and a quick note about udev rules.

## Asking for forgiveness won't work this time

After you've flashed a bootloader onto your DemonSeed and soldered into the USB
connector, you're ready to put a payload onto your device. Once you've
configured your Arduino IDE for the Digispark and you try to load your sketch,
you may encounter an error like this:

```shell
micronucleus: library/micronucleus_lib.c:66: micronucleus_connect: Assertion 'res >= 4' failed.
```

This happens because the default usb udev rules are set up to have the device
mounted as `root` with `0600` permissions. Thanks to [this forum post
here](https://digistump.com/board/index.php?topic=106.0) I found I could create
a file at `/etc/udev/rules.d/digispark.rules` like so...

```
SUBSYSTEM=="usb", ATTR{idVendor}=="16d0", ATTR{idProduct}=="0753", MODE="0660", GROUP="dialout"
```

Double-check your `dmesg` output to ensure that you're using the correct
`idVendor` and `idProduct` for the device you've connected. Now when you connect
your device, and assuming your user belongs to the `dialout` group, you should
be able to write to your DemonSeed without trouble.

## What's next?

By the [seventh
video](https://www.youtube.com/watch?v=ww_71dgkgW8&list=PLW5y1tjAOzI1xRXLCU1ROeZIuyVz7aF0e&index=7)
in O.MG's series, things start to get pretty complicated as he describes ways to
experiment with hardware such as radio interference, etc. This will require some
time and concentration. I'll certainly share any of my own discoveries here. In
the meantime this project has me inspired to put a little more time into playing
with the various micro-controller devices I've picked up over the years,
including a very cool programmer a friend and I assembled for the ESP8266 12F
chip.

There's less than a week until [DEFCON28: Safe Mode with
Networking](https://defcon.org), and following that I have resumed my labs to
prepare for my OSWE exam in October. It's going to be a sleepless couple of
months, no doubt.

## Links

* [O.MG DemonSeed EDU on Hak5](https://shop.hak5.org/products/o-mg-demonseed-edu) 
* [Setup page on O.MG's site](https://o.mg.lol/setup/OMGDemonSeedEDU/)
* [Digispark Wiki](http://digistump.com/wiki/digispark)
