import praw
from collections import Counter
list = ['ftfy', 'imo', 'DAE', 'ELI5', 'imho', 'TIL', 'IIRC', 'ITT', 'TLDR', 'TL;DR', 'MIC', 'MFW', 'SMH', 'MRW', 'AFAIK', 'AMA', 'FFS', 'NFSW', 'NSFL', 'TIFU', 'OP', '/s', 'SJW', 'Neckbeard', 'Karmawhore', 'Shitpost', 'Circlejerk' 'rip my inbox']
reddit = praw.Reddit(client_id='BvQLViitNTyU6A',
                     client_secret='IgYF_uDdUYH2Jl8tpY9UFuCf1yY',
                     password='Password1',
					 user_agent='This will be a script',
                     username='awaythrowcs')
print (reddit.user.me())
submission = reddit.submission(url='https://www.reddit.com/r/Jokes/comments/7fukkv/i_wish_my_college_was_run_by_ea/')
submission.comments.replace_more(limit=0)
for top_level_comment in submission.comments:
    if any(word in top_level_comment.body for word in list):
        help = Counter(top_level_comment.body.split()).most_common()
        print(help[:10])