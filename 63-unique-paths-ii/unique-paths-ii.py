class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[-1][-1] == 1 or obstacleGrid[0][0] == 1:
            return 0
        for row in range(len(obstacleGrid)):
            if obstacleGrid[row][0] == 1:
                break
            obstacleGrid[row][0] = -1
        for col in range(1, len(obstacleGrid[0])):
            if obstacleGrid[0][col] == 1:
                break
            obstacleGrid[0][col] = -1
        for row in range(1, len(obstacleGrid)):
            for col in range(1, len(obstacleGrid[0])):
                if obstacleGrid[row][col] != 1:
                    if obstacleGrid[row - 1][col] != 1:
                        obstacleGrid[row][col] += obstacleGrid[row - 1][col]
                    if obstacleGrid[row][col - 1] != 1:
                        obstacleGrid[row][col] += obstacleGrid[row][col - 1]

        return -obstacleGrid[-1][-1]