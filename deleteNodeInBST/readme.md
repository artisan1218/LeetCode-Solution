# Delete Node in a BST problem
![image](https://user-images.githubusercontent.com/25105806/205228565-8b68d248-8413-4a4c-a2a1-e41e818b34f6.png)

Leetcode link: https://leetcode.com/problems/delete-node-in-a-bst/

<br />

### Approach 1: deleteNode()

Credits to: https://www.geeksforgeeks.org/deletion-in-binary-search-tree/

The deletion can be divided into two cases:
1. Delete a node without children or only one children: The deletion can simply be done by returning the left or right subtree, which will make target node not pointed by any reference, thus went through garbage collection(deletion). 
2. Delete a node with left and right subtree: when both left and right subtree are presented, the first step is to find the successor of the target node, which is the smallest node at the right subtree of target. Then we will copy the value of successor to target node, this way, we 'deleted' the target node. Then for the successor, we call deleteNode() again to actually delete it in a recursive way, because we don't know whether it's a leaf node or not.

Code: 
```python3
def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
	if root is None:
		return root

	if key < root.val:
		root.left = self.deleteNode(root.left, key)
	elif key > root.val:
		root.right = self.deleteNode(root.right, key)
	else:
		if root.left is None:
			return root.right
		elif root.right is None:
			return root.left
		else:
			temp = root.right
			while temp.left is not None:
				temp = temp.left
			root.val = temp.val
			root.right = self.deleteNode(root.right, temp.val)
	return root
```

Time complexity is O(logn):
![image](https://user-images.githubusercontent.com/25105806/205229985-4f700cb0-9fad-4854-af58-7ce2dca25b4d.png)

