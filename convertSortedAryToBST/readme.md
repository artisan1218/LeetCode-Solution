# Convert Sorted Array to Binary Search Tree problem
![image](https://user-images.githubusercontent.com/25105806/135961637-a05d3ff5-32c0-401e-9800-41374a022bed.png)

Leetcode link: https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

<br />

### Approach 1: List Slicing, sortedArrayToBST1()
The idea is to first find the middle point of the sorted array, since the middle point value will be the root of the constructed BST. Then we will slice the sorted ary `nums` into two parts, corresponding to the left subtree and right subtree respectively. We do this recursively by calling:
```
root.left = self.sortedArrayToBST1(nums[0:mid])
root.right = self.sortedArrayToBST1(nums[mid+1:])
```

Full code:

```python3
def sortedArrayToBST1(self, nums: List[int]) -> Optional[TreeNode]:
    if len(nums)==0:
        return None
    else:
        # find a middle point
        mid = len(nums)//2
        # make middle point at the root 
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST1(nums[0:mid])
        root.right = self.sortedArrayToBST1(nums[mid+1:])
        return root
```

Time complexity is O(n^2) since we use list slicing recursively:\
![image](https://user-images.githubusercontent.com/25105806/135961884-8beb40a5-aa0c-4d53-a930-21de8ff0ea63.png)

<br />

### Approach 2: Use Index, sortedArrayToBST2()
Instead of use slicing to actually cut the sorted array `nums`, we can simply to index to bound the array. Then taking the middle value, simply calcualte by `mid=(low+high)//2`
and get left subtree and right subtree by
```
root.left = helper(nums, low, mid-1)
root.right= helper(nums, mid+1, high)
```

Full code:

```python3
def sortedArrayToBST2(self, nums: List[int]) -> Optional[TreeNode]:
    def helper(nums, low, high):
        if low > high:
            return None
        else:
            mid = (high+low)//2
            root = TreeNode(nums[mid])
            root.left = helper(nums, low, mid-1)
            root.right= helper(nums, mid+1, high)
            return root
    return helper(nums, 0, len(nums)-1)
```

Time complexity is O(n):\
![image](https://user-images.githubusercontent.com/25105806/135962122-7f7a3ae9-19d0-4c32-8898-403b393f6794.png)


