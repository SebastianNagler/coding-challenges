class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        pos_speed = zip(position, speed)
        pos_speed = [[i, j] for i, j in sorted(pos_speed, key=lambda x: x[0], reverse=True)]
        stack = []
        for i in range(n):
            if i + 1 < n and pos_speed[i][0] == pos_speed[i+1][0]:
                pos_speed[i + 1][1] = min(pos_speed[i + 1][1], pos_speed[i][1])
                continue
            extrap_time = (target - pos_speed[i][0]) / pos_speed[i][1]
            if (not stack) or extrap_time > stack[-1]:
                stack.append(extrap_time)
        return len(stack)