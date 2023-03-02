# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
#         curr = head
#         arr = []        
#         while curr != None:
#             arr.append(curr.val)
#             curr =  curr.next               
#         return arr == arr[::-1]:

        fast = head
        slow = head
        
        # Use fast slow pointers to find the middle node of the list
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Reverse the second half of the linked list
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
            
        # Check palindrome with two pointers
        left = head
        right = prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        
        return True
            
                
            
            