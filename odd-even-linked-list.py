# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next or not head.next.next:
            return head

        odd = current = head
        even = evenHead = head.next
        idx = 1
        while current:
            if idx > 2 and idx % 2 != 0:
                odd.next = current
                odd = odd.next
            elif idx > 2 and idx % 2 == 0:
                even.next = current
                even = even.next
            current = current.next
            idx += 1

        even.next = None
        odd.next = evenHead
        return head