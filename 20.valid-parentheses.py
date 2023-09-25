#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution(object):
    def isValid(self, s):
        stack = []
        for b in s:
            if b in ('(' , '[' , '{'):
                stack.append(b)
            elif len(stack):
               if abs(ord(stack.pop()) - ord(b)) not in (1,2):
                   return False                      
            else:
                return False

        if not len(stack):
            return True
        
        return False
        
# @lc code=end

