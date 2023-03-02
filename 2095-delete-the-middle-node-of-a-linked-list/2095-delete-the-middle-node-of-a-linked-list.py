# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:        
        #  base case
        if not head.next:
            return None
        
        slow = head
        fast = head
        #  to find the node before the middle node
        prev = ListNode(0,slow)
        
        while fast != None and fast.next != None:
            prev = prev.next
            slow = slow.next
            fast = fast.next.next
        #  delete the middle element    
        prev.next = prev.next.next
        return head