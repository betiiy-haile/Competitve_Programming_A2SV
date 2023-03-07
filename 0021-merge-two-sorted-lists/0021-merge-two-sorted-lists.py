# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        head = dummy
        def merge(list1,list2):
            nonlocal dummy
            nonlocal head
            if not list1 and not list2:
                return 
            elif not list1 and list2:
                head.next = list2
                head = head.next
            elif not list2 and list1:
                head.next = list1
                head = head.next
            elif list1.val < list2.val:
                temp = list1.next                 
                head.next = list1
                list1.next = None 
                head = head.next              
                merge(temp, list2)
            else:
                temp = list2.next 
                head.next = list2 
                list2.next = None
                head = head.next
                merge(list1, temp)
        merge(list1, list2)        
        return dummy.next  
                
