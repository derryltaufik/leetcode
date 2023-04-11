#
# @lc app=leetcode id=412 lang=python3
#
# [412] Fizz Buzz
#

# @lc code=start
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = []
        for i in range(1, n + 1):
            a = ""

            if i % 3 == 0:
                a += "Fizz"
            if i % 5 == 0:
                a += "Buzz"
            if a == "":
                a += str(i)
            ans.append(a)

        return ans


# @lc code=end
