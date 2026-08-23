class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        is_remaining = [True] * len(nums)

        def backtrack():
            if len(path) == len(nums):
                res.append(path[:])
                return
            for i in range(len(nums)):
                if not is_remaining[i]:    # pruning goes here
                    continue
                path.append(nums[i])      # choose
                is_remaining[i] = False
                backtrack()    # explore
                is_remaining[i] = True
                path.pop()               # unchoose
        backtrack()
        return res