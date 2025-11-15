# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        
        l1_current = l1
        l2_current = l2
        l3 = ListNode()
        l3_current = l3
        digit_extra = 0

        while l1_current or l2_current or digit_extra == 1:
            new_sum = (l1_current.val if l1_current else 0) + (l2_current.val if l2_current else 0) + digit_extra
            digit_extra, l3_current.val = divmod(new_sum, 10)
            if (l1_current.next if l1_current else None) or (l2_current.next if l2_current else None) or digit_extra == 1:
                l3_current.next = ListNode()
                l3_current = l3_current.next
            try:
                l1_current = l1_current.next
            except Exception:
                l1_current = None
            try:
                l2_current = l2_current.next
            except Exception:
                l2_current = None


        return l3

