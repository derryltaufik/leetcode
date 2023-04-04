#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        memo = {}
        best = nums[0]

        def local_maximum(index):
            if index == 0:
                memo[index] = nums[index]
            if index in memo:
                return memo[index]
            result = max(nums[index] + local_maximum(index - 1), nums[index])

            memo[index] = result
            nonlocal best
            best = max(best, result)
            return result

        # local_maximum(len(nums) - 1)
        # return best

        @cache
        def local_maximum_cache(index):
            if index == 0:
                return nums[index]

            return max(nums[index] + local_maximum_cache(index - 1), nums[index])

        for i in range(len(nums)):
            best = max(best, local_maximum_cache(i))

        return best


# @lc code=end
