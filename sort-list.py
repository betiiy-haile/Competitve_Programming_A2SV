# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:        
        def getMid(head):
            slow, fast = head, head.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow

        def merge(left, right):
            ans = curr = ListNode()
            while left and right:
                if left.val < right.val:
                    curr.next = left
                    left = left.next
                else:
                    curr.next = right
                    right = right.next
                curr = curr.next
            if left:
                curr.next = left
            if right:
                curr.next = right
            return ans.next

        if not head or not head.next:
            return head
        left = head
        right = getMid(head)
        temp = right.next
        right.next = None
        left = self.sortList(left)
        right = temp
        right = self.sortList(right)
        return merge(left,right)