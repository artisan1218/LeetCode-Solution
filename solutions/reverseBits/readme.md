# Best Time to Buy and Sell Stock IV problem
![Screenshot 2024-02-04 at 3 51 03 PM](https://github.com/artisan1218/LeetCode-Solution/assets/25105806/137da2d5-4da7-4809-b009-402aa4cffda6)



Leetcode link: [https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/description/](https://leetcode.com/problems/reverse-bits/)

<br />

### Approach 1: Loop, reverseBitsLoop()
This is similar to how we manually reverse something: we take the last element from the list and put it back to the front. But we do this using bit manipulation, where we can get the last digit of a number from unit digit to leading digit(right to left) in a loop using `(n >> i) & 1`. And we build a new number using the last digit, pad with 0, then we build another number, but each time the newly built number will be one digit less than previous one. Then we put them together to form the reversed number.

For example if we have a number 100101000111, we first take the last digit `1`, form a new number of length 12 padding with 0, which is `100000000000`. Then we take another digit from the end, but this time it's one digit to the left, which is still `1`, then we form another number `10000000000`, note that this number is 1 digit less than the first one. Then we combine them by taking the logical `or`: `100000000000` or `10000000000` = `110000000000`. Then we repeat this process until all digits are appened.

```python3
def reverseBitsLoop(self, n: int) -> int:
	res = 0
	for i in range(32):
		# get the last digit, since & 1 will only work on the unit digit of the shifted number
		bit = (n >> i) & 1
		# bit << (31 - i) to build a number of length 31-i, pad with 0
		# then take the or with res to append it to the end of res
		res = res | (bit << (31 - i))

	return res
```



Time complexity is O(n):

![Screenshot 2024-02-04 at 4 06 10 PM](https://github.com/artisan1218/LeetCode-Solution/assets/25105806/e2cd56aa-b31f-4d0a-b3e7-b6df26da1b35)
