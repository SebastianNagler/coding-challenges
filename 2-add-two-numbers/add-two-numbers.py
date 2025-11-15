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


        """
        while l1_current.next != None and l2_current.next != None:
            l1_current = l1_current.next
            l2_current = l2_current.next
            new_digit = l1_current.val + l2_current.val + digit_extra
            l3_current.next = ListNode((new_digit) % 10)
            digit_extra = (1 if new_digit > 9 else 0)
            l3_current = l3_current.next
        """

        # if l1_current and l2_current are not None, set l3_current value and update l1_current, l2_current, l3_current to next
        return l3

