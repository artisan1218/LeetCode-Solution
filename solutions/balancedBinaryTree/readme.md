# Balanced Binary Tree problem
![image](https://user-images.githubusercontent.com/25105806/140280620-86c928c8-3b96-4dda-bcf7-f4d398ad9765.png)

Leetcode Link: https://leetcode.com/problems/balanced-binary-tree/

<br />

### Approach 1: DFS, getDepth(), isBalanced()
The idea is to use DFS at each node of the `root` and find the depth of left branch and right branch of each node. Then compare the difference and check for the next node using DFS.

```python
def isBalanced(self, root: Optional[TreeNode]) -> bool:
    if root==None:
        return True
    else:
        leftDepth = self.getDepth(root.left) # get the depth of current left subtree
        rightDepth = self.getDepth(root.right) # get the depth of current right subtree
        if abs(leftDepth - rightDepth) > 1:
            return False
        else:
            # keep checking left subtree and right subtree
            return self.isBalanced(root.left) and self.isBalanced(root.right)

def getDepth(self, root):
    if root==None:
        return 0
    else:
        left = self.getDepth(root.left) + 1
        right = self.getDepth(root.right) + 1
        return max(left, right)
```

Time complexity is O(nlogn) as we will calculate depth for each node, which is `n`, and the depth calculation costs `logn`:\
![image](https://user-images.githubusercontent.com/25105806/140281093-bbafb925-36d1-44a9-9720-34e8b01745e4.png)

