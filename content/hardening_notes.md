Title: Science Friday - Basic Setup and Hardening of a Linux Server
Date: 2019-04-10
Category: Security

## What's this?

I put this guide together a couple of years ago for a number of friends of mine,
so that we had a baseline Debian setup for future projects. There are certainly
more or other things you can do to a new Linux installation, but this is what I
find to be a good, minimal, starting point.

## Prerequisites

- Install [VirtualBox](https://www.virtualbox.org/) for your platform
- Download a Debian netinst ISO from [Debian](https://www.debian.org/CD/netinst/)

## Setting up our machine

### Create a host-only network

In order for us to be able to access our virtual machine over the network, we
will need to create a host-only network. The finer points of what exactly this
means are beyond the scope of this document.

1. Open VirtualBox preferences
2. Select __Network__
3. Open the __Host-only Networks__ tab
4. Click on the __+__ button

This will add a new host-only network adapter, likely named vboxnet0.

### Create a new virtual machine

Click __New__. In the open dialog, give your machine a name, type and version.
In our case, we will be creating a Linux machine, version Debian (64-bit).
The next few pages, we will go with the defaults for memory and disk size.

Click on the newly created record and then click __Settings__. Under __Storage__,
select the installed device under Controller IDE labeled Empty. Next to the
Optical drive, click the disk icon and navigate to the Debian installation ISO
you downloaded earlier.

Under __Network__, click on the Adapter 2 tab and check Enable Network Adapter.
In the Attached to dropdown, select Host-only Adapter. vboxnet0 should appear
under name.

At this point we should be able to start the virtual machine and the Debian
installation media will boot.

## Intalling Debian

Debian has a number of installation options, including a graphical install. We
will be using the default install method. When the Debian installation screen
appears, press Enter. The first few screens ask information regarding
localization and keyboard maps. Do what you will.

You will encounter a screen labeled __Configure the Network__ where you should
see two available network interfaces. The default is to use eth0 as the primary
interface. This is fine.

Choose your hostname and domain. These can be changed later, and since we're
running on local VMs, it doesn't overly matter for what we're doing.

Choose a root password. You will also be asked to create a new user. Enter and
verify that user's password. We will be working with this user more later. 

Choose a timezone. When it is time to partition disks, choosing __Guided - use
entire disk__ and all files in one partition is fine for our purposes. Agree to
the partition table and continue.

It is ok to use the defaults when configuring the package manager.  After
choosing a location and a mirror (and configure a proxy if necessary) Debian
will download and install the base system.

On the software selection screen, we will deselect __Debian desktop environment__
and __print server__, but we will enable __SSH server__.  A desktop environment
may be added later if you want, but since this is intended as a server, we want
a pretty bare-bones system. Navigate thru the screen using your arrow keys.
Press the space bar to select or deselect an option. Tab to Continue and press
Enter. Debian will install the remaining packages.

You will be asked to install the GRUB boot loader, to which you will agree and
select `/dev/sda` as the installation target.

With this complete, you will be prompted to reboot. Don't worry about removing
the installation media, the system will do that for you.

In a few seconds, you will see the boot loader screen. Hit enter, or wait for
it to autoboot. You will then see a login prompt. You are now ready to log in.
The next few steps will require elevated privileges, so go ahead and log in as
root.

## Configure networking

In order to allow us to access our virtual machine over ssh, we need to enable
and configure the host-only network adapter we added to our virtual machine.
While this is not a step we would often perform when setting up a typical cloud
VPS, it is good to be at least aware of network interface configuration.

During installation, Debian only configures the primary interface, `eth0`.
We're going to leave this be and enable `eth1` for our remote access. While this
step is not typical when configuring a cloud server, the networking principles
are basic to Linux and worth at least being aware of.

### Verify network interfaces

Having logged into the virtual machine as root, check and verify that both
network interfaces are present:

```shell
ifconfig -a
```

You should see two configured interfaces: `eth0` and `eth1`. `eth0` will have
an IP4 address configured, and perhaps an IP6 address as well. `eth1` should not
have any addresses assigned

### Enable secondary interface

Using your editor of choice, open `/etc/network/interfaces`

To the end of the file you will want to add:

    # Secondary network interface, vbox host-only
    allow-hotplug eth1
    iface eth1 inet dhcp

Save and close the file.

The first line tells the server to automatically bring up the interface. The
second configures it for DHCP. A static address may be configured, but we'll
stick with this for now.

Now, reboot the machine:

```shell
shutdown -r now
```

When the machine comes back up, log in again as root and once again check our
interfaces by typing `ifconfig -a`.

We should now see the second interface, `eth1`, has an IP4 address assigned.
Make a note of this address as we'll need it later. We should also now be able
to access the virtual machine from our host machine over `ssh`:

```shell
ssh *youruser*@*yourip*
```

## Empower your user

It is best to do most if not all of your work as a less privileged user than
`root`. The Debian installation creates a user for this purpose. We will want to
allow this user to perform some tasks with escalated privileges.

First we will need to install `sudo` and give our user access.

```shell
apt-get install sudo
adduser *youruser* sudo
```

Now, log out of the root account and log back in with your less-privileged user.
We will test that we have access to `sudo`:

```shell
sudo ls
```

You should have been warned about the implications of using sudo and prompted
for your password.

## Improve SSH Access

### Generate a keypair

Our goal is to allow our user to authenticate to the virtual server using public
key encryption rather than passwords. To do this, we will have to generate a
keypair and install the public key on the virtual machine.

First, we need a safe place to keep our keys and configs. On your local machine:

```shell
mkdir ~/.ssh
chmod 700 ~/.ssh
```

Now, also on our local machine, we will generate our key. If a key name is not
specified, the default is to create a pair of files called id\_rsa and id\_rsa.pub.
Today we will create a keypair called `debian_server`

```shell
ssh-keygen -b 4096 -f ~/.ssh/debian_server
```

### Push your keypair

During keypair creation, you will be prompted for an optional passphrase. It is
up to you whether you use one, but an empty passphrase is also acceptable.

We will need to copy our public key to the virtual server to use it for remote
access. To do this, we'll use `ssh-copy-id`. On your local machine:

```shell
ssh-copy-id -i ~/.ssh/debian_server *youruser*@*yourip*
```

You will be prompted for your remote password, then the file will copy securely
to the remote machine. To verify the key is present on the virtual server, from
that machine type:

```shell
cat ~/.ssh/authorized_keys
```

You should see your key as the last item listed.

### Configure SSH locally

At this point you should be able to access the virtual server using your keypair
for authentication:

```shell
ssh -i ~/.ssh/debian_server *youruser*@*yourip*
```

However, why do so much typing? `ssh` allows us to configure our local client
for name-based access.

On your local machine, create or edit the file `~/.ssh/config` and add the
following:

    Host debian-server
        HostName *yourip*
        User *youruser*
        IdentityFile ~/.ssh/debian_server

With this in place, you may connect to the remote server simply by the name
configured:

```shell
ssh debian-server
```

## Lock down SSH access

### Disable root remote login

We have options to significantly restrict SSH access and to minimize the ability
for attackers to brute-force a remote login. First, we will require that all SSH
users are non-root users. We will edit `/etc/ssh/sshd_config`. Find the setting
`PermitRootLogin` and set it to `no`.

### Disable passwords

Still in `/etc/ssh/sshd_config`, look for the setting `PasswordAuthentication`
and set it to `no`.  This will disable the use of passwords when logging in over
SSH, thus requiring that your keys have been installed.

Now you may restart the SSH server for the new settings to take effect.

```shell
sudo systemctl restart sshd
```

You should now see access denied when trying to log in as root, or as any user
not configured in `~/.ssh/config`

## Removing unwanted services

There are likely at least a couple of services running on a default installation
that we do not want. To list the running services, type:

```shell
sudo netstat -tulpn
```

On my system, I expect to see `sshd` and `dhclient`, but I also so see `rpcbind`
`rpc.statd` and `exim`, which I currently do not intend to use. I see that
removing `rpcbind` will also remove `rpc.statd`, so I only have to uninstall
one.

```shell
sudo apt-get purge rpcbind exim4
sudo systemctl stop exim4
```

Running `sudo netstat -tulpn` again will show that now we are only running
`sshd` and `dhclient`.
