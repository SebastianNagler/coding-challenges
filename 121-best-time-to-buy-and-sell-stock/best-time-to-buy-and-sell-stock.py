class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        left = 0
        for right in range(len(prices)):
            left_price, right_price = prices[left], prices[right]
            if right_price < left_price:
                left = right
            else:
                max_profit = max(max_profit, right_price - left_price)
        return max_profit