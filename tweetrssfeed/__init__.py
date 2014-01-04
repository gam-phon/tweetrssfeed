#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tweet RSS Feed.

Usage:
  tweetrssfeed [--all] [--short] <username> <urls>...
  tweetrssfeed [--fetch] <username> <urls>...
  tweetrssfeed --short <username> <urls>...
  tweetrssfeed (-h | --help)
  tweetrssfeed --version

Options:
  -h --help     Show this screen.
  --version     Show version.
  --fetch       Just fetch feeds into Database without tweeting them.
  --all         Tweet all RSS Feeds that are in the rss now.
  --short       Shorten links with bitly

"""

from docopt import docopt

from tweetrssfeed import tweet_rss

__author__ = 'Yaser Alraddadi'
__email__ = 'yaser@yr.sa'
__version__ = '0.1.0'


def main():
    arguments = docopt(__doc__, version='Tweet RSS Feed 0.1')
    for url in arguments['<urls>']:
        tweet_rss(arguments['<username>'], url, short=arguments['--short'], fetch=arguments['--fetch'], all=arguments['--all'])


if __name__ == '__main__':
    main()
