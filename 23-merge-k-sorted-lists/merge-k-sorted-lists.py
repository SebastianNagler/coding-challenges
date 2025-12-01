# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def merge2Lists(self, list1, list2):
        if (not list1) and (not list2):
            return None
        prev = ListNode()
        curr = prev
        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
                curr = curr.next
            else:
                curr.next = list2
                list2 = list2.next
                curr = curr.next
        if list1:
            curr.next = list1
        else:
            curr.next = list2
        return prev.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        n = len(lists)
        if n == 0:
            return None
        if n == 1:
            return lists[0]
        appendum = [lists[-1]] if n % 2 == 1 else []
        return self.mergeKLists(
            [self.merge2Lists(lists[i], lists[i + 1]) for i in range(0, len(lists) - 1, 2)] + appendum
            )
