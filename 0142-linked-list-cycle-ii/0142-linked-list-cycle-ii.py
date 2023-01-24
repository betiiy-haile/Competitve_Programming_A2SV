# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        lookUp = set()
        
        while curr:
            if curr in lookUp:
                return curr
            else:
                lookUp.add(curr)
            curr = curr.next
        return None
            
