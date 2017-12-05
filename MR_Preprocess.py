import praw
from praw.models import Comment
import sys
import json

outfile = sys.argv[1] # file to print output to
sub = sys.argv[2] #subreddit to pull from
numPosts = int(sys.argv[3])
print(numPosts)

reddit = praw.Reddit(client_id='BvQLViitNTyU6A',
                     client_secret='IgYF_uDdUYH2Jl8tpY9UFuCf1yY',
					 user_agent='This will be a script',
                    )

sub = reddit.subreddit(sub)

outfile = open(outfile, 'w')

for post in sub.hot(limit = numPosts): #every post that we can get from this request
    post.comments.replace_more(limit=None) # getting rid of MoreComments objects
    for comment in post.comments.list(): # every comment in the flattened comment tree
        if isinstance(comment, Comment):
            karma = comment.score
            output = comment.body.encode('utf-8').replace('\n', '').replace('\t', '')
            outfile.write(str(karma) + " " + output + "\n")

# **debugging**
# post = reddit.submission(url='https://www.reddit.com/r/redditdev/comments/16a0p8/reddit_comments_list_api_acting_funny/')
# post.comments.replace_more(limit=None)
# for comment in post.comments.list(): # every comment in the flattened comment tree
#     if isinstance(comment, Comment):
#         karma = comment.score
#         output = comment.body.encode('utf-8').replace('\n', '')
#         outfile.write(output + " " + str(karma) +  "\n")
# **debugging**
outfile.close()
