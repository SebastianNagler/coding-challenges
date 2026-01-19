class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        no_overlap_yet = True

        for oldInterval in intervals:
            if oldInterval[1] >= newInterval[0] and oldInterval[0] <= newInterval[1]:
                if no_overlap_yet:
                    no_overlap_yet = False
                    res.append([min(newInterval[0], oldInterval[0]), max(newInterval[1], oldInterval[1])])
                else:
                    res[-1][1] = max(res[-1][1], oldInterval[1])
            elif oldInterval[0] > newInterval[1] and no_overlap_yet:
                no_overlap_yet = False
                res.append(newInterval)
                res.append(oldInterval)
            else:
                res.append(oldInterval)
        if no_overlap_yet:
            res.append(newInterval)


        return res