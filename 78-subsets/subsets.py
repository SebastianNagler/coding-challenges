class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def subsets_with_num(subsets: List[List[int]], num: int):
            return [subset + [num] for subset in subsets]

        def recursiveSubsets(numbers: List[int]):
            if not numbers: 
                return [[]]
            half_subsets = recursiveSubsets(numbers[:-1])
            return half_subsets + subsets_with_num(half_subsets, numbers[-1])

        return recursiveSubsets(nums)