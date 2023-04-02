#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        appendable = ["(", "{", "["]
        # using ASCII

        for i in s:

            if i in appendable:
                stack.append(i)
            else:
                if len(stack) > 0 and abs(ord(i) - ord(stack[-1])) <= 2:
                    stack.pop()
                else:
                    return False

        return len(stack) == 0


# @lc code=end
