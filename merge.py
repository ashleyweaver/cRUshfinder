#!/usr/bin/python2

import simplejson as json
import strip

#add stuff for getting the json from the server here

f = open("ru_crushes-user_timeline.json","r")
nf = open("cache.json","a")
fcheck = open("curmax.txt","r")

curMax = int(fcheck.readline().strip())
fcheck.close()

uncleanList = json.load(f)
f.close()

trimmedList = []

i = 0
while i<200:
	if int(uncleanList[199-i]['id']) > curMax:
		trimmedList.insert(0,uncleanList[199-i])
		curMax = int(uncleanList[199-i]['id'])
	i+=1

fwrite = open("curmax.txt","w")
fwrite.write(str(curMax) + "\n")
fwrite.close()

cleanedList = strip.main(trimmedList)
json.dump(cleanedList,nf)
nf.close()
