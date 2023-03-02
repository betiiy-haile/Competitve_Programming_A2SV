# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        arr = []
        while curr:
            arr.append(curr.val)
            curr = curr.next
            
        arr.sort()
        dummy = ListNode()
        temp = dummy
        for i in range(len(arr)):
            temp.next = ListNode(arr[i])
            temp = temp.next
            
        return dummy.next