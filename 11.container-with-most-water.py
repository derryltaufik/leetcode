#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        l = 0
        r = len(height)-1
        while l <r:
            max_area = max(max_area, min(height[l],height[r]) * (r-l) )

            if(height[r] > height[l]):
                l+=1
            else:
                r-=1
        
        return max_area


        
# @lc code=end

