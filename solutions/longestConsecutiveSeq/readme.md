# Longest Consecutive Sequence problem
![image](https://user-images.githubusercontent.com/25105806/155870706-0bc76273-1a6f-4e80-9cac-122ea1c02111.png)

Leetcode link: https://leetcode.com/problems/longest-consecutive-sequence/

<br/>


### Approach 1: Expand, longestConsecutiveExpand()
We can think of the `nums` as multiple groups of consecutive numbers in random order. First construct a hash set that enables constant lookup time for a specific number in `nums`. Then for each number, we check both the immediate smaller number and immediate greater number, which are the number smaller than current number by 1 and the number greater than current number by 1. Then we iteratively update the left boundary and right boundary in a loop until we've found the smallest number and greatest number in this group. 

Note that use of `see` set will make sure we only check number once and therefore speed up.

```python3
def longestConsecutiveExpand(self, nums: List[int]) -> int:
	numSet = set(nums)
	longest = 0
	seen = set()
	for num in nums:
		seen.add(num)
		left = num - 1 # we need left or right to make this num a streak
		right = num + 1
		while left in numSet or right in numSet:
			if left in numSet:
				left -= 1
				seen.add(left)
			if right in numSet:
				right += 1
				seen.add(right)

		longest = max(longest, right-left-1)

		if len(seen) == len(numSet):
			break
	return longest
```

Time complexity is O(n):\
![image](https://user-images.githubusercontent.com/25105806/155870897-ce521a96-761f-48c6-9e7c-1e3881ad005b.png)


<br/>

### Approach 2: longestConsecutiveFindStart()

Credits to: https://www.youtube.com/watch?v=P6RZZMu_maU

The idea is to find the start number of each streak in `nums`, then iteratively found the bigger numbers on the right. We can identify the first number by checking if `num-` exists in the `nums`, then simply count the number of bigger numbers on the right.

![image](https://user-images.githubusercontent.com/25105806/155870992-9e9de27d-f190-4bfc-a694-13175c5b4edf.png)


```python3
def longestConsecutiveFindStart(self, nums: List[int]) -> int:
	numSet = set(nums)
	longest = 0
	for num in numSet: # we want to iterate over the set not original num list because set removes duplicates and it's faster
		if num-1 not in numSet: # this is the start of a streak
			end = num + 1 # looking for the end of the streak
			while end in numSet:
				end += 1
			longest = max(longest, end-num)
	return longest
```

Time complexity is O(n):\
![image](https://user-images.githubusercontent.com/25105806/155870971-1f2e3451-fa05-4d51-be2c-afc7b61c996c.png)
