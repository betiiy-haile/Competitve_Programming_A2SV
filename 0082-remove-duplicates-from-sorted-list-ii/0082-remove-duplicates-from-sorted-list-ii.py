# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        temp = dummy
        left = right = head
        while right:
            while right and left.val == right.val:
                right = right.next
            if left.next == right:
                temp.next = left
                temp = temp.next
            left = right
        temp.next = None
        return dummy.next