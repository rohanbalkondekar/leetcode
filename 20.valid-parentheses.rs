/*
 * @lc app=leetcode id=20 lang=rust
 *
 * [20] Valid Parentheses
 */

// @lc code=start

impl Solution {
    pub fn is_valid(input_str: String) -> bool {
        let mut stack: Vec<char> = Vec::new();

        for curr_char in input_str.chars() {
            match curr_char {
                '(' | '{' | '[' => {
                    stack.push(curr_char);
                }

                ')' | '}' | ']' => match stack.pop() {
                    Some(popped_char) => match curr_char as i32 - popped_char as i32 {
                        2 | 1 => {
                            continue;
                        }
                        _ => {
                            return false;
                        }
                    },

                    None => {
                        return false;
                    }
                },

                _ => {}
            }
        }
        if stack.len() != 0 {
            return false;
        } else {
            true
        }
    }
}
// @lc code=end

