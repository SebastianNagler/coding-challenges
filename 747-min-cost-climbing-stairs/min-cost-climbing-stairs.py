class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        len_cost = len(cost)
        for i in range(2, len_cost):
            cost[i] += min(cost[i - 1], cost[i - 2])
        return min(cost[len_cost - 1], cost[len_cost - 2])