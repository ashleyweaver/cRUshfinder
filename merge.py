#!/usr/bin/python2

import simplejson as json
import strip

#add stuff for getting the json from the server here

f = open("ru_crushes-user_timeline.json","r")
nf = open("cache.json","a")
fcheck = open("curmax.txt","r")

curMax = fcheck.readline().strip()

uncleanList = json.load(f)
f.close()

i = 0
while i<200:
	i+=1


cleanedList = strip.main(uncleanList)
json.dump(cleanedList,nf)
nf.close()
