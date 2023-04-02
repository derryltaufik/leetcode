#
# @lc app=leetcode id=155 lang=python3
#
# [155] Min Stack
#

# @lc code=start
class MinStack:
    def __init__(self):
        self.stack = []
        self.minimum = []
        pass

    def push(self, val: int) -> None:
        if len(self.minimum) == 0 :
            self.minimum.append(val)
        else:
            self.minimum.append(min(val,self.minimum[-1]))

        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minimum.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minimum[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end
