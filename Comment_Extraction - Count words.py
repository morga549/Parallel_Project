import praw
from collections import Counter

reddit = praw.Reddit(client_id='BvQLViitNTyU6A',
                     client_secret='IgYF_uDdUYH2Jl8tpY9UFuCf1yY',
                     password='Password1',
					 user_agent='This will be a script',
                     username='awaythrowcs')
print (reddit.user.me())
submission = reddit.submission(url='https://www.reddit.com/r/cscareerquestions/comments/7cr3tf/should_i_continue_with_a_cs_major/')
submission.comments.replace_more(limit=0)
for top_level_comment in submission.comments:
    print(top_level_comment.body)
    help = Counter(top_level_comment.body.split()).most_common()
    print(help[:10])