#
# @lc app=leetcode id=350 lang=python3
#
# [350] Intersection of Two Arrays II
#

# @lc code=start
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        for i in nums1:
            if i in nums2:
                nums2.remove(i)
                ans.append(i)

        return ans        
# @lc code=end

