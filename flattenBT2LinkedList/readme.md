# Flatten Binary Tree to Linked List problem
![1636932923(1)](https://user-images.githubusercontent.com/25105806/141703165-2f110d5c-18d1-4e05-8830-7ed755d2819a.png)

Leetcode Link: https://leetcode.com/problems/flatten-binary-tree-to-linked-list/

<br />

### Approach 1: Brute Force, flattenBruteForce()
The brute force solution, what we do is simply get the preorder traversal result and store each node as reference in a list. Then point the current node in list to next node in list for each node

```python
def flattenBruteForce(self, root: Optional[TreeNode]) -> None:
    """
    Do not return anything, modify root in-place instead.
    """
    def preorder(root):
        if root!=None:
            result.append(root)
            preorder(root.left)
            preorder(root.right)

    result = list()
    preorder(root)

    # cannot reassign root directly because root=xx is the reference to local variable, not the actual root
    for i in range(len(result)-1):
        result[i].left = None
        result[i].right = result[i+1]
```

Time complexity is O(2n) and space complexity is O(n):\
![image](https://user-images.githubusercontent.com/25105806/141703267-565d182e-b7fd-4b00-ade2-e34a2525a983.png)


<br />

### Approach 2: Interation, flattenIteration()
The idea is to find the predecessor of preorder traversal for each node, insert the left subtree to the right subtree and repeat this process iteratively

```
e.g. 
    For tree:
        1
       / \
      2   5
     / \   \
    3   4   6
    
    We first insert left subtree of node 1 to right subtree
        1
         \    \
          2    5
         / \    \
        3   4    6
        
    Then concat right subtree to the end
        1
         \    
          2    
         / \    
        3   4   
             \
              5
               \
                6
    
    Then we do the same for the left subtree of node 2, etc.
```

<br />

```python
def flattenIteration(self, root: Optional[TreeNode]) -> None:
    cur = root
    while cur!=None:
        if cur.left!=None:
            nxt = cur.left
            pre = cur.left
            while pre.right!=None:
                pre = pre.right
            pre.right = cur.right
            cur.right = nxt
            cur.left = None
        else:
            cur = cur.right
```

Time complexity is O(n) and space complexity is O(1):\
![image](https://user-images.githubusercontent.com/25105806/141703415-6bf8d554-82c7-4188-be6f-5ef04550d67e.png)

<br />

### Approach 3: Recursion, flattenReversedPreorder()
The idea is from preorder traversal where we simply visit nodes in pre-order and change the pointer to next node iteratively. However, if we visit the nodes in pre-order and change the reference of current node, we will lose reference to the unvisited nodes. Instead, we can do preorder traversal in reverse order to avoid this problem, we therefore can make sure that each visited node is already updated.

```
For tree:
    1
   / \
  2   5
 / \   \
3   4   6

We visit in reversed pre-order, which is 6, 5, 4, 3, 2, 1
Then we update the right child of each node in order:
 6->5, 4, 3, 2, 1

 6->5->4, 3, 2, 1

 6->5->4->3, 2, 1

 6->5->4->3->2, 1

 6->5->4->3->2->1
```

<br />

Notice that variable `pre` needs to be a `self.pre` variable otherwise we cannot modify `pre` inside a function in class
```python
def flattenReversedPreorder(self, root: Optional[TreeNode]) -> None:
    self.pre = None
    def helper(root):
        if root!=None:
            pre = helper(root.right)
            pre = helper(root.left)

            root.right = self.pre # pre starts with None, which means the right child of last node is None
            root.left = None
            self.pre = root

    helper(root)
```

Time complexity is O(n) and space complexity is O(1):\
![image](https://user-images.githubusercontent.com/25105806/141703577-808ce2d5-3dfc-4389-a553-53816af0edab.png)

<br />

### Approach 4: Stack, flattenStack()
The idea is to use a stack to visit and store the nodes reference in preorder, then redirecting each node to the next node, which is the last node in stack. 

```python
def flattenStack(self, root: Optional[TreeNode]) -> None:
    if root!=None:
        stack = [root]
        while len(stack)!=0:
            curr = stack.pop()

            if curr.right!=None:
                stack.append(curr.right)
            if curr.left!=None:
                stack.append(curr.left)

            if len(stack)!=0:
                curr.right = stack[-1]

            curr.left = None
```

Time compleixty is O(n), space complexity is (1) since we use a stack to store the nodes reference:\
![image](https://user-images.githubusercontent.com/25105806/141703754-005dc97d-bdf0-44b9-ae88-c205c7983864.png)


