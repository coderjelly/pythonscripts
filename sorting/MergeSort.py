# Author: coderjelly
# Script in Python imlementing MERGE SORT

import sys

def MergeSort(A,p,q):
	if q > p:
		mid = int((p + q)/2)
		MergeSort(A,p,mid)
		MergeSort(A,mid+1,q)
		Merge(A,p,mid,q)

def Merge(A,p,mid,q):

	a = 0
	b = 0
	i = p

	L = A[p:mid+1]
	R = A[mid+1:q]

	maxL = len(L)
	maxR = len(R)

	L.append(sys.maxint)
	R.append(sys.maxint)

	while a < maxL and b < maxR:

		if L[a] < R[b]:
			A[i] = L[a]
			a += 1

		else:
			A[i] = R[b]
			b += 1

		i += 1

	while a < maxL:
		A[i] = L[a]
		a += 1
		i += 1

	while b < maxR:
		A[i] = R[b]
		b += 1
		i += 1

k = [1,2,7,1,9,-3,2,0]

print k

MergeSort(k,0,len(k))

print k
