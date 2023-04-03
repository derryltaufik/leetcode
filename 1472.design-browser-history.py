#
# @lc app=leetcode id=1472 lang=python3
#
# [1472] Design Browser History
#

# @lc code=start
class BrowserHistory:

    def __init__(self, homepage: str):
        self.index = 0
        self.history = [homepage]
        

    def visit(self, url: str) -> None:
        del self.history[self.index+1:]
        self.history.append(url)
        self.index = len(self.history)-1

    def back(self, steps: int) -> str:
        self.index -= steps
        self.index = max(0,self.index)
        
        return self.history[self.index]
        

    def forward(self, steps: int) -> str:
        self.index += steps
        self.index = min(len(self.history)-1,self.index)
        
        return self.history[self.index]

        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
# @lc code=end

