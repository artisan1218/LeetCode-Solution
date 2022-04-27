# Search in Rotated Sorted Array II problem
![image](https://user-images.githubusercontent.com/25105806/132747051-fa5cdaf3-64ab-4bbf-8fdd-8465cba2664b.png)

Leetcode link: https://leetcode.com/problems/search-in-rotated-sorted-array-ii/

<br />

### Approach 1: Binary Search, search()
The idea is same as [searchRotatedSortedAry](https://github.com/artisan1218/LeetCode-Solution/tree/main/searchRotatedSortedAry), first find the pivot point using a binary search, then find the `target` using another binary search in the correct subarray that contains the `target`. The only difference is that we need to handle the duplicates in the `nums` while using binary search to find the pivot point:
```
#handle the duplicates
while left<right and nums[mid]==nums[left]:
  left+=1
```

Complete code:

```python3
def search(self, nums: List[int], target: int) -> bool:
    # find the pivot point using binary search
    left = 0
    right = len(nums)-1
    while left < right:
        mid = (left + right)//2
        # incase we hit the target, early stopping
        if nums[mid]==target:
            return True

        # handle the duplicates
        while left<right and nums[mid]==nums[left]:
            left+=1

        if nums[right] < nums[mid]:
            left = mid + 1
        else:
            # right is greater than middle, meaning middle is at the rotated part of the array
            right = mid

    # update left and right to make sure left and right bound the correct subarray that contains target
    pivot = left
    left = 0
    right = len(nums)-1
    if target>=nums[pivot] and target<=nums[right]:
        left = pivot
    else:
        right = pivot

    # regular binary search
    while left<=right:
        mid = (left + right)//2
        if nums[mid]==target:
            return True
        elif nums[mid]>target:
            right = mid-1
        else:
            left = mid+1

    return False
```

Time complexity is O(logn), worst case is O(n) --- when all elements are duplicates\
![image](https://user-images.githubusercontent.com/25105806/132747553-e3ebc633-4734-408e-bbfa-909c9fce7e4e.png)


