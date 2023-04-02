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
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        a = []
        while head != None:
            a.append(head)
            head = head.next

        a.reverse()
        new_head = None
        temp = ListNode()
        for i in range(len(a)):

            temp.val = a[i].val
            temp.next = a[i + 1] if i + 1 < len(a) else None

            if i == 0:
                new_head = temp

            temp = temp.next


        return new_head


# @lc code=end
