class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        idx_set = set()
        curr = 0
        while curr not in idx_set:
            idx_set.add(curr)
            curr = nums[curr]
        return curr
