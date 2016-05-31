# Author : coderjelly

class Node:

	def __init__(self,val):
		self.value = val
		self.link = None

	def showNode(self):
		print "\t" + str(self.value) +"   "+ str(id(self.link)) + "  --->"


class LinkedList:

	def __init__(self):
		LinkedList.totalnodes = 0
		LinkedList.head = None

	def add(self,val):
		if val is None:
			return
		ntemp = Node(val)
		if LinkedList.head == None:
			LinkedList.head = ntemp
			return
		ptr = LinkedList.head
		while(ptr.link is not None):
			ptr = ptr.link

		ptr.link = ntemp
		LinkedList.totalnodes += 1

	def display(self):
		if LinkedList.head is None:
			print "LinkedList Empty. Nothing to display"
			return
		ptr = LinkedList.head
		print "Linked List has %d Nodes:\n" % LinkedList.totalnodes
		while(ptr is not None):
			ptr.showNode()
			ptr = ptr.link


a = [4, 5, 7, -1, 9]

l = LinkedList()

for i in a:
	l.add(i)

l.display()





