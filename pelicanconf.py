#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Agnieszka Kramarek'
SITENAME = u'4gn3s coding'
SITESUBTITLE = 'Programming adventures of a girl'
SITEURL = 'https://4gn3s.github.io'
SITELOGO = SITEURL + '/images/profile.png'
FAVICON = SITEURL + '/favicon.ico'

ROBOTS = 'index, follow'

PATH = 'content'

TIMEZONE = 'Europe/Warsaw'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM =	'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DISPLAY_PAGES_ON_MENU = False # Don't display all pages by default

MAIN_MENU = True

MENUITEMS = (('Archives', '/archives.html'),
             ('Categories', '/categories.html'),
             ('Tags', '/tags.html'),)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

STATIC_PATHS = ['images', 'extra']

# Theme
THEME = "themes/Flex"

BROWSER_COLOR = "#333"

SOCIAL = (('facebook', 'https://www.facebook.com/agnieszka.kramarek'),
          ('github', 'https://github.com/4gn3s'),
          ('linkedin', ''),
          ('rss', '/feeds/all.atom.xml'),)

PYGMENTS_STYLE = 'monokai'

EXTRA_PATH_METADATA = {
    'extra/custom.css': {'path': 'static/custom.css'},
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'}
}
CUSTOM_CSS = 'static/custom.css'

# Plugins
PLUGIN_PATHS = ['./plugins']
PLUGINS = [
    'better_figures_and_images',
    'post_stats'
]

# Setting for the better_figures_and_images plugin
RESPONSIVE_IMAGES = True
FIGURE_NUMBERS = True
