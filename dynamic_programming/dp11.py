# Given a rod of length n inches and an array of prices that contains prices of 
# all pieces of size smaller than n. Determine the maximum value obtainable by 
# cutting up the rod and selling the pieces. 

def CutRod(L,prices):
	size = len(prices)
	if size < L + 1: #prices includes price for 0 length
		return None

	F = [0]*(L+1)
	F[0] = 0
	splitter = []

	for i in xrange(1,L+1):
		currval = prices[i]
		for j in xrange(1,i):
			currval = max(currval, (prices[j] + F[i-j]))
		F[i] = currval
	return F


P = [0,3,5,8,9,10,17,17,20]
l = 8

print CutRod(l,P)