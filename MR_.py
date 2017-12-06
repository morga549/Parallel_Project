import praw
from collections import Counter
import json
import statistics as s

redditisms = ['FTFY', 'IMO', 'DAE', 'ELI5', 'IMHO', 'TIL', 'IIRC', 'ITT', 'TLDR', 'TL;DR', 'MIC', 'MFW', 'SMH', 'MRW', 'AFAIK', 'AMA', 'FFS', 'NFSW', 'NSFL', 'TIFU', 'OP', '/S', 'SJW', 'NECKBEARD', 'KARMAWHORE', 'SHITPOST', 'CIRCLEJERK', 'RIP MY INBOX']

with open("helpme.txt") as f:
    content = f.readlines()

dataDict = {key: [] for key in redditisms}

def commentSearch(comment, karma):

    output = set(comment).intersection(redditisms)

    for word in output:
    	a = int(karma)
        dataDict[word].append(a)

    return;

for line in content:
	lista = line.split(" ", 1)
	help = lista[0]
	help1 = lista[1]
	commentSearch(help1.upper().split(), help) #AB helped on this piece.

for k, v in dataDict.items():
	if(v):
		print(k + " " + str(s.mean(v)))