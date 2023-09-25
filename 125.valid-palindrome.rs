/*
 * @lc app=leetcode id=125 lang=rust
 *
 * [125] Valid Palindrome
 */

// @lc code=start
impl Solution {
    pub fn is_palindrome(s: String) -> bool {
        let mut char_array: Vec<char> = Vec::new();
        for c in s.to_ascii_lowercase().chars(){
            if c.is_alphanumeric(){
                char_array.push(c)
            }
        }

        for i in 0..char_array.len()/2 {
            if char_array[i] != char_array[char_array.len() - 1 - i]{
                return false;
            }
        }

        true
    }
}
// @lc code=end

