# Find largest subtree having identical left and right subtrees
# Given a binary tree, find the largest subtree having identical left and 
# right subtree. Expected complexity is O( n ).
# For example,
# Input: 
#        50
#     /      \
#   10       60
# /  \         /   \
# 5   20   70    70
#             / \     / \
#         65  80 65  80
# Output: 
# Largest subtree is rooted at node 60



def FindLargestSubtree(lnode, rnode, depth):

	if lnode is None and rnode is None:
		return depth

	if lnode is not None:
		if rnode is not None:
			if lnode.val == rnode.val:
				lval = FindLargestSubtree(lnode.left,rnode.left,depth+1)
				rval = FindLargestSubtree(lnode.right,rnode.right,depth+1)
				if lval != rval:
					return min(lval,rval)
				return lval

			else:
				lval = FindLargestSubtree(lnode.left,lnode.right,0)
				rval = FindLargestSubtree(rnode.left,rnode.right,0)
				return max(lval,rval)

		else: #rnode is None
			return (FindLargestSubtree(lnode.left,lnode.right,0)

	else: #lnode is None
		return (FindLargestSubtree(rnode.left,rnode.right,0))