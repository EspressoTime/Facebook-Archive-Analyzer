import re
import datetime
import numpy as np
import matplotlib.pyplot as plt

def extractFriendCount():
	# Read in friend.htm file
	with open('friends.htm') as file:
	   fileContent = file.read()

	# Match only list of current friends
	matchObj = re.search(r'<h2>Friends</h2><ul>(<li>(.+?)</li>)</ul>', fileContent)
	friends = matchObj.group(1)

	# Extract complete date each friend added (removes names and html tags)
	friendsMatch = re.findall('<li>[a-zA-Z ]+\((.+?)\)</li>', friends)

	# Find any dates without year listed (from current year) and add year
	for idx in range(len(friendsMatch)):
		ea = friendsMatch[idx]
		if len(ea) < 10:
			friendsMatch[idx] = ea + ", " + str(datetime.datetime.now().year)

	# Extract year only
	friendCount = {}
	for ea in friendsMatch:
		yearMatch = re.search('.+?, ([0-9]+)', ea)
		friendCount[yearMatch.group(1)] = friendCount.get(yearMatch.group(1), 0) + 1

	return friendCount

def makeGraph(friendCount):
	# Create sorted array of counts 
	data = []
	for ea in sorted(friendCount):
		data.append(friendCount[ea])

	# Pyplot defaults
	ind = np.arange(len(friendCount))    # Set number of graph bars to number of items in dictionary
	width = 0.35       # the width of the bars: can also be len(x) sequence
	p1 = plt.bar(ind, data, width) # add data array 

	# Chart labels
	plt.ylabel('Friends Added')
	plt.title('Facebook Friends Added by Year')
	xAxisLabels = [] # Create x-axis labels from dictionary
	for key in sorted(friendCount):
		xAxisLabels.append(key)

	# Get maximum data point and set appropriate increment scale
	data_max = max(data)
	if data_max < 16:
		increment = 1
	elif data_max < 50:
		increment = 5
	elif data_max < 100:
		increment = 10
	else:
		increment = 50
	max_label = data_max + (increment * 3)

	plt.xticks(ind, xAxisLabels)
	plt.yticks(np.arange(0, max_label, increment))

	return p1

# Add text value label above each bar
def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                '%d' % int(height),
                ha='center', va='bottom')

def main():
	friendCount = extractFriendCount()
	p1 = makeGraph(friendCount)
	autolabel(p1)
	plt.show()

if __name__ == '__main__':
	main()