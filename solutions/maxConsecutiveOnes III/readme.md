# Max Consecutive Ones III problem
<img width="645" alt="image" src="https://user-images.githubusercontent.com/25105806/216861662-c3b45d6a-276c-4dad-b4f5-cb6ba497af3f.png">


Leetcode link: https://leetcode.com/problems/max-consecutive-ones-iii/


<br/>

### Approach 1: Sliding Window, longestOnes()

The question can be translated to `find longest sequence with at most k 0s`. Main logic is to use two pointers to frame a window, if there are less than `k` or equal number of zeros, we can move the right pointer to the right to expand the window to make it longer, otherwise we move left pointer to the right until there are less than `k` or equal number of zeros. 

So we can start from `left=0` and `right=0`, if the current element at `right` is 1, then we can safely move the `right` pointer to right by 1 index, if the current element is 0, then we need to compare the number `k` we can still flip. If current `k` is greater than 0, we can subtract 1 from it and expand right pointer, otherwise we need to move `left` pointer and reclaim any `k` if the element at `left` pointer is 0, which means we no longer include that 0 in our window so we don't need to flip that 0 anymore.

```python3
def longestOnes(self, nums: List[int], k: int) -> int:
	left, right = 0, 0
	max_num = 0
	while right<len(nums):
		if nums[right]==1:
			right+=1
		else:
			if k>0:
				k-=1 # flip
				right+=1
			else:
				# used all flips and current right is 0
				# we need to move left pointer to left
				left+=1
				if nums[left]==0:
					k+=1 # reclaim one flip chance
		max_num = max(max_num, right-left)
	return max_num
```

Time complexity is O(n):

<img width="774" alt="image" src="https://user-images.githubusercontent.com/25105806/216862885-191b5ee3-1b0a-4962-a2ff-79d998460175.png">
