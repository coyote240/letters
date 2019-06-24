Title: Renovigu Vian Let's Encrypt Atestilo Por Via DigitalOcean Ŝarĝodistribuilo
Date: 2019-06-16
Category: Security
Tags: kubernetes, security, digitalocean
Slug: renew-lets-encrypt-certificate-for-digitalocean-load-balancer
Lang: eo
Status: draft

Ekde mi komencis lerni uzi [Kubernetes](https://kubernetes.io) por labori, mi
gastigi ĉi tiu retejo kaj kelkaj aliaj sur malgrandan sektoraron sur
[DigitalOcean](https://digitalocean.com). Dum mi tipe gastigis miajn retejojn
sur [Linode](https://linode.com), DigitalOcean enkonstruitis kelkaj bonan
subtenon por porokazaj uzantoj kiel mem, tiel imposti nur por laborantojn, kaj
aŭtomata agordo de ŝarĝodistribuilojn. Ekde DigitalOcean impostas por
ŝarĝodistribuilojn, mi gastigas miajn Vexing Workshop proĵektojn kiel reta
domajno sub sola ajna signo atestilo por helpi daŭrigu kostojn.

La iloj de DigitalOcean por demandi kaj administrati estas bona [Let's
Encrypt](https://letsencrypt.org), sed por agordo tiel min, vi devos administri
mem serĉadon, instaladon kaj alŝutadon vian atestiloj. Kiam mi unue faris ĉi tie
retejon, mi ofte referencas al la bonega kaj direkta artikolo de Anchorite:

[Creating a Wildcard SSL Certificate for a DigitalOcean Droplet](https://www.stauber.org/index.php/2018/12/02/creating-a-wildcard-ssl-certificate-for-a-digitalocean-droplet/)

Sekvi la instruadojn en ĉi tiu artikolo, mi instalis `certbot`, la oficiala
kliento de Let's Encrypt, kaj petis ajna signo atestilo uzadis DNS aŭtentikigi
mian peton. Antaŭ ol mi finis, mi generis miajn atestilojn loke kaj mi povis
instali ilin en mia DigitalOcean konto per la interreta konzolo.

## Kio mi provis unue?

Kiam me unue eksidis por ĝisdatigi mian atestilon, mi nur provis ruli `certbot
renew`, esperadadis ke tio estis ĝin. Tamen, mi ricevis ĉi tiu torda eraro:

```shell
Attempting to renew cert (vexingworkshop.com) from /etc/letsencrypt/renewal/vexingworkshop.com.conf produced an unexpected error: The manual plugin is not working; there may be problems with your existing configuration.
The error was: PluginError('An authentication script must be provided with --manual-auth-hook when using the manual plugin non-interactively.'). Skipping.
All renewal attempts failed. The following certs could not be renewed:
  /etc/letsencrypt/live/vexingworkshop.com/fullchain.pem (failure)
```

Tiel mi elfosis la [`certbot` dokumentado](https://certbot.eff.org/docs/), mi
trovis ke la `renew` komando ne estis kongrua kun la dialoga reĝimo priskribis
in la artikolo super. Mi devos eskribi iujn skriptojn por alvoko tra la
ĝisdatiga procezo. La celoj de ĉi ties skriptoj estas por kreiado da la necesa
agordadoj de DNS rikordoj, kaj la disponigoj, kaj la purigi poste. Tiel mi
komencis skribi la skriptojn, mi trovis ke jam estis [kromprogramoj
preta](https://certbot.eff.org/docs/using.html#id15) por mia provizanto de nubaj
servoj, ke povis helpi min kun ĉi tiu tasko!

## Let's set up some tools

Going forward, I'm going to assume you've followed Anchorite's instructions, or
that you have at least installed `certbot` and that your previously created
certificates are getting ready to expire.

Since I'm hosting my cluster on DigitalOcean, I chose the
[`certbot-dns-digitalocean`](https://certbot-dns-digitalocean.readthedocs.io/en/stable/)
plugin. While your distribution may have a package for this plugin, I'm on macOS
and `homebrew` _does not._ I did, however, find that all of the DNS plugins may
be found on `pip`. You may need to adjust the instructions below for your
particular system.

So, let's first start by creating a Python 3 virtual environment and activate
it.

```shell
$ python3 -mvenv ~/env/digitalocean
$ . ~/env/digitalocean/bin/activate
```

Now we'll install our plugin.

```shell
$ pip install certbot-dns-digitalocean
```

After a few minutes of downloading dependencies, your plugin has been installed.
You can verify this by listing installed packages _(output edited for brevity)_.

```shell
$ pip list

Package                  Version 
------------------------ --------
...
certbot                  0.35.1  
certbot-dns-digitalocean 0.35.1  
...
```

## If you want to keep a secret...

In order for `certbot` to authenticate against the DigitalOcean API, you're
going to need to generate an API key. If you already have a generated key and
you know where it is, skip this step. Otherwise, in the DigitalOcean web
console, navigate to __API__ screen which, at the time of this writing, opens to
the __Tokens/Keys__ section. Click on the __Generate New Token__ and follow the
instructions. Be sure to select both _read_ and _write_ options. Copy the key
when it is presented to you, the value will not be shown to you again.

The `certbot` client and our plugin will require our token to be stored in an
INI file. I've opted to store mine in a hidden directory in my $HOME, thus:

```shell
$ mkdir -p ~/.secrets/certbot/
$ touch ~/.secrets/certbot/digitalocean.ini
$ chmod 600 ~/.secrets/certbot/digitalocean.ini
```

And the contents of the file should look like this, with your token in its
place:

```config
dns_digitalocean_token = <my secret token>
```

Tools installed, token acquired, we're ready to proceed!

## Update, Upload, Verify

The `certbot-dns-digitalocean` plugin will do the greatest part of the work from
here on in. All we have to do now is to issue the renew command as I tried
before, but with a bit more information.

```shell
$ sudo certbot renew --dns-digitalocean \
    --dns-digitalocean-credentials ~/.secrets/certbot/digitalocean.ini

Saving debug log to /var/log/letsencrypt/letsencrypt.log

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Processing /etc/letsencrypt/renewal/vexingworkshop.com.conf
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Cert is due for renewal, auto-renewing...
Plugins selected: Authenticator dns-digitalocean, Installer None
Renewing an existing certificate
Performing the following challenges:
dns-01 challenge for vexingworkshop.com
dns-01 challenge for vexingworkshop.com
Waiting 10 seconds for DNS changes to propagate
Waiting for verification...
Cleaning up challenges

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
new certificate deployed without reload, fullchain is
/etc/letsencrypt/live/vexingworkshop.com/fullchain.pem
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

Congratulations, all renewals succeeded. The following certs have been renewed:
  /etc/letsencrypt/live/vexingworkshop.com/fullchain.pem (success)
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
```

With any luck, and if you followed instructions carefully, you should see output
like above, and you now have updated certificates on your local machine. Now we
have to get them to DigitalOcean where they'll be useful. This time, I've opted
to upload my certificate via the web UI, but you could certainly use
DigitalOcean's REST API to perform the same steps. Next time I update my
certificate I plan to do exactly that, and I'll update the site with my
findings.

In the web UI, under __Account__, navigate to __Security__. On this page you
will find, under a __Certificates__ heading, any certificates you've uploaded,
likely including your soon-to-expire certificate. Since I'm not aware of a way
to update a certificate in place, I chose to add my updated certificate along
side the existing one. Click __Add Certificate__, and in the dialog now choose
__Bring your own certificate__. Fill out the form, giving your certificate a
unque name.

The information you need to fill out the rest of the form should be found under
`/etc/letsencrypt/live/<your domain.com>/`. Copy the contents of `cert.pem` to
the field labeled __Certificate__; copy the contents of `privkey.pem` to the
field labeled __Private key__; then copy the contents of `chain.pem` to the
field labeled __Certificate chain__. Click __Save SSL Certificate__.

Now all you have to do is update the appropriate forwarding rules for your load
balancer, however you've got it set up. As this can vary a bit between
configurations, I'll leave this part to you.

Ĝis la revido!
