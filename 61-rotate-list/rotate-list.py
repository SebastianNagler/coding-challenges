# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head: return None
        len_list = 0
        curr = head
        while curr:
            len_list += 1
            if not curr.next:
                curr.next = head
                break
            curr = curr.next
        k = int(k % len_list)
        curr = head
        for i in range(len_list - k - 1):
            curr = curr.next
        curr.next, curr = None, curr.next
        return curr