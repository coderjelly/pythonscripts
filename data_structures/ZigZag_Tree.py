
class Node:
	def __init__(self,val):
		self.left = None
		self.right = None
		self.data = val

n1 = Node(0)
n2 = Node(2)
n3 = Node(6)
n4 = Node(-3)
n5 = Node(3)
n6 = Node(7)
n7 = Node(5)
n8 = Node(9)
n9 = Node(11)
n10 = Node(-1)

#			0
#		2	 	 6
# 	-3		3		 5
# -1	11		7		9

#create tree
root = n1
n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
n5.right = n6
n3.right = n7
n7.right = n8
n5.left = n9
n4.left = n10

def zigZag(node):
	if node is None:
		return

	stack1 = []
	stack2 = []

	stack1.append(node)

	while (stack1 or stack2):

		while stack1:
			thisnode = stack1.pop()
			print thisnode.data,
			if thisnode.right is not None:
				stack2.append(thisnode.right)
			if thisnode.left is not None:
				stack2.append(thisnode.left)
		print " "

		while stack2:
			thisnode = stack2.pop()
			print thisnode.data,		
			if thisnode.left is not None:
				stack1.append(thisnode.left)
			if thisnode.right is not None:
				stack1.append(thisnode.right)
		print " "


zigZag(root)







