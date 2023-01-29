# Valid Parenthesis String problem
![image](https://user-images.githubusercontent.com/25105806/151871354-8850c6cc-bf75-4ae7-8f98-487aaa6f70f2.png)

Leetcode link: https://leetcode.com/problems/valid-parenthesis-string/

<br/>

### Approach 1: DFS with memorization, checkValidStringDFS()
If there is no wildcard operator, the whole process of validating parentheses string will be simply comparing the number of open and close parenthesis in order. The presence of wildcard operator introduces three possibilities every time we meet a `*`. So we can handle this by using DFS to traverse all possible branchs of the possibilities. `left` marks the number of opening parenthesis that has not been paired up with a closing parenthesis. When we meet a `*`, three cases can happen:
1. We treat the `*` as `(`, so `left` should be increased by one
2. We treat the `*` as `)`, so `left` should be decreased by one
3. We treat the `*` as empty string, so `left` remains unchanged

But pure DFS is not efficient enough because it will check duplicate invalid substrings of `s`. So we can add memorization to speed up. 

The memorization is a 2-d array, where each row represents the `i`th index of the `s` and each column represents the number of open parenthesis we have at that place. 

```python
def checkValidStringDFS(self, s: str) -> bool:
    cache = [[None for _ in range(len(s))] for _ in range(len(s))]
    def dfs(s, i, left):
        if left<0:
            return False
        else:
            if i==len(s):
                return left==0
            else:
                if cache[i][left] != None:
                    return cache[i][left]
                else:
                    if s[i]=='(':
                        cache[i][left] = dfs(s, i+1, left+1)
                        return cache[i][left]
                    elif s[i]==')':
                        cache[i][left] = dfs(s, i+1, left-1)
                        return cache[i][left]
                    else: # wildcard *
                        cache[i][left] = dfs(s, i+1, left+1) or dfs(s, i+1, left-1) or dfs(s, i+1, left)
                        return cache[i][left]
    return dfs(s, 0, 0)
```

Time complexity is O(n^2):\
![image](https://user-images.githubusercontent.com/25105806/151872979-207588f1-bec5-4fe4-a179-2c6be4981895.png)

<br />

### Approach 2: Two Pass Scan, checkValidStringTwoPass()
Credits to: https://leetcode.com/problems/valid-parenthesis-string/discuss/107581/O(n)-time-O(1)-space-no-Recursion-just-scan-from-left-and-then-scan-from-right

The idea is to scan the string `s` twice, once from left and once from right. The result must be valid in both ways to ensure the `s` is valid. When scanning from left, we count `(` as open parenthesis and compare the number of open parthesis, close parenthesis and star in each iteration. We scanning from right, we should reverse the string `s` and treat `)` as open parenthesis.

```python
def checkValidStringTwoPass(self, s: str) -> bool:
    def scan(dir, s):
        open, close, star = 0, 0, 0
        # we will need to reverse the string when scanning from right
        if dir=='right':
            s = s[::-1]

        for c in s:
            if c=='(':
                open+=1
            elif c==')':
                close+=1
            else:
                star+=1

            # when scanning from right, we should treat ) as open parenthesis, but we don't
            # need to rewrite the code block, simply swap the open and close when comparing them
            if (dir=='left' and close > (open + star)) or (dir=='right' and open > (close + star)):
                return False 
        return True

    return scan('left', s) and scan('right', s)
```

Time complexity is O(n):\
![image](https://user-images.githubusercontent.com/25105806/151873538-f0fd2932-facb-489a-9eb0-2e146babc3af.png)

<br />

### Approach 3: One Pass Scan, Greedy, checkValidStringOnePass()
Credits to: https://www.youtube.com/watch?v=QhPdNS143Qg

The idea is similar to validate parenthesis string without wildcard operators. The only difference is that, when we have a `*`, the possible branches goes up, which means we have more possibilities on the number of left parenthesis `left`. So we can have two variables `leftMin` and `leftMax` to represent the upper and lower boundary of the possibilities. The string `s` will be valid as long as 0 falls in beween `leftMin` and `leftMax`. 

```python3
def checkValidStringOnePass(self, s: str) -> bool:
    leftMin, leftMax = 0, 0
    for c in s:
        if c=='(': 
            # if (, then the left open parenthesis is counted one more, which means we need one more closing parenthesis to validate the string
            leftMin+=1 
            leftMax+=1
        elif c==')':
            # if ), then the left open parenthesis is counted one less, which means we need one less closing parenthesis to validate the string
            leftMin-=1
            leftMax-=1
        else:
            # if *, then we can have one more open OR one less open parenthesis OR nothing. 
            # leftMin and leftMax marks the boundary of number of open parenthesis we can have based on different choices of wildcard character
            leftMin-=1
            leftMax+=1
        leftMin = max(0, leftMin) # leftMin cannot be negative, reset it 0 once it drops below 0
        if leftMax < 0:
            # if leftMax is below 0, which means we have more closing parenthesis than open parenthesis. 
            # We will never recover from this state, so it's immediately invalid. consider ))(())
            return False 
    return leftMin==0
```

Time complexity is O(n):\
![image](https://user-images.githubusercontent.com/25105806/151874121-95ff8829-749c-4bdf-a778-b8bab76e0952.png)

