# Construct Binary Tree from Inorder and Postorder Traversal problem
![image](https://user-images.githubusercontent.com/25105806/135960716-7a25d3bf-f84f-49a5-bf04-d2d1533f5e93.png)

<br />

### Approach 1: buildTree()
The idea is similar to previous question [buildTreeFromPreorderAndInorderTraversal](https://github.com/artisan1218/LeetCode-Solution/tree/main/buildTreeFromPreorderAndInorder). The difference is that, instead of getting root value from the start of `preorder` list, we now getting root value from the back of `postorder`, then do the similar thing by finding the index of root in `inorder` list to decide what is the value range in the left subtree and wwhat is the value range in the right subtree

Time complexity is O(n^2):\
![image](https://user-images.githubusercontent.com/25105806/135960993-fe4fcea6-358e-41e6-94f5-fd2ba6e77090.png)

