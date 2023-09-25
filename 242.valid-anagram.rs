/*
 * @lc app=leetcode id=242 lang=rust
 *
 * [242] Valid Anagram
 */

// @lc code=start
impl Solution {
    pub fn is_anagram(s: String, t: String) -> bool {
        if (s.len() | t.len() == 0) | (s.len() != t.len()){
           return false
        }

        let mut num_frequency: [i32; 26] = [0; 26];

        for c in s.chars(){
            let serial_no:usize = (c as usize) - ('a' as usize);
            num_frequency[serial_no] += 1;   
        }
        
        for c in t.chars(){
            let serial_no:usize = (c as usize) - ('a' as usize);
            num_frequency[serial_no] -= 1;   
        }

        for n in num_frequency{
            if n != 0 {
                return false;
            }
        }

        true            
    }
}
// @lc code=end

