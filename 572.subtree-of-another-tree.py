#
# @lc app=leetcode id=572 lang=python3
#
# [572] Subtree of Another Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSame(a, b):
            if a is None and b is None:
                return True
            if a is None or b is None or a.val != b.val:
                return False

            return isSame(a.left, b.left) and isSame(a.right, b.right)

        def search(node, target):

            if node is None:
                return False
            if isSame(node, target):
                return True

            return search(node.left, target) or search(node.right, target)

        return search(root, subRoot)


# @lc code=end
