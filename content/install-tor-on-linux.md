Title: Installing TorBrowser for Easy Update on GNU/Linux
Date: 2020-03-30
Category: Security
Tags: linux, security, linux, tor, privacy
Status: draft


This issue has come to my attention a couple of times now: users new to Linux
and Tor have installed the TorBrowser package, but come update time find they
have to reinstall.

## Create and Join the `tor` Group

The first thing I want to do is create a group to own the Tor application files.
I could certainly give ownership of the application to my own user account, but
this allows for a little bit more flexibility, should I decide to add users to
my system.

```shell
$ sudo groupadd tor
```

Then I want to add my user account to the `tor` group I just created.

```shell
$ usermod -aG tor signal9
```

These steps will become more important in a few minutes once we've downloaded
and extracted the Tor Browser. You need to log out and back into your session
in order for joining the group to fully take effect.

## Download & Verify Tor Browser

Navigate to the [Tor Project](https://www.torproject.org/download/) website and
click on the Download link. These instructions are for Linux, so click the
"Download for Linux" link. You will also need to download the Signature file.

On my laptop, this has downloaded to my Downloads directory. I have chosen the
64-bit version, which at the time of this writing is at version
[9.0.7](https://www.torproject.org/dist/torbrowser/9.0.7/tor-browser-linux64-9.0.7_en-US.tar.xz).

I have also downloaded the [signature
file](https://dist.torproject.org/torbrowser/9.0.7/tor-browser-linux64-9.0.7_en-US.tar.xz.asc)
which I require to verify the downloaded files.

Rather than document the process of verifying your download here, I'll direct
you to the [really excellent documentation](https://support.torproject.org/tbb/how-to-verify-signature/) at the Tor website.

**Do not skip the verification step!** Tor Browser is a controversial piece of
software globally, and as such is a high-value target for criminal and state
actors alike. Verifying against a signature is one step towards ensuring a safer
Tor experince.

## Install TorBrowser

To install the Tor Browser, we will extract the downloaded archive to the `/opt`
directory. You will need sudo access to your machine for this step.

```shell
$ sudo tar -xvf ~/Downloads/tor-browser-linux64-9.0.7_en-US.tar.xz -C /opt
```

This will have created a new folder at `/opt/tor-browser_en-US`. If you've
chosen a different language, you may have a slightly different folder name.

Now that we've extracted the application, we'll want to give ownership of the
directory to the `tor` group we created earlier.

```shell
$ sudo chgrp -R tor /opt/tor-browser_en-US/
```

We also want to change the permissions of the directory so that members of the
`tor` group will have read, write and execute privileges.

```shell
$ sudo chmod -R 770 /opt/tor-browser_en-US/
```

Now only `root` and members of the `tor` group may read, execute or modify the
Tor application, but other users may not read the directory at all.

## Update
