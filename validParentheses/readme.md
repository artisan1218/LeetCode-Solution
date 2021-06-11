# Valid Parentheses problem
* Given a string s containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.
* An input string is valid if:
   1. Open brackets must be closed by the same type of brackets.
   2. Open brackets must be closed in the correct order.

### Approach 1: Stack, isValid(), Python
If an input string is valid, then we can always match a left parenthesis with a right one, then these two cancel out and we do this multiple times untill all left and right parentheses are canceled out. The idea is to go over the input string, then use a FIFO stack to store the seen char and try to match it with the last element of the stack, if they match, we can remove these two and go to the next char. If the length of the stack is 0 at the end, that means we've matched all pairs and the string is valid, otherwise it is not valid.\

![validParenthesesAnimation](https://user-images.githubusercontent.com/25105806/121675759-b068cd80-ca68-11eb-9803-d5eac138f431.gif)


Time complexity is O(n) since we only go through the input string once. 
![image](https://user-images.githubusercontent.com/25105806/120406786-8d1f7f00-c300-11eb-9da1-268e17552579.png)

**Note: Click [here](https://github.com/artisan1218/LeetCode-Solution/blob/main/validParentheses/validParenthesesAnimation.ppsx) to download the animation to play for yourself.**

### Approach 2: Turing Machine, valid(), Java
Turing Machine is a very powerful machine that can be used to compute anything that can be computed according to Church-Turing thesis. Turns out we can construct a TM to check the input string. If the input string is valid, then this TM will accept it otherwise it will reject it. The construction of the TM is EXTREMELY complicated and very inefficient and should be avoided in practice. I implement this approach just for fun and verify it's viable.\
The constructed TM is shown below:

<img src="https://user-images.githubusercontent.com/25105806/120407064-38303880-c301-11eb-948d-425737be43cf.png" height="60%" width="60%">

We will replace `()` with `XX`, `[]` with `YY` and `{}` with `ZZ`. For example, the denotation of `'((R'` means read a `'('`, change it to `'('` and move head to right. \
Actual running time is:

![image](https://user-images.githubusercontent.com/25105806/120407287-b096f980-c301-11eb-824b-98642c0ea1b3.png)
