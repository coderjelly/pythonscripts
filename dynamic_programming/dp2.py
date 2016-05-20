# Author: coderjelly
# Given two strings str1 and str2 and below operations that can performed on str1. 
# Find minimum number of edits (operations) required to convert str1 into str2.

# Insert
# Remove
# Replace

import sys

A = "abc"
B = "12cy"

M = len(A)
N = len(B)

F = []

for i in range(M+1):
	F.append([None]*(N+1))

for i in range(M+1):
	F[i][N] = 1   #only one string has one character, other string is null

for j in range(N+1):
	F[M][j] = 1  # same as above

F[M][N] = 0 #both strings are null

for i in range(M-1,-1,-1):
	for j in range(N-1,-1,-1):
		if A[i] == B[j]:
			F[i][j] = F[i+1][j+1]
		else:
			F[i][j] = min([F[i+1][j+1]+1,F[i+1][j]+1,F[i][j+1]+1])

print F[0][0]






