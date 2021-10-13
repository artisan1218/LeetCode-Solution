# Delete Nodes And Return Forest problem
![image](https://user-images.githubusercontent.com/25105806/137052457-5b67998f-8e54-4208-9530-a4d54b85bf63.png)

Leetcode link: https://leetcode.com/problems/delete-nodes-and-return-forest/

<br />

### Approach 1: BFS, delNodes1()
The idea is to use BFS to explore each nodes, at each node, we have two choices: either delete the node or keep it. If we delete the node, we need to first check its left and right subtree recursively to delete any nodes in `to_delete` list. Then we simply return `None` because this means the current node has been deleted, there is nothing to add. If the node is in `to_delete`, which means we should delete the current node, we then need to check the flag `parentExist`, which tells us if the current node is the top of current subtree, the current node can be the root of the initial tree or its parent node has been deleted, if there is no parent, we can add the root to `result`. Then again, we go to its left and right subtree recursively to delete any nodes in the `to_delete` list. At the end, instead of returning None, we should return `root` becase we want to keep the current node.

```python
def delNodes1(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
    delete = set(to_delete)
    result = []

    def helper(root, delete, result, parentExist):
        if root==None:
            return None
        else:
            if root.val in delete:
                # current root is to be deleted, so return None
                # we need to check left branch and right branch of the current root tree
                root.left = helper(root.left, delete, result, False)
                root.right = helper(root.right, delete, result, False)
                return None
            else:
                # parent not exists, either is the root of the tree, or the parents is deleted
                # we should add it to the forest result
                if not parentExist:
                    result.append(root)
                # check left branch and right branch
                root.left = helper(root.left, delete, result, True) # parent exists because root not in delete
                root.right = helper(root.right, delete, result, True)
                # root is kept, so return root itself instead of None
                return root

    # start at root, root has no parent, so False
    helper(root, delete, result, False)
    return result
```

Time complexity is O(n+m) where n is the number of nodes in the tree and m is the length of `to_delete` list:\
![image](https://user-images.githubusercontent.com/25105806/137054263-4c263832-2554-4966-a9bd-3c6cee987579.png)


<br />

### Approach 1: BFS, delNodes2()
The idea is similar to approach 1, but this time we first delete any nodes in `to_delete` list in left and right subtree of a node then we decide if we should add the current node to `result` 

```python
def delNodes2(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
    delete = set(to_delete)
    result = []

    def deleteNodes(root, delete, result):
        if root==None:
            return None
        else:
            # first delete nodes in left branch and right branch
            root.left = deleteNodes(root.left, delete, result)
            root.right = deleteNodes(root.right, delete, result)

            # we should not add root to result because it is to be deleted
            if root.val in delete:
                if root.left != None:
                    result.append(root.left)
                if root.right != None:
                    result.append(root.right)
                return None

            return root

    deleteNodes(root, delete, result)
    if root.val not in delete:
        result.append(root)

    return result
```

Time complexity is O(n+m) where n is the number of nodes in the tree and m is the length of `to_delete` list:\
![image](https://user-images.githubusercontent.com/25105806/137054307-cd565c07-13d1-4436-95e5-e8c7c4ae4875.png)


