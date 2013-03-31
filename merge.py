#!/usr/bin/python2

import simplejson as json
import strip

#add stuff for getting the json from the server here

FILE_LEN = 200

f = open("new.json","r")
cache = open("cache.json","r")
fcheck = open("curmax.txt","r")

curMax = int(fcheck.readline().strip())
fcheck.close()

oldCache = json.load(cache)
uncleanList = json.load(f)
f.close()

trimmedList = []

i = 0
while i<FILE_LEN:
	if int(uncleanList[FILE_LEN-1-i]['id']) > curMax:
		trimmedList.append(uncleanList[FILE_LEN-1-i])
		curMax = int(uncleanList[FILE_LEN-1-i]['id'])
	else:
		break
	i+=1

fwrite = open("curmax.txt","w")
fwrite.write(str(curMax) + "\n")
fwrite.close()

newCache = strip.main(trimmedList)

for item in newCache:
	oldCache.insert(0,item)

nf = open("cache.json","w")
json.dump(oldCache,nf)
nf.close()
