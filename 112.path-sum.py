#
# @lc app=leetcode id=112 lang=python3
#
# [112] Path Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        if root is None:
            return False

        def isLeaf(node):
            if node.left:
                return False
            if node.right:
                return False
            return True

        def getSum(parent, node, curSum):
            if node is None:
                if curSum == targetSum and isLeaf(parent):
                    return True
                else:
                    return False

            return getSum(node, node.left, curSum + node.val) or getSum(
                node, node.right, curSum + node.val
            )

        return getSum(None, root, 0)


# @lc code=end
