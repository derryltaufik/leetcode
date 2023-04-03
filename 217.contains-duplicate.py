#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#

# @lc code=start
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        exist = set(())
        for i in nums:
            if i in exist:
                return True
            else:
                exist.add(i)

        return False


# @lc code=end
