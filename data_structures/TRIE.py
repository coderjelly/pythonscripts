# You are given a list of words. Find if two words can be joined 
# together to form a palindrome. eg Consider a list {bat, tab, cat} 
# Then bat and tab can be joined to gather to form a palindrome. 
# Expecting a O(nk) solution where n = number of words and k is length 
# There can be multiple pairs, return all

class TrieNode:

	def __init__(self):
		self.nodes = {}
		self.word = None

	def add(self,strn,idx=0):
		c = strn[idx]
		l = len(strn)
		if c not in self.nodes:
			self.nodes[c] = TrieNode()
		if idx == l - 1:
			self.nodes[c].word = strn
		else:
			self.nodes[c].add(strn,idx+1)

	def getAll(self):
		words = []
		for key, value in self.nodes.iteritems():
			if value.word is not None:
				words.append(value.word)
			words += value.getAll()

		return words


sentence = "the holidayer this that hol holi holiday thyme theatre thistle home throat"

arr = sentence.split()

root = TrieNode()

for w in arr:
	root.add(w)

print root.getAll()
