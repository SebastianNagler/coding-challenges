steps_dict = {1:1, 2:2}

class Solution:
    def climbStairs(self, n: int) -> int:
        if n in steps_dict:
            return steps_dict[n]
        num_ways = self.climbStairs(n-2) + self.climbStairs(n-1)
        steps_dict[n] = num_ways
        return num_ways
