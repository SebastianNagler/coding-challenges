class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = {tuple()}
        for num in nums:
            local_set = set()
            for tup in res:
                local_set.add(tup + (num,))
            res |= local_set
        return [list(tup) for tup in res]