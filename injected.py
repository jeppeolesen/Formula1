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
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

def updateCountdown(subredditObject):
    try:
        print("Updating the F1 sidebar")
        nextRace = nextDate()
        delta = datetime.datetime(int(nextRace[0]), int(nextRace[1]), int(nextRace[2]), int(nextRace[3])) - datetime.datetime.utcnow()
        hours = int((delta.seconds - delta.seconds%3600)/3600)
        minutes = int((delta.seconds%3600)/60)
        wikiContent = r.subreddit('formula1').wiki['sidebar'].content_md
        countdown = "{0} day{1}, {2} hour{3} and {4} minute{5}".format(delta.days, "s"*(delta.days != 1), hours, "s"*(hours != 1),  minutes, "s"*(minutes != 1))
        sidebar = wikiContent.replace("{countdown}", countdown)
        subredditObject.mod.update(description=sidebar)
        print("Sucessfully updated the sidebar")
    except Exception as e:
        print "Error: {}".format(e)

def nextDate():
    dates = [[2017, 3, 26, 6], [2017, 4, 9, 7], [2017, 4, 16, 16], [2017, 4, 30, 13], [2017, 5, 14, 13], [2017, 5, 28, 13], [2017, 6, 11, 19], [2017, 6, 25, 14], [2017, 7, 9, 13], [2017, 7, 16, 13], [2017, 7, 30, 13], [2017, 8, 27, 13], [2017, 9, 3, 13], [2017, 9, 17, 13], [2017, 10, 1, 9], [2017, 10, 8, 6], [2017, 10, 22, 20], [2017, 10, 29, 19], [2017, 11, 12, 16],[2017, 11, 26, 21]]
    currentDate = datetime.datetime.utcnow()
    for date in dates:
        thenDate = datetime.datetime(date[0], date[1], date[2], date[3])
        if currentDate < thenDate:
            return date
    return dates[-1]

updateCountdown(subreddit)
    
