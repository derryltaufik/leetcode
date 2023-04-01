#
# @lc app=leetcode id=1470 lang=python3
#
# [1470] Shuffle the Array
#

# @lc code=start
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        a = nums[0:n]
        b = nums[n:]

        for i in range(len(nums)):
            if(i % 2 == 0):
                nums[i] = a[i//2]
            else:
                nums[i] = b[i//2]

        return nums
        
# @lc code=end

