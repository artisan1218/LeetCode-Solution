# Min Stack problem

![image](https://user-images.githubusercontent.com/25105806/212526665-c5467494-27dc-4d2c-b4ab-9833977abd77.png)

Leetcode link: https://leetcode.com/problems/min-stack/description/

<br/>

### Approach 1: Doubly LinkedList

The idea is to have a doubly linked list storing the current min value at each node. This way when popping the top node, we can remove the min value associated with that node at the same time, so min value can also be updated.

`topNode` always points to the newly pushed node.

```python3
class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.min = float('inf')
        self.next = None
        self.prev = None
        
class minStack:
    def __init__(self):
        self.topNode = ListNode()
        self.begin = self.topNode
        
    def push(self, val):
        newVal = ListNode(val)
        if val < self.topNode.min:
            newVal.min = val
        else:
            newVal.min = self.topNode.min
        self.topNode.next = newVal
        newVal.prev = self.topNode
        self.topNode = self.topNode.next
        
    def pop(self):
        result = self.topNode
        self.topNode = self.topNode.prev
        self.topNode.next = None
        result.prev = None
        return result.val
        
    def top(self):
        return self.topNode.val
        
    def getMin(self):
        return self.topNode.min
        
```

Complexity is O(1) for all operations:
![image](https://user-images.githubusercontent.com/25105806/212527088-ef68e646-3778-4334-aa2e-e61a94dd840c.png)
