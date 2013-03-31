#!/usr/bin/python

import string
import simplejson as json
from operator import itemgetter

# This entire script will be moved into a function to be called by another script.
# This other script will import the newest tweets into an array then remove all dupes
# from the array. This shortened array will be passed to the strip function. The
# stripped array will then be appended to the cache.

# These are the 100 most commonly used words in English according to Wikipedia.
removedWords = ["the","be","to","of","and","a","in","that","have","i","it","for","not","on","with","he","as","you","do","at","this","but","his","by","from","they","we","say","her","she","or","an","will","my","one","all","would","there","their","what","so","up","out","if","about","who","get","which","go","me","when","make","can","like","time","no","just","him","know","take","people","into","year","your","good","some","could","them","see","other","than","then","now","look","only","come","its","over","think","also","back","after","use","two","how","our","work","first","well","way","even","new","want","because","any","these","give","day","most","us"]

f = open("ru_crushes-user_timeline.json","r")
nf = open("ru_crushes-clean.json","w")

uncleanList = json.load(f)
f.close()
cleanedList = []

for item in uncleanList:
	words = string.split(item["text"])
	newWords = []
	while len(words)>0:
		# This lowercases the words, strips punctuation, then removes mid-word apostrophes to
		# handle posessives. I don't know whether anyone is going to hashtag the name of the
		# person they have a crush on so I included octothorpes in the punctuation filter.
		word = string.split(string.strip(string.lower(words.pop()),",.!?';:#"),"'")[0]
		
		add = True
		for rmWord in removedWords:
			if rmWord == word:
				add = False
				break
		if add:
			newWords.append(word)
	cleanedItem = {"words" : newWords,"id" : item["id_str"],"date" : item["created_at"],"coincidence":0}
	cleanedList.append(cleanedItem)

json.dump(cleanedList,nf)

nf.close()