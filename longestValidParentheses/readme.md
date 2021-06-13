# Longest Valid Parentheses problem
* Given a string containing just the characters `'('` and `')'`, find the length of the longest valid (well-formed) parentheses substring.

### Approach 1: Two Stacks, longestValidParenthesesTwoStacks()
This approach takes idea from [validParentheses](https://github.com/artisan1218/LeetCode-Solution/tree/main/validParentheses) problem. Besides the stack used to store parentheses, we also use another stack `idxList` to store the indices of parentheses. If a pair of parentheses is matched, their indices will be popped out from the stack, so the remaining indices are the indices of remaining parentheses that can not be paired up. We then use these indices to compute the longest valid parentheses.\
Time complexity is O(n) with worst case in O(2n). We will scan the input string `s` to get the indices of left-over parentheses then scan the stack `idxList` again to get the longest length of valid substring.

![image](https://user-images.githubusercontent.com/25105806/121797662-8df4c280-cbd6-11eb-89e5-607990c17f08.png)


<br />

### Approach 2: Dynamic Programming, longestValidParenthesesDP()
This approach basically store the length of longest valid substring seen so far in a list and update the length list according to new parenthesis. We make use of a `dp` list where ith element of `dp` represents the length of the longest valid substring ending at ith index.\
If a `(` is met, simply put 0 in length list because '(' can not form a valid parentheses substring with parentheses **before** it. If a `)` is met, there are several cases to consider:
1. if the char before current index is a `(`, which means we can pair up with it, so we should update the length list by appending length of 2. However if the parentheses before this pair is also valid, for example `()()`, we should also add the length of previous valid substring.
2. if the char before current index is a `)`, then we should go the **beginning index of current valid substring** to check if there is more than one pair of parentheses that can be paired up. For example `()(())`, when reading the last parenthesis `)`, we should go to the index `i=2` because `(())` are two paris. Then go to the **previous index of the beginning index of current valid substring** to check if there are any valid substring connects to current one. For example we should then go to index `i=1` because `()` is also a valid substring immediately before `(())` and we should add the length of `()` as well.

![longestValidParentheses](https://user-images.githubusercontent.com/25105806/121798760-fd6db080-cbdc-11eb-81fd-d01b3f8c2fbe.gif)

**Note: Click [here](https://github.com/artisan1218/LeetCode-Solution/tree/main/longestValidParentheses) to download the animation to play for yourself.**

For the input string `s = "(()))())("`, the corresponding length list should be:
```
[0]
[0, 0]
[0, 0, 2]
[0, 0, 2, 4]
[0, 0, 2, 4, 0]
[0, 0, 2, 4, 0, 0]
[0, 0, 2, 4, 0, 0, 2]
[0, 0, 2, 4, 0, 0, 2, 0]
[0, 0, 2, 4, 0, 0, 2, 0, 0]
```
Therefore the longest length is 4.

Time complexity is O(n) because we only go through the input `s` once.\
Actual running time:\
![image](https://user-images.githubusercontent.com/25105806/121798130-62bfa280-cbd9-11eb-971b-fe46ef738fb1.png)

