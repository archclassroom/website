#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Arch Linux Classroom'
SITENAME = 'Arch Linux Classroom'
SITEURL = 'https://archclassroom.github.io'

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

#Menu
MENUITEMS = (('Upcoming classes', '#'),)

# Blogroll
LINKS = (('Arch Wiki', 'https://wiki.archlinux.org/index.php/Classroom'),
         ('Github', 'https://github.com/archclassroom'),
         ('Code of Conduct', 'https://wiki.archlinux.org/index.php/Code_of_conduct'),)

# Social widget
SOCIAL = (('Connecting to IRC chat', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 6

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
