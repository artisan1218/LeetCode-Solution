# Find Minimum in Rotated Sorted Array problem
<img width="735" alt="image" src="https://user-images.githubusercontent.com/25105806/206638787-c96f5106-3931-45ee-9c53-45751e536915.png">

Leetcode link: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

<br />

### Approach 1: Binary Search, findMin()

When the required time complexity is O(logn), it's easy to think of binary search as the solution. Since the array is sorted(but rotated), which means the array can be divided into two parts, each part is sorted by itself, we can start from left and right ends and make the range smaller and smaller and finally get the min number.

The idea is similar to binary search. The difference is that in this problem, we do not know the target, so the condition we use to shrink the range is the comparsion between `mid` and `right`. When `mid` is larger than `right`, this means current `mid` number is greater than the biggest number in the right array, which means the pivot point and min number must also be on the right side. So we should update `left` boundary to `mid + 1`. Otherwise, we update `right` boundary to `mid`. 

Notice that `left` can be updated to `mid + 1`, +1 because current `mid` is greater than the `right`, so `mid` cannot be the min number, so we can skip this one. But we cannot do the same when updating `right`.

```python3
def findMin(self, nums: List[int]) -> int:
	left = 0
	right = len(nums)-1
	while right > left:
		mid = (left+right)//2
		if nums[mid] > nums[right]:
			left = mid + 1
		else:
			right = mid

	return nums[left]
```


Time complexity is O(logn): 
<img width="852" alt="image" src="https://user-images.githubusercontent.com/25105806/206640864-fcaba1e2-8858-4709-9523-59135c808716.png">

