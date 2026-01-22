class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if len(gas) == 1:
            return -1 if gas[0] - cost[0] < 0 else 0
        diff = [gas[i] - cost[i] for i in range(len(gas))]
        min_entry_idx = (diff[0], 0)
        for i in range(1, len(diff)):
            diff[i] += diff[i-1]
            if diff[i] < min_entry_idx[0]:
                min_entry_idx = (diff[i], i)
        if diff[-1] < 0:
            return -1
        res = min_entry_idx[1] + 1
        return 0 if res == len(gas) else res
