# Validate Binary Search Tree problem
![image](https://user-images.githubusercontent.com/25105806/135770320-2a106846-a750-44fd-bd2f-479e12fcbc73.png)


### Approach 1: BFS Inorder Traversal, isValidBSTInorderBFS()
This solution uses BFS traversal, we will maintain a stack that stores the node in in-order order and check if each node is within the valid range. We will update the valid range for each node as we explore the nodes

Time complexity O(n) where n is the number of nodes in the BST:
![image](https://user-images.githubusercontent.com/25105806/135770394-36ff1f7e-d160-4c9f-9517-fd58f14ccb42.png)


<br />

### Approach 2: DFS, isValidBSTInorderDFS()
Credits to: https://leetcode.com/problems/validate-binary-search-tree/discuss/32112/Learn-one-iterative-inorder-traversal-apply-it-to-multiple-tree-questions-(Java-Solution)

Similar to approach 1, we still use a stack to store the nodes as we explore the tree. But this time we also main another node called `pre`. `pre` is always the immediate left of the current node `root` so we only need to make sure `root.val` is greater than `pre.val`

Time complexity is O(n):

![image](https://user-images.githubusercontent.com/25105806/135770462-ffe1b1f7-5a2b-42ca-9ef9-56b8593d3b6e.png)

<br />

### Approach 2: DFS, isValidBSTDFS()
Credits to: https://leetcode.com/problems/validate-binary-search-tree/discuss/32193/1-ms-Java-Solution-using-Recursion

This is a recursive solution, we main two variables `minVal` and `maxVal` that bounds each node and update these two variables as we explore more nodes:
`helper(root.left, minVal, root.val) and helper(root.right, root.val, maxVal)`

Time complexity O(n):\
![image](https://user-images.githubusercontent.com/25105806/135770597-987c86ec-afa0-41ce-8c43-497bba70d755.png)
