# Number of 1 Bits problem
<img width="720" alt="image" src="https://github.com/artisan1218/LeetCode-Solution/assets/25105806/9f8348d8-579d-4d57-9f0d-efba62c30e47">



Leetcode link: https://leetcode.com/problems/number-of-1-bits/

<br />

### Approach 1: Loop over all digits, hammingWeightLoopAllDigits()

The idea is borrowed from [reverseBits](https://github.com/artisan1218/LeetCode-Solution/tree/main/solutions/reverseBits) where we can use `(n>>i) & 1` to get the last digit of a binary number in a loop, then simply sum all the 1's to get the final result

```python3
def hammingWeightLoopAllDigits(self, n: int) -> int:
	ans = 0
	for i in range(32):
		ans += (n >> i) & 1
	
	return ans
```


Time complexity is O(n) where n is the length of the input:

<img width="682" alt="image" src="https://github.com/artisan1218/LeetCode-Solution/assets/25105806/f1f29ce9-70d2-4143-9182-5820702cae0b">




<br>

### Approach 2: Loop over all 1's, hammingWeightLoopOnes()

Credits to: https://leetcode.com/problems/number-of-1-bits/discuss/55255/C%2B%2B-Solution%3A-n-and-(n-1)

Since we're only interested in the number of 1's, we can use to `n = n & (n-1)` remove 1's from the binary input one by one, and at the same time use a counter to count the number of 1's removed.

The idea is that `n-1` will flip the bits after the last 1, and we can use a logical and operator to remove the flipped 1's to keep only un-counted 1's in the front:

```
For example n = 00101100. This binary representation has three 1s.

n = 00101100, then n - 1 = 00101011, so n & (n - 1) = 00101100 & 00101011 = 00101000. Count = 1.

n = 00101000, then n - 1 = 00100111, so n & (n - 1) = 00101000 & 00100111 = 00100000. Count = 2.

n = 00100000, then n - 1 = 00011111, so n & (n - 1) = 00100000 & 00011111 = 00000000. Count = 3.
```

Code:
```python3
def hammingWeightLoopOnes(self, n: int) -> int:
	ans = 0
	while n:
		n = n & (n-1)
		ans+=1
	
	return ans
```

Time complexity is O(n) where n is the number of 1's in the input, which can be quicker:

<img width="692" alt="image" src="https://github.com/artisan1218/LeetCode-Solution/assets/25105806/aecd25fc-8754-4a21-b650-769f41aaca29">
