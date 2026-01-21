class Solution {
    public int searchInsert(int[] nums, int target) {

        // Traverse the array
        for (int i = 0; i < nums.length; i++) {

            // If target is found OR current number is greater than target
            if (nums[i] >= target) {
                return i;
            }
        }

        // If target is greater than all elements
        return nums.length;
    }
}
