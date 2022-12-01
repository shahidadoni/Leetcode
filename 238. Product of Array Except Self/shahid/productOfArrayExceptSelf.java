// This solution calculates value of current position 
// which is product till current position - 1 of original array  in first loop
// from starting index to end index.
// Example: current position = product till (current - 1) position

// Second loop calculate from end index till start index 
// but this time the value of current position is the product of current position of result array
// with product till current position + 1 of original array.
// Example: current position = current position of result array * product till (current + 1)
public class Solution {
    public int[] productExceptSelf(int[] nums) {
        int n = nums.length;
        int[] res = new int[n];
        // Calculate lefts and store in res.
        int left = 1;
        for (int i = 0; i < n; i++) {
            if (i > 0)
                left = left * nums[i - 1];
            res[i] = left;
        }
        // Calculate rights and the product from the end of the array.
        int right = 1;
        for (int i = n - 1; i >= 0; i--) {
            if (i < n - 1)
                right = right * nums[i + 1];
            res[i] *= right;
        }
        return res;
    }
}