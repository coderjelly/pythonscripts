#Author: Coderjelly
# DFS order traversal of a tree

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

#			0
#		2	 	 6
#	-3		3		 5
#				7

#create tree
root = n1
n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
n5.right = n6
n3.right = n7


# inorder
def inorder(nod):
	if nod is None:
		return
	inorder(nod.left)
	print(nod.data)
	inorder(nod.right)

# postorder
def postorder(nod):
	if nod is None:
		return	
	postorder(nod.left)
	postorder(nod.right)
	print(nod.data)


inorder(root)
print("\n")
postorder(root)
