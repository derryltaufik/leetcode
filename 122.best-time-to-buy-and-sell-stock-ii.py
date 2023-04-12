#
# @lc app=leetcode id=122 lang=python3
#
# [122] Best Time to Buy and Sell Stock II
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        profit = 0
        prev = prices[0]
        for i in prices[1:]:
            if i > prev:
                profit += i - prev
            prev = i

        return profit


# @lc code=end
