# Populating Next Right Pointers in Each Node II problem 
<img width="1043" alt="image" src="https://user-images.githubusercontent.com/25105806/147619397-d89d8725-8dd4-4814-b4d4-032a274037a3.png">

Leetcode link: https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/

<br />

### Approach 1: BFS, connectBFS()
This approach simply traverse nodes in the `root` level by level using BFS and redirect the `next` pointer one by one. This approach is the same as approach #1 in https://github.com/artisan1218/LeetCode-Solution/tree/main/populatingNxtPtr

```python3
def connectBFS(self, root: 'Node') -> 'Node':
    if root is None:
        return None
    else:
        stack = [root]
        nextLevel = []

        while len(stack)!=0:
            node = stack.pop(0)
            if node.left is not None:
                nextLevel.append(node.left)
            if node.right is not None:
                nextLevel.append(node.right)

            if len(stack)==0:
                for i in range(len(nextLevel)-1):
                    nextLevel[i].next = nextLevel[i+1]
                stack = nextLevel.copy()
                nextLevel = []
        return root
```

Time complexity is O(n):\
<img width="657" alt="image" src="https://user-images.githubusercontent.com/25105806/147619459-ec3be977-00fa-45ab-a0d7-a427275753ca.png">

<br />

### Approach 2: BFS, connectBFS2()
Credits to: https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/discuss/961868/Python-O(n)-solution-explained

This approach is still based on level by level BFS traversal, but a different implementation that uses constant space. The key idea is to use two pointers `curr` and `nextLevel` to change the `next` pointer of nodes and hold the reference to next level respectively.

We will do this level by level and at each level, check the left and right child of the current node. We will move the `curr` pointer and use it to change the `next` pointer at each node if left and right child is not `None`, then use the `next` pointer of the previous level to move the to the next node in the same level.

```python3
def connectBFS2(self, root: 'Node') -> 'Node':
    sentinel = root
    while root:
        curr = nextLevel = Node(0)
        while root:
            # redirect 'next' pointer
            if root.left:
                curr.next = root.left
                curr = curr.next
            if root.right:
                curr.next = root.right
                curr = curr.next
            root = root.next # move to the next node in the same level
        root = nextLevel.next

    return sentinel
```

Time complexity is O(n):\
<img width="661" alt="image" src="https://user-images.githubusercontent.com/25105806/147619611-ad8b11d5-d2b0-4962-a240-894126ef9431.png">

