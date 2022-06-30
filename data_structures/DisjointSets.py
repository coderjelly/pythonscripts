
class DisjointSets:

	def __init__(self, size):
		self.root = [i for i in range(size)]
		self.rank = [1] * size


	def find(self, x):
		if x == self.root[x]:
			return x
		self.root[x] = self.find(self.root[x])
		return self.root[x]

	def union(self, x, y):
		rootX = self.find(x)
		rootY = self.find(y)

		if rootY != rootX:
			if self.rank[rootX] > self.rank[rootY]:
				self.root[rootY] = rootX
			elif self.rank[rootY] > self.rank[rootX]:
				self.root[rootX] = rootY
			else:
				self.root[rootX] = rootY
				self.rank[rootY] += 1
	def connected(self, a, b):
		return self.find(a) == self.find(b)


# Test Case
uf = DisjointSets(10)
# 1-2-5-6-7 3-8-9 4
uf.union(1, 2)
uf.union(2, 5)
uf.union(5, 6)
uf.union(6, 7)
uf.union(3, 8)
uf.union(8, 9)
print(uf.connected(1, 5))  # true
print(uf.connected(5, 7))  # true
print(uf.connected(4, 9))  # false
# 1-2-5-6-7 3-8-9-4
uf.union(9, 4)
print(uf.connected(4, 9))  # true