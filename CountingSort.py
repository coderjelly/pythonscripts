# Author: coderjelly
# Script in Python demonstrating CountingSort

# k is the max val (min is 0) of any number in tha unsorted array A
# final sorted array rests in B

def CountingSort(A,B,k):
	C = [0]*(k+1)

	size = len(A)
	lim = k + 1

	for i in range(size):
		if A[i] < 0:
			print "Invalid value found!"
			return
		C[A[i]] = C[A[i]] + 1

	for j in range(1,lim):
		C[j] = C[j] + C[j-1]

	for i in range(size-1,-1,-1):
		B[C[A[i]]-1] = A[i]
		C[A[i]] = C[A[i]] - 1


# Testing

SomeArray = [2,1,0,3,7,23,9,2,11]

print SomeArray

AnotherArray = [None]*(len(SomeArray))

CountingSort(SomeArray,AnotherArray,max(SomeArray))

print AnotherArray
