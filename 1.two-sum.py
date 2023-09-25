#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}
        for index, number in enumerate(nums):
            difference =  target - number
            if difference in num_dict:
                return [num_dict[difference], index]
            num_dict[number] = index
        
# @lc code=end

