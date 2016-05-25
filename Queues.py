#Author: coderjelly

from collections import deque


class Queue:
	totalvals = 0

	def __init__(self):
		self.quelist = deque()

	def add(self, val):
		if val is None:
			print "Cannot add None"
			return
		self.quelist.append(val)
		Queue.totalvals += 1

	def remove(self):
		if Queue.totalvals == 0:
			return None
		t = self.quelist.popleft()
		Queue.totalvals -= 1
		return t

	def printQueue(self):
		if Queue.totalvals == 0:
			print "Nothing to show"
		for item in self.quelist:
			print item


a = [4, 5, 7, -1, 9]

q = Queue()

for i in a:
	q.add(i)

q.printQueue()

print "******"

while(True):
	t = q.remove()
	if t is None:
		break
	print t 

q.printQueue()

