# Populating Next Right Pointers in Each Node problem
![image](https://user-images.githubusercontent.com/25105806/147433511-bc0602cc-f28e-40ca-8cfd-4c843e766bce.png)

Leetcode link: https://leetcode.com/problems/populating-next-right-pointers-in-each-node/

<br />

### Approach 1: BFS, connectBFS()
This approach simply traverse nodes in the `root` level by level using BFS and redirect the `next` pointer one by one.

```python3
def connectBFS(self, root: 'Optional[Node]') -> 'Optional[Node]':
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
![image](https://user-images.githubusercontent.com/25105806/147433605-ddecf01d-c5be-451a-89e7-38cb5f327fcd.png)

<br />

### Approach 2: BFS, connectBFS2()
This approach is still based on level by level BFS traversal, but a different implementation that uses constant space.

```python3
def connectBFS2(self, root: 'Optional[Node]') -> 'Optional[Node]':
    head = root # sentinel node
    while root and root.left:
        nextLevel = root.left # reference to the next level
        # populating next pointer at the same level
        while root is not None:
            root.left.next = root.right
            if root.next is not None: # default value for next pointer is None, so no need to change it if root.next is None
                root.right.next = root.next.left
            root = root.next
        # move to the next level
        root = nextLevel
    return head
```

Time complexity is O(n):\
![image](https://user-images.githubusercontent.com/25105806/147433693-c3edbc5d-8022-4469-b9a6-cbc268d0ca9d.png)

<br />

### Approach 3: Recursion, connectRecursion()
Since the next pointer always points to the next immediate node in the same level, we can use recursion on the left and right node of a root node and redirect the next pointer recursively. 

1. If current root node is the left node, then point `next` pointer to the right node
2. If current root node is the right node, then check if `next` pointer of the parent node is null. If it's null, that means the current right node is the right-most node and hence `next` pointer remains null.

```python3
def connectRecursion(self, root: 'Optional[Node]') -> 'Optional[Node]':
    def recursion(root):
        if root is None:
            return None
        else:
            if root.left is not None:
                root.left.next = root.right
                if root.next is not None:
                    root.right.next = root.next.left
        recursion(root.left)
        recursion(root.right)

    recursion(root)
    return root

```

Time complexity is O(n):\
![image](https://user-images.githubusercontent.com/25105806/147433942-6cfce2ab-578b-464a-8fee-b43c4d0ab73e.png)

