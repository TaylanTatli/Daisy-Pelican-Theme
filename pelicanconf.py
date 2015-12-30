#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# Site Settings
AUTHOR = 'Author Name'
SITENAME = 'Site Name'
SITEURL = 'http://site.url'
SITESUBTITLE="Site Subtitle"
SITEDESCRIPTION='Site Description''
THEME ='path/to/folder/Daisy'
PATH = 'content'

# General Settings
TIMEZONE = 'Europe/Istanbul'
DEFAULT_LANG = 'tr'
DISPLAY_CATEGORIES_ON_MENU = True
DISPLAY_PAGES_ON_MENU = True
DEFAULT_PAGINATION = 15
SUMMARY_MAX_LENGTH = 30
DISQUS_SITENAME = "disqussitename"

# Pages Settings
PAGE_URL = "{slug}/"
PAGE_SAVE_AS = "{slug}/index.html"

# Articles Settings
ARTICLE_URL = "posts/{slug}/"
ARTICLE_SAVE_AS = "posts/{slug}/index.html"

# Feed Generation
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/category/%s.atom.xml'
TAG_FEED_ATOM = 'feeds/tag/%s.atom.xml'
FEED_ALL_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'
TAG_FEED_RSS = 'feeds/tag/%s.rss.xml'

# Social Accounts
SOCIAL = (('gplus-circled', 'https://plus.google.com/u/0/+TaylanTatl%C4%B1'),
         ('facebook-circled', 'https://www.facebook.com/taylantatli34'),
         ('twitter-circled', 'https://twitter.com/tatlitaylan'),
         #('vimeo-circled', ''),
         #('pinterest-circled', ''),
         #('flickr-circled', ''),
         #('stumbleupon-circled', ''),
         ('tumblr-circled', 'http://eflatungemi.tumblr.com/'),
         ('lastfm-circled', 'http://www.last.fm/tr/user/tatlitaylan'),
         #('linkedin-circled', ''),
         #('rdio-circled', ''),
         #('skype-circled', ''),
         ('github-circled', 'https://github.com/TaylanTatli'),
         #('dribbble-circled', ''),
         #('spotify-circled', ''),
         )


# Extensions
MD_EXTENSIONS = [
'codehilite(css_class=highlight,linenums=False,guess_lang=True,use_pygments=True)',
'extra']
