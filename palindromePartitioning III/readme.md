# Partition List problem
* Given the `head` of a linked list and a value `x`, partition it such that all nodes less than `x` come before nodes greater than or equal to `x`.
* You should preserve the original relative order of the nodes in each of the two partitions.

Leetcode link: https://leetcode.com/problems/partition-list/

<br />

### Approach 1: Naive, partition()
The idea is to first connecting all nodes that are smaller than `x`, storing references of nodes that are greater than `x` in a pass. Then connecting all nodes greater than `x` stored in previous list. This is a working solution but can be improved.

```python3
def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
    sentinel = ListNode(-101, head)
    l = sentinel
    check = head
    rList = []

    # connect all nodes that are smaller than x
    # and store references of nodes that are greater than x
    while check!=None:
        if check.val < x:
            l.next = check
            l = l.next
            check = check.next
        else:
            rList.append(check)
            check = check.next

    # connect all nodes that are greater than x
    for node in rList:
        l.next = node
        l = l.next

    # disconnecting the last node to prevent circling
    l.next=None

    return sentinel.next
```


Time complexity is (n+m) where n is the length of the linked list and n is the number of nodes that are greater than x:
![image](https://user-images.githubusercontent.com/25105806/133676929-5b906e26-a122-4c49-bba8-be680b6ae111.png)

<br />

### Approach 2: Two Pointers, partitionTwoPointers()
Turns out we can just use two pointers, one is "before", representing all nodes that are smaller than `x` and one is "after", representing all nodes that are greater than `x`. When iterating through the linked list, whenever we meet a node that is smaller than `x`, we will connect it to `before` and if a node is greater than `x`, we will connect it to `after`. Finally, we connect these two parts together.

```python3
def partitionTwoPointers(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
    # beforeHead and afterHead are two pointers represent the nodes smaller than x and greater than x
    beforeHead = before = ListNode(0)
    afterHead = after = ListNode(0)

    while head!=None:
        if head.val < x:
            before.next = head
            before = before.next
        else:
            after.next = head
            after = after.next
        head = head.next

    # cut the circle
    after.next = None
    # connecting two parts
    before.next = afterHead.next

    return beforeHead.next
```

Time complexity is O(n) because we just iterate through the linked list once:
![image](https://user-images.githubusercontent.com/25105806/133677569-2bb8330f-0a6c-481b-bb84-392f8982692c.png)

