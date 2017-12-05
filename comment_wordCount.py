import praw
from collections import Counter
from collections import defaultdict
import json
import sys
import statistics as s

outfile = sys.argv[1] # file to print output to
sub = sys.argv[2] # subreddit to pull from
numPosts = int(sys.argv[3]) # number of posts to scrape]
print(numPosts)


# seach terms
redditisms = ['FTFY', 'IMO', 'DAE', 'ELI5', 'IMHO', 'TIL', 'IIRC', 'ITT', 'TLDR',
            'TL;DR','MIC', 'MFW', 'SMH', 'MRW', 'AFAIK', 'AMA', 'FFS', 'NFSW', 'NSFL',
            'TIFU', 'OP', '/S', 'SJW', 'NECKBEARD', 'KARMAWHORE', 'SHITPOST', 'CIRCLEJERK']

dataDict = {key: [] for key in redditisms}


# unauthorized reddit instance
reddit = praw.Reddit(client_id='BvQLViitNTyU6A',
                     client_secret='IgYF_uDdUYH2Jl8tpY9UFuCf1yY',
					 user_agent='This will be a script',
                    )
# r/cscareerquestions instance
sub = reddit.subreddit(sub)

# **debugging**
#
# for post in cscc.top(limit=1):
#     post.comments.replace_more(limit=None)
#     for comment in post.comments.list():
#         print(comment.body)
#         print("\n\n")
#
# submission = reddit.submission(url='https://www.reddit.com/r/AskReddit/comments/7gy8ve/whats_the_most_expensive_thing_youve_ever_touched/')
# submission.comments.replace_more(limit=None)
# for comment in submission.comments.list():
#     commentSearch(comment, outfile)
#
# **debugging**

def commentSearch(comment, outfile):

    karma = comment.score
    words = comment.body.encode('utf-8').upper().split()

    output = set(words).intersection(redditisms)

    for word in output:
        outfile.write(str(karma) + " " + word)

def commentSearch(comment):

    karma = comment.score
    words = comment.body.encode('utf-8').upper().split()

    output = set(words).intersection(redditisms)

    for word in output:
        dataDict[word].append(karma)

outfile = open(outfile, 'a')

for post in sub.hot(limit = numPosts): #every post that we can get from this request
    print(post.title + "\n")
    post.comments.replace_more(limit=None) # getting rid of MoreComments objects
    for comment in post.comments.list(): # every comment in the flattened comment tree
        commentSearch(comment)

for k, v in dataDict.items():
    if(v):
        outfile.write(k + " " + str(s.mean(v)) + '\n')

outfile.close()
