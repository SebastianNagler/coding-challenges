# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def reverseList(head):
            res = None
            while head:
                head_copy = head
                head = head.next
                head_copy.next = res
                res = head_copy
            return res

        head_rev = reverseList(head)
        if n == 1:
            return reverseList(head_rev.next)
        if n == 2:
            head_rev.next = head_rev.next.next
            return reverseList(head_rev)
        curr = head_rev
        nr = 2
        while nr < n:
            curr = curr.next
            nr += 1
        curr.next = curr.next.next
        return reverseList(head_rev)