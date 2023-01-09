# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        while cur:
            temp = head
            while temp != cur:
                if temp.val > cur.val: 
                    temp.val, cur.val = cur.val, temp.val
                temp = temp.next
            cur = cur.next
        return head