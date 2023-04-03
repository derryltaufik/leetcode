#
# @lc app=leetcode id=881 lang=python3
#
# [881] Boats to Save People
#

# @lc code=start
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left = 0
        right = len(people)-1

        boatCount = 0
        while left <= right:
            if people[left] + people[right] <= limit:
                left += 1

            right -= 1
            boatCount += 1

        return boatCount


# @lc code=end
