class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #time complexity: O(s + t)
        # space complexity: O(1) we have at most 26 difference characters
        if len(s) != len(t):
            return False
        countS = {}
        countT = {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        # for j in countS:
        #     if countS[j] != countT.get(j,0):
        #         return False
        return countS == countT


        