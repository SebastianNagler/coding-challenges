class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def pReq(s):
            res = 1
            curr = s
            for num in nums:
                if num <= curr:
                    curr -= num
                else:
                    curr = s - num
                    res += 1
            return res

        low = max(nums) # 17
        high = sum(nums) # 17
        while low <= high:
            mid = int((low + high) // 2) # 16
            if pReq(mid) <= k:
                high = mid - 1
            else:
                low = mid + 1
        return low