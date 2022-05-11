# Binary Tree Level Order Traversal problem
![image](https://user-images.githubusercontent.com/25105806/135959044-2e29e7f5-0ff8-4524-b092-7bcc5a8d91df.png)

Leetcode link: https://leetcode.com/problems/binary-tree-level-order-traversal/

<br />

### Approach 1: BFS, levelOrder1()
The approach uses two list `level` and `nextLevel` to hold the nodes in current level and next level, so that we don't mix them together. 

```python3
def levelOrder1(self, root: Optional[TreeNode]) -> List[List[int]]:
    if root!=None:
        result = list()
        level = [root]
        result.append([node.val for node in level])
        while len(level)!=0:
            nextLevel = list()
            for node in level:
                if node.left!=None:
                    nextLevel.append(node.left)
                if node.right!=None:
                    nextLevel.append(node.right)
            result.append([node.val for node in nextLevel])
            level = nextLevel

        return result[:-1]
    else:
        return []
```

Time complexity is O(n):\
![image](https://user-images.githubusercontent.com/25105806/135959177-22711919-b83c-4649-a66e-5a43a7bd7cf4.png)

<br />

### Approach 2: BFS, levelOrder2()
Instead of using two list, we can instead using only one queue. But we need to get the length of each level at the beginning of loop so that we don't mix them up with the nodes on the next level

```python3
def levelOrder2(self, root: Optional[TreeNode]) -> List[List[int]]:
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
        return result
    else:
        return []
```

Time complexity is O(n):\
![image](https://user-images.githubusercontent.com/25105806/135959285-5c415451-324c-4e50-9957-152bfb79ee48.png)
