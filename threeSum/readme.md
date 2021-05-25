# 3Sum problem
* Given an integer array nums, return all the triplets `[nums[i], nums[j], nums[k]]` such that `i != j`, `i != k`, and `j != k`, and `nums[i] + nums[j] + nums[k] == 0`.
* Notice that the solution set must not contain duplicate triplets.

### Approach 1: Brute Force, threeSumBruteForce()
This the easiest solution and the also most inefficient one. Use nested loop to go through each 3-tuple combination of the numbers and check if they add up to 0. Since we use three nested for-loop, the time complexity is therefore O(n^3), which will lead to TLE(Time Limit Exceed).

### Approach 2: Generating all twoSums and store, threeSum2()
Use a O(n^2) algorithm first to generate all possible sums of two numbers and store them in a dict then go through the number list again to retrieve the desired sum using O(n) time. The time complexity is therefore O(n^2). But since this approach will also compute lots of unnecessary twoSums and store them in a dict, this will also lead to TLE.

### Approach 3: Generating desired twoSums on the fly, threeSumHash()
Similar to approach 2, but this time we only compute necessary twoSums instead of computing all of them and store. The details are: go through the list once and generate the desired twoSum value using O(n) time. twoSum is generated by using dict, which uses hasing to achieve constant lookup time. The time complexity for twoSumHash() is therefore O(n). The total time complexity is therefore O(n^2)
![image](https://user-images.githubusercontent.com/25105806/119203779-c62a3a80-ba48-11eb-82e6-6ff42952bc69.png)

### Approach 4: Two Pointers, threeSumOptimal()
Turns out we can first sort the list using built-int `.sort()` function, then again go through the list and use two pointers, `left` and `right` to bound the range that we take three values to check. There are three cases:
1. If the sum of current three values is smaller than 0, then that means the value pointer by `left` is too small and we should move the `left` to `left+1`.
2. If the sum of current three values is greater than 0, then that means the value pointer by `right` is too large and we should move the `right` to `right+1`.
3. If the sum of current three values is 0, then we're good.

* Note that we can use two pointers to adjust the sum of three numbers because the list is sorted, which means elements to the left are always smaller than the elements to the right.

Time complexity is O(n^2) because the sorting takes O(nlog(n)) time, the loop takes O(n^2) time.
![image](https://user-images.githubusercontent.com/25105806/119204207-b9f2ad00-ba49-11eb-8463-cc5817059055.png)