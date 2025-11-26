class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] <= nums[-1]:
            return nums[0]
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            val = nums[mid]
            if val > nums[-1]:
                left = mid + 1
            else:
                right = mid - 1
        return nums[left]