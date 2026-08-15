class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        cum_max = -101
        i = 0
        for j in range(len(nums)):
            if nums[j] > cum_max:
                cum_max = nums[j]
                nums[j], nums[i] = nums[i], nums[j]
                i += 1

        return i
