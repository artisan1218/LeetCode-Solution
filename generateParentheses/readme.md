# Generate Parentheses problem
* Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

### Approach 1: Dynamic Programming, generateParenthesis()
The idea is to build the result from the start and add 1 more pair step by step. For example if `n=3`, we start with `n=1` and build `n=2`, and based on `n=2` we build `n=3`.\
If we only see the opening parenthesis `(`, we can find a pattern that when adding 1 more pair of `()`, the new position of the `(` must be greater than the previous right-most `(` and smaller than the right-most `)` of current n. That is, the new pos of `(` when adding a new pair must be in the range of `range(prev[-1]+1, 2*(i+1)-1)`, where `prev[-1]` is the right-most `(` of `n-1` and `i` is n.\
For example, if current `n=2` and we are building `n=3` from it. When adding 1 more pair, for previous index `0, 1` we have new index of `2, 3, 4` because the new index has to be greater than 1 and smaller than 5 (2\*3-1)\
The image below can better demonstrate it:

<img src="https://user-images.githubusercontent.com/25105806/120617728-3fde0300-c40f-11eb-9fea-5f940d3f875e.png" height="45%" width="45%">

We can use the above logic to first gain the indices of all possible `(` and convert them into final string. T
Actual running time:
![image](https://user-images.githubusercontent.com/25105806/120618587-1376b680-c410-11eb-8836-a5001a44458e.png)

