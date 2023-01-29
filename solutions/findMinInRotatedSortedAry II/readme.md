# Find Minimum in Rotated Sorted Array II problem
![image](https://user-images.githubusercontent.com/25105806/206944393-9776221d-1947-411e-8757-cc55359fb2af.png)

Leetcode link: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/description/

<br />

### Approach 1: Recurssion, findMinRecurssion()

The idea is based on [findMinInRotatedSortedAry I](https://github.com/artisan1218/LeetCode-Solution/tree/main/findMinInRotatedSortedAry). When there are no duplicates in the `nums`, we have two cases: when `nums[mid] > nums[right]` and else. When there are duplicates, we have to deal with an additional case where `nums[right]==nums[mid]`. In this case, there is no way to decide which side of the nums the pivot is on. So we can recursively find min in both side and choose the min one.

```python3
def findMinRecurssion(self, nums: List[int]) -> int:
	left = 0
	right = len(nums)-1
	while right > left:
		mid = (left+right)//2
		if nums[mid] > nums[right]:
			left = mid + 1
		elif nums[mid] == nums[right]:
			return min(self.findMin(nums[mid:right]), self.findMin(nums[left:mid+1]))
		else:
			right = mid
	return nums[left]
```

Running time:\
![image](https://user-images.githubusercontent.com/25105806/206944909-0ad3ee5d-8bc7-4371-b007-7e51492e242c.png)

<br />

### Approach 2: Iterative, findMinIterative()

Instead of using recursion in the case where `nums[right]==nums[mid]`, we can also simply move the `right` pointer to left by 1 index, this means we will shrink the range one by one.

```python3
def findMinIterative(self, nums: List[int]) -> int:
	left = 0
	right = len(nums)-1
	while right > left:
		mid = (left+right)//2
		if nums[mid] > nums[right]:
			left = mid + 1
		elif nums[mid] == nums[right]:
			right-=1
		else:
			right = mid
	return nums[left]
```

Time complexity is O(logn) with O(n) as the worst case:\
![image](https://user-images.githubusercontent.com/25105806/206945284-c843a59e-0c41-4bb6-b338-04e9e2a7710b.png)
