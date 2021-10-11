# The Most Similar Path in a Graph problem
![image](https://user-images.githubusercontent.com/25105806/136862053-9b60b524-bc1e-4a7b-b8b6-d08e9ef0b3ba.png)
![image](https://user-images.githubusercontent.com/25105806/136862066-8d013d09-a0a6-42ac-9209-50fd1831c4b8.png)

Leetcode link: https://leetcode.com/problems/the-most-similar-path-in-a-graph/

<br />

### Approach 1: Dynamic Programming, mostSimilar()
We will initialize a 2d `dp` array to store the edit distance and path that ending at node `i` and `targetPath` ending at `j`.

For the input 
```
n = 5
roads = [[0,2],[0,3],[1,2],[1,3],[1,4],[2,4]]
names = ["ATL","PEK","LAX","DXB","HND"]
targetPath = ["ATL","DXB","HND","LAX"]
```
The built dp array can look like this:
```
[[(0, [0]), (2, [2, 0]), (1, [0, 3, 0]), (4, [1, 4, 2, 0])],
 [(1, [1]), (2, [2, 1]), (1, [0, 3, 1]), (2, [0, 2, 4, 1])],
 [(1, [2]), (1, [0, 2]), (3, [1, 4, 2]), (1, [0, 2, 4, 2])],
 [(1, [3]), (0, [0, 3]), (3, [2, 0, 3]), (2, [0, 3, 0, 3])],
 [(1, [4]), (2, [1, 4]), (1, [0, 2, 4]), (2, [0, 3, 1, 4])]]
```

We will update the `dp` array column by column from left to right. We first calculate the edit distance for node `names[r]` and `targetPath[c]`. Then we will look at the `adj` graph to retrieve the connected nodes and their corresponding minimal edit distance and path. Then we update `dp[r][c]` based on the previous edit distance and path

```python
def mostSimilar(self, n: int, roads: List[List[int]], names: List[str], targetPath: List[str]) -> List[int]:
    cols = len(targetPath)
    # construct graph
    adj = [[] for _ in range(n)]
    for u, v in roads:
        adj[u].append(v)
        adj[v].append(u)
        
    #first element in tuple stands for edit distance, second element is the path
    #dp[i][j] means the minimum edit distance w/ path ending at node i and targetPath ending at j

    dp = [[(float('inf'), []) for _ in range(cols)] for _ in range(n)]

    # update dp column by column from left to right
    for c in range(cols):
        for r in range(n):
            editDist = int(names[r] != targetPath[c])
            if c == 0: 
                # for the first column, the edit distance will simply be 0 if first name
                # matches with the first name in targetPath, otherwise 1
                dp[r][c] = (editDist, [r])
            else:
                # get all names connected with current name, then pick the smallest one
                prevEditDistance, prePath = min(dp[k][c-1] for k in adj[r])
                dp[r][c] = (prevEditDistance + editDist, prePath+[r])

    return min(dp[r][-1] for r in range(n))[1]
```
    
Time complexity is O(m\*n):
![image](https://user-images.githubusercontent.com/25105806/136862506-ef75e826-fe64-44dd-8902-0f2ec462a5a8.png)

