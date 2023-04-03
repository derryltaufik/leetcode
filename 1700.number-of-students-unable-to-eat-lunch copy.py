#
# @lc app=leetcode id=1700 lang=python3
#
# [1700] Number of Students Unable to Eat Lunch
#

# @lc code=start
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        while True:
            if(not students):
                break
            if(sandwiches[0] in students): # if anyone in the line want the sandwiches
                students.remove(sandwiches[0]) # one person takes the sandwich
                sandwiches.pop(0) # sandwich taken
            else:
                break
        return len(students)
        
# @lc code=end

