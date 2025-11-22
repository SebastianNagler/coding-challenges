# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        try:
            tortoise = head.next
            hare = head.next.next
        except:
            return None

        while tortoise != hare:
            try:
                tortoise = tortoise.next
                hare = hare.next.next
            except:
                return None

        tortoise = head

        while tortoise != hare:
            tortoise = tortoise.next
            hare = hare.next

        return tortoise
        

        