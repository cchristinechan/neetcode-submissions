class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # brute force solution
        # time complexity: O(n^2)
        # space complexity: O(1)
        result = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    result = [i, j]
        return result

        