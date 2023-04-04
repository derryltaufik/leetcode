#
# @lc app=leetcode id=1572 lang=python3
#
# [1572] Matrix Diagonal Sum
#

# @lc code=start
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        sum = 0
        length = len(mat)
        for i in range(length // 2):
            a = i
            b = length - 1 - i
            sum += mat[a][a] + mat[a][b] + mat[b][a] + mat[b][b]

        if length % 2 != 0:
            sum += mat[length // 2][length // 2]

        return sum


# @lc code=end
