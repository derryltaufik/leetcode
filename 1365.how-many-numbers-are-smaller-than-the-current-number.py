#
# @lc app=leetcode id=1365 lang=python3
#
# [1365] How Many Numbers Are Smaller Than the Current Number
#

# @lc code=start
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        count = {}
        a = nums.copy()
        nums.sort()
        for i, _ in enumerate(nums):
            if nums[i] not in count:
                count[nums[i]] = i

        return [count[i] for i in a]


# @lc code=end
