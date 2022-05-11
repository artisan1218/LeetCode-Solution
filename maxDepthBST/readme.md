# Maximum Depth of Binary Tree problem
![image](https://user-images.githubusercontent.com/25105806/135959810-5e9325a4-46cc-4ec9-9daf-07abb7132221.png)

Leetcode link: https://leetcode.com/problems/maximum-depth-of-binary-tree/

<br />

### Approach 1: DFS, maxDepth()
This approach simply uses DFS to get the depth of left and right subtree, then take the maximum value of these two subtree plus one. We do this recursively to get the max depth.

```python3
def maxDepth(self, root: Optional[TreeNode]) -> int:
    if root!=None:
        left = 0
        right = 0
        if root.left!=None:
            left = self.maxDepth(root.left)
        if root.right!=None:
            right = self.maxDepth(root.right)

        return 1 + max(left, right)
    else:
        return 0
```

Time complexity is O(n):\
![image](https://user-images.githubusercontent.com/25105806/135959929-b49577f9-fdd3-444b-a740-41bcb32d516e.png)

<br />

### Approach 2: DFS, maxDepthOneline()
Same method, but in oneline

```python3
def maxDepthOneline(self, root: Optional[TreeNode]) -> int:
    return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right)) if root!=None else 0
    
```

Time complexity is O(n):\
![image](https://user-images.githubusercontent.com/25105806/135959970-292c2b56-a1b8-4c51-887a-c33c638e195e.png)
