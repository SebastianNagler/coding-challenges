class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        if len(nums) == 1:
            return [nums]
        """
        perms_per_i = 1
        for i in range(2, len(nums)):
            perms_per_i *= i
        """
        for i in range(len(nums)):
            rest = nums[:i] + nums[i+1:]
            rest_perms = self.permute(rest)
            for perm in rest_perms:
                perm.append(nums[i])
            res += rest_perms

        return res