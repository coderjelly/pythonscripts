# take an array and print non over lapping in order pairs. example:
# [1,2,3,4] => input

# output below is in order combination

# (1234)
# (1)(234)
# (1)(23)(4)
# (1)(2)(34)
# (12)(34)
# (12)(3)(4)
# (123)(4)
# (1)(2)(3)(4)

def parenthesize(prefix,arr1):

	if prefix is None:
		return

	len1 = len(arr1)

	if len1 == 0:
		print prefix 
		return

	print prefix + "(" + arr1 + ")" 

	for k in xrange(1,len1):
		newPrefix = prefix + "(" + arr1[:k] + ")"
		parenthesize(newPrefix,arr1[k:])

parenthesize("","1234")