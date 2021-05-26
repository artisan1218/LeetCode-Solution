# 4Sum problem
* Given an array nums of n integers, return an array of all the unique quadruplets `[nums[a], nums[b], nums[c], nums[d]]` such that:
```
0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
```
You may return the answer in any order.

### Approach 1: Two Pointers, fourSumBasedOnThreeSum()
This approach is based on [3Sum](https://github.com/artisan1218/LeetCode-Solution/tree/main/threeSum) problem. The idea is to go through the list, fix one number at a time and find corresponding three sum and append them together. We just grab threeSum() and use it in a loop to achieve this. Time complexity is simply O(n\*threeSum Complexity), which is O(n^3).\
Actual running time is indeed quite slow:

![image](https://user-images.githubusercontent.com/25105806/119611564-b778b600-bdaf-11eb-833d-eaa0a89855ef.png)


### Approach 2: Two Pointers, Recursion, Solution.fourSum()
Credits to https://leetcode.com/problems/4sum/discuss/8545/Python-140ms-beats-100-and-works-for-N-sum-(Ngreater2)
\
This approach considers a more generalized case of kSum. We can solve 2Sum problem really quick using two pointers, to solve 3Sum problem, simply fix a number and use 2Sum algorithm to find the rest two numbers. The idea can be extended to kSum by using recursion. 
1. Base case: 2Sum using two pointers
2. Recursive step: kSum = nSum(nums, k-1, k-1 result)

We use recursion to reduce k down to 2 and keep the k-1 result to append it to k result. So that we always fix a number and find k-1 sum.

Actual running time is quite fast:

![image](https://user-images.githubusercontent.com/25105806/119612527-d9bf0380-bdb0-11eb-9bfa-f65f11284c64.png)


