# Search in Rotated Sorted Array problem
* There is an integer array `nums` sorted in ascending order (with distinct values).
* Prior to being passed to your function, `nums` is rotated at an unknown pivot index `k` (`0 <= k < nums.length`) such that the resulting array is `[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed)`. For example, `[0,1,2,4,5,6,7]` might be rotated at pivot index 3 and become `[4,5,6,7,0,1,2]`.
* Given the array `nums` **after** the rotation and an integer target, return the index of target if it is in `nums`, or `-1` if it is not in `nums`.
* You must write an algorithm with `O(log n)` runtime complexity.

![image](https://user-images.githubusercontent.com/25105806/145897103-385b8abe-1f65-4e00-8667-c21e47d0d217.png)

Leetcode link: https://leetcode.com/problems/search-in-rotated-sorted-array/

<br/>

### Approach 1: Binary Search with Recursion, searchBinarySearch1()
Since the arra `nums` is guaranteed to be rotated at some pivot, we can first use binary search to find the pivot point, then find the target according to the pivot point using again, binary search.\
The function `binarySearchPivot()` is used to find pivot point with recursion. If the pivot is not presented in a subarray, it will return -1 (Note here that -1 simply means the pivot point is **NOT** in this subarray) and take the max value of the pivot of two subarrays to find the actual pivot point.\
The function `binarySearchTarget()` is to find the actual target. It will first decide which part of the entire array does the target locate in, then just search using regular binary search.

```python
def searchBinarySearch1(self, nums: List[int], target: int) -> int:
    # first to find the pivot index
    pivot = self.binarySearchPivot(nums, 0)
    pivot = len(nums)-1 if pivot==-1 else pivot
    # then find the target according to pivot index
    idx = self.binarySearchTarget(nums, target, pivot)
    return idx

def binarySearchTarget(self, nums: List[int], target: int, pivot: int) -> int:
    if len(nums)==1:
        return 0 if nums[0]==target else -1
    else:
        # decide which side of pivot does the target locate
        if nums[0] < target:
            # target is in the left side of pivot
            left = 1
            right = pivot+1
        elif nums[0] > target:
            # target is in the right side of the pivot
            left = pivot
            right = len(nums)
        else:
            # nums[0] == target
            return 0

        # binary search the target
        while left!=right:
            checkPt = int((left + right)/2)
            if nums[checkPt]<target:
                left = checkPt+1
            elif nums[checkPt]>target:
                right = checkPt
            else:
                return checkPt
        return -1

def binarySearchPivot(self, nums: List[int], totalIndex: int) -> int:
    # the -1 here simply means we cannot find the pivot point in this subarray
    if len(nums)==1:
        return -1
    else:
        # index where we partition the list into two parts to perform binary search
        checkPt = int(len(nums) / 2)
        if checkPt+1 < len(nums) and nums[checkPt] > nums[checkPt+1]:
            return checkPt + totalIndex
        elif checkPt-1 >=0 and nums[checkPt] < nums[checkPt-1]:
            return checkPt - 1 + totalIndex
        else:
            # totalIndex is to calculate the index of the pivot point in entire list not just this subarray
            leftSideIdx = self.binarySearchPivot(nums[0:checkPt], totalIndex)
            rightSideIdx = self.binarySearchPivot(nums[checkPt:], totalIndex+checkPt)
            # the partition without pivot point will always have a result of -1
            return max(leftSideIdx, rightSideIdx)
```

The time complexity is O(log n) because we merely use two binary search, which is O(log n) for each.
![image](https://user-images.githubusercontent.com/25105806/121980659-30c95000-cd41-11eb-8c39-772032e4b718.png)

<br />

### Approach 2: Improved Binary Search, searchBinarySearch2()
The idea is the same as approach 1 but use iteration to find the pivot point instead of recursion. This is also an O(log n) solution with two pass binary search. First to find pivot and second to find actual target.

Demo:\
<img src="https://user-images.githubusercontent.com/25105806/121984069-30cc4e80-cd47-11eb-860b-c0822d67db05.gif" height="90%" width="90%">

**Note: Click [here](https://github.com/artisan1218/LeetCode-Solution/blob/main/searchRotatedSortedAry/searchRotatedSortedAry.ppsx) to download the animation to play for yourself**

```python
def searchBinarySearch2(self, nums: List[int], target: int) -> int:
    left = 0
    right = len(nums)-1

    # use binary search to find the pivot point
    while left<right:
        midpoint = int((left + right)/2)
        if nums[midpoint] > nums[right]:
            # the midpoint value is larger than the right value
            # so this is the subarray where rotation happens
            # move the left pointer up the point where midpoint
            # value is not longer greater than right value
            left = midpoint+1
        else:
            # if midpoint value is smaller than the right value
            # then this means the subarray bounded by left and right
            # is sorted, so we should move right pointer to the midpoint
            # to check the other half of the array
            right = midpoint

    # left and right pointer will finally meet at the same point
    # this is where begin our next binary search to find the target
    pivot = left
    left = 0
    right = len(nums)-1

    # first to decide which part of the array should we perform bianry search on
    if target>=nums[pivot] and target<=nums[right]:
        # the right part of the array
        left = pivot
    else:
        # the left part of the array
        right = pivot

    # this is where regular binary search begins
    while left<=right:
        midpoint = int((left+right)/2)
        if nums[midpoint]<target:
            left = midpoint+1
        elif nums[midpoint]>target:
            right = midpoint-1
        else:
            return midpoint
    return -1
```

Actual running time:\
![image](https://user-images.githubusercontent.com/25105806/121980862-8dc50600-cd41-11eb-83a7-348a00de126a.png)
