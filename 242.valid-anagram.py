#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t) or (len(s) == 0 or len(t) == 0):
            return False
        
        letter_count = [0] * 26

        for c in s:
            letter_count[ord(c) - ord("a")] += 1

        for c in t:
            letter_count[ord(c) - ord("a")] -= 1

        for n in letter_count:
            if n:
                return False
        
        return True

# @lc code=end
