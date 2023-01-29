# Evaluate Reverse Polish Notation problem
<img width="817" alt="Screen Shot 2022-10-01 at 6 51 34 PM" src="https://user-images.githubusercontent.com/25105806/193434455-4638816b-3a56-4695-8850-dab706e869d2.png">

Reverse Polish Notation: http://en.wikipedia.org/wiki/Reverse_Polish_notation

Leetcode link: https://leetcode.com/problems/evaluate-reverse-polish-notation/

<br />

### Approach 1: Stack, evalRPN()
The solution is to scan from left to right and find each operators(`+`, `-`, `*`, `/`). Everytime we meet an operator, we take its previous two operands and do the calculation, until we reach the end.

Because we're scanning from left to right, we can guarantee that there are no operators present on the left side or current element, so we can always do valid calculations

```python3
def evalRPN(self, tokens: List[str]) -> int:
    result = 0
    stack = []
    operators = {"+", "-", "*", "/"}
    for token in tokens:
        if token not in operators:
            stack.append(token)
        else:
            num2 = stack.pop()
            num1 = stack.pop()
            # int(eval()) is to round the division result towards zero
            result = int(eval(num1 + token + num2))
            stack.append(str(result))

    return int(stack[0])
```

Time complexity is O(n):

<img width="789" alt="image" src="https://user-images.githubusercontent.com/25105806/193434659-667db61d-c245-41af-a9d0-d9918246b3c3.png">

