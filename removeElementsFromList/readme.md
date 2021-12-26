# Remove Element problem
* Given an array nums and a value `val`, remove all instances of that value in-place and return the new length.
* Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
* The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Leetcode link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/

<br />

### Approach 1: Two Pointers, removeElementTwoPointers()
This approach is very similar to [Remove Duplicates](https://github.com/artisan1218/LeetCode-Solution/tree/main/removeDuplicatesFromList) problem, we still use two pointers, one points to the array itself to modify the value, the other pointer is used to traverse the array to get new element.\

```python3
def removeElementTwoPointers(self, nums: List[int], val: int) -> int:
    modifier = 0
    for idx in range(len(nums)):
        if nums[idx] != val:
            nums[modifier] = nums[idx]
            modifier+=1
    return modifier
```

Time complexity is O(n):\
![image](https://user-images.githubusercontent.com/25105806/120942888-8b7b0000-c6e0-11eb-8fba-e01ba5dfdfcb.png)

<br />

### Approach 2: Built-in Function, removeElementBuiltinFunc()
Turns out there is another easier solution to this: the built-in `.remove()` function in Python. Simply check for every element in the array and remove it if it is equal to `val`.

```python3
def removeElementBuiltinFunc(self, nums: List[int], val: int) -> int:
    while val in nums:
        nums.remove(val)
    return len(nums)
```

Time complexity is O(n^2) because we will iterate over the array once and `.remove()` function uses O(n) time.\
![image](https://user-images.githubusercontent.com/25105806/120942968-f75d6880-c6e0-11eb-9341-f53552815edf.png)

