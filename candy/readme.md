# Construct Binary Tree from Preorder and Inorder Traversal problem
![image](https://user-images.githubusercontent.com/25105806/135960196-d35fd783-254b-46fc-91a6-12bd390e645b.png)

<br />

### Approach 1: buildTree()
We have `preorder` and `inorder` traversal list. Since we know that the first element in the `preorder` traversal list is always going to be the root value. So we can find the root value for the tree. Then we will find the index of root value in `inorder` traversal to get the range of left subtree and right subtree. We do this recursively for each subtree until we've explored all values in the list

Time complexity is O(n^2) since we use `.index()` function and list slicing in recusion:\
![image](https://user-images.githubusercontent.com/25105806/135960488-87cf60cf-82b3-4a43-8c8b-d25efeba2653.png)
