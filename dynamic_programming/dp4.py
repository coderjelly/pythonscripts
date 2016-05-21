# Author: coderjelly
# LCS Problem Statement: Given two sequences, find the length of longest subsequence present in both of them. 
# A subsequence is a sequence that appears in the same relative order, 
# but not necessarily contiguous. 
# For example, "abc", "abg", "bdf", "aeg", "acefg", .. etc are subsequences of "abcdefg". 
# So a string of length n has 2^n different possible subsequences.

def LCS(A, B):
	M = len(A)
	N = len(B)

	f = [[0]*(N+1) for i in xrange(M+1)]

	for i in xrange(M-1,-1,-1):
		for j in xrange(N-1,-1,-1):
			if A[i] == B[j]:
				f[i][j] = f[i+1][j+1] + 1
			else:
				f[i][j] = max(f[i][j+1],f[i+1][j])

	return f[0][0]


str1 = "abcdefg"
str2= "bciefk"

print LCS(str1,str2)