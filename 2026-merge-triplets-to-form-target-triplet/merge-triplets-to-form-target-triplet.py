class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        curr_approx = None
        for triplet in triplets:
            if triplet[0] == target[0] and triplet[1] <= target[1] and triplet[2] <= target[2]:
                curr_approx = triplet
                break
        if curr_approx is None:
            return False
        if curr_approx[1] < target[1]:
            for triplet in triplets:
                if triplet[1] == target[1] and triplet[0] <= target[0] and triplet[2] <= target[2]:
                    curr_approx = [target[0], target[1], max(curr_approx[2], triplet[2])]
                    break
            if curr_approx[1] < target[1]:
                return False
        if curr_approx[2] < target[2]:
            for triplet in triplets:
                if triplet[2] == target[2] and triplet[0] <= target[0] and triplet[1] <= target[1]:
                    return True
            return False
        return True