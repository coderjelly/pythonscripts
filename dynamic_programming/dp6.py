# Given a set of numbers: {1, 3, 2, 5, 4, 9}, find the number of subsets that sum 
# to a particular value k (say, 9 for this example).


def NumOfSets(Arr,k):

	N = len(Arr)

	f = [1] + [0]*k

	for i in range(N):
		for j in range(k,-1,-1):
			if j >= Arr[i]:
				f[j] += f[j-Arr[i]]

	return f[k]

SomeArray = [1, 3, 2, 5, 4, 9]
k = 9 

print NumOfSets(SomeArray,k)