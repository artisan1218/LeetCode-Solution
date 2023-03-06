# Binary Search Tree Iterator problem
<img width="804" alt="image" src="https://user-images.githubusercontent.com/25105806/223025531-bead5b0a-a584-44e8-8a65-f6132075870d.png">

<img width="808" alt="image" src="https://user-images.githubusercontent.com/25105806/223025548-83b37b4c-2044-4a0d-ac26-7679c017d870.png">


Leetcode link: https://leetcode.com/problems/binary-search-tree-iterator/

<br />

### Approach 1: DFS, BSTIterator()

The idea is pretty simple, we first use DFS to traverse the tree and keep all nodes in a `result` list, then pop the node out of `result` on every `next()` function call.

```python3
class BSTIterator:
    
    def __init__(self, root: Optional[TreeNode]):
        self.result = []
        self.helper(root)
    
    def helper(self, root):
        if root:
            self.helper(root.left)
            self.result.append(root.val)
            self.helper(root.right)
        
    def next(self) -> int:
        return self.result.pop(0)

    def hasNext(self) -> bool:
        return len(self.result)>0
```

Time complexity for constructor is O(n), next() and hasNext() is O(1):

<img width="621" alt="image" src="https://user-images.githubusercontent.com/25105806/223025965-cad3c45d-6fc1-4356-8bf7-9ae609dcf747.png">


<br />

### Approach 2: BFS, BSTIterator2()

We notice that wo actually only need to get the next node when `next()` is called and thus no need to traverse the whole BST when initializing. So `next()` function is actually finding the immediate successor of current node. 

```python3
class BSTIterator2:
    
    def __init__(self, root: Optional[TreeNode]):
        self.stack = list()
        self.helper(root)
        
    def next(self) -> int:
        nextNode = self.stack.pop()
        self.helper(nextNode.right)
        return nextNode.val

    def hasNext(self) -> bool:
        return len(self.stack)>0
    
    def helper(self, node):
        while node:
            self.stack.append(node)
            node = node.left
```

Average time complexity is O(1) because we only get the element when we actually need to:

<img width="630" alt="image" src="https://user-images.githubusercontent.com/25105806/223026547-baf085c1-c9b0-4f1d-b199-7865ef9bc727.png">
