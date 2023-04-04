#
# @lc app=leetcode id=1832 lang=python3
#
# [1832] Check if the Sentence Is Pangram
#

# @lc code=start
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        exist = set(())
        for i in sentence:
            exist.add(i)

        return len(exist) == 26


# @lc code=end
