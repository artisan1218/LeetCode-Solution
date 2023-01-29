# Binary Tree Level Order Traversal II problem
![image](https://user-images.githubusercontent.com/25105806/135961171-59f716f0-9b90-450d-ae3c-016ea5bafa9a.png)

Leetcode link: https://leetcode.com/problems/binary-tree-level-order-traversal-ii/

<br />

### Approach 1: BFS, levelOrderBottom():
Based on [levelOrderTraversal](https://github.com/artisan1218/LeetCode-Solution/tree/main/levelOrderTraversal), when we get the top-bottom order list, we just simply reverse the list and return it

```python3
def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
    if root!=None:
        result = list()
        queue = [root]
        while len(queue)!=0:
            levelLen = len(queue)
            level = list()
            for i in range(levelLen):
                node = queue.pop(0)
                level.append(node.val)
                if node.left!=None:
                    queue.append(node.left)
                if node.right!=None:
                    queue.append(node.right)
            result.append(level)
        return result[::-1]
    else:
        return []
```

Time complexity O(n):\
![image](https://user-images.githubusercontent.com/25105806/135961361-84769ad6-170e-4b6f-b567-7fa6f12fe6d6.png)
