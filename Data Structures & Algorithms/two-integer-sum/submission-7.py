class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # hash map: one pass
        # given: guaranteed one solution
        # time complexity: O(n)
        # space complexity: O(n)
        seen = {}
        for i, v in enumerate(nums):
            complement = target - v
            if complement in seen:
                return [seen[complement], i]
            seen[v] = i
        