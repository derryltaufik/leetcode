#
# @lc app=leetcode id=1700 lang=python3
#
# [1700] Number of Students Unable to Eat Lunch
#

# @lc code=start
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        repeating = 0
        while True:
            if(repeating == len(students)):
                break
            if(students[0] == sandwiches[0]):
                students.pop(0)
                sandwiches.pop(0)
                repeating = 0
            else:
                val = students.pop(0)
                students.append(val)
                repeating+=1
        return len(students)
        
# @lc code=end

