#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connectBFS(self, root: 'Node') -> 'Node':
        if root is None:
            return None
        else:
            stack = [root]
            nextLevel = []

            while len(stack)!=0:
                node = stack.pop(0)
                if node.left is not None:
                    nextLevel.append(node.left)
                if node.right is not None:
                    nextLevel.append(node.right)

                if len(stack)==0:
                    for i in range(len(nextLevel)-1):
                        nextLevel[i].next = nextLevel[i+1]
                    stack = nextLevel.copy()
                    nextLevel = []
            return root

    def connectBFS2(self, root: 'Node') -> 'Node':
        sentinel = root
        while root:
            curr = nextLevel = Node(0)
            while root:
                # redirect 'next' pointer
                if root.left:
                    curr.next = root.left
                    curr = curr.next
                if root.right:
                    curr.next = root.right
                    curr = curr.next
                root = root.next # move to the next node in the same level
            root = nextLevel.next

        return sentinel


if __name__ == '__main__':
    solver = Solution()

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    #root.right.left = Node(6)
    root.right.right = Node(7)

    solver.connectBFS(root)


# In[ ]:




