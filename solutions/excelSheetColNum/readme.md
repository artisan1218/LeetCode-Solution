# Excel Sheet Column Number problem
<img width="624" alt="image" src="https://user-images.githubusercontent.com/25105806/222935892-f6940d43-324e-44da-9d31-3f1f9eccb827.png">


Leetcode link: https://leetcode.com/problems/excel-sheet-column-number/
 
<br />
 
### Approach 1: Math, titleToNumber()

The idea is same as converting binary number to decimal number. Each char corresponds to a number from 1 to 26 and depnding on their position in the given string, we need to multiply a power of 26 with that number, then sum all the numbers together.

For example

`ZCY -> 26(Z) * 26^2 + 3(C) * 26^1 + 25(Y) * 26^0 = 17679`

Python code:
```python3
def titleToNumber(self, columnTitle: str) -> int:
	n = len(columnTitle)
	result = 0
	for c in columnTitle:
		result += (ord(c) - 64) * (26 ** (n-1))
		n -= 1
	return result
```

<br />

C++ code:
```c++
int titleToNumber(std::string columnTitle) {
	int n = columnTitle.length();
	int result = 0;
	for (char c : columnTitle) {
		result += (int(c) - 64) * pow(26, n - 1);
		n--;
	}
	return result;
}
```


Time complexity is O(n):

<img width="808" alt="image" src="https://user-images.githubusercontent.com/25105806/222936027-71484547-23e6-4ea5-a337-518aef09179f.png">
