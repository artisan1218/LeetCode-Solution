# Maximum Subarray problem
* Given an integer array `nums`, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.


Leetcode link: https://leetcode.com/problems/maximum-subarray/

<br />

### Approach 1: Bruth Force, maxSubArrayBruteForce()
This solution leads to TLE\
The idea is to exhaust all possible subarrays of the `nums` array and calculate sum and return the maximum sum. Time complexity is therefore O(n^3) where finding all possible subarrays will take O(n^2) and calculate sum of subarray will take O(n)

```java
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

public int getSum(int[] nums, int left, int right) {
    int sum = 0;
    while (left <= right) {
        sum += nums[left];
        left++;
    }
    return sum;
}
```


<br />


### Approach 2: Dynamic Programming, maxSubArrayDP()
Algorithm credits to https://leetcode.com/problems/maximum-subarray/discuss/20193/DP-solution-and-some-thoughts

The main idea is to use an array `dp` to holds the maximum sum of subarray up to index `i`: For example `dp[i]=3` means the maximum sum subarrays ending at index `i` is 3.\
We will only pass the `nums` once, for each of the new element, if the previous element in `dp` is greater than 0, which means the maximum sum if greater than 0, we can then sum up the current value with `dp[i-1]` because adding previous value will make our sum bigger. However, if the previous value in `dp` array is 0 or smaller than 0, we should add current value directly to `dp` array because adding previous value will make our sum smaller, so we will be better off if ignoring all values before current one. Then we can simply maintain a variable to hold the maximum sum seen so far and return it at the end.

![maxSubarrayAnimation](https://user-images.githubusercontent.com/25105806/126414463-64f0ff28-791c-44b3-ad80-2f9de23b135f.gif)


**Note: Click [here](https://github.com/artisan1218/LeetCode-Solution/blob/main/solutions/maximumSubarray/maxSubarrayAnimation.ppsx) to download the animation to play for yourself.**


```java
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
```

Time complexity is O(n)\
![image](https://user-images.githubusercontent.com/25105806/126412809-138d3f81-764c-4fe8-99dd-b23eec194138.png)
