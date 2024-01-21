# Rotate Array problem
<img width="653" alt="image" src="https://github.com/artisan1218/LeetCode-Solution/assets/25105806/acdc175b-9084-42b6-9a3e-169d014f8026">


Leetcode link: https://leetcode.com/problems/rotate-array/description/

<br />

### Approach 1: Naive, rotatePopAndInsertOneByOne()
This is the naive solution where we just imitate the actual `rotation` process, we pop one element from the end and insert it back to the beginning k times to get the result.

```python
def rotatePopAndInsertOneByOne(self, nums: List[int], k: int) -> None:
	"""
	Do not return anything, modify nums in-place instead.
	"""
	for i in range(k):
		transfer = nums.pop(-1)
		nums.insert(0, transfer)
```

Time complexity is O(kn) because `.insert()` function is O(n) and we do it for `k` times. This is TLE'ed


<br>

### Approach 2: Slicing, rotateCut()

Instead of transferring the elements in array one by one, we can slice the array and move them to the beginning all at once.


```python
def rotateCut(self, nums: List[int], k: int) -> None:
	"""
	Do not return anything, modify nums in-place instead.
	"""
	k  = k % len(nums) # if k is longer than length of nums, take the remainder of it
	end = nums[:len(nums)-k] # get the part that will be attached to the end
	del nums[:len(nums)-k] # remove the part from front
	nums.extend(end) # attach to end
```

Running time:

<img width="674" alt="Screenshot 2024-01-20 at 9 36 33 PM" src="https://github.com/artisan1218/LeetCode-Solution/assets/25105806/f3f60135-df3a-4be0-879c-f3e6aa743e83">


However, this is not using O(1) space as we need to store the slice temporarily in memory


<br>

### Approach 3: Swapping, rotateO1Space()

If we observe the rotation of the array, we can notice that the array can be in-place swapped to save memory. Since we're doing `k` rotations, we can 'rotate' the part before k and after k by swapping the elements. 

Code:

```python
 def rotateO1Space(self, nums: List[int], k: int) -> None:
	"""
	Do not return anything, modify nums in-place instead.
	"""
	k  = k % len(nums)
	def reverseSubList(nums, left, right):
		for i in range((right-left)//2):
			nums[left+i], nums[right-i-1] = nums[right-i-1], nums[left+i]
		
	reverseSubList(nums, 0, len(nums)-k)
	reverseSubList(nums, len(nums)-k, len(nums))
	nums.reverse()
```


If the original array is `[1, 2, 3, 4, 5, 6, 7]` and `k` is 3, then the process follows:

```
[1, 2, 3, 4, 5, 6, 7]
[4, 2, 3, 1, 5, 6, 7]
[4, 3, 2, 1, 5, 6, 7]
[4, 3, 2, 1, 7, 6, 5]
```
Then simply reverse the entire array to get the result: `[5, 6, 7, 1, 2, 3, 4]`



Since we are not storing any extra value in memory, the space complexity is O(1):

<img width="657" alt="Screenshot 2024-01-20 at 9 44 25 PM" src="https://github.com/artisan1218/LeetCode-Solution/assets/25105806/9db6be4c-90a0-4214-88d5-4fbe8cd27570">



