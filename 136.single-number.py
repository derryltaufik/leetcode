#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(0, len(nums)-1, 2):
            if nums[i] != nums[i + 1]:
                return nums[i]
        return nums[-1]

# @lc code=end