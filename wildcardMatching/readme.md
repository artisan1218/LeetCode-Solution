# Wildcard Matching problem
Given an input string `(s)` and a pattern `(p)`, implement wildcard pattern matching with support for `'?'` and `'*'` where:
1. `'?'` Matches any single character.
2. `'*'` Matches any sequence of characters (including the empty sequence).

The matching should cover the entire input string (not partial).

Leetcode link: https://leetcode.com/problems/wildcard-matching/

<br />


### Approach 1: Backtracking, isMatchBacktracking()
**Note: this solution is slow and lead to TLE**

The idea is similar to how we human solve this type of question:
1. If a char or `'?'` is matched in `p` and `s`, we can safely go to the next index of `p` and `s` since char or `'?'` can not be used for multiple times.
2. If a `'*'` is read, since it can be matched with multiple characters and we do not know how many characters can it match in order to get the correct result, we try all possible number of characters on it, and if later we find out that this number of char does not give a correct result, we 'backtrack' to this index and try next number of characters until we find a solution.

We can implement this idea using backtracking and recursion. If `'*'` is found, move the index of `s` to next char and enter a recursion to check if this is a valid path, otherwise we backtrack and try next one.

Consider the example where `s='acccb'` and p=`'a*c?b'`\
`*` can match none, `c`, `cc`, `ccc`, `cccc`, but only when `*` matches `c` will give a valid solution

![image](https://user-images.githubusercontent.com/25105806/123190120-d7090a00-d453-11eb-9367-6b41b01da599.png)

```python3
def isMatchBacktracking(self, s: str, p: str) -> bool:
    if len(p)!=0 and all([c=='*' for c in p]):
        return True
    else:
        return self.backtrack(s, p, 0, 0)

def backtrack(self, s: str, p: str, strStart: int, patternStart: int):
    if strStart == len(s) and patternStart==len(p):
        return True
    elif strStart == len(s) and all([c=='*' for c in p[patternStart:]]):
        return True
    else:
        for i in range(len(s[strStart:])):
            for j in range(len(p[patternStart:])):
                if p[j+patternStart] == '*':
                    # try all number of chars that can be matched with *
                    for numMatched in range(len(s)-strStart+1):
                        if self.backtrack(s, p, strStart+numMatched, patternStart+1):
                            return True
                    return False
                elif p[j+patternStart] == '?':
                    return self.backtrack(s, p, strStart+1, patternStart+1)
                else:
                    if p[j+patternStart] == s[i+strStart]:
                        return self.backtrack(s, p, strStart+1, patternStart+1)
                    else:
                        return False
    return False
```

Since this solution will try ALL possible pathes, it is very slow and lead to TLE. But the idea is simple and definitely works.

<br />

### Approach 2: Dynamic Programming, isMatchDP()
This approach is similar to [Regular Expression Matching](https://github.com/artisan1218/LeetCode-Solution/tree/main/regExpMatching), the solutions of both questions are all built upon previous result.\
Credits to: https://www.youtube.com/watch?v=fWeTjhgDt3A

We can use 2d array to represent the result table of each stage. the size of 2d array is one more than size of `p` and `s` because the first element will be `''`. Since `'' ` always matches `''`, `dp[0][0]` is always `True`

Then we can start the real DP part, there are 4 cases:
1. we read a `?` in pattern. Consider in this way: if the `?` is valid, then the result of this slot only depends on the previous substring of `s` and previous sub-pattern of `p`, which means we can 'remove' this pattern `?` and the current char by looking at `dp[i-1][j-1]`. If `dp[i-1][j-1]` is valid, then this is valid as well.
    ```
    p = "a?"
    s = "ab"
    ```
   we read a `?` and we only need to check if `p = "a"` and `s = "a"` is a matching because `?` can match any single char, if the pattern matches the substring before b, it will also matche `'ab'`
  
2. we read a `*`. The `*` can match empty string or one/more string. If it matches empty string, which is equivalent to 'remove' the current `*` by looking at `dp[i][j-1]`; if it matches more string, which is equivalent to 'remove' the current char by looking at `dp[i-1][j]`
    ```
    p = "a?c*"
    s = "abcd"
    ```
    we read a `*` and we need to check if `p = "a?c"` and s = `"abcd"` is a valid matching(`*` matches none) or if `p = "a?c*"` and s = `"abc"` is a valid matching(`*` matches `d`)
3. If the string char matches the pattern char, again we can 'remove' this pattern char and the string char by looking at `dp[i-1][j-1]`
    ```
    p = "abc"
    s = "abc"
    ```
    we read a `c` and `c` is equal to `c` in pattern. So we only need to check if `ab` in pattern matches `ab` in string. If they match then so does `abc`
4. If the string char does not match the pattern char, we can simply put `False` there because it not going to be valid at this index due to the bad matching.


```python3
def isMatchDP(self, s: str, p: str) -> bool:
    # initialize 2d dp array, the size of array is one more than size of p and s
    # because the first element will be ''
    dp = [[False for _ in range(len(p)+1)] for _ in range(len(s)+1)]
    # '' always matches ''
    dp[0][0] = True

    # change all slot to True if read a * until the first non * char is met
    # this addresses the pair where p='***' and s=''
    for i in range(len(p)):
        if p[i]=='*':
            dp[0][i+1] = True
        else:
            break

    # real DP part
    # traverse all substring of s
    for i in range(1, len(dp)):
        # traverse all sub-pattern of p
        for j in range(1, len(dp[i])):
            '''
            read a ?
            if the ? is valid, then the result of this slot only depends on the previous substring of s
            and previous substring of p, which means we can 'remove' this pattern p and the current 
            char s by looking at dp[i-1][j-1]. If dp[i-1][j-1] is valid, then this is valid.
            '''
            if p[j-1]=='?':
                dp[i][j] = dp[i-1][j-1]
            elif p[j-1]=='*':
                '''
                read a *
                the * can match empty string or one/more string
                If it matches empty string, which is equivalent to 'remove' the current * by looking at dp[i][j-1]
                if it matches more string, which is equivalent to 'remove' the current char s by looking at dp[i-1][j]
                '''
                dp[i][j] = dp[i-1][j] or dp[i][j-1]
            # read a char
            else:
                '''
                if this char matches the pattern char, again we can 'remove' this pattern p and the current 
                char s by looking at dp[i-1][j-1]
                '''
                if p[j-1] == s[i-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    # the current char does not match with pattern, simply put False there
                    dp[i][j] = False

    return dp[-1][-1]
```

Time complexit is O(p\*s) since we use a 2d array table of size `p+1` and `s+1`:
![image](https://user-images.githubusercontent.com/25105806/123191050-767acc80-d455-11eb-9e9b-ccc72a7920fd.png)
