class Solution:
    def maxSubArray(self, nums):
        def findIndex():
            curSum = 0
            maxSum = nums[0]
            l, r, maxL, maxR = 0, 0, 0, 0

            for r in range(len(nums)):
                n = nums[r]
                if curSum + n < n:
                    l = r
                curSum = max(curSum + n, n)

                if curSum > maxSum:
                    maxL, maxR = l, r
                maxSum = max(curSum, maxSum)

            return (maxL, maxR)

        return findIndex()


print(Solution().maxSubArray([5,4,-1,7,8]))
