# Author: coderjelly
# Basic Node definition in python using classes

class Node:
	'basic Node definition'
	totalNodes = 0

	def __init__(self,value=0):
		self.left = None
		self.right = None
		self.value = value
		Node.totalNodes += 1
		print "\n#######"
		print "Node created, with value = %d" % value

	def printNode(self):
		print "\n_____________\n"
		print "Node value = " + str(self.value)
		if self.right is None:
			print "Right = None" 
		else:
			print "Right = " + str(self.right.value)
		if self.left is None:
			print "Left = None" 
		else:
			print "Left = " + str(self.left.value)



n1 = Node(4)
n1.printNode()

n2 = Node(7)
n2.printNode()

n3 = Node(8)
n3.printNode()

n3 = Node()
n3.printNode()

n1.right = n2
n1.left = n3
n1.printNode()

print Node.totalNodes