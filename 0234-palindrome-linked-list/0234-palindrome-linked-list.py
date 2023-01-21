# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        curr = head
        arr = []        
        while curr != None:
            arr.append(curr.val)
            curr =  curr.next   
            
        if arr == arr[::-1]:
            return True
        else: 
            return False
                
            
            