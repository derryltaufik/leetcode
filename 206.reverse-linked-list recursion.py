#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getNode(self, prev: ListNode, curr: ListNode):
        if curr != None:
            next = curr.next
            curr.next = prev

            return self.getNode(curr, next)
        else:
            return prev

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        return self.getNode(None, head)


# @lc code=end
