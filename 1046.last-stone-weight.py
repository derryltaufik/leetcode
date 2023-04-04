#
# @lc app=leetcode id=1046 lang=python3
#
# [1046] Last Stone Weight
#

# @lc code=start
import bisect


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        while len(stones) > 1:
            a = stones.pop()
            b = stones.pop()
            diff = abs(a - b)
            if diff > 0:
                bisect.insort(
                    stones, diff
                )  # alt binary search & insert / search & sort

            print(stones)

        return 0 if len(stones) == 0 else stones[0]


# @lc code=end
