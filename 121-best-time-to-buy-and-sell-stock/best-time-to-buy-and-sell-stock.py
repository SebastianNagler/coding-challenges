class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cum_min = list(itertools.accumulate(prices, func=min))
        max_profit = float("-inf")
        for i in range(len(prices)-1):
            max_profit = max(max_profit, prices[i+1] - cum_min[i])

        return max_profit if max_profit > 0 else 0
