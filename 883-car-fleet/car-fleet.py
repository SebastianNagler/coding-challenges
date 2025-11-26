class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        pos_speed = zip(position, speed)
        pos_speed = [[i, j] for i, j in sorted(pos_speed, key=lambda x: x[0], reverse=True)]
        extrap_time = None
        num_fleets = 0
        for i in range(n):
            if i + 1 < n and pos_speed[i][0] == pos_speed[i+1][0]:
                pos_speed[i + 1][1] = min(pos_speed[i + 1][1], pos_speed[i][1])
                continue
            time = (target - pos_speed[i][0]) / pos_speed[i][1]
            if extrap_time == None or time > extrap_time:
                extrap_time = time
                num_fleets += 1
        return num_fleets