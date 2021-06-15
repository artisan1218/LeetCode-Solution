# Search in Rotated Sorted Array problem
* There is an integer array `nums` sorted in ascending order (with distinct values).
* Prior to being passed to your function, `nums` is rotated at an unknown pivot index `k` (`0 <= k < nums.length`) such that the resulting array is `[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed)`. For example, `[0,1,2,4,5,6,7]` might be rotated at pivot index 3 and become `[4,5,6,7,0,1,2]`.
* Given the array `nums` **after** the rotation and an integer target, return the index of target if it is in `nums`, or `-1` if it is not in `nums`.
* You must write an algorithm with `O(log n)` runtime complexity.


### Approach 1: Binary Search with Recursion, searchBinarySearch1()
Since the arra `nums` is guaranteed to be rotated at some pivot, we can first use binary search to find the pivot point, then find the target according to the pivot point using again, binary search.\
The function `binarySearchPivot()` is used to find pivot point with recursion. If the pivot is not presented in a subarray, it will return -1 (Note here that -1 simply means the pivot point is **NOT** in this subarray) and take the max value of the pivot of two subarrays to find the actual pivot point.\
The function `binarySearchTarget()` is to find the actual target. It will first decide which part of the entire array does the target locate in, then just search using regular binary search.

The time complexity is O(log n) because we merely use two binary search, which is O(log n) for each.
![image](https://user-images.githubusercontent.com/25105806/121980659-30c95000-cd41-11eb-8c39-772032e4b718.png)

<br />

### Approach 2: Improved Binary Search, searchBinarySearch2()
The idea is the same as approach 1 but use iteration to find the pivot point instead of recursion. This is also an O(log n) solution with two pass binary search. First to find pivot and second to find actual target.

Demo:

<img src="https://user-images.githubusercontent.com/25105806/121984069-30cc4e80-cd47-11eb-860b-c0822d67db05.gif" height="90%" width="90%">

**Note: Click [here](https://github.com/artisan1218/LeetCode-Solution/blob/main/searchRotatedSortedAry/searchRotatedSortedAry.ppsx) to download the animation to play for yourself**

Actual running time:\
![image](https://user-images.githubusercontent.com/25105806/121980862-8dc50600-cd41-11eb-83a7-348a00de126a.png)
