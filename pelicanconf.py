#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'MB'
SITENAME = "Apps in Integrative Analytics and Informatics"
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Pacific/Honolulu'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


# Blogroll
# LINKS = (('ICS', 'http://www.ics.hawaii.edu/'),
#          ('HIMB', 'http://www.himb.hawaii.edu/'),
#          ('HI-DSI', 'http://datascience.hawaii.edu/'),)

# Social widget
SOCIAL = (('LinkedIn', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

STATIC_PATHS = ['images']

#Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True


DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
MENUITEMS = (
    ('HOME', '/'),
    ('ABOUT', '/pages/about.html'),
    ('PEOPLE', '/pages/people.html'),
    ('CONTACT', '/pages/contact.html'),
)

THEME= "notmyidea"

USE_FOLDER_AS_CATEGORY = True
ARTICLE_SAVE_AS = '{category}/{slug}.html/'
