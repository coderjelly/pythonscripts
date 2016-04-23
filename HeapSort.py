# Author: coderjelly
# Script in Python demonstrating heap sort


def Left(i):
	return 2*i + 1

def Right(i):
	return 2*i + 2

def Parent(i):
	return (i - 1)/2

def Swap(A,i,j):
	if i == j:
		return
	temp = A[i]
	A[i] = A[j]
	A[j] = temp

#check if definition is correct:
for i in range(5):
	print i == Parent(Left(i))
	print i == Parent(Right(i))


def MaxHeapify(A,i,lim):
	
	l = Left(i)
	r = Right(i)

	largest = i

	if l < lim and A[l] > A[i]:
		largest = l

	if r < lim and A[r] > A[largest]:
		largest = r

	if largest != i:
		Swap(A,largest,i)
		MaxHeapify(A,largest,lim)

def BuildMaxHeap(A):
	mid = len(A)/2
	for i in range(mid,-1,-1):
		MaxHeapify(A,i,len(A))


def HeapSort(A):
	BuildMaxHeap(A)
	size = len(A) - 1
	for i in range(size,0,-1):
		Swap(A,i,0)
		MaxHeapify(A,0,i)

# Testing

SomeArray = [2,1,0,-3,7,23,9,-2,11]

BuildMaxHeap(SomeArray)

print SomeArray

AnotherArray = [-2,6,1,0,11,4,17,-12,5]

print AnotherArray

HeapSort(AnotherArray)

print AnotherArray

