# Excel Sheet Column Title problem
<img width="812" alt="image" src="https://user-images.githubusercontent.com/25105806/220211524-ecfc44b5-10dc-4693-90fe-5eaa462f9f62.png">

Leetcode link: https://leetcode.com/problems/excel-sheet-column-title/description/
 
<br />
 
### Approach 1: Math, convertToTitle()

This is similar to a 26-nary number system. We can simply divide the number by 26, calculate the corresponding character of the remainder, and keep dividing the number until it's smaller than 26. The only special case is when the number is a multiple of 26, we need some special handling, that is:

```python3
if r==0:
	result += 'Z'
	columnNumber = (columnNumber // 26) - 1 
```


Because the number system is not 0 based, so instead of 10 after 9, it's 11, as in decimal system.


Full code:
```python3
def convertToTitle(self, columnNumber: int) -> str:
	result = ''
	while columnNumber > 26:
		r = columnNumber % 26
		if r==0:
			result += 'Z'
			columnNumber = (columnNumber // 26) - 1 
		else:
			result += chr(r + 64)
			columnNumber = columnNumber // 26
	result += chr(columnNumber + 64)
	return result[::-1]
```

Time complexity is O(n/26):
<img width="828" alt="image" src="https://user-images.githubusercontent.com/25105806/220212364-0da09caf-d647-46cf-be1c-145c14776148.png">


<br />

### Approach 2: Math, convertToTitle2()

Credits to: https://leetcode.com/problems/excel-sheet-column-title/solutions/441430/detailed-explanation-here-s-why-we-need-n-at-first-of-every-loop-java-python-c/?orderBy=most_votes


Since the number system is 1-based instead of 0-based, we can decrement the number by 1 everytime before we dividing 26. This is like making the number 0 based. So we don't need the special case anymore.

```python3
def convertToTitle(self, columnNumber: int) -> str:
	result = ''
	while columnNumber > 0:
		columnNumber -= 1
		r = columnNumber % 26
		result += chr(r + 65)
		columnNumber = columnNumber // 26
	return result[::-1]
```

Time complexity is the same O(n):
<img width="828" alt="image" src="https://user-images.githubusercontent.com/25105806/220212859-4eab7cca-d349-424e-a65c-4c9b8b4e8be6.png">

