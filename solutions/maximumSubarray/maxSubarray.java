public class maxSubarray {

    public static void main(String[] args) {
	// TODO Auto-generated method stub
	int[] nums = new int[] { 1, 2, -1, -2, 2, 1, -2, 1, 4, -5, 4 };
	Solution solver = new Solution();
	System.out.println(solver.maxSubArrayDP(nums));
    }

    static class Solution {

	public int maxSubArrayDP(int[] nums) {
	    // dp[i] is the maximum sum of subarray up to index i
	    int[] dp = new int[nums.length];
	    dp[0] = nums[0];
	    int maxSum = dp[0];

	    for (int i = 1; i < nums.length; i++) {
		// previous sum is greater than 0, we should sum nums[i] with previous value
		// previous value is smaller or equal to 0, we should only add nums[i]
		dp[i] = nums[i] + (dp[i - 1] > 0 ? dp[i - 1] : 0);
		maxSum = Math.max(maxSum, dp[i]);
	    }

	    return maxSum;
	}

	public int getSum(int[] nums, int left, int right) {
	    int sum = 0;
	    while (left <= right) {
		sum += nums[left];
		left++;
	    }
	    return sum;
	}

	public int maxSubArrayBruteForce(int[] nums) {
	    int maxSum = Integer.MIN_VALUE;
	    for (int i = 0; i < nums.length; i++) {
		for (int j = nums.length - 1; j >= i; j--) {
		    int curMax = getSum(nums, i, j);
		    if (curMax > maxSum) {
			maxSum = curMax;
		    }
		}
	    }

	    return maxSum;
	}
    }
}
