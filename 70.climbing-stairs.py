#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:

        # memo = {}

        # def recur(steps):
        #     if steps <= 1:
        #         return 1

        #     if steps in memo:
        #         return memo[steps]

        #     res = recur(steps - 1) + recur(steps - 2)
        #     memo[steps] = res
        #     return res

        # return recur(n)

        # using @cache
        @lru_cache
        def recur2(steps):
            if steps <= 1:
                return 1
            return recur2(steps - 1) + recur2(steps - 2)

        return recur2(n)


# @lc code=end
