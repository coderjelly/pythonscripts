import string

# Given:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]
# As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog"
alphabet = list(string.ascii_lowercase)


#incorrect
def wordLadder(wordList, beginWord, endWord, visited,count):
	l = len(beginWord)
	for i in xrange(l):
		for c in alphabet:
			newword = beginWord[:i] + c + beginWord[i+1:]
			print newword
			if newword == endWord:
				print "*********" + newword
				return count + 1
			if newword not in visited and newword in wordList:
				visited.add(newword)
				count += 1
				beginWord = newword
	return count


print wordLadder(["hot","dot","dog","lot","log"],"hit","cog", set("hit"),0)