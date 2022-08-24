# 08/22/2022 21:30	Accepted	1036 ms	46.6 MB	python3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        stack = []
        cur = head
        while cur != None:
            stack.append(cur.val)
            cur = cur.next
        #print(stack)
        cur = head
        while cur != None:
            x = stack.pop()
            #print("{} {}".format(x, cur.val))
            if cur.val != x:
                return False
            cur = cur.next
        
        return True
        
