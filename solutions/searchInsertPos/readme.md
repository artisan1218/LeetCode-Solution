# Search Insert Position problem
* Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
* You must write an algorithm with `O(log n)` runtime complexity.

Leetcode link: https://leetcode.com/problems/search-insert-position/

<br />

### Approach 1: Binary Search, searchInsert()
This nothing but a regular binary search. The only tricky thing is that: if the target does not exist in the array `nums`, the place where it would be if it were inserted in order is exactly the place where `left` and `right` meet because they narrow down the range in searching for target and they meet before finding the target, so, just return `left` if it were not found.

```python3
def searchInsert(self, nums: List[int], target: int) -> int:
    left = 0
    right = len(nums)-1

    # regular binary search
    while left<=right:
        midpoint = int((left+right)/2)
        if nums[midpoint] < target:
            left = midpoint+1
        elif nums[midpoint] > target:
            right = midpoint-1
        else:
            return midpoint

    # if not found, the index where left and right meet will be the place for insertion
    return left
```


Time complexity is O(log n) for binary search:
![image](https://user-images.githubusercontent.com/25105806/122149655-47d77300-ce11-11eb-86df-c404f0796066.png)


