#
# @lc app=leetcode id=224 lang=python3
#
# [224] Basic Calculator
#

# @lc code=start
class Solution:
    def calculate(self, s: str) -> int:
        curNum = ans = 0
        curSign = 1  # 1 for +, -1 for -
        curStack = []
        for i in s:

            # digit
            if i.isdigit():
                curNum = curNum * 10 + int(i)
            # +-
            elif i in "+-":
                ans += curNum * curSign
                if i == "-":
                    curSign = -1
                else:
                    curSign = 1
                curNum = 0
            # (
            elif i == "(":
                curStack.append(ans)
                curStack.append(curSign)
                ans = 0
                curNum = 0
                curSign = 1
            # )
            elif i == ")":
                ans += curNum * curSign
                tempSign = curStack.pop()
                tempNum = curStack.pop()
                ans = (ans * tempSign) + tempNum
                curNum = 0

        ans += curNum * curSign
        return ans


# @lc code=end
