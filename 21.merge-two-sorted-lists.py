#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        temp_head = ListNode()
        ans = temp_head
        while list1 != None and list2 != None:

            if list1.val < list2.val:
                temp_head.next = list1
                list1 = list1.next
            else:
                temp_head.next = list2
                list2 = list2.next

            temp_head = temp_head.next
        
        if list1 or list2:
            temp_head.next = list1 if list1 else list2

        return ans.next


# @lc code=end
