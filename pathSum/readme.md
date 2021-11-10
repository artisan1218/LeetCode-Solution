# Path Sum problem
![image](https://user-images.githubusercontent.com/25105806/141026405-d81de4f6-8f54-4d1d-8dc7-999dbded132c.png)

Leetcode Link: https://leetcode.com/problems/path-sum/

<br />

### Approach 1: DFS, hasPathSum()
Use DFS to explore the tree and store every path sum to a set `result` then simply return true if the `targetSum` exists in the set `result`

```python
def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
   def dfs(root, result, curSum):
       if root!=None:
         if root.left==None and root.right==None:
             result.add(curSum + root.val)

         if root.left!=None:
             dfs(root.left, result, curSum + root.val)

         if root.right!=None:
             dfs(root.right, result, curSum + root.val)

   result = set()
   dfs(root, result, 0)
   return targetSum in result          
```

Time complexity is O(n):\
![image](https://user-images.githubusercontent.com/25105806/141026666-eaaba32b-a0b6-4ffd-847f-c04abfc1b090.png)

<br />

### Approach 2: DFS, hasPathSum2()
Similar to approach 1, but this time we update `targetSum` every time we found a new node in a path. We will still explore every path using DFS but we only store whether the path sum is equal to `targetSum` instead of the exact sum value. 

```python
def hasPathSum2(self, root: Optional[TreeNode], targetSum: int) -> bool:
    def dfs(root, result, target):
        if root!=None:
            if root.left==None and root.right==None and target==root.val:
                result.append(True)

            if root.left!=None:
                dfs(root.left, result, target - root.val)

            if root.right!=None:
                dfs(root.right, result, target - root.val)

    result = list()
    dfs(root, result, targetSum)
    return any(result)
```

Time complexity is O(n):\
![image](https://user-images.githubusercontent.com/25105806/141026925-2e07f756-a7a1-423f-afe0-b31c48bc7fe0.png)


<br />

### Approach 3: DFS, hasPathSum3()
It's possible to stop the algorithm early if we already found the valid path. So we use the early stopping condition in the code to test if we've already found the valid path.

```python
def hasPathSum3(self, root: Optional[TreeNode], targetSum: int) -> bool:
    def dfs(root, curSum):
        result = False
        if root!=None:
            if root.left==None and root.right==None and curSum + root.val == targetSum:
                return True

            if root.left!=None:
                result = result or dfs(root.left, curSum + root.val)

            if root.right!=None:
                result = result or dfs(root.right, curSum + root.val)

            return result

    return dfs(root, 0)
```

Time complexity is O(n) in worst case:\
![image](https://user-images.githubusercontent.com/25105806/141027131-0a1dddec-b7e0-4c53-83d9-896fe278e761.png)

<br />

### Approach 4: DFS, hasPathSum4()
Similar to approach 3 but different implementation

```python
def hasPathSum4(self, root: Optional[TreeNode], targetSum: int) -> bool:
    if root==None:
        return False
    elif root.left==None and root.right==None and targetSum==root.val:
        return True
    else:
        left = self.hasPathSum4(root.left, targetSum-root.val)
        right = self.hasPathSum4(root.right, targetSum-root.val)
        return left or right
```

Time complexity is O(n):\
![image](https://user-images.githubusercontent.com/25105806/141027302-4c276c18-5d7d-4ef1-8e55-0f5ed7e53313.png)

