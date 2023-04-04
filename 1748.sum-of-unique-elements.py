#
# @lc app=leetcode id=1748 lang=python3
#
# [1748] Sum of Unique Elements
#

# @lc code=start
class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        counter = Counter(nums)
        sum = 0
        for (k, v) in counter.items():
            if v == 1:
                sum += k

        return sum


# @lc code=end
