#
# @lc app=leetcode id=230 lang=python3
#
# [230] Kth Smallest Element in a BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        counter = 0
        stack = []

        def search(node):
            nonlocal counter
            nonlocal stack
            if node:
                search(node.left)
                if counter == k:
                    return
                stack.append(node.val)
                counter += 1
                search(node.right)

        search(root)
        return stack[-1]


# @lc code=end
