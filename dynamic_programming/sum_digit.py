

def countNums(S,n):
	f = [[0]*(n+1) for j in xrange(S+1)]

	for i in xrange(S+1):
		for j in xrange(1,n+1):
			if i == 0:
				f[i][j] = 1
			elif j == 1:
				if i >= 0 and i <= 9:
					f[i][j] = 1
			else:
				if j == n:
					start = 1
				else:
					start = 0
				for k in xrange(start,10):
					if i >= k:
						f[i][j] += f[i-k][j-1]
	return f

print countNums(7,3)
