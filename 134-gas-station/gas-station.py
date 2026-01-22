class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        gas[0] -= cost[0]
        if len(gas) == 1:
            return -1 if gas[0] < 0 else 0
        min_entry_idx = (gas[0], 0)
        for i in range(1, len(gas)):
            gas[i] += gas[i-1] - cost[i]
            if gas[i] < min_entry_idx[0]:
                min_entry_idx = (gas[i], i)
        if gas[-1] < 0:
            return -1
        res = min_entry_idx[1] + 1
        return 0 if res == len(gas) else res
