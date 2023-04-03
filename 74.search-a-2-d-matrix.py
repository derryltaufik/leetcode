#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#

# @lc code=start


def closestBinarySearch(arr, l, r, target):
    if l <= r:
        m = (r + l) // 2
        x = arr[m]
        if x > target:
            return closestBinarySearch(arr, l, m - 1, target)
        elif x<target:
            return closestBinarySearch(arr, m + 1, r, target)
        else:
            return m
    else:
        return l-1


def binarySearch(arr, l, r, target):
    if l <= r:
        m = (r + l) // 2
        x = arr[m]
        if x == target:
            return m
        elif x > target:
            return binarySearch(arr, l, m - 1, target)
        else:
            return binarySearch(arr, m + 1, r, target)
    else:
        return -1


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # search  containing row first
        rowHeader = []
        for i in matrix:
            rowHeader.append(i[0])

        row_index = closestBinarySearch(rowHeader, 0, len(rowHeader) - 1, target)

        row = matrix[row_index]

        index = binarySearch(row, 0, len(row) - 1, target)

        return index != -1


# @lc code=end
