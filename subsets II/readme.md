# Subsets II problem
* Given an integer array `nums` that may contain duplicates, return all possible subsets (the power set).
* The solution set must not contain duplicate subsets. Return the solution in any order.

Leetcode link: https://leetcode.com/problems/subsets-ii/

<br />

### Approach 1: Generate All and Remove Dup, subsetsWithDupRemoveDupSubsets()
This solution is a brute force solution, we first generate all subsets like what we did in [subset](https://github.com/artisan1218/LeetCode-Solution/tree/main/subsets), then use `set` to remove any duplicate results.

```python3
def subsetsWithDupRemoveDupSubsets(self, nums: List[int]) -> List[List[int]]:
	def backtrack(nums, cur, result, start, length):
		if len(cur)==length:
			result.append(cur.copy())
		else:
			for i in range(start, len(nums)):
				if len(cur) + len(nums) - i + 1 >= length: # pruning
					cur.append(nums[i])
					backtrack(nums, cur, result, i+1, length)
					cur.pop()

	result = []
	for length in range(1, len(nums)+1):
		backtrack(nums, [], result, 0, length)

	# remove duplicates
	result = [tuple(sorted(subset)) for subset in result]
	result = list(set(result))
	result = [list(subset) for subset in result]
	return [[]] + result
```

Actual running time:\
![image](https://user-images.githubusercontent.com/25105806/134554504-7d213786-fb7c-4c00-9025-0567fd915500.png)

<br />

### Approach 2: DFS, subsetsWithDupDFS()
This solution is optimal one, which we still use DFS to exhaust all possible solutions, but add pruning conditions to prevent explore duplicate elements:
```
if i > start and nums[i] == nums[i-1]:
    continue
```

```python3
def subsetsWithDupDFS(self, nums: List[int]) -> List[List[int]]:
	def dfs(nums, cur, ret, start):
		ret.append(cur.copy())
		for i in range(start, len(nums)):
			# if this is not the first element in current level, we should check
			# the element before it to make sure we do not add duplicates
			if i > start and nums[i] == nums[i-1]:
				continue
			else:
				cur.append(nums[i])
				dfs(nums, cur, ret, i+1)
				cur.pop()

	ret = []
	dfs(sorted(nums), [], ret, 0)
	return ret
```

Actural running time:\
![image](https://user-images.githubusercontent.com/25105806/134554935-fc255db8-3ce3-4a4e-b130-8b38bfc528d2.png)
