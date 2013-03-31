import simplejson as json
from operator import itemgetter

def main(nam,fromDate):
	names = str.split(str.lower(nam))
	f = open("ru_crushes-clean.json","r")
	postList = json.load(f)
	f.close()
	
	# Find coincidence between tweet content and name array
	for name in names:
		for item in postList:
			for word in item["words"]:
				word = str.lower(word)
				if word == name:
					item["coincidence"]+=1
					break
	
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