#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    memo = []

    def recur(self,steps):
        if(steps <=1):
            return 1
        
        if self.memo[steps] != None:
            return self.memo[steps]
        else:
            self.memo[steps] = self.recur(steps-1) + self.recur(steps-2)
            return self.memo[steps]
        

    def climbStairs(self, n: int) -> int:
        self.memo = [None] * (n+1)
        return self.recur(n)

# @lc code=end

