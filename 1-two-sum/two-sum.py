class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_set = set()
        for i in range(len(nums)):
            if target - nums[i] in num_set:
                if nums[i] * 2 == target:
                    return [nums.index(nums[i]), nums.index(nums[i], nums.index(nums[i]) + 1)]
                else:
                    return [i, nums.index(target - nums[i])]
            else:
                num_set.add(nums[i])

    def alternativeTwoSum(self, nums: List[int], target: int) -> List[int]:
        sorted_nums = sorted(nums)
        i = 0
        j = len(nums) - 1
        for x in range(len(nums)):
            if sorted_nums[i] + sorted_nums[j] < target:
                i += 1
            elif sorted_nums[i] + sorted_nums[j] > target:
                j -= 1
            else:
                break
        flag = True
        for k in range(len(nums)):
            if nums[k] == sorted_nums[i] and flag == True:
                i = k
                flag = False
                continue
            if nums[k] == sorted_nums[j]:
                j = k
        return [i, j]
