# Find First and Last Position of Element in Sorted Array problem
* Given an array of integers `nums` sorted in ascending order, find the starting and ending position of a given `target` value.
* If target is not found in the array, return `[-1, -1]`.
* You must write an algorithm with `O(log n)` runtime complexity.

![image](https://user-images.githubusercontent.com/25105806/145897375-5e242413-fba4-47bb-97ce-8ecc612d1551.png)

Leetcode link: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

<br/>

### Approach 1: Binary Search and Expand Around Center, searchRangeExpandAroundMiddle()
Since the array `nums` is a non-decreasing array, we can use binary search to first find the target value. Note that there might be several target values in the array, the goal here is find one of them, then we expand to left and right around that 'center' value. 

```python
def searchRangeExpandAroundMiddle(self, nums: List[int], target: int) -> List[int]:
    # regular binary search to find the index of a target
    left = 0
    right = len(nums)-1

    # 'middle' denotes the index of the target
    # middle is not necessarily the exact middle point of the range, but just a point in the range
    middle = -1
    while left<=right:
        midpoint = int((left+right)/2)
        if nums[midpoint] < target:
            left = midpoint+1
        elif nums[midpoint] > target:
            right = midpoint-1
        else:
            middle = midpoint
            break

    # if the target is not found
    if middle==-1:
        return [-1, -1]
    else:
        # middle is not necessarily the exact middle point of the range, but just a point in the range
        start = middle
        end = middle

        # This is not really an O(log n) code block but it works
        # expand the range at the 'middle' point to the left and right 
        while start>=0 and nums[start]==target or end<len(nums) and nums[end]==target:
            if start>=0 and nums[start]==target:
                start -= 1
            if end<len(nums) and nums[end]==target:
                end += 1

        return [start+1, end-1]
```

The time complexity is not strictly O(log n) but O(log n + m) where m is the length of the valid targets.\
Actual running time:\
![image](https://user-images.githubusercontent.com/25105806/122143381-39d02500-ce06-11eb-9525-0f29ef74343c.png)

<br />

### Approach 2: Two Pass Binary Search, searchRangeTwoPassBinarySearch()
This approach is a strictly O(log n) approach where we first search for the starting index of the range using one binary search, which takes O(log n) time then use another binary search to find the ending index of the range, which is also O(log n).\
We need to modify the standard binary search algorithm in order to find the starting or ending index of the target. The idea is:
1. When finding the starting index, if the midpoint value is equal to target, we do not return it yet, instead, keep moving right pointer to left to check the values before the midpoint value.
2. When finding the ending index, if the midpoint value is equal to target, we do not return it yet, instead, keep moving left pointer to the right to check the values after the midpoint value.

```python
def searchRangeTwoPassBinarySearch(self, nums: List[int], target: int) -> List[int]:
    # use binary search to find the start index of the range
    left = 0
    right = len(nums)-1
    start = -1
    while left<=right:
        midpoint = int((left+right)/2)
        if nums[midpoint] < target:
            left = midpoint+1
        else:
            if nums[midpoint] > target:
                right = midpoint-1
            else:
                # nums[midpoint] == target
                # if midpoint is the beginning of the nums, or the previous value is not equal to target
                # this means midpoint is now the starting index of the range, simply return it
                if midpoint==0 or nums[midpoint-1]!=target:
                    start = midpoint
                    break
                # otherwise we should move rigth pointer as if nums[midpoint] > target 
                # because we want midpoint goes to left
                # this is why this algorihtm still have O(log n) complexity
                else:
                    right = midpoint-1

    if start==-1:
        return [-1, -1]
    else:
        # use binary search to find the end index of the range only when start is not -1
        # left can be start index because we've ruled out every element before start
        left = start
        right = len(nums)-1
        end = -1
        while left<=right:
            midpoint = int((left+right)/2)
            if nums[midpoint] <= target:
                if nums[midpoint] < target:
                    left = midpoint+1
                else:
                    # case where midpoint is equal to target
                    # if midpoint is the ending of the nums, or the next value is not equal to target
                    # this means midpoint is now the ending index of the range, simply return it
                    if midpoint==len(nums)-1 or nums[midpoint+1]!=target:
                        end = midpoint
                        break
                    # otherwise we should move the left pointer because we want
                    # the midpoint to goes to right
                    # this is why this algorihtm still have O(log n) complexity
                    else:
                        left = midpoint+1
            else:
                # nums[midpoint] > target
                right = midpoint-1

    return [start, end]
```

The total time complexity is therefore O(2\*logn) which is O(log n)\
Actual running time:\
![image](https://user-images.githubusercontent.com/25105806/122143548-8582ce80-ce06-11eb-9707-ccc640010d8c.png)
