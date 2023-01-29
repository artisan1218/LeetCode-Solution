# Remove Duplicates from Sorted List II problem
* Given the `head` of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.

Leetcode link: https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

<br />

### Approach 1: Two Pointers, deleteDuplicates()
Use two pointers, one fast, one slow. Slow pointer will be used to modify the linked list while fast pointer will be used to get new value and check for duplicates.

```python3
def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
    sentinel = ListNode(0, head)
    pred = sentinel # predecessor

    while head!=None:
        if head.next!=None and head.val==head.next.val:
            # we have duplicates, should skip this sublist
            while head.next!=None and head.val==head.next.val:
                # repeatedly skip duplicates value
                head = head.next
            # we have skiped this duplicates sublist, we can temporarily move 'next' pointer of pred here
            # but since we don't know if there are more duplicates upfront, don't move pointer of pred itself here
            # 3 3 4 4, we have skiped 3 3, but don't know how many 4's are there
            pred.next = head.next                
        else:
            # next two values are not the same, we can safely move pred
            pred = pred.next

        # move head to next
        head = head.next

    return sentinel.next
```

Time complexity is O(n):\
![9400470eb4f90d209f7648cc75c51eb](https://user-images.githubusercontent.com/25105806/132803589-5d3e76a1-1b84-4da3-ba9c-ad96259d6a89.png)
