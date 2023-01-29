# Construct Binary Tree from Inorder and Postorder Traversal problem
![image](https://user-images.githubusercontent.com/25105806/135960716-7a25d3bf-f84f-49a5-bf04-d2d1533f5e93.png)

Leetcode link: https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/

<br />

### Approach 1: buildTree()
The idea is similar to previous question [buildTreeFromPreorderAndInorderTraversal](https://github.com/artisan1218/LeetCode-Solution/tree/main/buildTreeFromPreorderAndInorder). The difference is that, instead of getting root value from the start of `preorder` list, we now getting root value from the back of `postorder`, then do the similar thing by finding the index of root in `inorder` list to decide what is the value range in the left subtree and wwhat is the value range in the right subtree

```python3
def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
    if len(inorder)==0 or len(postorder)==0:
        return None
    else:
        # we can get root from the last element in postorder
        root = TreeNode(postorder[-1])

        # then find the root index in the inorder list, left sublist will be elements on the left subtree
        # right sublist will be on the right substree
        inorderRootIdx = inorder.index(postorder[-1])

        # split the inorder list at the root index, do the same thing to postorder except for the last element,
        # which is the root value, we skip that because root is already used
        root.left = self.buildTree(inorder[0:inorderRootIdx], postorder[0:inorderRootIdx])
        root.right = self.buildTree(inorder[inorderRootIdx+1:], postorder[inorderRootIdx:-1])
        return root
```

Time complexity is O(n^2):\
![image](https://user-images.githubusercontent.com/25105806/135960993-fe4fcea6-358e-41e6-94f5-fd2ba6e77090.png)

