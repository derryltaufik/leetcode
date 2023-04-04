#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def symmetric(left, right):

            if left is None and right is None:
                return True
            if not left or not right or left.val != right.val:
                return False
            return symmetric(left.left, right.right) and symmetric(
                left.right, right.left
            )

        return True if root is None else symmetric(root.left, root.right)


# @lc code=end
