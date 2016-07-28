dic = {}

def mapper(val):
	l = len(val)
	if l > 2 or l < 1:
		return None
	return chr(int(val) + 96)

def decode(str1,prefix):
	if str1 is None:
		return None
	l = len(str1)
	if l == 0:
		print prefix
		return
	if l == 1:
		print prefix + dic[str1]
		return
	for j in xrange(1,3):
		newPrefix = str1[:j]
		if newPrefix in dic:
			updatePrefix = prefix + dic[newPrefix]
			decode(str1[j:],updatePrefix)

for i in xrange(1,27):
	s = str(i)
	dic[s] = mapper(s)

decode("12267","")
