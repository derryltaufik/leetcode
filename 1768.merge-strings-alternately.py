#
# @lc app=leetcode id=1768 lang=python3
#
# [1768] Merge Strings Alternately
#

# @lc code=start
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        p1 = 0
        p2 = 0
        l1 = len(word1)
        l2 = len(word2)
        ans = ""

        while p1 < l1 or p2 < l2:
            if p1 < l1:
                ans += word1[p1]
                p1 += 1
            if p2 < l2:
                ans += word2[p2]
                p2 += 1
        return ans


# @lc code=end
