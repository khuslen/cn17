import json
#import urllib2
#import httplib
#import time
import praw
from praw.models import MoreComments

# Custom files
import commandFuncs
import formatOutput

##################################################

#####   LOGIC FOR API   ##########################

##################################################

# returns top subs with title and score

itemsArr = []
subId = []

# create an instance of reddit and subreddit using praw
# Zak's credentials lolz
reddit = praw.Reddit(client_id='ilgRMpq1J-Kx4w',
                     client_secret='wsjtyoqyNVKm0Ds8nTTGJNU-YIE',
                     user_agent='inter_webz')

def main_api_logic(subReddit, subreddit_sort, nextNum):

    # Stores the listed items in an array so we can access them with a number
    global itemsArr

    this_subreddit = reddit.subreddit(subReddit[1])

    if nextNum == 0:
        storeItems(this_subreddit, subreddit_sort)

    itemsData = []
    for item in commandFuncs.itemsArr:
        itemsData.append(item.title)

    formatOutput.printList(itemsData, nextNum, ["37;40m", "35;40m"])


def storeItems(subreddit, subreddit_sort):
    all_submissions_pre = "subreddit." + subreddit_sort + "(limit=100)"
    all_submissions = eval(all_submissions_pre)

    # for submission in subreddit.top(limit=100):
    for submission in all_submissions:
        commandFuncs.itemsArr.append(submission)
        subId.append(submission.id)


def readPost(itemNum):
    print 'reading post'
    print itemNum
    submission = reddit.submission(subId[itemNum -1])
    formatOutput.printPost(submission)


def readComments(itemNum):
    topComments = []
    print 'read comments'
    submission = reddit.submission(subId[itemNum - 1])
    for top_level_comment in submission.comments:
        if isinstance(top_level_comment, MoreComments):
            continue
        topComments.append(top_level_comment.body)
    
    formatOutput.printList(topComments, 0, ["32;40m", "36;40m"])
    
def saveSubmissions(subreddit):
    this_subreddit = reddit.subreddit(subreddit)

    if nextNum == 0:
        storeItems(this_subreddit, subreddit_sort)

    itemsData = []
    for item in commandFuncs.itemsArr:
        itemsData.append(item.title)
