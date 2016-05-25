#author : coderjelly


class Stack:

	totalitems = 0

	def __init__(self):
		self.stacklist = []

	def push(self,val):
		if val is not None:
			self.stacklist.append(val)
			Stack.totalitems += 1

	def pop(self):
		if Stack.totalitems == 0:
			return None
		Stack.totalitems -= 1
		return self.stacklist.pop()

	def printStack(self):
		if Stack.totalitems == 0:
			return
		print "Printing in LIFO form:"
		for item in self.stacklist:
			print item


a = [4, 5, 7, -1, 9]

s = Stack()

for i in a:
	s.push(i)

s.printStack()

while(True):
	t = s.pop()
	if t is None:
		print "Underflow!..breaking..."
		break
	print t 

s.printStack()







