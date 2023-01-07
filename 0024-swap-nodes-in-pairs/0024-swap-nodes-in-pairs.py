# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        prev = None
        curr = head
        nxt = curr.next
        nextHead = nxt
        
        while curr and nxt:
            # swap nodes
            curr.next = nxt.next
            nxt.next = curr
            if prev:
                prev.next = nxt
                
            # advance nodes
            prev = curr
            curr = curr.next
            if curr:
                nxt = curr.next
                
                
        return nextHead
            
        