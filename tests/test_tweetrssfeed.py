#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_tweetrssfeed
----------------------------------

Tests for `tweetrssfeed` module.
"""

import unittest

from tweetrssfeed import twitter_connection, bitly_connection


def test_twitter(api):
    ''' Test Twitter '''
    twitter_name = api.me().name
    assert twitter_name is not None
    print(twitter_name)


def test_bitly(api):
    data = api.shorten('http://google.com/')
    assert data is not None
    assert data['long_url'] == 'http://google.com/'
    assert data['hash'] is not None
    print(data['url'])


class TestTweetrssfeed(unittest.TestCase):

    def setUp(self):
        pass

    def test_something(self):
        pass

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
    # Access
    api_twitter = twitter_connection()
    api_bitly = bitly_connection()

    #Test
    test_twitter(api_twitter)
    test_bitly(api_bitly)
