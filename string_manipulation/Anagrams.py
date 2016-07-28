# Print all anagrams/permutations of a string (unique chars)
# Author: coderjelly


def swap(s,i,j):
	if i == j:
		return
	s[i],s[j] = s[j],s[i]

def anagram(A,i,j):
	if i == j:
		x = ''.join(A)
		print x
	for k in xrange(i,j+1):
		swap(A,k,i)
		anagram(A,i+1,j)
		swap(A,k,i)

a = "ABC"

alist = list(a)

anagram(alist,0,len(alist)-1)
