# Fraction to Recurring Decimal problem
![image](https://user-images.githubusercontent.com/25105806/215300417-35ee0b93-2dd3-4e79-912d-c9e962c50c42.png)

Leetcode link: https://leetcode.com/problems/fraction-to-recurring-decimal/

<br />

### Approach 1: Mathmatical Division, fractionToDecimal()

Credits to: https://leetcode.com/problems/fraction-to-recurring-decimal/solutions/180004/python-4-lines-32ms-beats-100-with-explanation/

The challenging part is how to find the repeating/recurring pattern in decimal part. If we do the division by hand and list all intermediate result, we can see that remainder also repeats itself if there is repeating pattern:

```
       0.1234...
    +---------
4950|611
       0
     ---------
     6110      <- remainder is 611
     4950
     ---------
     11600     <- remainder is 1160
      9900
     ---------
      17000    <- remainder is 1700
      14850
     ---------
       21500   <- remainder is 2150
       19800
     ---------
        1700   <- remainder is 1700, here we got 1700 again, so this is where repeating pattern ends
        ...
```

So we can divide the number digit by digit and store the index of the intermediate remainder, the index is simply the position of the decimal digit in the result. The first time we see a duplicate remainder, it means we've found the end of a repeating pattern, then we can exit the loop.


```python3
def fractionToDecimal(self, numerator: int, denominator: int) -> str:
	if numerator % denominator == 0:
		return str(numerator//denominator)

	res = '' if ((numerator>0) == (denominator>0)) else '-' # sign
	num, den = map(abs, (numerator, denominator))
	res += str(num//den) # int part
	res += '.'

	remainder = num % den
	index_map = dict()
	"""
	for example: 611 ÷ 4950

	 611    ÷ 4950 = 0...611
	 611*10 ÷ 4950 = 1...1160
	1160*10 ÷ 4950 = 2...1700
	1700*10 ÷ 4950 = 3...2150
	2150*10 ÷ 4950 = 4...1700 (we get 1700 again, so first the occurrence is the start of 
	repeating pattern and this occurrence is the end of repeating pattern)
	"""
	# the first time we see repeated remainder is where repeating pattern ends
	# so the loop while generate a decimal number repeating only once
	while remainder not in index_map:
		index_map[remainder] = len(res)
		res += str(remainder*10 // den) # next digit
		remainder = remainder*10 % den
		if remainder==0:
			return res

	# index_map[remainder] is where repeating starts    
	return res[:index_map[remainder]] + '(' + res[index_map[remainder]:] + ')'
```

Actual running time:
![image](https://user-images.githubusercontent.com/25105806/215300755-116cfe2c-7aea-45eb-85b6-d329a12b7970.png)
