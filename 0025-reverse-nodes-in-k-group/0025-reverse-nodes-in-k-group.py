# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1: 
            return head

        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1
        
        curr,dummy = head,ListNode()
        tail = dummy

        for i in range(length//k):
            prev = None

            for x in range(k):
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            tail.next = prev
            for x in range(k): 
                tail = tail.next 

        tail.next = curr
        return dummy.next