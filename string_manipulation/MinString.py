# Given an array with unique characters arr and a string str, 
# find the smallest substring of str containing all characters of arr.

# Example:
# arr: [x,y,z], str: xyyzyzyx
# result: zyx
import sys

def findMinStr(arr,str1):
	l = len(arr)
	l1 = len(str1)
	left = 0
	right = 0
	unique = 0

	minstr = None
	minLen = sys.maxint

	mapper = {}

	for a in arr:
		mapper[a] = 0

	while (right < l1):
		if str1[right] in mapper:
			num = mapper[str1[right]]
			if num == 0:
				unique += 1
			mapper[str1[right]] += 1
		else:
			right += 1
			continue
		while(unique == l):
			thislen = len(str1[left:right+1])
			if thislen < minLen:
				minLen = thislen
				minstr = str1[left:right+1]
			if str1[left] not in mapper:
				left += 1
				continue
			thisCount  = mapper[str1[left]]
			if thisCount == 1:
				unique -=1
			mapper[str1[left]] -= 1
			left += 1
		right += 1

	return minstr


print findMinStr(['x','y','z'],"xyyzyzyx")
