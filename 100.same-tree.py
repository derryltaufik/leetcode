#
# @lc app=leetcode id=100 lang=python3
#
# [100] Same Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def search(p, q):
            if p is None and q is None:
                return True
            if (not q or not p) or (p.val != q.val):
                return False

            return search(p.left, q.left) and search(p.right, q.right)

        return search(p, q)


# @lc code=end
