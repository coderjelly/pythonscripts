# Given weights and values of n items, put these items in a knapsack of capacity W to 
# get the maximum total value in the knapsack. In other words, given two integer arrays 
# val[0..n-1] and wt[0..n-1] which represent values and weights associated with n items 
# respectively. Also given an integer W which represents knapsack capacity, 
# find out the maximum value subset of val[] such that sum of the weights of this subset 
# is smaller than or equal to W. 
import sys

def KnapSack(Weights,Values,W):

	N  = len(Weights)

	if W <= 0:
		return 0

	f = [[0]*(W+1) for i in xrange(N+1)]

	for i in xrange(N-1,-1,-1):
		for j in xrange(1,W+1):
			f[i][j] = f[i+1][j]
			if j >= Weights[i]:
				f[i][j] = max(f[i][j],f[i+1][j-Weights[i]]+Values[i])

	return f[0][W]


val = [60, 100, 120]
wt = [10, 20, 30]
W = 50

print KnapSack(wt , val, W)