import numpy as np

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr_min = prices[0]
        max_profit = float("-inf")
        for i in range(1, len(prices)):
            curr_price = prices[i]
            max_profit = max(max_profit, curr_price - curr_min)
            curr_min = min(curr_min, curr_price)

        return max_profit if max_profit > 0 else 0
