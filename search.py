import string
import simplejson as json
from operator import itemgetter

def main(nam,fullMatch,fromDate):
	names = string.split(string.lower(nam))
	f = open("cache.json","r")
	postList = json.load(f)
	f.close()
	
	# Find coincidence between tweet content and name array
	for name in names:
		for item in postList:
			for word in item["words"]:
				word = string.lower(word)
				if word == name:
					item["coincidence"]+=1
					break
	if fullMatch:
		i=0
		while i<len(postList):
			if postList[i]["coincidence"]!=len(names):
				del postList[i]
			else:
				i+=1
	else:
		# Remove all tweets with 0 coincidence
		i=0
		while i<len(postList):
			if postList[i]["coincidence"]==0:
				del postList[i]
			else:
				i+=1

		# Sort it ascending because I can't figure out how the hell
		# to sort it descending
		postList.sort(key=itemgetter('coincidence')) 

	# Then I just append the contents to an empty array, popping
	# them to reverse the order
	idArray = []
	while len(postList)>0:
		idArray.append(postList.pop()['id'])
	#print(idArray)

	return idArray
