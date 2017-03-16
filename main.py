#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This code was written for /r/formula1
Written by /u/Redbiertje
16 March 2017
"""

#Imports
from __future__ import division
import datetime
import botData as bd
import time
import praw

#Login
r = praw.Reddit(client_id=bd.app_id, client_secret=bd.app_secret, password=bd.password, user_agent=bd.app_user_agent, username=bd.username)
if(r.user.me()=="F1-Bot"):
    print("Successfully logged in")
subreddit = r.subreddit("formula1")
private_subreddit = r.subreddit("formula1bot")

#Keep the bot alive
while True:
    try:
        currentTime = datetime.datetime.utcnow()
        print("[{0}:{1}:{2}] New loop".format(currentTime.hour, currentTime.minute, currentTime.second))
        execfile("injected.py", globals(), locals())
        time.sleep(30)
    except Exception as e:
        print("Major error in loop: {}".format(e))
