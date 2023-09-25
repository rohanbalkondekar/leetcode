/*
 * @lc app=leetcode id=1 lang=rust
 *
 * [1] Two Sum
 */

// @lc code=start
use std::{collections::HashMap, vec};
use std::convert::TryInto;

impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut nums_map: HashMap<i32, usize> = HashMap::new();

        for (index, num) in nums.iter().enumerate(){
            let diffrence = target - num;
            if nums_map.contains_key(&diffrence){
                return vec![nums_map[&diffrence].try_into().unwrap(), index.try_into().unwrap()];
            }
            nums_map.insert(*num, index);
        }
        vec![]
    }
}
// @lc code=end

