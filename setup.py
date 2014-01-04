#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(
    name='tweetrssfeed',
    version='0.1.5',
    description='Tweet RSS Feeds',
    long_description=readme + '\n\n' + history,
    author='Yaser Alraddadi',
    author_email='yaser@yr.sa',
    url='https://github.com/gam-phon/tweetrssfeed',
    packages=[
        'tweetrssfeed',
    ],
    package_dir={'tweetrssfeed': 'tweetrssfeed'},
    include_package_data=True,
    install_requires=[
        'tweepy==2.1',
        'feedparser==5.1.3',
        'bitly-api==0.3',
        'docopt==0.6.1',
    ],
    license="BSD",
    zip_safe=False,
    keywords='tweetrssfeed twitter rss',
    entry_points={'console_scripts': ["tweetrssfeed = tweetrssfeed:main"]},
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],
    test_suite='tests',
)