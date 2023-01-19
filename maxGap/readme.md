# Maximum Gap problem
![image](https://user-images.githubusercontent.com/25105806/213358476-19b31534-7cbe-4807-9e69-e9add2e1cad3.png)


Leetcode link: https://leetcode.com/problems/maximum-gap/description/

<br />

### Approach 1: Bucket Sort, maximumGap()

Credits to: https://leetcode.com/problems/maximum-gap/solutions/1241681/java-python-bucket-idea-with-picture-clean-concise-o-n/

Because the time complexity is O(n) and memory complexity is O(n), we can think of bucket sort to use in this question. The idea is to divide the number in `nums` into `n` buckets, each buckets will hold a range of number. Then we only calculate the gap between max number of previous bucket and min number of current bucket, this will reduce the calculations to `n-1`. Also, since we only care about the min and max in each bucket, we can only store these two numbers in each bucket. In implementation, we can use `minBuckets` and `maxBuckets` list to store the value.

When calculating the gap, `maxGap` can be initialized to `bucketSize` because `maxGap` is always greater or equal to `bucketSize`, why? Because we have `n` buckets but we evenly distribute the all possible numbers(`maxNum-minNum`) in `nums` into `n-1` ranges, which means, at least one bucket must be empty according to pigeon hole's principle. So the max gap must be between two buckets and the empty bucket must be next to one of the two buckets.

```python3
def maximumGap(self, nums: List[int]) -> int:
	minNum = min(nums)
	maxNum = max(nums)
	n = len(nums)

	if minNum == maxNum:
		return 0  # all nums are the same
	else:
		bucketSize = math.ceil((maxNum-minNum) / (n-1))
		# since we only need to store the min and max value in each bucket, 
		# we can simply use two bucket lists to represent the min and max at each bucket
		minBuckets = [float('inf')] * n
		maxBuckets = [float('-inf')] * n
		for num in nums:
			idx = (num - minNum) // bucketSize # find out which bucket num belongs to
			minBuckets[idx] = min(minBuckets[idx], num)
			maxBuckets[idx] = max(maxBuckets[idx], num)

		# maxGap can be initialized to bucketSize because maxGap is always greater 
		# or equal to bucketSize
		maxGap = bucketSize 
		prevMax = maxBuckets[0]
		for i in range(1, n):
			if minBuckets[i] == float('inf'):
				continue # skip the empty bucket
			else:
				# subtract max value in previous bucket from current min value 
				maxGap = max(maxGap, minBuckets[i] - prevMax)
				prevMax = maxBuckets[i]
		return maxGap
```

Time complexity is O(n): ![image](https://user-images.githubusercontent.com/25105806/213359481-ea529735-e601-46b2-b26f-622469cff80c.png)
