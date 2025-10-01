class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        if nums == []:
            return 0
        for j in range(len(nums)):
            if nums[j] == val:
                j += 1
            else:
                nums[i] = nums[j]
                i += 1
                j += 1
        return i