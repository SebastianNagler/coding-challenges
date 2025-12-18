class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def recursivePermute(nums):
            len_nums = len(nums)
            if len_nums == 1:
                nums_copy = copy.deepcopy(nums)
                return [nums_copy]
            perms = [copy.deepcopy(item) for item in recursivePermute(nums[:-1]) for _ in range(len_nums)]
            new_num = nums[-1]
            i = 0
            for perm in perms:
                perm.insert(i, new_num)
                i += 1
                if i >= len_nums:
                    i -= len_nums

            return perms
                
        return recursivePermute(nums)