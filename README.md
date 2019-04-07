# Letters

https://letters.vexingworkshop.com

## Goals

### No Frameworks!

* Using, as much as possible, only native browser frameworks
* Use WebComponents where practical for more involved features
* Use ES6 as much as is practical

#### How?

For now, I really only care about Firefox. This is my toy, and I feel perfectly
fine going retro-90's and saying that my site is best viewed with Firefox. That
being said, these should also be *standard* features, so they should work on
Firefox and webkit-derived browsers.

### Offline!

* Don't go blank or freak out when a device is offline
* Queue up network interactions where they can be

#### How?

_Offline First_ isn't quite the right term, as web pages have to be delivered to
an online client first, but it is my intention to build this site such that it
will keep working when offline, or fail gracefully where it may not.

### Multilingual, EN/EO

* Multilingual website, hosted in both English and Esperanto
* Navigation, etc. in both languages
* Content in both, if practical
* Easy to switch languages

#### How?

Proxy the `navigator.language` object and switch on change.
