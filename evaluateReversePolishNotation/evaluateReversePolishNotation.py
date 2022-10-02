# %%
from typing import List

class Solution:
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

if __name__ == "__main__":
    solver = Solution()
    tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    print(solver.evalRPN(tokens))

# %%



