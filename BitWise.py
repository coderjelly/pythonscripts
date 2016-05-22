# CoderJelly
# Write a method to determine if the bit-wise representation of an integer is a palindrome.


m = 9
n = 0

orig = m

while m:
	k = m & 1
	n = n << 1
	n = n ^ k
	m = m >> 1

print n == orig

#alternate: 

n = bin(orig)[2:]
if n!=n[::-1]:
       print 'NO' 
else:
       print 'YES'