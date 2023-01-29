# 3Sum Closest problem
* Given an array `nums` of n integers and an integer `target`, find three integers in `nums` such that the sum is closest to `target`. Return the sum of the three integers. You may assume that each input would have exactly one solution.

Leetcode link: https://leetcode.com/problems/3sum-closest/

<br />

### Approach 1: Brute Force, Skipped
Use three nested for loop to iterate over the given `nums` three times and compare the result, keep the best one. Time complexity is O(n^3)

<br />

### Approach 2: Two Pointers, threeSumClosest()
The idea is pretty similar to [3Sum](https://github.com/artisan1218/LeetCode-Solution/tree/main/threeSum) problem, that we can first sort the list using built-int `.sort()` function, then again go through the list and use two pointers, `left` and `right` to bound the range that we take three values to check. There are three cases:
1. If the sum of current three values is smaller than `target`, then that means the value pointer by `left` is too small and we should move the `left` to `left+1`.
2. If the sum of current three values is greater than `target`, then that means the value pointer by `right` is too large and we should move the `right` to `right+1`.
3. If the sum of current three values is equal to `target`, then simply break the loop and return the target value.

The only difference is that we need to keep track of the closest sum so far because we're not guaranteed that the exact match exist in the given `nums`.

* Note that we can use two pointers to adjust the sum of three numbers because the list is sorted, which means elements to the left are always smaller than the elements to the right.


```python3
def threeSumClosest(nums: List[int], target: int) -> int:
    result = list()
    nums.sort()
    
    closest = 0
    prev_diff = float('inf')
    # at least three elements in nums is needed, otherwise just return empty list
    for idx in range(len(nums)-2):
        # use two pointers to bound the range
        left = idx+1 # left pointer always start at current index + 1 so that it never visit seen elements
        right = len(nums)-1
        if idx==0 or nums[idx]!=nums[idx-1]: #will skip the same value
            while left < right:
                # update the best result so far
                curr_diff = abs(target - (nums[idx] + nums[left] + nums[right]))
                if curr_diff < prev_diff:
                    prev_diff = curr_diff
                    closest = nums[idx] + nums[left] + nums[right]
                    
                # update pointers
                if nums[idx] + nums[left] + nums[right] == target:
                    return target
                elif nums[idx] + nums[left] + nums[right] < target:
                    left+=1
                else:
                    right-=1
    return closest

```

Time complexity is O(n^2) because the sorting takes O(nlog(n)) time, the loop takes O(n^2) time.
![image](https://user-images.githubusercontent.com/25105806/119450519-dfe9ad00-bce8-11eb-9c53-9c4d7541f279.png)
