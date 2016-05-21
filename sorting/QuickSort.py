# Author: coderjelly
# Script in Python demonstrating QuickSort

def Swap(A,i,j):
	if i == j:
		return
	temp = A[i]
	A[i] = A[j]
	A[j] = temp

def QuickSort(A,p,r):
	if p >= r:
		return
	q = Partition(A,p,r)
	QuickSort(A,p,q-1)
	QuickSort(A,q+1,r)

def Partition(A,p,r):
	pivot = A[r]
	i = p - 1
	for j in range(p,r):
		if A[j] < pivot:
			i = i + 1
			Swap(A,i,j)
	Swap(A,i+1,r)
	return i + 1


# Testing

SomeArray = [2,1,0,-3,7,23,9,-2,11]

print SomeArray

QuickSort(SomeArray,0,len(SomeArray)-1)

print SomeArray