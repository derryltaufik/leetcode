#
# @lc app=leetcode id=1446 lang=python3
#
# [1446] Consecutive Characters
#

# @lc code=start
class Solution:
    def maxPower(self, s: str) -> int:

        count = maxLen = 0
        previous = None
        for i in s:

            if i == previous:
                count += 1
            else:
                previous = i
                maxLen = max(maxLen, count)
                count = 1

        maxLen = max(maxLen, count)
        return maxLen


# @lc code=end
