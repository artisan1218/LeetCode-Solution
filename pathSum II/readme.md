# Path Sum II problem
![image](https://user-images.githubusercontent.com/25105806/141027556-c36b95c9-a4fb-4c0e-a249-259d9b886e16.png)

Leetcode link: https://leetcode.com/problems/path-sum-ii/

<br />

### Approach 1: DFS, pathSum()
The idea is to use DFS to explore every path and keep track of current path node, whenever we reach a leaf node and the pathSum is equal to `targetSum`, we will append the current path to the `result`.

```python
def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
    def dfs(root, targetSum, curPath, result):
        if root!=None:
            if root.left==None and root.right==None and sum(curPath)+root.val==targetSum:
                result.append(curPath+[root.val])

            if root.left!=None:
                dfs(root.left, targetSum, curPath+[root.val], result)

            if root.right!=None:
                dfs(root.right, targetSum, curPath+[root.val], result)

    result = []
    dfs(root, targetSum, [], result)
    return result
```

Time complexity is O(n):\
![image](https://user-images.githubusercontent.com/25105806/141027786-79b6b5b9-0e17-4e87-9660-d27b9ce9ee27.png)
