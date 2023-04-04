#
# @lc app=leetcode id=1207 lang=python3
#
# [1207] Unique Number of Occurrences
#

# @lc code=start
class Solution:
    # def uniqueOccurrences(self, arr: List[int]) -> bool:
    #     count = {}
    #     for i in arr:
    #         if i in count:
    #             count[i] += 1
    #         else:
    #             count[i] = 1
    #     seen = set(())
    #     for i in count.values():
    #         if i in seen:
    #             return False
    #         else:
    #             seen.add(i)

    #     return True

    # using counter
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = Counter(arr)
        seen = set(count.values())
        return len(count) == len(seen)


# @lc code=end
