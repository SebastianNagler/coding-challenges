class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_len = 0
        nums_set = set(nums)
        while nums_set:
            num = nums_set.pop()
            local_max_len = 1
            greater = num + 1
            smaller = num - 1
            while greater in nums_set:
                nums_set.remove(greater)
                local_max_len += 1
                greater += 1
            while smaller in nums_set:
                nums_set.remove(smaller)
                local_max_len += 1
                smaller -= 1
            max_len = max(max_len, local_max_len)
            
        return max_len