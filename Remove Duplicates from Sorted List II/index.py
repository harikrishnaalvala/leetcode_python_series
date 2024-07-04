# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        next = head.next

        if next.val == head.val:
            while next and next.val == head.val:
                next = next.next
            return self.deleteDuplicates(next)
        else:
            head.next = self.deleteDuplicates(next)
            return head
