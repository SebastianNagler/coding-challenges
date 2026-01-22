class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total = gas[0] - cost[0]
        min_entry, min_entry_idx = total, 0
        for i in range(1, len(gas)):
            total = total + gas[i] - cost[i]
            if total < min_entry:
                min_entry, min_entry_idx = total, i
        if total < 0:
            return -1
        return (min_entry_idx + 1) % len(gas)
