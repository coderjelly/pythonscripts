# Given a set of non-negative integers, and a value sum, 
# determine if there is a subset of the given set with sum equal to given sum.

# Examples: set[] = {3, 34, 4, 12, 5, 2}, sum = 9
# Output:  True  //There is a subset (4, 5) with sum 9.



def ContainsSum(A,s):

	N = len(A)

	f = [[False]*(s+1) for i in range(N+1)]

	for i in xrange(N-1,-1,-1):
		for j in xrange(1,s+1):
			if A[i] == j:
				f[i][j] = True
			elif j > A[i]:
				f[i][j] = f[i+1][j] or f[i+1][j-A[i]]
			else:
				f[i][j] = f[i+1][j]

	return f[0][s]


Arr = [3, 34, 4, 12, 5, 2]

Sum = 11

print ContainsSum(Arr,Sum)
