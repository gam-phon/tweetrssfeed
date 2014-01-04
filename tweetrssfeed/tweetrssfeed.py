#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sqlite3

import tweepy
import feedparser
import bitly_api

BITLY_ACCESS_TOKEN = "BITLY_ACCESS_TOKEN"
TWITTER_CONSUMER_KEY = "TWITTER_CONSUMER_KEY"
TWITTER_CONSUMER_SECRET = "TWITTER_CONSUMER_SECRET"
TWITTER_ACCESS_TOKEN = "TWITTER_ACCESS_TOKEN"
TWITTER_ACCESS_TOKEN_SECRET = "TWITTER_ACCESS_TOKEN_SECRET"

DATABASE = "tweets.sqlite"


def check_env(*args):
    for arg in args:
        if arg not in os.environ:
            raise ValueError("Environment variable '{}' required".format(arg))


def bitly_connection(username):
    #Check Environments
    env_access_token = "{}_{}".format(username, BITLY_ACCESS_TOKEN)
    check_env(env_access_token)

    #Get Environments
    access_token = os.getenv(env_access_token)

    #Access
    bitly = bitly_api.Connection(access_token=access_token)
    return bitly


def twitter_connection(username):
    #Check Environments
    env_consumer_key = "{}_{}".format(username, TWITTER_CONSUMER_KEY)
    env_consumer_secret = "{}_{}".format(username, TWITTER_CONSUMER_SECRET)
    env_access_token = "{}_{}".format(username, TWITTER_ACCESS_TOKEN)
    env_access_token_secret = "{}_{}".format(username, TWITTER_ACCESS_TOKEN_SECRET)
    check_env(env_consumer_key, env_consumer_secret, env_access_token, env_access_token_secret)

    #Get Environments
    consumer_key = os.getenv(env_consumer_key)
    consumer_secret = os.getenv(env_consumer_secret)
    access_token = os.getenv(env_access_token)
    access_token_secret = os.getenv(env_access_token_secret)

    #Access
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    return api


def tweet_rss(username, url, short=False, fetch=False, all=False):
    #Access
    api_bitly = bitly_connection(username)
    api_twitter = twitter_connection(username)

    #Database Connection
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    #create the table if it doesn't exist
    c.execute('CREATE TABLE IF NOT EXISTS RSSContent (key TEXT, value TEXT)')

    # Fetch Feed
    d = feedparser.parse(url)
    #print(len(d['entries']))
    for entry in d['entries']:
        if not all:
            #check for duplicates
            c.execute('select * from RSSContent where key=? AND value=?', (username, entry['link']))

        if not c.fetchall():
            #Tweet feeds
            if not fetch:
                if short:
                    bitly_short = api_bitly.shorten(entry['link'])
                    api_twitter.update_status("%s %s" % (entry['title'][:115], bitly_short['url']))
                else:
                    api_twitter.update_status("%s %s" % (entry['title'][:115], entry['link']))
                print("Tweeted \"%s\" to %s account." % (entry['title'][:115], username))

            #Update database
            c.execute('insert into RSSContent values (?,?)', (username, entry['link']))
    conn.commit()
