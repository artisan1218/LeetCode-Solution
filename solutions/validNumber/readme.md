# Valid Number problem
* A valid number can be split up into these components (in order):
  1. A decimal number or an integer.
  2. (Optional) An 'e' or 'E', followed by an integer.

* A decimal number can be split up into these components (in order):
  1. (Optional) A sign character (either '+' or '-').
  2. One of the following formats:
     a. One or more digits, followed by a dot '.'.
     b. One or more digits, followed by a dot '.', followed by one or more digits.
     c. A dot '.', followed by one or more digits.

* An integer can be split up into these components (in order):
  1. (Optional) A sign character (either '+' or '-').
  2. One or more digits.
* For example, all the following are valid numbers: `["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"]`, while the following are not valid numbers: `["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"]`.

Given a string `s`, return true if `s` is a valid number.

Leetcode link: https://leetcode.com/problems/valid-number/

<br />

### Approach 1: DFA, isNumber()
This solution is based on Deterministic Finite Automata, we can represent the logic using state machine below and implement the state machine complete
![image](https://user-images.githubusercontent.com/25105806/130333840-1174d28c-7847-4b54-93f9-acf1c0b71db6.png)

Note that start state is state 0 in code. State with double circle is the accept state.

```python3
def isNumber(self, s: str) -> bool:
    state = 0
    acceptState = {3, 6, 7, 8, 10}
    for char in s:
        if state==0:
            if char=='+' or char=='-':
                state = 1
            elif char.isnumeric():
                state = 7
            elif char=='.':
                state = 9
            else:
                return False
        elif state==1:
            if char=='.':
                state = 2
            elif char.isnumeric():
                state = 7
            else:
                return False
        elif state==2:
            if char.isnumeric():
                state = 3
            else:
                return False
        elif state==3:
            if char=='e' or char=='E':
                state = 4
            elif char.isnumeric():
                state = 3
            else:
                return False
        elif state==4:
            if char=='+' or char=='-':
                state = 5
            elif char.isnumeric():
                state = 10
            else:
                return False
        elif state==5:
            if char.isnumeric():
                state = 6
            else:
                return False
        elif state==6:
            if char.isnumeric():
                state = 6
            else:
                return False
        elif state==7:
            if char.isnumeric():
                state = 7
            elif char=='.':
                state = 8
            elif char=='e' or char=='E':
                state = 4
            else:
                return False
        elif state==8:
            if char.isnumeric():
                state = 3
            elif char=='e' or char=='E':
                state = 4
            else:
                return False
        elif state==9:
            if char.isnumeric():
                state = 8
            else:
                return False
        elif state==10:
            if char.isnumeric():
                state = 10
            else:
                return False

    return state in acceptState
```

Time complexity is O(n) because we will only go over the string `s` once:
![0a3fabe91808b5b345433a9a93b0da1](https://user-images.githubusercontent.com/25105806/130333855-93c1a8d8-ce26-4916-a1a7-903e4a22204b.png)


