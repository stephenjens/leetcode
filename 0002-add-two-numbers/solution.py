# 08/22/2022 11:16	Accepted	144 ms	14 MB	python3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def add_and_carry(x, y, c = 0):
        carry = 0
        s = x + y + c
        if s >= 10:
            carry += 1
            s -= 10
        return (s, carry)
    
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        s, carry = Solution.add_and_carry(l1.val, l2.val)
        
        answer = ListNode(s)
        
        a = l1.next
        b = l2.next
        
        current = answer
        while a is not None or b is not None:
            a_val = a.val if a is not None else 0
            b_val = b.val if b is not None else 0

            s, carry = Solution.add_and_carry(a_val, b_val, carry)
            
            current.next = ListNode(s)
            current = current.next
            
            a = a.next if a is not None else None
            b = b.next if b is not None else None
        
        if carry > 0:
            current.next = ListNode(carry)
        
        return answer
