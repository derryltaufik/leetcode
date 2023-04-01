#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        existed = []
        for i in nums:
            if i not in existed:
                existed.append(i)
            
        nums[:len(existed)] = existed
        return len(existed)


# @lc code=end
