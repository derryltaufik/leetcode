#
# @lc app=leetcode id=383 lang=python3
#
# [383] Ransom Note
#

# @lc code=start
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        lenr = len(ransomNote)
        lenm = len(magazine)
        if lenr > lenm:
            return False

        magdict = Counter(magazine)

        for i in ransomNote:
            if i in magdict:
                magdict[i] -= 1
                if magdict[i] == 0:
                    del magdict[i]
            else:
                return False

        return True


# @lc code=end
