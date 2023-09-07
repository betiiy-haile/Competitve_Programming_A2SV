"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        if not head:
            return None
        
        curr = head
        while curr:
            if curr.child:
                tail = curr.child
                while tail.next:
                    tail = tail.next
                tail.next = curr.next
                if tail.next:
                    tail.next.prev = tail
                curr.next = curr.child
                curr.next.prev = curr
                curr.child = None
                    
            else:
                curr = curr.next
                
        return head
        
                    
                    
            
            
                
        