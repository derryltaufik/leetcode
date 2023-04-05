#
# @lc app=leetcode id=2439 lang=python3
#
# [2439] Minimize Maximum of Array
#

# @lc code=start
class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        curSum = 0
        maxx = nums[0]
        for i, val in enumerate(nums):
            curSum += val
            curAvg = curSum / (i + 1)
            maxx = max(maxx, math.ceil(curAvg))

        return maxx


# @lc code=end
