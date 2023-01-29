# Generate Parentheses problem
* Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

![image](https://user-images.githubusercontent.com/25105806/145904187-6c113690-d64d-4b05-acf6-3391aa5b990a.png)

Leetcode link: https://leetcode.com/problems/generate-parentheses/

<br/>

### Approach 1: Dynamic Programming, generateParenthesisDP1()
The idea is to build the result from the start and add 1 more pair step by step. For example if `n=3`, we start with `n=1` and build `n=2`, and based on `n=2` we build `n=3`.\
If we only see the opening parenthesis `(`, we can find a pattern that when adding 1 more pair of `()`, the new position of the `(` must be greater than the previous right-most `(` and smaller than the right-most `)` of current n. That is, the new pos of `(` when adding a new pair must be in the range of `range(prev[-1]+1, 2*(i+1)-1)`, where `prev[-1]` is the right-most `(` of `n-1` and `i` is n.\
For example, if current `n=2` and we are building `n=3` from it. When adding 1 more pair, for previous index `0, 1` we have new index of `2, 3, 4` because the new index has to be greater than 1 and smaller than 5 (2\*3-1)\
The image below can better demonstrate it:

<img src="https://user-images.githubusercontent.com/25105806/120617728-3fde0300-c40f-11eb-9fea-5f940d3f875e.png" height="50%" width="55%">

```python
def generateParenthesisDP1(self, n: int) -> List[str]:
    idx_result = [[0]]
    tmp_res = []
    for i in range(1, n):
        for prev in idx_result: # [0]
            # the new pos of the opening parenthesis can only be greater than the current right-most one
            # and smaller than the right-most closing parenthesis  
            for newPos in range(prev[-1]+1, 2*(i+1)-1):
                # form new idx result by appending new position of the opening parenthesis to the 
                # end of each previous result
                tmp_res.append(prev + [newPos])
        idx_result = tmp_res
        tmp_res = []
        # we can simply replace the above two nested loop with the statement below
        #idx_result = [prev+[newPos] for prev in idx_result for newPos in range(prev[-1]+1, 2*(i+1)-1)]

    # turn idx_result in to actual string
    str_result = []
    for res in idx_result:
        # default char is closing parenthesis, we will replace ')' at given index with '('
        template = [')'] * 2 * n
        for pos in res:
            template[pos] = '('
        str_result.append(''.join(template))
    return str_result
```

We can use the above logic to first gain the indices of all possible `(` and convert them into final string.\
The actual running time:\
![image](https://user-images.githubusercontent.com/25105806/120618587-1376b680-c410-11eb-8836-a5001a44458e.png)

<br/>

### Approach 2: Dynamic Programming, generateParenthesisDP2()
This approach also uses dynamic programming, but in a different way than approach 1. The basic idea is similar: we divide the `n=n` problem into sub-problems: `n=1`, `n=2`, etc. and build up the final answer out of the sub-problems.\
We start with `n=0`, which means the answer is just empty string `''`, this is will serve as the base case and we will build `n=1` from this. The template we use is `( x ) y`, in which `x` and `y` are answers of the sub-problems. When `n=1`, the sub-problem answer is simply `''`, so the result when `n=1` is simply `()`.\
A more complicated case is when building `n=3` from `n=2`, in which `x` will range from answers of `n=1, 2, 3` and `y` will range from answers of `n=2, 1, 0`. Simply get all combinations of `x` and `y`.\
The image below demonstrates the logic:
<img src="https://user-images.githubusercontent.com/25105806/120749805-0f9f6e80-c4ba-11eb-8ca5-5255cd1296e5.png" height="80%" width="80%">

```python
def generateParenthesisDP2(self, n: int) -> List[str]:
    dp = [[] for i in range(n + 1)]
    dp[0].append('')

    # increase n by 1 each time, solve sub-problems one by one
    for curr_n in range(n + 1):
        # for each of the result in previous n, which is the 'sub-problem'
        for prev in range(curr_n):
            # get all permutations of sub problem solutions and form new solution
            for x in dp[prev]:
                for y in dp[curr_n - prev - 1]:
                    dp[curr_n] += ['(' + x + ')' + y ]
            # the above nested loop can be replaced with this statement
            #dp[i] += ['(' + x + ')' + y for x in dp[j] for y in dp[i - j - 1]]
    # dp contains of solutions to all sub-problems, we only want the solution for n
    return dp[-1]
```

Actual running time:\
![image](https://user-images.githubusercontent.com/25105806/120749934-483f4800-c4ba-11eb-8234-5dea0037bfed.png)

<br/>

### Approach 3: Backtracking, generateParenthesisBacktrack()
This approach again, divide the problem into sub-problems and build up the final result out of the sub-problems. The only difference is that this approach utilizes recursion to get all combinations of the parentheses. The idea is to count the number of openning parenthesis(`openP`) and closing parenthesis(`closeP`), if `openP` is less than `n`, then it is ok and safe to add one more `(` to the string, if `closeP` is less than `openP` then it is also ok and safe to add one more `)` to the string. We will use recursion to get all of these logic done. \
The image below demonstrates the logic:
<img src="https://user-images.githubusercontent.com/25105806/120751281-a10fe000-c4bc-11eb-8142-1553bca5d08e.png" height="80%" width="80%">

```python
def generateParenthesisBacktrack(self, n: int) -> List[str]:
    result = []
    self.backtrack(result, '', 0, 0, n)
    return result

def backtrack(self, result, string, openP, closeP, n):
    if len(string)==2*n:
        result.append(string)
        return  

    # if openning parenthesis is less than n, then we can add more openning parenthesis
    if openP < n:
        self.backtrack(result, string+'(', openP+1, closeP, n)

    # if closing parenthesis is less than opening parenthesis, then we can one more closing 
    # parenthesis to match up the openning parenthesis
    if closeP < openP:
        self.backtrack(result, string+')', openP, closeP+1, n)
```

Actual running time:\
![image](https://user-images.githubusercontent.com/25105806/120750262-ecc18a00-c4ba-11eb-8437-84f64b455bf6.png)



