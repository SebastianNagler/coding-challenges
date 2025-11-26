class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged_nums = []
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                merged_nums.append(nums1[i])
                i += 1
            else:
                merged_nums.append(nums2[j])
                j += 1
        if i < len(nums1):
            merged_nums = merged_nums + nums1[i:]
        if j < len(nums2):
            merged_nums = merged_nums + nums2[j:]
        len_merged_nums = len(merged_nums)
        if len_merged_nums == 0:
            return 0
        median_index = (len(merged_nums) - 1) >> 1
        if len_merged_nums % 2 == 0:
            return (merged_nums[median_index] + merged_nums[median_index + 1]) / 2
        else:
            return merged_nums[median_index]