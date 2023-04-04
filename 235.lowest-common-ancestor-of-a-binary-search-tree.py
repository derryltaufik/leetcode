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
        # a = min(p.val, q.val)
        # b = max(p.val, q.val)
        # while root:
        #     if root.val < a:
        #         root = root.right
        #     elif root.val > b:
        #         root = root.left
        #     else:
        #         return root

        # using recursion

        small = big = 0
        if p.val > q.val:
            small = q.val
            big = p.val
        else:
            small = p.val
            big = q.val

        def search(node, small, big):
            if node is None:
                return None

            if small <= node.val <= big:
                return node
            elif node.val > small:
                return search(node.left, small, big)
            elif node.val < big:
                return search(node.right, small, big)

        return search(root, small, big)


# @lc code=end
