#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u'Hai Lang'
SITENAME = u'Raging Scholars'
SITEURL = 'www.hailang.me'

TIMEZONE = 'Asia/Kuala_Lumpur'

DEFAULT_LANG = u'en'

# Blogroll
LINKS =  (
            ('FreeBSD Project', 'http://freebsd.org'),
            ('Google', 'http://google.com'),
         )

# Social widget
SOCIAL = (
            ('Ren TianZi', 'http://rentianzi.com'),
        )

DEFAULT_PAGINATION = 10

###Extra Configurations
USE_FOLDER_AS_CATEGORY = True
DEFAULT_CATEGORY = 'Misc'
DISPLAY_PAGES_ON_MENU = True

###URL Settings
#ARTICLE_URL = 'posts/{slug}.html'
#ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/{category}/{slug}.html'
ARTICLE_URL = 'posts/{date:%Y}/{date:%b}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/{slug}/index.html'
PAGE_URL = 'pages/{slug}.html'
PAGE_SAVE_AS = 'pages/{slug}.html'
AUTHOR_URL = 'author/{slug}.html'
AUTHOR_SAVE_AS = 'author/{slug}.html'
CATEGORY_URL = 'category/{slug}.html'
CATEGORY_SAVE_AS = 'category/{slug}.html'
TAG_URL = 'tag/{slug}.html'
TAG_SAVE_AS = 'tag/{slug}.html'

###Feed Settings
FEED_DOMAIN = 'http://feed.hailang.me'

###Theme Settings
THEME = "pelican-chunk"
#THEME = "dev-random"
DEFAULT_DATE_FORMAT = ('%b %d %Y')
SITESUBTITLE = "uprintf(\'There is no place like ::1\');"
FOOTER_TEXT = "<b>Powered by <a href='http://getpelican.com'>Pelican</a> Theme by <a href='http://bunnyman.info'>tBunnyMan</a></b>"
DISPLAY_CATEGORIES_ON_MENU = True
SINGLE_AUTHOR = False
MINT = False
LINKS = (
            ('HOME', 'http://hailang.me'),
        )

###MISC
DISQUS_SITENAME = 'ragingscholars'
GOOGLE_ANALYTICS = 'UA-12039368-4'
