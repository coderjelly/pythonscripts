# The longest Increasing Subsequence (LIS) problem is to find the length of the longest 
# subsequence of a given sequence such that all elements of the subsequence are sorted 
# in increasing order.

# For example, length of LIS for { 10, 22, 9, 33, 21, 50, 41, 60, 80 } is 6
# and LIS is {10, 22, 33, 50, 60, 80}.


def LIS(Arr):
	N = len(Arr)

	f = [0]*(N+1)
	f[N-1] = 1

	out = []

	for i in xrange(N-2,-1,-1):
		if Arr[i] < Arr[i+1]:
			f[i] = f[i+1] + 1
		else:
			f[i] = f[i+1]

	return f[0]



A = [10, 22, 9, 33, 21, 50, 41, 60, 80]

print LIS(A)