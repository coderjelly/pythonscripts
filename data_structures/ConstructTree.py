# Construct a Binary Tree from Postorder and Inorder
# Given Postorder and Inorder traversals, construct the tree.

class Node:
	def __init__(self,val):
		self.val = val
		self.left = None
		self.right = None


def createTree(inorder,postorder):
	li = len(inorder)
	lp = len(postorder)

	if li == 0 or lp == 0 or lp != li:
		return None

	if li == 1:
		return Node(inorder[0])

	root = postorder[-1]

	#divide it:
	for i in xrange(li):
		if inorder[i] == root:
			break
	leftstri = inorder[:i]
	rightstri = inorder[i+1:]

	rightstrp  = postorder[len(leftstri):lp-1]
	leftstrp = postorder[:len(leftstri)]

	print leftstrp, rightstrp
	print leftstri, rightstri

	leftchild = createTree(leftstri,leftstrp)
	rightchild = createTree(rightstri,rightstrp)

	currNode = Node(root)
	currNode.left = leftchild
	currNode.right = rightchild
	return currNode

def inorder(nod):
	if nod is None:
		return
	inorder(nod.left)
	print nod.val,
	inorder(nod.right)


inord = [4, 8, 2, 5, 1, 6, 3, 7]
postord = [8, 4, 5, 2, 6, 7, 3, 1]

inorder(createTree(inord,postord))


