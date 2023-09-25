#
# @lc app=leetcode id=217 lang=python
#
# [217] Contains Duplicate
#

# @lc code=start
class Solution(object):
    def containsDuplicate(self, nums):
        num_set = set()
        for num in nums:
            if num in num_set:
                return True
            num_set.add(num)
        
        return False
        
# @lc code=end

