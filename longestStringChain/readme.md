# Longest String Chain problem
![image](https://user-images.githubusercontent.com/25105806/136459344-9c7dabde-dde9-48f8-9bcb-e3dfddafa63d.png)

Leetcode link: https://leetcode.com/problems/longest-string-chain/

<br />

### Approach 1: Dynamic Programming, longestStrChainDP()
The idea is to iterate over the entire `words` list, initialize each word with value of `1` and store it in a dict, then check each possible predecessor of that word to see if the `pred` is in the dict, the update the dict value as we go over the list

```python
def longestStrChainDP(self, words: List[str]) -> int:
    dp = {}
    result = 1

    for word in sorted(words, key=len):
        dp[word] = 1
        # go through each possible predecessor word
        for i in range(len(word)):
            pred = word[:i] + word[i + 1:] 
            if pred in dp:
                dp[word] = dp[pred] + 1
                result = max(result, dp[word])
    return result
```

Actural running time:\
![image](https://user-images.githubusercontent.com/25105806/136459730-446e86e1-350c-42e7-9e48-a1e5dcbb8bd1.png)

<br />

### Approach 2: DFS, longestStrChainDFS()
This idea is to use a DFS to calculate the longest word chain for each word in the list `words` and keep the longest one. We go from top(last word in chain) to bottom(first word in chain)

```python
def longestStrChainDFS(self, words: List[str]) -> int:
    def dfs(word):
        if word in dp: 
            return dp[word]
        else:
            ans = 1
            # go through each predecessor
            for i in range(len(word)):
                pred = word[:i] + word[i + 1:]
                if pred in words_set:
                    ans = max(1 + dfs(pred), ans)
            dp[word] = ans
            return ans

    ans = 0
    words_set =set(words)
    dp = {}    
    # go through each word and compute word chain separately
    for word in words:
        ans = max(ans, dfs(word))
    return ans
```

Actural running time:\
![image](https://user-images.githubusercontent.com/25105806/136460057-28170728-c285-4ad1-a3c2-44b28dc1bd27.png)
