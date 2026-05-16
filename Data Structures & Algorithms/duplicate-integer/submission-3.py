class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # time complexity: O(n)
        # space complexity: O(n)
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False

        