impl Solution {
    pub fn contains_duplicate(nums: Vec<i32>) -> bool {
        let mut num_set: HashSet<i32> = HashSet::new();

        for num in nums{
            if num_set.contains(&num){
                return true
            }
            num_set.insert(num);
        }
        false
    }
}