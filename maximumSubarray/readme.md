# Maximum Subarray problem
* Given an integer array `nums`, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.


### Approach 1: Bruth Force, maxSubArrayBruteForce()
This solution leads to TLE\
The idea is to exhaust all possible subarrays of the `nums` array and calculate sum and return the maximum sum. Time complexity is therefore O(n^3) where finding all possible subarrays will take O(n^2) and calculate sum of subarray will take O(n)



### Approach 2: Dynamic Programming, maxSubArrayDP()
Algorithm credits to https://leetcode.com/problems/maximum-subarray/discuss/20193/DP-solution-and-some-thoughts

The main idea is to use an array `dp` to holds the maximum sum of subarray up to index `i`: For example `dp[i]=3` means the maximum sum subarrays ending at index `i` is 3.\
We will only pass the `nums` once, for each of the new element, if the previous element in `dp` is greater than 0, which means the maximum sum if greater than 0, we can then sum up the current value with `dp[i-1]` because adding previous value will make our sum bigger. However, if the previous value in `dp` array is 0 or smaller than 0, we should add current value directly to `dp` array because adding previous value will make our sum smaller, so we will be better off if ignoring all values before current one. Then we can simply maintain a variable to hold the maximum sum seen so far and return it at the end.

Time complexity is O(n)\
![image](https://user-images.githubusercontent.com/25105806/126412809-138d3f81-764c-4fe8-99dd-b23eec194138.png)
