# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        
        if not head:
            return None
    
        curr = head
        while curr and curr.next:
            
            g = gcd(curr.val, curr.next.val)
            new_node = ListNode(g)
            
            new_node.next = curr.next
            curr.next = new_node
            curr = new_node.next

        return head