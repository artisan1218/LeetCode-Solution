#  Binary Tree Inorder Traversal problem
* Given the `root` of a binary tree, return the inorder traversal of its nodes' values.

### Approach 1: DFS, inorderTraversalDFS()
The standard in-order traversal of a binary tree:

![image_1556551007](https://user-images.githubusercontent.com/25105806/135376395-0ffc3d36-0f59-4d2d-a134-58f15e3bb831.png)

Actual running time:

![image](https://user-images.githubusercontent.com/25105806/135376828-70d25e2c-7af4-4951-9fb7-3a50d9d66701.png)


<br />

### Approach 2: Iteration, inorderTraversalIteration()
The idea is to two a stack and a list to complete the inorder traversal. The stack is used to hold the reference of node(instead of `node.val`) in the inorder order, which is going along the way down to left first and go to right whenever we cannot go any further left. Then pop each node out, add the val and go to right branch of that node. Note that we store the reference of node is to get the right branch of that node, otherwise we cannot go to right.

Actual running time:

![image](https://user-images.githubusercontent.com/25105806/135376885-f3429c20-26b0-496b-a480-43100dda248c.png)


<br />

### Approach 3: Morris Traversal, inorderTraversalMorris()

Credits to: https://www.youtube.com/watch?v=wGXB9OWhPTg&t=1s

Instead of using a stack or recursio to keep track of the path, Morris basically creates a bridge whenever we've reached the end of predecessor of a node. This enables us to traval back to the root node from left subtree. 

Time complexity is O(n) and space complexity is O(1):

<img width="638" alt="image" src="https://user-images.githubusercontent.com/25105806/135798306-ca466c0c-87d6-4f16-ba9a-64c6bf48de8f.png">

