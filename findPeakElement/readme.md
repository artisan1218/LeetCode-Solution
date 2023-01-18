# Find Peak Element problem
![Screenshot 2023-01-17 at 9 49 30 PM](https://user-images.githubusercontent.com/25105806/213094583-eba0f9cf-99f0-40c2-93ba-832f6d631b89.png)


Leetcode link: https://leetcode.com/problems/find-peak-element/description/

<br/>

### Approach 1: Binary Search, findPeakElement()

It's easy to think of binary search algorithm when the run time complexity is O(logn). Some obsevations we get from the problem statement:
1. When finding the peak element, we only need to compare three elements one time: left, mid and right. These three elements corresponds to the three elements we need to compare with in the binary search
2. It's possible that there are multiple peak elements and there must be at least one element. We only need to find one element.

For example, if the `nums` is in increasing order, then the peak element is the right-most one. If the `nums` is in decreasing order, then the peak element will be the left-most one. In all other cases, peak element(s) will be in the middle(not on the side) of `nums`.

When doing binary search, we take the mid element as usual and compare it with the elements on the left(`mid-1`) and on the right(`mid+1`) because these are the only two elements we need to check before making sure that `nums[mid]` is an peak element. If mid is smaller than its right element, then this means `nums[mid+1:]` is still increasing, so there must be at least one peak element in this subarray no matter whether it will be decreasing on the right or not, note that there still might be peak elements on the left part but we don't care about that, all we need to know is we can put our focus on the right side because it's still increasing. So we can simply nail down our search range to [mid+1, right]. Similarily, we can nail down our search range to [left, mid-1] if the current mid element is smaller than left element.


```python3
def findPeakElement(self, nums: List[int]) -> int:
	left = 0
	right = len(nums)-1
	while left <= right:
		mid = (left + right)//2
		left_nei = nums[mid-1] if mid-1 >= 0 else float('-inf')
		right_nei = nums[mid+1] if mid+1 <= len(nums)-1 else float('-inf')

		if nums[mid] > right_nei and nums[mid] > left_nei:
			return mid
		elif nums[mid] < right_nei:
			# there must exist a peak element on the right
			# even though there also might be peak elements on the left
			left = mid+1
		else:
			right = mid-1
```

Time complexity is O(logn):
![image](https://user-images.githubusercontent.com/25105806/213096617-f2de89da-efdf-4bab-affa-1e111870a7b7.png)
