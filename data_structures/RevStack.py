#reverse stack using only stack operations


def RevThis(stack, val):

	if not stack:
		stack.append(val)
		return
	else:
		thisval = stack.pop()
		RevThis(stack,val)
		stack.append(thisval)

def Reverse(stack):
	if len(stack) < 2:
		return stack
	first = stack.pop()
	Reverse(stack)
	RevThis(stack,first)

arr = [1,2,3,4,5,6,7,8,9,10]

print arr 

Reverse(arr)

print arr
