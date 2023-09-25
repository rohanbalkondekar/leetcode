/*
 * @lc app=leetcode id=121 lang=rust
 *
 * [121] Best Time to Buy and Sell Stock
 */

// @lc code=start
impl Solution {
    pub fn max_profit(prices: Vec<i32>) -> i32 {
     let mut p1 = 0;
     let mut p2 = 0; 
     let mut max_profit = 0;
    
     while p2 < prices.len(){
         max_profit = (prices[p2] - prices[p1]).max(max_profit);
         if prices[p2] < prices[p1]{
            p1 = p2;
         }
         p2 += 1;
     }

     max_profit
    }
}
// @lc code=end

