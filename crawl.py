#!/usr/bin/python
# -*- coding: utf-8 -*-

# Twitter Clawler
#  (C) Takekatsu Hiramura
#
# Usage:
#  python clawl.py

#  Python-twitter https://pypi.python.org/pypi/twitter


from twitter import *
from time import gmtime, strftime
import codecs

# Setting
t = Twitter(
            auth=OAuth(
                       "<YOUR_OAUTH_TOKEN>", # OAUTH_TOKEN
                       "<YOUR_OAUTH_SECRET>", # OAUTH_SECRET,
                       "<YOUR_CONSUMER_KEY>", # CONSUMER_KEY,
                       "<YOUR_CONSUMER_SECRET>" # CONSUMER_SECRET
                       )
           )
# Keyword
#id = "@SBCare"
id = "<TARGET_TWITTER_ID>" # Twitter ID
# Output directory
out_dir = "<OUTPUT_DIRECTORY>"

# Get timelines
timeline = t.search.tweets(q=id, count=200)

# Extract statuses
timeline_statuses = timeline['statuses']

# Parse
lines = []
for msg in timeline_statuses:
   #print msg
   text_escape = msg['text'].replace("\n"," ")
   line = str(msg['id'])+ '\t' +msg['created_at'] + '\t' + text_escape
   lines.append(line)

# Save
time=strftime("%Y%m%d_%H%M%S",gmtime())
f = codecs.open(out_dir + "tweet_"+time+".txt","a","utf-8")
f.write("\n".join(lines))
f.close()

