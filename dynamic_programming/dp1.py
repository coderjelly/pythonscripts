# Author: coderjelly
# Problem Statement: On a positive integer, you can perform any one of the following 3 steps. 
# 1.) Subtract 1 from it. ( n = n - 1 )  , 2.) If its divisible by 2, divide by 2.
# ( if n % 2 == 0 , then n = n / 2  )  , 3.) If its divisible by 3, divide by 3.
# ( if n % 3 == 0 , then n = n / 3  ). 
# Now the question is, given a positive integer n, 
# find the minimum number of steps that takes n to 1

def MinSteps(k,A):
	if k == 1:
		A[k] = 0
		A[0] = 0
		return

	if k == 0:
		return

	A[k] = A[k-1] + 1

	if k%2 == 0:
		A[k] = min(A[k],A[int(k/2)] + 1)

	if k%3 == 0:
		A[k] = min(A[k],A[int(k/3)] + 1)


N = 11
A = []

for i in range(N+1):
	A.append(None) #means value not valid

for j in range(1,N+1):
	MinSteps(j,A)

print A[N]
