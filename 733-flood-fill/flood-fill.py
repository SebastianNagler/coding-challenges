class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        def dfs(sr, sc):
            prev_color = image[sr][sc]
            image[sr][sc] = color
            if sc > 0 and image[sr][sc - 1] == prev_color:
                dfs(sr, sc - 1)
            if sr > 0 and image[sr - 1][sc] == prev_color:
                dfs(sr - 1, sc)
            if sc < len(image[0]) - 1 and image[sr][sc + 1] == prev_color:
                dfs(sr, sc + 1)
            if sr < len(image) - 1 and image[sr + 1][sc] == prev_color:
                dfs(sr + 1, sc)

        if image[sr][sc] != color:
            dfs(sr, sc)
        return image