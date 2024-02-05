# Reverse Bits problem
![Screenshot 2024-02-04 at 3 51 03 PM](https://github.com/artisan1218/LeetCode-Solution/assets/25105806/137da2d5-4da7-4809-b009-402aa4cffda6)



Leetcode link: [https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/description/](https://leetcode.com/problems/reverse-bits/)

<br />

### Approach 1: Loop, reverseBitsLoop()
This is similar to how we manually reverse something: we take the last element from the list and put it back to the front. But we do this using bit manipulation, where we can get the last digit of a number from unit digit to leading digit(right to left) in a loop using `(n >> i) & 1`. And we build a new number using the last digit, pad with 0, then we build another number, but each time the newly built number will be one digit less than previous one. Then we put them together to form the reversed number.

For example if we have a number `100101000111`, we first take the last digit `1`, form a new number of length 12 padding with 0, which is `100000000000`. Then we take another digit from the end, but this time it's one digit to the left, which is still `1`, then we form another number `10000000000`, note that this number is 1 digit less than the first one. Then we combine them by taking the logical `or`: `100000000000` or `10000000000` = `110000000000`. Then we repeat this process until all digits are appened.

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


<br>

### Approach 1: Divide And Conquer, reverseBitsDivideAndConquer()
Credits to: https://leetcode.com/problems/reverse-bits/discuss/54741/O(1)-bit-operation-C%2B%2B-solution-(8ms)

This approach utilizes the divide and conquer logic: to reverse a number is equivalent to split the entire number into two parts of same length recursively until there is only one digit, then reverse the adjacent two digits, and combine them together.

For example 

```

original input number: 10010111

First we split it into two parts: 1001 0111
Then we split the two parts again: 10 01 01 11
Then split again: 1 0 0 1 0 1 1 1
Then reverse it and combine: 01 10 10 11 -> 1001 1110 -> 11101001

```

We can do this using bit manipulation with masks, note that each mask group has two maskes that are reversed to each other. This is to take the different part of the original number:

```
Note that >> 16 and << 16 is equivalent to taking the first 16 digits and last 16 digits

0xff00ff00 = 0b11111111000000001111111100000000
0x00ff00ff = 0b00000000111111110000000011111111

0xf0f0f0f0 = 0b11110000111100001111000011110000
0x0f0f0f0f = 0b00001111000011110000111100001111

0xcccccccc = 0b11001100110011001100110011001100
0x33333333 = 0b00110011001100110011001100110011

0xaaaaaaaa = 0b10101010101010101010101010101010
0x55555555 = 0b01010101010101010101010101010101

Step 0.
abcd efgh ijkl mnop qrst uvwx yzAB CDEF <-- n

Step 1.
                    abcd efgh ijkl mnop <-- n >> 16, same as (n & 0xffff0000) >> 16
qrst uvwx yzAB CDEF                     <-- n << 16, same as (n & 0x0000ffff) << 16
qrst uvwx yzAB CDEF abcd efgh ijkl mnop <-- after OR

Step 2.
          qrst uvwx           abcd efgh <-- (n & 0xff00ff00) >> 8
yzAB CDEF           ijkl mnop           <-- (n & 0x00ff00ff) << 8
yzAB CDEF qrst uvwx ijkl mnop abcd efgh <-- after OR

Step 3.
     yzAB      qrst      ijkl      abcd <-- (n & 0xf0f0f0f0) >> 4
CDEF      uvwx      mnop      efgh      <-- (n & 0x0f0f0f0f) << 4
CDEF yzAB uvwx qrst mnop ijkl efgh abcd <-- after OR

Step 4.
  CD   yz   uv   qr   mn   ij   ef   ab <-- (n & 0xcccccccc) >> 2
EF   AB   wx   st   op   kl   gh   cd   <-- (n & 0x33333333) << 2
EFCD AByz wxuv stqr opmn klij ghef cdab <-- after OR

Step 5.
 E C  A y  w u  s q  o m  k i  g e  c a <-- (n & 0xaaaaaaaa) >> 1
F D  B z  x v  t r  p n  l j  h f  d b  <-- (n & 0x55555555) << 1
FEDC BAzy xwvu tsrq ponm lkji hgfe dcba <-- after OR
```

```python3
def reverseBitsDivideAndConquer(self, n: int) -> int:
	
	n = (n >> 16) | (n << 16);
	n = ((n & 0b11111111000000001111111100000000) >> 8) | ((n & 0b00000000111111110000000011111111) << 8);
	n = ((n & 0b11110000111100001111000011110000) >> 4) | ((n & 0b00001111000011110000111100001111) << 4);
	n = ((n & 0b11001100110011001100110011001100) >> 2) | ((n & 0b00110011001100110011001100110011) << 2);
	n = ((n & 0b10101010101010101010101010101010) >> 1) | ((n & 0b01010101010101010101010101010101) << 1);
	return n
```

Time complexity is O(1):

![image](https://github.com/artisan1218/LeetCode-Solution/assets/25105806/526b63af-cc09-4888-96bb-3043048bc525)


![Screenshot 2024-02-04 at 4 06 10 PM](https://github.com/artisan1218/LeetCode-Solution/assets/25105806/e2cd56aa-b31f-4d0a-b3e7-b6df26da1b35)

