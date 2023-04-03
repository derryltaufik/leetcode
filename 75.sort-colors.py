#
# @lc app=leetcode id=75 lang=python3
#
# [75] Sort Colors
#

# @lc code=start


from typing import List


def swap(nums, a,b):
    nums[a], nums[b] = nums[b], nums[a]


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        curr = 1
        while curr < len(nums):
            l = curr - 1
            r = curr
            while l >= 0 and nums[r] < nums[l]:
                swap(nums, r, l)
                l -= 1
                r -= 1
            curr += 1


# @lc code=end
