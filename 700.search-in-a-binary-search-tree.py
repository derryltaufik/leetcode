#
# @lc app=leetcode id=700 lang=python3
#
# [700] Search in a Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def findNode(node):
            if node is None or node.val == val:
                return node
            if val < node.val:
                return findNode(node.left)
            if val > node.val:
                return findNode(node.right)

        node = findNode(root)

        return node


# @lc code=end
