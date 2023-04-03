#
# @lc app=leetcode id=912 lang=python3
#
# [912] Sort an Array
#

# @lc code=start


def merge(arr, l, m, r):

    arr1 = arr[l:m+1]
    arr2 = arr[m+1:r+1]
    index = l
    while len(arr1) > 0 and len(arr2) > 0:
        if arr1[0] <= arr2[0]:
            arr[index] = arr1.pop(0)
        else:
            arr[index] = arr2.pop(0)
        index += 1

    while len(arr1) > 0:
        arr[index] = arr1.pop(0)
        index += 1

    while len(arr2) > 0:
        arr[index] = arr2.pop(0)
        index += 1


# merge sort
def mergeSort(arr, l, r):
    if l < r:

        m = (l + r) // 2
        mergeSort(arr, l, m)
        mergeSort(arr, m + 1, r)

        merge(arr, l, m, r)


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        mergeSort(nums, 0, len(nums)-1)
        return nums


# @lc code=end
