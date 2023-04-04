#
# @lc app=leetcode id=918 lang=python3
#
# [918] Maximum Sum Circular Subarray
#

# @lc code=start
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:

        curMaxSum = curMinSum = 0
        maxSum = minSum = nums[0]
        for n in nums:

            curMaxSum = max(n, curMaxSum + n)
            maxSum = max(curMaxSum, maxSum)
            curMinSum = min(n, curMinSum + n)
            minSum = min(curMinSum, minSum)

        ans = 0
        if maxSum < 0:
            ans = maxSum
        else:
            ans = max(maxSum, sum(nums) - minSum)

        return ans


# @lc code=end
