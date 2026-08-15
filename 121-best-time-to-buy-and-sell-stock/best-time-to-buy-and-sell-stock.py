import numpy as np

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cum_min = list(itertools.accumulate(prices, func=min))
        max_profit = max(np.array(prices) - np.array(cum_min))

        return int(max_profit) if max_profit > 0 else 0
