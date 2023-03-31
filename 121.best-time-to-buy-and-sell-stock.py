#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max = 0

        left = 0

        for j in range(left + 1, len(prices)):
            profit = prices[j] - prices[left]
            if prices[left] < prices[j]:
                if profit > max:
                    max = profit
            else:
                left = j
        return max


# @lc code=end
