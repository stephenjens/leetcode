# 08/22/2022 21:41	Accepted	66 ms	15.4 MB	python3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head is None or head.next is None:
            return head
        
        prev = None
        cur = head
        future = head.next
        while future is not None:
            cur.next = prev
            prev = cur
            cur = future
            future = cur.next
        
        cur.next = prev
        return cur

