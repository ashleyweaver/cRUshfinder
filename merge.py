#!/usr/bin/python2

import simplejson as json
import strip

#add stuff for getting the json from the server here

f = open("ru_crushes-user_timeline.json","r")
nf = open("ru_crushes-clean.json","w")

uncleanList = json.load(f)
f.close()

cleanedList = strip.main(uncleanList)
json.dump(cleanedList,nf)
nf.close()
