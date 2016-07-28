class Solution(object):

    def reverseList(self, head):
        if head is None:
            return None
        self.main = None
        t = self.reverse(head)
        return self.main
        
    def reverse(self,node):
        if node.next is not None:
            k = self.reverse(node.next)
        else:
            self.main = node
            return node
        k.next = node
        node.next = None
        return node
        


s = Solution()

s.moveZeroes([0,1,0,3,12])

