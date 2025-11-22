class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted_intervals = sorted(intervals, key = lambda x: x[0])
        output = [sorted_intervals[0]]
        for interval in sorted_intervals:
            if interval[0] <= output[-1][1]:
                output[-1][1] = max(output[-1][1], interval[1])
            else:
                output.append(interval)
        return output