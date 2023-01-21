# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        stack1 = []
        stack2 = []        
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
            
        while l2:
            stack2.append(l2.val)
            l2 = l2.next
            
        carry, head = 0, None

        while stack1 or stack2 or carry:            
            v1 = stack1.pop() if stack1 else 0
            v2 = stack2.pop() if stack2 else 0
            val = v1 + v2 + carry
            carry = val // 10
            val = val%10
            newHead = ListNode(val)
            newHead.next = head
            head = newHead
              
        return head
            
            