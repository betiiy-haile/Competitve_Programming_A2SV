# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
            parts =[None] * k
            length = 0
            curr = head
            while curr:
                length +=1
                curr = curr.next
            
            n, r = divmod(length, k)
            curr = head
            prev = None
            
            for i in range(k):
                parts[i] = curr
                for j in range(n + (r > 0)):
                    prev = curr
                    if curr:
                        curr = curr.next
                    else:
                        curr = None
                if prev:
                    prev.next = None
                r -= 1
                
            return parts
                    
            