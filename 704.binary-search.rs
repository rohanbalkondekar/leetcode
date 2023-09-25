/*
 * @lc app=leetcode id=704 lang=rust
 *
 * [704] Binary Search
 */

// @lc code=start
impl Solution {
    pub fn search(nums: Vec<i32>, target: i32) -> i32 {
        let mut begin = 0;
        let mut end = nums.len() - 1;

        while begin < end {
            let mid = begin + (end - begin) / 2;
            if target < nums[mid] {
                end = mid - 1;
            } else if target > nums[mid] {
                begin = mid + 1;
            } else {
                return mid as i32;
            }
        }

        return -1;
    }
}

// @lc code=end
