#
# @lc app=leetcode id=235 lang=python3
#
# [235] Lowest Common Ancestor of a Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        a = min(p.val, q.val)
        b = max(p.val, q.val)
        while root:
            if root.val < a:
                root = root.right
            elif root.val > b:
                root = root.left
            else:
                return root


# @lc code=end
