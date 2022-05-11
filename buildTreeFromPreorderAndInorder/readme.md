# Construct Binary Tree from Preorder and Inorder Traversal problem
![image](https://user-images.githubusercontent.com/25105806/135960196-d35fd783-254b-46fc-91a6-12bd390e645b.png)

Leetcode link: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

<br />

### Approach 1: buildTree()
We have `preorder` and `inorder` traversal list. Since we know that the first element in the `preorder` traversal list is always going to be the root value. So we can find the root value for the tree. Then we will find the index of root value in `inorder` traversal to get the range of left subtree and right subtree. We do this recursively for each subtree until we've explored all values in the list

```python3
def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    if len(preorder)==0 or len(inorder)==0:
        return None
    else:
        # root is always the first element in preorder traversal
        rootVal = preorder[0]
        root = TreeNode(rootVal)
        # find the index of root at inorder list because to get the left subtree and right subtree
        inorderRootIdx = inorder.index(rootVal)

        # for the left subtree, we know the possible range are all the values before the rootIdx and after 1
        # because we've used the first element, which is the current root
        # for the right subtree, we know the possible range are all the values after the rootIdx in inorder traversal
        root.left = self.buildTree(preorder[1:inorderRootIdx+1], inorder[0:inorderRootIdx])
        root.right = self.buildTree(preorder[inorderRootIdx+1:], inorder[inorderRootIdx+1:])
        return root            
```

Time complexity is O(n^2) since we use `.index()` function and list slicing in recusion:\
![image](https://user-images.githubusercontent.com/25105806/135960488-87cf60cf-82b3-4a43-8c8b-d25efeba2653.png)
