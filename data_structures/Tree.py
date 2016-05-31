# author : coderjelly

class Node:

	totalNodes = 0

	def __init__(self,val):
		if val is None:
			return
		self.left = None
		self.right = None
		self.data = val
		Node.totalNodes += 1

	def display(self):
		print "\t %d \t" % self.data

	def addNode(self,node,mode):
		if node is None:
			print "Cannot add null node"
		if mode == True:
			self.left = node
		else:
			self.right = node


class Tree:

	flag = True

	def __init__(self,node):
		if node is None:
			print "Cannot initialize"
		self.root = node

	def printTree(self,node):
		if node == None:
			return
		self.printTree(node.left)
		node.display()
		self.printTree(node.right)

	def addEdge(self,pnode,cnode):
		pnode.addNode(cnode,Tree.flag)
		Tree.flag = not Tree.flag


nroot = Node(0)
ntree = Tree(nroot)

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)

ntree.addEdge(nroot,n1)
ntree.addEdge(nroot,n2)
ntree.addEdge(n1,n3)
ntree.addEdge(n2,n4)

ntree.printTree(nroot)



