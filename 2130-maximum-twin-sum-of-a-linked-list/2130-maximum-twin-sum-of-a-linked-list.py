# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head
        
        # get the mid node
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            
        # reverse the second half
        curr = slow
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            
        # find the max sum
        maxSum = 0
        temp = head
        while prev:
            Sum = temp.val+ prev.val
            maxSum = max(maxSum, Sum)
            temp = temp.next
            prev = prev.next
            
        return maxSum
        
        