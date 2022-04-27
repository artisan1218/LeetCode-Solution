#  Binary Tree Inorder Traversal problem
* Given the `root` of a binary tree, return the inorder traversal of its nodes' values.

Leetcode link: https://leetcode.com/problems/binary-tree-inorder-traversal/

<br />

### Approach 1: DFS, inorderTraversalDFS()
The standard in-order traversal of a binary tree:

![image_1556551007](https://user-images.githubusercontent.com/25105806/135376395-0ffc3d36-0f59-4d2d-a134-58f15e3bb831.png)


```python3
def inorderTraversalDFS(self, root: Optional[TreeNode]) -> List[int]:
    result = []
    def dfs(root, result):
        if root==None:
            return []
        else:
            # visit left branch and add elements in the left branch first
            if root.left!=None:
                dfs(root.left, result)
            result.append(root.val) # add root value
            # visit right branch and add elements in the right branch 
            if root.right!=None:
                dfs(root.right, result)

    dfs(root, result)
    return result
```

Actual running time:\
![image](https://user-images.githubusercontent.com/25105806/135376828-70d25e2c-7af4-4951-9fb7-3a50d9d66701.png)


<br />

### Approach 2: Iteration, inorderTraversalIteration()
The idea is to two a stack and a list to complete the inorder traversal. The stack is used to hold the reference of node(instead of `node.val`) in the inorder order, which is going along the way down to left first and go to right whenever we cannot go any further left. Then pop each node out, add the val and go to right branch of that node. Note that we store the reference of node is to get the right branch of that node, otherwise we cannot go to right.

```python3
def inorderTraversalIteration(self, root: Optional[TreeNode]) -> List[int]:
    result = []
    stack = []
    while root!=None or len(stack)!=0:
        while root!=None:
            # explore all left branches
            stack.append(root) # not root.val but root, records the path or inorder traversal
            root = root.left
        node = stack.pop()
        result.append(node.val)
        root = node.right

    return result
```

Actual running time:\
![image](https://user-images.githubusercontent.com/25105806/135376885-f3429c20-26b0-496b-a480-43100dda248c.png)


<br />

### Approach 3: Morris Traversal, inorderTraversalMorris()

Credits to: https://www.youtube.com/watch?v=wGXB9OWhPTg&t=1s

Instead of using a stack or recursio to keep track of the path, Morris basically creates a bridge whenever we've reached the end of predecessor of a node. This enables us to traval back to the root node from left subtree. 

```python3
def inorderTraversalMorris(self, root: Optional[TreeNode]) -> List[int]:
    current = root
    result = list()
    while current!=None:
        # if left is null, visit current and go to right
        if current.left==None:
            result.append(current.val)
            # either go to the actual right, or its immediate right through the bridge
            current = current.right 
        else:
            # if left is not null, find the predecessor
            pre = current.left # first go to left
            # then go all the way to right, make sure pre.right!=current so that we don't enter loop
            while pre.right!=current and pre.right!=None:
                pre = pre.right

            if pre.right == None:
                # create a bridge that connects current node and its predecessor
                pre.right = current
                current = current.left # visit left
            else:
                pre.right = None # unbridge the link
                result.append(current.val)
                current = current.right
    return result
```

Time complexity is O(n) and space complexity is O(1):\
<img width="638" alt="image" src="https://user-images.githubusercontent.com/25105806/135798306-ca466c0c-87d6-4f16-ba9a-64c6bf48de8f.png">

