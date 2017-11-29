import praw
from collections import Counter
import json

def words_in_string(word_list, a_string):
    return set(word_list).intersection(a_string.split())

redditisms = ['FTFY', 'IMO', 'DAE', 'ELI5', 'imho', 'TIL', 'IIRC', 'ITT', 'TLDR', 'TL;DR', 'MIC', 'MFW', 'SMH', 'MRW', 'AFAIK', 'AMA', 'FFS', 'NFSW', 'NSFL', 'TIFU', 'OP', '/s', 'SJW', 'Neckbeard', 'Karmawhore', 'Shitpost', 'Circlejerk' 'rip my inbox']
reddit = praw.Reddit(client_id='BvQLViitNTyU6A',
                     client_secret='IgYF_uDdUYH2Jl8tpY9UFuCf1yY',
                     password='Password1',
					 user_agent='This will be a script',
                     username='awaythrowcs')
print (reddit.user.me())
submission = reddit.submission(url='https://www.reddit.com/r/movies/comments/488gjl/leo_gets_the_oscar/')
submission.comments.replace_more(limit=0)

commentDict = {}

dataFile = open('redditisms.txt', 'w')

def commentSearch(comments, karma):
    for word in comments:
        for redditism in redditisms:
            if word.upper() == redditism:
                commentDict[redditism] = karma
    return;

for sub in submission.comments.list():
    help1 = sub.body.encode('utf-8').split()
    commentSearch(sub.body.encode('utf-8').split(), sub.score)

for pairs in commentDict.iteritems():
    print>>dataFile, pairs
