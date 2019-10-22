Title: Kismet / Kali Linux Pi Zero WiFi Attack Sidecar
Date: 2019-09-29
Category: Security
Tags: hacking, linux, security, kismet, kali, linux
Status: draft


It's a breezy autumn Sunday. It is warm, the sky is clear and after this past
week the trees are certainly showing the season. Nights have been cool and the
forecast says the days will soon be as well. A favorite soup recipe is on the
menu for tonight's dinner and I'd hoped to make baguettes to go with it, but
I'll be damned if I can get dough to agree with me today. After two botched
attempts, looks like I'll be running to the bakery before dinner.

Baking foibles aside, I have had some luck lately making a [Raspberry Pi
Zero](https://www.raspberrypi.org/products/raspberry-pi-zero-w/) into a [USB
Ethernet Gadget](https://learn.adafruit.com/turning-your-raspberry-pi-zero-into-a-usb-gadget/ethernet-gadget)
While I was able to do most of what I wanted following Lady Ada's instructions,
I did encounter a few gotchas, plus I wanted to do the same thing but running
[Kali Linux](https://www.kali.org) instead.

## Why do I want this?

Typically I do most of my work on my now-aging MacBook Pro, running Kali Linux
on a virtual machine. This is a typical setup and generally works just fine.
Where it falls down is when I'm playing with my
[RTL-SDR](https://www.rtl-sdr.com/) software defined radio, or my Great Scott's
[YARD Stick One](https://greatscottgadgets.com/yardstickone/). For some reason I
just can't get the devices to behave or to stay online, a problem I haven't had
running Linux on the metal. I've also had occasional trouble running wifi
attacks on external hardware. While I do intend to move back to a Linux laptop
in the foreseeable future, it would be nice to have a small, easy-to-use Kali
machine in my pocket when the need arises. The Pi Zero also lends itself to some
naughty use cases, what with it's super-small form factor.

So, I'm going to document here exactly how I get my Pi setup and configured, up
to and including getting [Kismet](https://www.kismetwireless.net/)set up for
portable WiFi mischief. For the remainder of this write-up, I'm assuming you are
running on an up-to-date version of MacOS. Linux should be similar up to a
point, but you Window$ users are on your own.

## Download and flash MicroSD

First off, download the latest [Kali ARM
image](https://www.offensive-security.com/kali-linux-arm-images/) for the
Raspberry Pi Zero/Zero W. Before you transfer the image to your SD card, verify
it's hash against the one presented next to the image's torrent link.

```shell
$ shasum sha256sum ~/Downloads/kali-linux-2019-3-rpi0w-nexmon-img-xz/kali-linux-2019.3-rpi0w-nexmon.img.xz
0c06f7220f585552e57bcd62a683d4ef6a6409cfd6ea3d63ce96c39792acd918  /Users/adam/Downloads/kali-linux-2019-3-rpi0w-nexmon-img-xz/kali-linux-2019.3-rpi0w-nexmon.img.xz
```

While you can use `dd` to write the image to your SD card, I've found
[balenaEtcher](https://www.balena.io/etcher/) to be easier and much faster doing
basically the same thing. They must know exactly which switches to flip. In any
case, select your verified image and target SD card and click "Flash!"

## Configure USB gadget

Flashing your card will take a bit, I think it took about 15 minutes to flash
and validate on my machine, your mileage may vary. Once that's done, eject and
re-insert the SD card. The next couple of steps will be done directly to files
on the root of the card's filesystem. These steps are basically verbatim from
Lady Ada's tutorial referenced above and below.

### Edit config.txt & cmdline.txt

My SD card mounted at `/Volumes/NO\ NAME/`.

First add `dtoverlay=dwc2` to the last line of `config.txt`.

```shell
echo "dtoverlay=dwc2" >> /Volumes/NO\NAME/config.txt
```

Next open up cmdline.txt and at the end of the first line, after `rootwait` add
`modules-load=dwc2,g_ether`.

```shell
dwc_otg.lpm_enable=0 console=serial0,115200 console=tty1 root=/dev/mmcblk0p2
rootfstype=ext4 elevator=deadline fsck.repair=yes rootwait modules-load=dwc2,g_ether
```

### Enable SSH

Super easy, enable SSH into the Pi be dropping an empty file called `ssh` at the
root of the SD card:

```shell
touch /Volumes/NO\ NAME/ssh
```

Now we should be able to boot up and ssh into our Pi. Eject your SD card from
your host computer, insert it into your Pi, and plug a USB cable from your
computer to the Pi. Be sure to use the port labeled "USB" and not the one
labeled "PWR".

## Enable networking

## Update Kali

## Install Kismet

## Configure wireless device

## References

* [Turning your Raspberry PI Zero into a USB Gadget](https://learn.adafruit.com/turning-your-raspberry-pi-zero-into-a-usb-gadget/ethernet-gadget)
* [Share an Internet Connection with a Raspberry Pi Zero over USB](https://stevegrunwell.com/blog/raspberry-pi-zero-share-internet/)
* [Official Kismet Packages](https://www.kismetwireless.net/docs/readme/packages/)
