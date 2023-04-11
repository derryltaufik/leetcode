#
# @lc app=leetcode id=1342 lang=python3
#
# [1342] Number of Steps to Reduce a Number to Zero
#

# @lc code=start
class Solution:
    # def numberOfSteps(self, num: int) -> int:

    #     ans = 0

    #     while num > 0:
    #         if num % 2 == 0:
    #             num //= 2
    #         else:
    #             num -= 1
    #         ans += 1
    #     return ans

    def numberOfSteps(self, num: int) -> int:

        a = bin(num)

        length = len(a[2:])
        bit = 0

        for i in a[2:]:
            bit += int(i)

        return length + bit - 1


# @lc code=end
