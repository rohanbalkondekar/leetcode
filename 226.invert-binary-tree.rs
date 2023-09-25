/*
 * @lc app=leetcode id=226 lang=rust
 *
 * [226] Invert Binary Tree
 */

// @lc code=start
// Definition for a binary tree node.
// #[derive(Debug, PartialEq, Eq)]
// pub struct TreeNode {
//   pub val: i32,
//   pub left: Option<Rc<RefCell<TreeNode>>>,
//   pub right: Option<Rc<RefCell<TreeNode>>>,
// }
// 
// impl TreeNode {
//   #[inline]
//   pub fn new(val: i32) -> Self {
//     TreeNode {
//       val,
//       left: None,
//       right: None
//     }
//   }
// }
use std::rc::Rc;
use std::cell::RefCell;
impl Solution {
    pub fn invert_tree(root: Option<Rc<RefCell<TreeNode>>>) -> Option<Rc<RefCell<TreeNode>>> {
        if let Some(node) = root.clone() {
            let mut node_borrow = node.borrow_mut();
            
            // Swap the children one at a time
            let left_child = std::mem::replace(&mut node_borrow.left, None);
            let right_child = std::mem::replace(&mut node_borrow.right, None);
            
            // Swap the children back into their respective places
            node_borrow.left = Solution::invert_tree(right_child);
            node_borrow.right = Solution::invert_tree(left_child);
        }

        root
    }
}
// @lc code=end

