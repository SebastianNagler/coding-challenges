class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [pair[0] for pair in Counter(nums).most_common(k)]