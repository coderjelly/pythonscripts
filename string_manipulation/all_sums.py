#all possible sums

def summer(arr,t,res):
	l = len(arr)
	if t <= 0 :
		print res
		return

	for a in arr:
		if a <= t and not a > res[-1]:
			newarr = arr
			summer(newarr,t-a,res+[a])
		else:
			return


summer([1,2,3,4],9,[])
