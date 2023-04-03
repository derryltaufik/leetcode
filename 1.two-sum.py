#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index = {} # value, index
        for i, val in enumerate(nums):
            pair = target-val
            if(pair in index):
                return [index[pair] , i]
            else:
                index[val] = i

        
# @lc code=end

