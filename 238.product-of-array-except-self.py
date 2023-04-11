#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start
class Solution:
    # def productExceptSelf(self, nums: List[int]) -> List[int]:
    #     pre = [nums[0]]
    #     post = [nums[-1]]
    #     length = len(nums)
    #     for i in range(1, length):
    #         b = length - i - 1
    #         pre.append(pre[-1] * nums[i])
    #         post.insert(0, post[0] * nums[b])
    #     ans = [post[1]]
    #     for i in range(1, length - 1):
    #         ans.append(pre[i - 1] * post[i + 1])
    #     ans.append(pre[-2])
    #     return ans

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        length = len(nums)
        tempPre = 1
        for i in range(0, length):
            ans.append(tempPre)
            tempPre *= nums[i]

        tempPost = 1
        for i in range(length - 1, -1, -1):
            ans[i] *= tempPost
            tempPost *= nums[i]
        return ans


# @lc code=end
