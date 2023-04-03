#
# @lc app=leetcode id=704 lang=python3
#
# [704] Binary Search
#

# @lc code=start


def binarySearch(arr, l, r, target):
    if l <= r:
        m = (r + l) // 2
        x = arr[m]
        if x == target:
            return m
        elif x > target:
            return binarySearch(arr, l, m - 1, target)
        else:
            return binarySearch(arr, m+1, r, target)
    else:
        return -1


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return binarySearch(nums, 0, len(nums) - 1, target)


# @lc code=end
