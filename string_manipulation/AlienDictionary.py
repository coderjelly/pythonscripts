# Given a sorted dictionary (array of words) of an alien language, 
# find order of characters in the language.

graph = {}

def comparewords(word1,word2):
	if word1 == word2:
		return None
	l1 = len(word1)
	l2 = len(word2)
	l = min(l1,l2)
	i = 0
	while i < l:
		if word1[i] != word2[i]:
			return (word1[i],word2[i])
		i += 1
	return None

def addToGraph(ch1,ch2):
	if ch1 in graph:
		graph[ch1].add(ch2)
	else:
		graph[ch1] = set([ch2])

def createCharGraph(wordsArr):
	l = len(wordsArr)

	for i in xrange(1,l):
		charPair = comparewords(wordsArr[i-1],wordsArr[i])
		if charPair is not None:
			first = charPair[0]
			second = charPair[1]
			addToGraph(first,second)

final = []
seen = set()
def topological(node):
	if node in seen:
		return
	if node in graph:
		seen.add(node)
		for v in graph[node]:
			topological(v)
	final.append(node)


words = ["baa", "abcd", "abca", "cab", "cad"]

createCharGraph(words)
for k in graph.keys():
	topological(k)
print final[::-1]



