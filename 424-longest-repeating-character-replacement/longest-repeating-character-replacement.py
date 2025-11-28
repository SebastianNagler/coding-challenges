class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_length = 0
        histogram = Counter()
        left = 0
        for right in range(len(s)):
            if histogram[s[right]]:
                histogram[s[right]] += 1
            else:
                histogram[s[right]] = 1
            while sum([j for i, j in histogram.most_common()[1:]]) > k:
                histogram[s[left]] -= 1
                if histogram[s[left]] == 0:
                    del histogram[s[left]]
                left += 1
            max_length = max(max_length, right - left + 1)

        return max_length

        (len(histogram) > 2)  or (len(histogram) == 2 and all(histogram[key] > 1 for key in histogram))