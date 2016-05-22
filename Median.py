# Question: There are 2 sorted arrays A and B of size n each. 
# Write an algorithm to find the median of the array obtained after merging the 
# above 2 arrays(i.e. array of length 2n). The complexity should be O(log(n))

def FindMedian(A,B):

	M = len(A)
	N = len(B)

	if M != N:
		return

	m1 = int(M/2)
	m2 = int(N/2)

	#how to slice the arrays? depends on the length being odd or even
	if M % 2 == 0:
		flag = True
	else:
		flag = False

	if M == 2:
		print "Median is = ", min(A[1],B[1]),",", max(A[0],B[0])
		return

	if A[m1] == B[m2]:
		print "Median is = ", A[m1]
		return

	elif A[m1] < B[m2]:
		newA = A[m1:]
		if flag:
			newB = B[:m2]
		else:
			newB = B[:m2+1]

	else:
		newB = B[m2:]
		if flag:
			newA = A[:m1]
		else:
			newA = A[:m1+1]

	FindMedian(newA,newB)

ar1 = [1, 2, 3, 6, 11]
ar2 = [4, 6, 8, 10, 13]

FindMedian(ar1,ar2)
