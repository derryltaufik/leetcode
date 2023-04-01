#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#


# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        find = 0
        swap = len(nums) -1
        for i in nums:
            if(find > swap):
                break
            if(nums[find] == val):
                nums[find] = nums[swap]
                swap-=1
            else:
                find+=1
        return swap+1

        
# @lc code=end

