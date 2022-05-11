# Binary Tree Zigzag Level Order Traversal problem
![image](https://user-images.githubusercontent.com/25105806/135959482-4e9db087-7ec6-4300-beba-708fab26fe28.png)

Leetcode link: https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

<br />

### Approach 1: zigzagLevelOrder()
This solution is based on [levelOrderTraversal](https://github.com/artisan1218/LeetCode-Solution/tree/main/levelOrderTraversal) but use another variable to mark in which order should we add the node in current level in the `result` list, then simply alternating the order

```python3
def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    if root!=None:
        result = list()
        level = [root]
        result.append([node.val for node in level])
        l2r = False
        while len(level)!=0:
            nextLevel = list()
            for node in level:
                if node.left!=None:
                    nextLevel.append(node.left)
                if node.right!=None:
                    nextLevel.append(node.right)
            if l2r:
                result.append([node.val for node in nextLevel])
            else:
                result.append([node.val for node in reversed(nextLevel)])
            level = nextLevel
            l2r = not l2r

        return result[:-1]
    else:
        return []
```

Time complexity is O(n):\
![image](https://user-images.githubusercontent.com/25105806/135959603-8349b72a-e499-47a7-be5b-dd0ce965ec60.png)
