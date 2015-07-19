#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'ggshiney'
SITENAME = u'ggshiney blog'
SITEURL = ''
#SITEURL = 'http://blog.ggshiney.com'

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = u'zh'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('Pelican', 'http://getpelican.com/'),
          ('Python.org', 'http://python.org/'),
          ('Jinja2', 'http://jinja.pocoo.org/'),) 

# Social widget
SOCIAL = (('twitter', 'http://twitter.com/ggshiney'),
          ('github', 'http://github.com/ggshiney'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = '../pelican-themes/pelican-bootstrap3'
#THEME = 'elegant'

## URL Setting
ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}.html'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}.html'

## Theme Setting
# bootstrap3
DISPLAY_CATEGORIES_ON_MENU = []

