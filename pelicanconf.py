#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Mark Gondree'
SITENAME = u'[d0x3d!]'
HIDE_SITENAME = True

SITEURL = 'http://localhost:8000'
SITELOGO = None
JUMBOLOGO = 'images/logo.png'
SITELOGO_SIZE = '30'
FAVICON = 'images/favicon.ico'

TIMEZONE = 'US/Pacific'
DEFAULT_LANG = u'en'

# We will not really use this as a blog
SUMMARY_MAX_LENGTH = 2000
DEFAULT_PAGINATION = 1000
USE_PAGER = False

# Plugins
PLUGIN_PATHS = ["plugins"]
PLUGINS = ['i18n_subsites']


JINJA_ENVIRONMENT = {
    'extensions': ['jinja2.ext.i18n'],
}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

PATH = 'content'
BOOTSTRAP_THEME = ""

STATIC_PATHS = ['images',
    'extras/css/d0x3d.css',
    #'extras/CNAME',
    #'extras/google14081f6503dca9ab', # req'd for Google+ website verification
]

EXTRA_PATH_METADATA = {
    'extras/css/d0x3d.css': {'path': 'css/d0x3d.css'},
    #'extras/CNAME' : {'path': 'CNAME'},
    #'extras/google14081f6503dca9ab' : {'path' : 'google14081f6503dca9ab.html'},
}

# Category options
USE_FOLDER_AS_CATEGORY = True
CATEGORY_SAVE_AS = 'category/{slug}.html'
DEFAULT_CATEGORY = 'Blog'

# Article saving options
ARTICLE_URL = 'article/{slug}.html'
ARTICLE_SAVE_AS = 'article/{slug}.html'
INDEX_SAVE_AS = 'all.html'
DISPLAY_ARTICLE_INFO_ON_INDEX = False

# Article meta info shown
SHOW_ARTICLE_AUTHOR = False
SHOW_DATE_MODIFIED = False
SHOW_SERIES = False
SHOW_ARTICLE_CATEGORY = False
PDF_PROCESSOR = False

# Menu items
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_ARCHIVE_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False
DISPLAY_SOCIAL_ON_MENU = False
MENUITEMS = (('welcome', './index.html'),
             ('get the game', './get'),
             ('ideas for use', './ideas'),
             ('about', './about'),
             ('faq', './faq'),
             ('media', './media'),
            )

# Sidebar options
AVATAR = None
HIDE_SIDEBAR = True
LINKS = ()

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/d0x3d'),
          ('youtube', 'https://www.youtube.com/user/TableTopSecurity'),
          ('flickr', 'https://www.flickr.com/tabletopsecurity'),
          ('boardgamegeek', 'https://boardgamegeek.com/boardgamepublisher/23997/tabletop-security'),
          ('google-plus', 'https://plus.google.com/114066012466458862886'),
          ('github', 'http://github.com/tabletopsecurity')
         )

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Theme related settings
THEME = 'themes/pelican-bootstrap3'
THEME_STATIC_PATHS=['static']
CSS_FILE='d0x3d.css'
CUSTOM_CSS = 'css/d0x3d.css'

# Caching
LOAD_CONTENT_CACHE = False
