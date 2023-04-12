#
# @lc app=leetcode id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#

# @lc code=start
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        subs = [nums[0]]
        for num in nums:
            if num > subs[-1]:
                subs.append(num)
            else:
                # replace the number in sub with new value
                insert_index = bisect_left(subs, num)
                subs[insert_index] = num

        return len(subs)


# @lc code=end
