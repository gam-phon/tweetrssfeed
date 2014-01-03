========
Usage
========

To use Tweet RSS Feed in a project. First export your access tokens in your environments for your twitter and bitly account. For example my twiiter account is "gam-phon"::

    export gam-phon_BITLY_ACCESS_TOKEN=""
    export gam-phon_TWITTER_CONSUMER_KEY=""
    export gam-phon_TWITTER_CONSUMER_SECRET=""
    export gam-phon_TWITTER_ACCESS_TOKEN=""
    export gam-phon_TWITTER_ACCESS_TOKEN_SECRET=""

Then::

	from tweetrssfeed import tweet_rss
    tweet_rss(username, url, short=False, fetch=False, all=False)

For cron job::

    #set virtual environments 
    gam-phon_BITLY_ACCESS_TOKEN=""
    gam-phon_TWITTER_CONSUMER_KEY=""
    gam-phon_TWITTER_CONSUMER_SECRET=""
    gam-phon_TWITTER_ACCESS_TOKEN=""
    gam-phon_TWITTER_ACCESS_TOKEN_SECRET=""
    * * * * * path/to/env/python path/to/tweetrssfeed.py


To use the command lines::

    Usage:
        tweetrssfeed.py [--all] [--short] <username> <urls>...
        tweetrssfeed.py [--fetch] <username> <urls>...
        tweetrssfeed.py --short <username> <urls>...
        tweetrssfeed.py (-h | --help)
        tweetrssfeed.py --version

    Options:
        -h --help     Show this screen.
        --version     Show version.
        --fetch       Just fetch feeds into Database without tweeting them.
        --all         Tweet all RSS Feeds that are in the rss now.
        --short       Shorten links with bitly