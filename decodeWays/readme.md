# Decode Ways problem
![image](https://user-images.githubusercontent.com/25105806/134601605-477fefb5-577c-4d7f-a017-e9f7692cff1c.png)

### Approach 1: DFS, numDecodings(), dfs()
The idea is very straightforward, for each of the char, we decide if this single char is valid (not `0`) and if the next char combined with current one is valid (smaller than `26`). Then use DFS recursion to explore all possible combinations.


![image](https://user-images.githubusercontent.com/25105806/134601811-30026aeb-af25-4a3b-8440-0684c4a3287f.png)

```python3
def numDecodings(self, s: str) -> int:
    return self.dfs(s, 0, dict())

def dfs(self, s, i, cache):
    # we have reached the end of s, this is a valid solution
    if i==len(s):
        return 1
    else:
        result=0
        if s[i]!='0': # single digit
            # memorization
            if s[i+1:] not in cache:
                cache[s[i+1:]] = self.dfs(s, i+1, cache)
            result += cache[s[i+1:]]

        # two digits, either start with 1 or start with 2 and second digit is smaller or equal than 6
        if i+1<len(s) and (s[i]=='1' or (s[i]=='2' and ord(s[i+1]) <= ord('6'))):
            # memorization
            if s[i+2:] not in cache:
                cache[s[i+2:]] = self.dfs(s, i+2, cache)
            result += cache[s[i+2:]]

        return result
```


Actual running time:\
![image](https://user-images.githubusercontent.com/25105806/134601856-2d4c0016-716b-4a6c-a310-bda8c50cde3c.png)

<br />

### Approach 2: Dynamic Programming with O(N) Space, numDecodingsDP1()
This question is similar to Fibonacci series where current value is only depend on previous two. We can then use a dp array to represent all possible decode ways at index `i`. If the current value is not `0`, then there are at least `dp[i-1]` ways of decoding. If the previous value is `1` OR (previous value is `0` and current value is within the range 1 to 6), then we should add `dp[i-2]` to current `dp[i]` as well.

```python3
def numDecodingsDP1(self, s: str) -> int:
    dp = [0 for _ in range(len(s))]

    if s[0]!='0':
        dp[0] = 1

    for i in range(1, len(s)):
        if s[i]!='0':
            dp[i] += dp[i-1]

        if s[i-1]=='1' or (s[i-1]=='2' and ord(s[i])<=ord('6')):
            if i-2>=0:
                dp[i] += dp[i-2]
            else:
                dp[i] += 1

    return dp[-1]
```

Time complexity is O(N):\
![1632444802(1)](https://user-images.githubusercontent.com/25105806/134602242-eb5b7a23-afeb-4172-9160-2605dd0a16e4.png)

<br />

### Approach 3: Dynamic Programming with O(1) Space, numDecodingsDP2()
Since we can treat the problem as Fibonacci series, then we can simply usee two variables `left` and `right` to represent previous two values and one temp variable to calcualte current value. Exchange and update `left` and `right` and return `right` at the end.

```python3
def numDecodingsDP2(self, s: str) -> int:
    left = 1 
    right = 1 if s[0]!='0' else 0

    for i in range(1, len(s)):
        newRight = 0
        if s[i]!='0':
            newRight = right

        if s[i-1]=='1' or (s[i-1]=='2' and ord(s[i])<=ord('6')):
            newRight += left
        left, right = right, newRight

    return right
```

This way we ensure the O(1) space complexity:\
![image](https://user-images.githubusercontent.com/25105806/134602406-e98d1b9b-4d3e-4ae0-9ea6-5fb00094fab1.png)
