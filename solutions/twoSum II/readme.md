# Two Sum II problem
<img width="980" alt="image" src="https://user-images.githubusercontent.com/25105806/215598069-c37272df-69a1-431c-ac9a-d110f43a418c.png">


Leetcode link: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

<br />

### Approach 1: Two Pointer, twoSumTwoPointer()

Since the input `numbers` is sorted, we can assure that number one the right must not be smaller than the number on the left. We can use two pointers, one points to the first element and one points to the last element, then start comparing the sum of these two with `target`. If sum is smaller than `target`, we can safely move the left pointer to right by 1 index, and move right pointer to the left by 1 index if sum is greater than `target`. Keep doing this until we find the answer.

```python3
def twoSumTwoPointer(self, numbers: List[int], target: int) -> List[int]:
	left, right = 0, len(numbers)-1
	cur_sum = numbers[left]+numbers[right]
	while cur_sum != target:
		if cur_sum > target:
			right-=1
		else:
			left+=1

		cur_sum = numbers[left]+numbers[right]
	return [left+1, right+1] # +1 because it's 1-based
```

Time complexity is O(n) and space complexity is O(1):

<img width="597" alt="image" src="https://user-images.githubusercontent.com/25105806/215598837-5199402d-26c4-4245-be7f-8f47a639c11e.png">

<br />

### Approach 2: Map, twoSumMap()

Since we are looking for sum of two numbers, we can first iterate over `numbers`, storing all numbers and its index in a map, then in another iteration over the `numbers`, looking for existence of `target-num` in the map, since map lookup time is O(1), we can do this in O(n).

```python3
def twoSumMap(self, numbers: List[int], target: int) -> List[int]:
	num_dict = dict()
	for i, n in enumerate(numbers):
		num_dict[n] = i

	for i, num in enumerate(numbers):
		target2 = target-num
		if target2 in num_dict:
			return [min(i+1, num_dict[target2]+1), max(i+1, num_dict[target2]+1)]
```

Time complexity is O(n) and space complexity is O(n):

<img width="601" alt="image" src="https://user-images.githubusercontent.com/25105806/215599370-f1d47bfb-f90c-42c3-8a7c-930e9e434ef1.png">
