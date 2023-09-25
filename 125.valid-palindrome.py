#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # fmt_string = re.sub(r'[^a-zA-Z0-9]', '', s.lower())
        fmt_string = ""
        for c in s.lower():
            if c.isalnum():
                fmt_string += c 

        str_len = len(fmt_string)
        for i in range(0, str_len//2):
            if fmt_string[i] != fmt_string[str_len - 1 - i]:
                return False

        return True
        
# @lc code=end