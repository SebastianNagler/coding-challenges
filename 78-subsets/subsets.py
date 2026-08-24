class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        len_nums = len(nums)
        res = []
        path = []

        def backtracking(start):
            res.append(path[:])
            if start == len_nums:
                return
            for i in range(start, len_nums):
                path.append(nums[i])
                backtracking(i + 1)
                path.pop()

        backtracking(0)
        return res