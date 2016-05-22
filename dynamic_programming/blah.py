def NumOfSets(Arr,k):

	f = [1] + [0] * k
	print f
	for cur in Arr:
		for j in xrange(0, k - cur + 1):
			f[j + cur] += f[j]
			print j
		print f
	return f

SomeArray = [1, 3, 9, 5, 2, 4]
k = 9 

print NumOfSets(SomeArray,k)

