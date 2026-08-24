class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        path = []

        def backtrack(start):
            if len(path) == k:
                res.append(path[:])      # copy, not reference
                return
            for i in range(start, len(path) + n - k + 1):
                path.append(i+1)      # choose
                backtrack(i+1)    # explore
                path.pop()               # unchoose
        backtrack(0)
        return res