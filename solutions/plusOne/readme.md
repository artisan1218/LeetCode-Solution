# Plus One problem
* Given a **non-empty** array of decimal digits representing a non-negative integer, increment one to the integer.
* The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.
* You may assume the integer does not contain any leading zero, except the number 0 itself.

Leetcode link: https://leetcode.com/problems/plus-one/

<br />

### Approach 1: Math, plusOne()
This approach is same as how we manually plus one to a digit. Starting from the least digit, add 1 to it and take care of carry on digit if the sum exceeds 10.

```python3
def plusOne(self, digits: List[int]) -> List[int]:
    carryOn = True
    i = len(digits)-1
    while carryOn:
        if i<0:
            # 999 -> 1000
            digits.insert(0, 1)
            break
        else:
            digits[i] += 1
            if digits[i] == 10:
                # 459 -> 460
                digits[i] = 0
                i -= 1
            else:
                # 123 -> 124
                carryOn = False

    return digits
```

Time complexity is O(n):\
![7e59b64e1930fae438e26a48556f583](https://user-images.githubusercontent.com/25105806/130334530-8735046f-04de-4097-975d-5f9c19fb839a.png)



