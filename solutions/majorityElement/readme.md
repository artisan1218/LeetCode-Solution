# Majority Element problem
![image](https://user-images.githubusercontent.com/25105806/222879813-6fe8e45e-e76c-4193-a956-30464c3b4198.png)

Leetcode link: https://leetcode.com/problems/majority-element/

<br />

### Approach 1: Boyer–Moore Algorithm, majorityElement()

Credits to: https://www.youtube.com/watch?v=7pnhv842keE

The idea is still to count the number of occurrences of the numbers, but instead of counting and storing occurrences of every number, we only use one variable to store the count and current num because we know that

`The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.` 

This means the occurrences of the majority element will always be greater than the rest of numbers. So we can just start iterate over the `nums` list and to see if the next number if equal to current `result`, if so, increment the count by 1, otherwise decrement by 1. This is similar to let each elements cancel out each other and since we know there are more majority elements than all the other elements combined, the remaining element will always be the majority element, so it does not matter what element we start with.

The only case is when the count is 0, which means some element(might be majority elements) cancelled out the same amount of other elements at current index, instead of keep decrementing the count, we can let it start from 1 again and assign current `num` to `result` so that it can start 'cancel out' again.

Code: 
```python3
def majorityElement(self, nums: List[int]) -> int:
	count = 0
	result = 0
	for num in nums:
		if count==0:
			result = num
			count = 1
		else:
			if num==result:
				count+=1
			else:
				count-=1
	return result
```

Time complexity is O(n) and space complexity is O(1):
![image](https://user-images.githubusercontent.com/25105806/222880282-9933e7bd-3e6f-4371-80a1-19179be4b54e.png)
