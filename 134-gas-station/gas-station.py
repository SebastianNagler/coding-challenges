class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        gas[0] -= cost[0]
        min_entry_idx = (gas[0], 0)
        for i in range(1, len(gas)):
            gas[i] += gas[i-1] - cost[i]
            if gas[i] < min_entry_idx[0]:
                min_entry_idx = (gas[i], i)
        if gas[-1] < 0:
            return -1
        return 0 if min_entry_idx[1] + 1 == len(gas) else min_entry_idx[1] + 1
