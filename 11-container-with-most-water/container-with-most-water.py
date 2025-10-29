class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = float('-inf')
        n = len(height)
        i = 0
        j = n - 1
        while j > i:
            area = (j - i) * min(height[i], height[j])
            if area > max_area:
                max_area = area
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return max_area

    # Alternative, slower solution:
    """
    def maxArea(self, height: List[int]) -> int:
        sorted_enum = sorted(list(enumerate(height)), key = lambda x: x[1], reverse = True)
        sorted_indices = [indx for indx, hght in sorted_enum]
        max_area = -1
        n = len(height)
        slice_end = 0
        for i in sorted_indices[1:]:
            slice_end += 1
            if height[i] * (n-1) < max_area:
                break
            if height[i] * max(i, n - 1 - i) < max_area:
                continue
            for j in sorted_indices[:slice_end]:
                local_area = (abs(j-i)) * min(height[i], height[j])
                if local_area > max_area:
                    max_area = local_area
        return max_area
    """