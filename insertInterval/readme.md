# Generate Parentheses problem
* Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

### Approach 1: Dynamic Programming, generateParenthesisDP1()
The idea is to build the result from the start and add 1 more pair step by step. For example if `n=3`, we start with `n=1` and build `n=2`, and based on `n=2` we build `n=3`.\
If we only see the opening parenthesis `(`, we can find a pattern that when adding 1 more pair of `()`, the new position of the `(` must be greater than the previous right-most `(` and smaller than the right-most `)` of current n. That is, the new pos of `(` when adding a new pair must be in the range of `range(prev[-1]+1, 2*(i+1)-1)`, where `prev[-1]` is the right-most `(` of `n-1` and `i` is n.\
For example, if current `n=2` and we are building `n=3` from it. When adding 1 more pair, for previous index `0, 1` we have new index of `2, 3, 4` because the new index has to be greater than 1 and smaller than 5 (2\*3-1)\
The image below can better demonstrate it:

<img src="https://user-images.githubusercontent.com/25105806/120617728-3fde0300-c40f-11eb-9fea-5f940d3f875e.png" height="50%" width="55%">

We can use the above logic to first gain the indices of all possible `(` and convert them into final string.\
The actual running time:

![image](https://user-images.githubusercontent.com/25105806/120618587-1376b680-c410-11eb-8836-a5001a44458e.png)

### Approach 2: Dynamic Programming, generateParenthesisDP2()
This approach also uses dynamic programming, but in a different way than approach 1. The basic idea is similar: we divide the `n=n` problem into sub-problems: `n=1`, `n=2`, etc. and build up the final answer out of the sub-problems.\
We start with `n=0`, which means the answer is just empty string `''`, this is will serve as the base case and we will build `n=1` from this. The template we use is `( x ) y`, in which `x` and `y` are answers of the sub-problems. When `n=1`, the sub-problem answer is simply `''`, so the result when `n=1` is simply `()`.\
A more complicated case is when building `n=3` from `n=2`, in which `x` will range from answers of `n=1, 2, 3` and `y` will range from answers of `n=2, 1, 0`. Simply get all combinations of `x` and `y`.\
The image below demonstrates the logic:
<img src="https://user-images.githubusercontent.com/25105806/120749805-0f9f6e80-c4ba-11eb-8ca5-5255cd1296e5.png" height="80%" width="80%">

Actual running time:

![image](https://user-images.githubusercontent.com/25105806/120749934-483f4800-c4ba-11eb-8234-5dea0037bfed.png)

### Approach 3: Backtracking, generateParenthesisBacktrack()
This approach again, divide the problem into sub-problems and build up the final result out of the sub-problems. The only difference is that this approach utilizes recursion to get all combinations of the parentheses. The idea is to count the number of openning parenthesis(`openP`) and closing parenthesis(`closeP`), if `openP` is less than `n`, then it is ok and safe to add one more `(` to the string, if `closeP` is less than `openP` then it is also ok and safe to add one more `)` to the string. We will use recursion to get all of these logic done. \
The image below demonstrates the logic:
<img src="https://user-images.githubusercontent.com/25105806/120751281-a10fe000-c4bc-11eb-8142-1553bca5d08e.png" height="80%" width="80%">

Actual running time:

![image](https://user-images.githubusercontent.com/25105806/120750262-ecc18a00-c4ba-11eb-8437-84f64b455bf6.png)



