# *===============================================
# * DESCRIPTION
# *===============================================
# File Name: More-Bot.py
# CCOMP-12P
# Spring 2021
# *===============================================

# *===============================================
# * LIBS
# *===============================================

# import Python Reddit API Wrapper
import praw 

# import regular expressions library
import re

# *===============================================

# *===============================================
# * LICENSE_INFO
# *===============================================

# If I had license info, it would go here...

# *===============================================

# *===============================================
# * VARIABLE DECLARATION
# *===============================================
## Variables: Application
appName = "More Bot"
appVersion = "1.0.0"
appArch = "x86&x64"
appLang = "EN"
appScriptVersion = "1.0.0"
appScriptDate = "2021.04.09"
appScriptAuthor = "KTeuton"

# *===============================================
## Misc. Variables
# *===============================================

# reddit bot login details
client_id = "" 
client_secret = "" 
username = "" 
password = "" 
user_agent = "" 

# list of comments that have been replied to
comm_list = []

# keyword for searching posts
keyword = "bot"

# *===============================================

# Reddit bot code taken from: https://levelup.gitconnected.com/creating-a-reddit-bot-using-python-5464d4a5dff2

# creating an authorized reddit instance 
reddit = praw.Reddit(
    client_id = client_id,  
    client_secret = client_secret,  
    username = username,  
    password = password, 
    user_agent = user_agent
)

# test account connection
# learned from: https://praw.readthedocs.io/en/latest/getting_started/authentication.html#
print(f"Connected to Reddit as:", reddit.user.me())

# connect to the subreddit
subreddit = reddit.subreddit('mechanicalMercs')

# for each submission in the subreddit (up to 50 submissions)
# learned from https://www.pythonforengineers.com/build-a-reddit-bot-part-2-reply-to-posts/
for submission in subreddit.hot(limit=50):
    # using regular expressions, see if the keyword exists in the title
    if re.search(keyword, submission.title, re.IGNORECASE):
        # if the keyword exists in the title...
        # print that we found a matching submission
        print(f"Found post with keyword: {keyword}. Submission ID: {submission.id}. Commenting...")
        # append the submission ID to the list, for tracking
        comm_list.append(submission.id)
        # reply back to the submission
        submission.reply(f"itchy-throat-6754 bot says: Found post containing the word: {keyword}! \n\n Hello! \n\n List of posts commented on this session, so far: {len(comm_list)} | {comm_list}")
        # print the list of submissions that have been commented on this session
        print(f"List of posts commented on this session: ({len(comm_list)}) | {comm_list}")
        # upvote the submission
        reddit.submission(submission.id).upvote()
