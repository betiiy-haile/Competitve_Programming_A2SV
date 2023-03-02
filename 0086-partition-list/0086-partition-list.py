# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        left = ListNode()
        right = ListNode()
        lEnd = left
        rEnd = right
        while head:
            if head.val < x:
                lEnd.next = head
                lEnd = lEnd.next
            else:
                rEnd.next = head
                rEnd = rEnd.next
            head = head.next
            
        lEnd.next = right.next    
        rEnd.next = None    
            
        return left.next
            