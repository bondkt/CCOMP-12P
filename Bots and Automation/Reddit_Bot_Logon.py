# *===============================================
# * DESCRIPTION
# *===============================================
# File Name: Reddit_Bot_Logon.py
# CCOMP-12P
# Spring 2021
# *===============================================

# *===============================================
# * LIBS
# *===============================================

# import Python Reddit API Wrapper
import praw 

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
appName = "Reddit Bot Logon"
appVersion = "1.0.0"
appArch = "x86&x64"
appLang = "EN"
appScriptVersion = "1.0.0"
appScriptDate = "2021.04.01"
appScriptAuthor = "KTeuton"

# *===============================================
## Misc. Variables
# *===============================================

# initialize with appropriate values 
client_id = "" 
client_secret = "" 
username = "itchy-throat-6754" 
password = "" 
user_agent = "python test script by u/itchy-throat-6754" 

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

# connect to natureisfuckinglit and pull the top post to prove the connection is working
subreddit = reddit.subreddit('natureisfuckinglit') 
# for each submission in the list of top submissions...
for submission in subreddit.top(limit = 1): 
    # displays the submission title 
    print(f"Title:", submission.title)   
    # displays the net upvotes of the submission 
    print(f"Upvotes:", submission.score)   
    # displays the submission's ID 
    print(f"ID:",submission.id)    
    # displays the url of the submission 
    print(f"URL:",submission.url)  

# submitting a post
# title of the post
post_title="Testing Bot - KTeuton"
# body of the post
post_body="This is a test bot, made by KTeuton."
# connect to mechanicalMercs, and post the title and body
reddit.subreddit('mechanicalMercs').submit(title=post_title, selftext=post_body)

# the ID of the comment 
comment_id = "gsv5h7i"
# instantiating the Comment class 
comment = reddit.comment(comment_id)
print("Score before upvoting: " + str(comment.score)) 
# upvoting the comment
comment.upvote() 
# refresh the comment
# learned from: https://www.reddit.com/r/redditdev/comments/izlqfu/does_praw_upvote_work/
comment.refresh()
print("Score after upvoting: " + str(comment.score)) 
