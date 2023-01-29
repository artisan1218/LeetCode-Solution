# Reverse Linked List II problem
![image](https://user-images.githubusercontent.com/25105806/134728460-0e643792-5c29-4ce3-a22f-e996eb55eb18.png)

Leetcode link: https://leetcode.com/problems/reverse-linked-list-ii/

<br />

### Approach 1: Iteration, reverseBetween()
The solution is based on the [reverseLinkedList](https://github.com/artisan1218/LeetCode-Solution/tree/main/reverseLinkedList), the only difference is that we have to first identify the node at index `left-1` and `right` in order to reverse the nodes in between. The reversing process is same as [reverseLinkedList](https://github.com/artisan1218/LeetCode-Solution/tree/main/reverseLinkedList), where we use three pointers to hold the remaining linked list, reverse current node and refer the new head. 

```python3
def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
    sentinel = ListNode(next=head)

    # find linkedlist on the left-side(pre) and right-side(suf) of left and right
    count = 1
    pre = sentinel
    while count!=left:
        pre = pre.next
        count+=1

    count = 0
    suf = head
    while count!=right:
        suf = suf.next
        count+=1

    # reverse left to right
    revHead = suf
    cursor = pre.next
    while cursor!=suf:
        nextNode = cursor.next
        cursor.next = revHead
        revHead = cursor
        cursor = nextNode

    # connect pre
    pre.next = revHead

    return sentinel.next
```

Time complexity is O(n) and space complexity is O(1):
![image](https://user-images.githubusercontent.com/25105806/134728948-44a0f7b2-9c83-4cd0-b090-2447331aec4d.png)

