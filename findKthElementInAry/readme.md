# Kth Largest Element in an Array problem
<img width="615" alt="image" src="https://user-images.githubusercontent.com/25105806/195516883-09951ab9-cc60-4630-a795-79a15754e7db.png">


Leetcode link: https://leetcode.com/problems/kth-largest-element-in-an-array/

<br />

### Approach 1: Quickselect, findKthLargest()

Reference: https://www.youtube.com/watch?v=XEmy13g1Qxc

The idea is similar to Quicksort algorithm. We first pick a pivot point and swap the elements in `nums` to make sure
1. Every element less than pivot on the LHS of pivot
2. Every element greater than pivot on the RHS of pivot

This part is identical to quicksort. However, since we only care about the `kth` element, we don't need to sort all elements in the array, we only need to process either the left part or the right part of the array, depending on whether the kth element is smaller than pivot or greater than pivot, which saves lots of time.

Consider this example:
```
nums = [3, 5, 1, 4, 6, 2]
k = 2

Since we want kth largest element, the index we're looking for is actually len(nums)-k, which is 4. So this is the element index as if the array is sorted.

We pick pivot point always to be the right most element, which is 4.

i,p            pivot
[3, 5, 1, 4, 6, 2]

 p     i       pivot
[3, 5, 1, 4, 6, 2]     at this step, we swap nums[p] and nums[i] because nums[i] is smaller than pivot

    p        i pivot
[1, 5, 3, 4, 6, 2]     keep looping and reached the rightmost-1 index, next step is to swap p and pivot

  pivot         p
[1, 2, 3, 4, 6, 5]     at this step, all elements on the LHS of pivot is smaller than pivot and all elements on RHS is greater than pivot

```

<br />

If the kth element is smaller than pivot point, then we only need to keep search on the left part because we know that the kth element will not appear in the right part and vice versa. If, however, kth element is exactly the pivot, then we can simply return the result.

<br />

Note: depending on whether we want kth smallest element or kth largest element, we can change the `kth` variable accordingly and the rest is the same

```python3
def findKthLargest(self, nums: List[int], k: int) -> int:
	kth = len(nums) - k
	# kth = k - 1 if want kth smallest element

	def quickSelect(l, r):
		# similar to quicksort
		# nums[r] is the pivot value
		ptr = l
		for i in range(l, r):
			if nums[i] < nums[r]:
				nums[ptr], nums[i] = nums[i], nums[ptr]
				ptr += 1
		# swap ptr with nums[r](the pivot value) to make
		# every element less than pivot on the LHS of pivot
		# every element greater than pivot on the RHS of pivot
		nums[ptr], nums[r] = nums[r], nums[ptr]

		# ptr is the index of the pivot now
		if kth < ptr:
			# kth element index is less than p, then we know target k will be on the left hand side
			return quickSelect(l, ptr-1)
		elif kth > ptr:
			# kth element index is greater than p, then focus on right part of p
			return quickSelect(ptr+1, r)
		else:
			return nums[ptr]  # kth==p
	return quickSelect(0, len(nums)-1)
```

Time complexity is O(n): the first time we swap the array is O(n), then next we only need to swap half of the array, O(n/2), then O(n/4), etc. This series sums up to O(2n) which is O(n) complexity. Space complexity is O(1) because no extra space is used:
<img width="772" alt="image" src="https://user-images.githubusercontent.com/25105806/195520228-529f3b31-23e9-4fa6-9334-20138365b8ed.png">



