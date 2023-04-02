#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            last = stack[-1] if len(stack) > 0 else None

            if i == ")":
                if last == "(":
                    stack.pop()
                else:
                    return False
            elif i == "]":
                if last == "[":
                    stack.pop()
                else:
                    return False
            elif i == "}":
                if last == "{":
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)

        return len(stack) == 0


# @lc code=end
