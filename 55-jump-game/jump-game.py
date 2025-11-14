class Solution:
    def canJump(self, nums: List[int]) -> bool:
        highest = 0
        len_nums = len(nums)
        for num_index in range(len_nums):
            if num_index == len_nums - 1:
                return True
            num = nums[num_index]
            if num_index + num > highest:
                highest = num_index + num
            elif num_index == highest:
                return False
        return True