#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:

        memo = [None] * len(nums)

        def find(i):
            if i < 0:
                return 0
            if memo[i] is not None:
                return memo[i]

            res = max(find(i - 2) + nums[i], find(i - 1))
            memo[i] = res
            return res

        return find(len(nums) - 1)


# @lc code=end
