#
# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    # def hasCycle(self, head: Optional[ListNode]) -> bool:
    #     visited = []

    #     while head:
    #         if head in visited:
    #             return True
    #         visited.append(head)
    #         head = head.next

    #     return False

    # using tortoise hare cycle detection
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        try:
            tortoise = head
            hare = head.next
            while tortoise != hare:
                tortoise = tortoise.next
                hare = hare.next.next
        except:
            return False

        return True


# @lc code=end
