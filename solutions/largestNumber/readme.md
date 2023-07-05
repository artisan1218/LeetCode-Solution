# Largest Number problem
![image](https://github.com/artisan1218/LeetCode-Solution/assets/25105806/47fdd64d-dd2c-4647-b90e-968f89241ccf)


Leetcode link: https://leetcode.com/problems/largest-number/description/

<br/>

### Approach 1: Custom Sorting, largestNumber()
The key part is to think of this question as a sorting problem instead of how to build the largest number. Building of the largest number is actually to sort the number list in an order such that `a+b` is larger than `b+a`, note that `+` sign means concatenation instead of mathematical plus. We don't need to come up with the logic of building the largest number, we just need to let `.sort()` handle it. This is also a smart use of sort function with custom keys.

Code:
```python3
def largestNumber(self, nums: List[int]) -> str:
	custom_key = functools.cmp_to_key(lambda a, b: 1 if b+a>a+b else -1)
	
	strNums = map(str, nums)
	trim_zeros = int(''.join(sorted(strNums, key=custom_key)))
	return str(trim_zeros)
```

Actual running time:
![image](https://github.com/artisan1218/LeetCode-Solution/assets/25105806/d9872f13-ab0c-4d09-9a29-c15a6d7b371f)
