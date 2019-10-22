#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'signal9'
SITENAME = 'Letters'
SITESUBTITLE = 'from the workshop'
SITEURL = 'https://letters.vexingworkshop.com'

PATH = 'content'
STATIC_PATHS = [
    'files/keybase.txt',
    'files/robots.txt',
    'files/security.txt'
]
EXTRA_PATH_METADATA = {
    'files/keybase.txt': {'path': 'keybase.txt'},
    'files/robots.txt': {'path': 'robots.txt'},
    'files/security.txt': {'path': '.well-known/security.txt'}
}

TIMEZONE = 'America/Denver'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
THEME = './themes/letters'

# Blogroll
LINKS = (('Electronic Frontier Foundation', 'https://www.eff.org'),
         ('Esperanto USA', 'https://esperanto-usa.org'),)

# Social widget
SOCIAL = (('GitHub', 'https://github.com/coyote240'),
          ('Twitter', 'https://twitter.com/AdamAGShamblin'),
          ('LinkedIn', 'https://www.linkedin.com/in/adam-shamblin/'),
          ('Webring', 'https://webring.xxiivv.com/#random'))

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
