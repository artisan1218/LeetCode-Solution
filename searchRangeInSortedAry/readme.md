# Find First and Last Position of Element in Sorted Array problem
* Given an array of integers `nums` sorted in ascending order, find the starting and ending position of a given `target` value.
* If target is not found in the array, return `[-1, -1]`.
* You must write an algorithm with `O(log n)` runtime complexity.


### Approach 1: Binary Search and Expand Around Center, searchRangeExpandAroundMiddle()
Since the array `nums` is a non-decreasing array, we can use binary search to first find the target value. Note that there might be several target values in the array, the goal here is find one of them, then we expand to left and right around that 'center' value. 

The time complexity is not strictly O(log n) but O(log n + m) where m is the length of the valid targets.\
Actual running time:
![image](https://user-images.githubusercontent.com/25105806/122143381-39d02500-ce06-11eb-9525-0f29ef74343c.png)

<br />

### Approach 2: Two Pass Binary Search, searchRangeTwoPassBinarySearch()
This approach is a strictly O(log n) approach where we first search for the starting index of the range using one binary search, which takes O(log n) time then use another binary search to find the ending index of the range, which is also O(log n).\
We need to modify the standard binary search algorithm in order to find the starting or ending index of the target. The idea is:
1. When finding the starting index, if the midpoint value is equal to target, we do not return it yet, instead, keep moving right pointer to left to check the values before the midpoint value.
2. When finding the ending index, if the midpoint value is equal to target, we do not return it yet, instead, keep moving left pointer to the right to check the values after the midpoint value.

The total time complexity is therefore O(2\*logn) which is O(log n)

Actual running time:\
![image](https://user-images.githubusercontent.com/25105806/122143548-8582ce80-ce06-11eb-9707-ccc640010d8c.png)
