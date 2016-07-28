# Given a 2D array, print it in spiral form. 


def PrintSpiral(matrix, i0, j0 , m, n):
	if m < 1 and n < 1:
		return
	if i0 >= m and j0 >= n:
		return


	i = i0
	j = j0

	M = i0 + m
	N = j0 + n

	while(j < N):
		print matrix[i][j],
		j += 1

	j -= 1
	i += 1

	while(i< M):
		print matrix[i][j],
		i += 1

	i -= 1
	j -= 1

	while(j >= j0):
		print matrix[i][j],
		j -= 1

	j += 1
	i -= 1

	while(i > i0):
		print matrix[i][j],
		i -= 1

	PrintSpiral(matrix,i0+1,j0+1,m-2,n-2)


arr1 = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

PrintSpiral(arr1,0,0,4,4)