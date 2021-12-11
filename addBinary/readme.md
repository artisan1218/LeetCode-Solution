# Add Binary problem
* Given two binary strings `a` and `b`, return their sum as a binary string.

### Approach 1: Math, addBinary()
Since `a` and `b` are given as strings and they might have different length, we first pad the shorter string with 0 to make it as long as the longer string. Then simply use python `zip()` function to add the digits vertically.

```python
def addBinary(self, a: str, b: str) -> str:
    result = ''
    maxLen = max(len(a), len(b))
    # padding
    a = a.rjust(maxLen, '0')
    b = b.rjust(maxLen, '0')

    carry = 0
    for a_digit, b_digit in zip(reversed(a), reversed(b)):
        digit = int(a_digit) + int(b_digit) + carry
        # 1 + 1
        if digit==2:
            digit = 0
            carry = 1
        # 1 + 1 + 1, 1 is carry on digit
        elif digit==3:
            digit = 1
            carry = 1
        # 1 + 0 or 0 + 0
        else:
            carry = 0
        result = str(digit) + result

    if carry == 1:
        result = '1' + result
    return result
```

Time complexity is O(n):\
![957d46d1ff4ad47efe8745dc7461a70](https://user-images.githubusercontent.com/25105806/130334479-9e85c23a-1d9e-475d-a27e-293a97936d61.png)
