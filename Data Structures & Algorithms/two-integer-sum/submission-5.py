class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # hash map: two pass
        # time complexity: O(n)
        # space complexity: O(n)
        indices = {}
        for i, v in enumerate(nums):
            indices[v] = i
        for i, v in enumerate(nums):
            complement = target - v
            if complement in indices and indices[complement] != i:
                return [i, indices[complement]]
        return []

        