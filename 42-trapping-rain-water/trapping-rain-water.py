class Solution:
    def trap(self, height: List[int]) -> int:
        volume = 0
        max_height = (0, None)
        for i in range(len(height)):
            if height[i] > max_height[0]:
                max_height = (height[i], i)
        if max_height[1] == None:
            return 0
        left_curr_max = 0
        right_curr_max = 0
        for i in range(max_height[1]):
            left_curr_max = max(left_curr_max, height[i])
            volume += left_curr_max - height[i]
        for i in range(len(height)-1, max_height[1], -1):
            right_curr_max = max(right_curr_max, height[i])
            volume += right_curr_max - height[i]
        return volume