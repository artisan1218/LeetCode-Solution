# Maximum Product Subarray
![image](https://user-images.githubusercontent.com/25105806/201553990-4192b726-b202-44e4-a229-1554acda1f0e.png)


Leetcode Link: https://leetcode.com/problems/maximum-product-subarray/

<br />

### Approach 1: Seperate By 0 and Count Neg, maxProductCountNegNum()

This solution is based on two observations:
1. 0 will make our product reset to 0, so we do not want 0 in our subarray
2. If the subarray has all positive numbers or even number of negative numbers, we can simply multiply them all together

Therefore, we can first split the array by 0, which means we will only look at subarrays without 0. Then we'll count the number of negative numbers in the subarray, if even number, then simply multiply them together, otherwise, we need to exclude one negative number from the subarray when calculating the max product, because excluding one negative number will make total number of negative numbers back to even. Since the subarray has to be continuous, we only need to consider excluding the first negative or last negative.

Actual code:
```python3
def maxProductCountNegNum(self, nums: List[int]) -> int:
	def maxProductInAryWithoutZero(nums):
		if len(nums) == 1:
			return nums[0]
		else:
			firstNegIndex = -1
			lastNegIndex = -1
			negCount = 0
			for i, n in enumerate(nums):
				if n < 0:
					negCount += 1
					if firstNegIndex == -1:
						firstNegIndex = i
					lastNegIndex = i
			if negCount%2 == 0:
				return math.prod(nums)
			else:
				# odd number of negative number, then we only care about the first and last neg number
				# we can either include the first one and exclude the last one
				# or exclude the first one and include the last one
				return max(math.prod(nums[0:lastNegIndex]), math.prod(nums[firstNegIndex+1:]))

	# split by 0
	subary = []
	result = max(nums)
	for i, n in enumerate(nums):
		if n==0:
			if len(subary)!=0:
				result = max(result, maxProductInAryWithoutZero(subary.copy()))
				subary = []
		else:
			subary.append(n)
			if i==len(nums)-1:
				result = max(result, maxProductInAryWithoutZero(subary.copy()))
	return result
```

Time complexity is O(n):
![image](https://user-images.githubusercontent.com/25105806/201554416-9eeb6ec2-8595-450e-b881-61b7b01524ce.png)


<br />

### Approach 2: Left and Right Scan, maxProductLeftAndRightScan()

Credits to: https://leetcode.com/problems/maximum-product-subarray/discuss/48302/2-Passes-scan-beats-99

1. When the array has even number of negative numbers eg. [1,2,-3,-4,5,6]. Both left and right scans yield the same result.
2. When the array has multiple odd number of negative integers. eg. [1,2,-3,-4,-5, 6]. We can think of the "last" negative number in each scan breaks the array into 2 halves. In this case , the max array in left scan is the maximum of ([1,2,-3,-4] and [6]) which is 24. In the reverse, the split is delimited by -3. So the max subarrray is teh maximum of ([6,-5,-4] and [2])

```Python3
def maxProductLeftAndRightScan(self, nums: List[int]) -> int:
	leftMax, rightMax = float('-inf'), float('-inf')
	product = 1
	for n in nums:
		product *= n
		leftMax = max(leftMax, product)
		if n==0:
			product = 1

	product = 1
	for n in nums[::-1]:
		product *= n
		rightMax = max(rightMax, product)
		if n==0:
			product = 1

	return max(leftMax, rightMax)
```

Time complexity is O(n):
![image](https://user-images.githubusercontent.com/25105806/201555103-93120336-708d-47ef-a272-c980b664afb2.png)


<br />

### Approach 3: One Scan, maxProductSingleScan()

Credits to: https://www.youtube.com/watch?v=lXVy6YWFcRM

When we scan from left to right, it's possible that one negative number will make our current max result the smallest result, and vice versa. The result is going back and forth between min and max. If wen can record both current min result and current max result, then we only need one scan. 

Note that when calculating the `curMin` and `curMax`, we also need to compare with `n`. Consider the case `[-1, 8]`, when `curMin` and `curMax` are both `-1`, the product will be `-8` if we don't compare with sole `n`.

```Python3
def maxProductSingleScan(self, nums: List[int]) -> int:
	result = max(nums)
	curMin, curMax = 1, 1
	for n in nums:
		tmp = curMin
		curMin = min(curMin*n, curMax*n, n)
		curMax = max(tmp*n, curMax*n, n)
		result = max(result, curMax)
	return result
```

Time complexity is O(n):
![image](https://user-images.githubusercontent.com/25105806/201555621-aaf07a1c-817e-47ba-ab89-5a1390f8fe09.png)

