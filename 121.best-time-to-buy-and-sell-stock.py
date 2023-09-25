#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        print()
        p1  = 0
        p2  = 0
        max_profit = 0

        while p2 < len(prices):
            max_profit = max((prices[p2] - prices[p1]), max_profit)
            if prices[p2] < prices[p1]:
                p1 = p2
            p2 += 1

        return max_profit
        
# @lc code=end

