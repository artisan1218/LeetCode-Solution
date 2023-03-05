# Validate Binary Search Tree problem
![image](https://user-images.githubusercontent.com/25105806/135770320-2a106846-a750-44fd-bd2f-479e12fcbc73.png)


### Approach 1: BFS Inorder Traversal, isValidBSTInorderBFS()
This solution uses BFS traversal, we will maintain a stack that stores the node in in-order order and check if each node is within the valid range. We will update the valid range for each node as we explore the nodes

```python3

def isValidBSTInorderBFS(self, root: Optional[TreeNode]) -> bool:
	# BFS traversal
	# each element in level list is a 3-tuple consists of parent node value, valid range of left subtree value
	# and valid range of right subtree value
	level = [(root, (float('-inf'), root.val), (root.val, float('inf')))]

	while len(level)!=0:
		parent, leftRange, rightRange = level.pop()
		if parent.left!=None:
			if parent.left.val > leftRange[0] and parent.left.val < leftRange[1]:
				# update new left and right subtree value range for left node of current parent node
				leftLeftRange = (leftRange[0], parent.left.val)
				leftRightRange = (parent.left.val, leftRange[1])
				level.append((parent.left, leftLeftRange, leftRightRange))
			else:
				return False

		if parent.right!=None:
			if parent.right.val > rightRange[0] and parent.right.val < rightRange[1]:
				# update new left and right subtree value range for right node of current parent node
				rightLeftRange = (rightRange[0], parent.right.val)
				rightRightRange = (parent.right.val, rightRange[1])
				level.append((parent.right, rightLeftRange, rightRightRange))
			else:
				return False

	return True
```

Time complexity O(n) where n is the number of nodes in the BST:
![image](https://user-images.githubusercontent.com/25105806/135770394-36ff1f7e-d160-4c9f-9517-fd58f14ccb42.png)


<br />

### Approach 2: DFS, isValidBSTInorderDFS()
Credits to: https://leetcode.com/problems/validate-binary-search-tree/discuss/32112/Learn-one-iterative-inorder-traversal-apply-it-to-multiple-tree-questions-(Java-Solution)

Similar to approach 1, we still use a stack to store the nodes as we explore the tree. But this time we also main another node called `pre`. `pre` is always the immediate left of the current node `root` so we only need to make sure `root.val` is greater than `pre.val`

```python3
def isValidBSTInorderDFS(self, root: Optional[TreeNode]) -> bool:
	if root==None:
		return True
	else:
		stack = list()
		pre = None

		while len(stack)!=0 or root!=None:
			# DFS, append left node all the way down
			while root != None:
				stack.append(root)
				root = root.left

			# pop one out to check
			root = stack.pop()
			# bad condition, root should be greater than pre
			if pre!=None and root.val <= pre.val:
				return False

			# pre is always on the immediate left of root
			pre = root
			root = root.right
		return True
```

Time complexity is O(n):

![image](https://user-images.githubusercontent.com/25105806/135770462-ffe1b1f7-5a2b-42ca-9ef9-56b8593d3b6e.png)

<br />

### Approach 3: DFS, isValidBSTDFS()
Credits to: https://leetcode.com/problems/validate-binary-search-tree/discuss/32193/1-ms-Java-Solution-using-Recursion

This is a recursive solution, we maintain two variables `minVal` and `maxVal` that bounds each node and update these two variables as we explore more nodes:
`helper(root.left, minVal, root.val) and helper(root.right, root.val, maxVal)`

```python3
def isValidBSTDFS(self, root: Optional[TreeNode]) -> bool:
        
	def helper(root, minVal, maxVal):
		if root==None:
			return True
		elif root.val <= minVal or root.val >= maxVal:
			return False
		else:
			return helper(root.left, minVal, root.val) and helper(root.right, root.val, maxVal)

	return helper(root, float('-inf'), float('inf'))
```

Time complexity is O(n):\
![image](https://user-images.githubusercontent.com/25105806/135770597-987c86ec-afa0-41ce-8c43-497bba70d755.png)
