#
# @lc app=leetcode id=2103 lang=python3
#
# [2103] Rings and Rods
#

# @lc code=start
class Solution:
    def countPoints(self, rings: str) -> int:
        rods = {}

        for i in range(0, len(rings), 2):

            color = rings[i]
            rod = rings[i + 1]
            if rod not in rods:
                rods[rod] = set((color))
            else:
                rods[rod].add(color)
        sum = 0

        for i in rods.values():
            if len(i) == 3:
                sum += 1

        return sum


# @lc code=end
