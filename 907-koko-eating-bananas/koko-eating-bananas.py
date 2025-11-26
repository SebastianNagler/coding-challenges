class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_k = -1
        max_bananas = max(piles)
        low_speed, high_speed = 1, max_bananas
        while low_speed <= high_speed:
            mid_speed = (low_speed + high_speed) // 2
            hours_required = sum([ceil(height / mid_speed) for height in piles])
            if hours_required <= h:
                high_speed = mid_speed - 1
                min_k = mid_speed
            else:
                low_speed = mid_speed + 1

        return min_k