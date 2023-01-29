# Convert Sorted List to Binary Search Tree problem
![image](https://user-images.githubusercontent.com/25105806/136265678-ea7faf58-ea09-45af-9e0e-0d76e35ed259.png)

Leetcode link: https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/

<br />

### Approach 1: Convert to List, sortedListToBST()
The idea is based on [convertSortedAryToBST](https://github.com/artisan1218/LeetCode-Solution/tree/main/convertSortedAryToBST) and easy to think of. Simply convert the linked list to a list, and use the same approach as convertSortedAryToBST to solve this.

```python3
def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
    nums = []
    while head!=None:
        nums.append(head.val)
        head = head.next

    def convert(nums):
        if len(nums)==0:
            return None
        else:
            # find a middle point
            mid = len(nums)//2
            # make middle point at the root 
            root = TreeNode(nums[mid])
            root.left = convert(nums[0:mid])
            root.right = convert(nums[mid+1:])
            return root
        return root
    return convert(nums)
```

Time complexity is O(n):\
![image](https://user-images.githubusercontent.com/25105806/136265953-7bba2928-f03a-423b-bb37-d5950a6fb318.png)

<br />

### Approach 2: Inorder Simulation, sortedListToBST()

![image](https://user-images.githubusercontent.com/25105806/136266096-9aface95-4183-4447-80b7-97e68aaec3d1.png)
![image](https://user-images.githubusercontent.com/25105806/136266159-3c261487-e44a-4dd8-ba2d-47e4ab013239.png)
![image](https://user-images.githubusercontent.com/25105806/136266184-99df86e0-ac06-4b28-9639-34a59b9be04d.png)

```python3
def sortedListToBST2(self, head: Optional[ListNode]) -> Optional[TreeNode]:
    # find the length of the linked list
    def findSize(head):
        ptr = head
        size = 0
        while ptr!=None:
            ptr = ptr.next
            size += 1
        return size

    def convert(l, r):
        nonlocal head

        if l>r:
            return None
        else:
            mid = (l+r)//2

            leftBranch = convert(l, mid-1) # left subtree
            root = TreeNode(head.val) # root is not the element at mid, but head, we will build the leftsubtree first
            root.left = leftBranch # connect root and left subtree

            head = head.next # move the head to right, build the right subtree
            rightBranch = convert(mid+1, r) # right subtree
            root.right = rightBranch # connect

            return root

    size = findSize(head)
    return convert(0, size-1)
```

Time complexity is O(n):\
![image](https://user-images.githubusercontent.com/25105806/136266353-a0709edf-0e0c-4ae8-8828-f6ded9d6a2a4.png)
