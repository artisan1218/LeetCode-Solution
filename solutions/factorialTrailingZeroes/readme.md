# Factorial Trailing Zeroes problem
<img width="629" alt="image" src="https://user-images.githubusercontent.com/25105806/222944882-1e9a8a93-c90e-4985-af86-434b802e6ac5.png">

Leetcode link: https://leetcode.com/problems/factorial-trailing-zeroes/description/

<br/>

### Approach 1: Brute Force, trailingZeroesBruteForce()

We simply calculate the factorial, then count the number of trailing zeroes.


```python3
def trailingZeroesBruteForce(self, n: int) -> int:
	if n==0:
		return 0

	fact = 1
	while n>0:
		fact = fact * n
		n-=1

	fact_str = str(fact)
	zeros = 0
	i = len(fact_str) - 1
	while fact_str[i] == '0':
		zeros+=1
		i-=1
	return zeros
```
Time complexity is O(n):

<img width="803" alt="image" src="https://user-images.githubusercontent.com/25105806/222944976-79993ba7-71f1-4da2-8cfe-8fb2b8d93f3c.png">

<br/>

### Approach 1: Math, trailingZeroesMath()

Credits to: https://leetcode.com/problems/factorial-trailing-zeroes/solutions/52470/4-lines-4ms-c-solution-with-explanations/?orderBy=most_votes

We know that trailing zeroes are contributed by a number multiplied by `10`, and since `10` can be splitted to `2*5` and there are more `2`s than `5`s in the factorial, we only need to care about the number of `5`s (because each even number will have at least one `2`).

So we now know that each `5` will contribute to a trailing zero. But some numbers are multiple of power of 5, such as `25=5*5` and `125=5*5*5`, so these numbers will contribute one more or two more, etc, trailing zeros.

```python3
def trailingZeroesMath(self, n: int) -> int:
	result = 0
	fiveMultiple = 5
	while n >= fiveMultiple:
		result += n//fiveMultiple
		fiveMultiple *= 5
	return result
```

Time complexity is O(logn), base is 5:

<img width="807" alt="image" src="https://user-images.githubusercontent.com/25105806/222945240-869a81ad-2ee0-4118-9f62-5c8cd39cfdf5.png">
