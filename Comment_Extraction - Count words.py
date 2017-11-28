import praw
from collections import Counter

def words_in_string(word_list, a_string):
    return set(word_list).intersection(a_string.split())

redditisms = ['ftfy', 'imo', 'DAE', 'ELI5', 'imho', 'TIL', 'IIRC', 'ITT', 'TLDR', 'TL;DR', 'MIC', 'MFW', 'SMH', 'MRW', 'AFAIK', 'AMA', 'FFS', 'NFSW', 'NSFL', 'TIFU', 'OP', '/s', 'SJW', 'Neckbeard', 'Karmawhore', 'Shitpost', 'Circlejerk' 'rip my inbox']
reddit = praw.Reddit(client_id='BvQLViitNTyU6A',
                     client_secret='IgYF_uDdUYH2Jl8tpY9UFuCf1yY',
                     password='Password1',
					 user_agent='This will be a script',
                     username='awaythrowcs')
print (reddit.user.me())
submission = reddit.submission(url='https://www.reddit.com/r/OutOfTheLoop/comments/1yqdkg/what_the_hell_does_ftfy_mean/')
submission.comments.replace_more(limit=0)
for sub in submission.comments.list():
    help1 = sub.body.split()
    print([sub.score, help1])