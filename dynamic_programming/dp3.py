# Author: coderjelly
# Given a distance dist, count total number of ways to cover the distance 
# with up to k steps (1,2,3...k)

# E.g.:
# Input:  n = 3
# 		k = 3

# Output: 4
# Below are the four ways
#  1 step + 1 step + 1 step
#  1 step + 2 step
#  2 step + 1 step
#  3 step


def CountSteps(k,n):
	if k <= 0 or n <= 0:
		return None
	f = [0]*n
	f[0] = 1
	f[1] = 2
	for i in range(2,n):
		for j in range(1,k+1):
			if j <= i:
				f[i] += f[i-j]
	return f


s = 5
m = 2
print CountSteps(m,s)
		