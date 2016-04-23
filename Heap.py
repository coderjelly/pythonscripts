# Author: coderjelly
# Script in Python giving heap examples

import heapq

y = [1,4,3,-2,0,9,11,8]


#method 1
heapq.heapify(y)

z = []

#method 2 to create heap from y

for item in x:
	heapq.heappush(z,item)

#print them

while y:
	item = heapq.heappop(y)
	print item


while z:
	item = heapq.heappop(z)
	print item