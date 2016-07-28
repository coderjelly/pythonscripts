#find square root of a number number N

def sqrt(num,lo,hi):
	mid = (lo+hi)/2.0
	val = mid*mid
	diff = abs(val - num) 

	if diff < 0.01:
		return mid

	if val > num:
		return sqrt(num,lo,mid)
	return sqrt(num,mid,hi)


print sqrt(45,0,45)


