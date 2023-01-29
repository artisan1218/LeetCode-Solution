# Insertion Sort List problem
Given the head of a singly linked list, sort the list using insertion sort, and return the sorted list's head.

The steps of the insertion sort algorithm:

1. Insertion sort iterates, consuming one input element each repetition and growing a sorted output list.
2. At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list and inserts it there.
3. It repeats until no input elements remain.

The following is a graphical example of the insertion sort algorithm. The partially sorted list (black) initially contains only the first element in the list. One element (red) is removed from the input data and inserted in-place into the sorted list with each iteration.

![Insertion-sort-example-300px](https://user-images.githubusercontent.com/25105806/181845834-36dec319-5e6f-4531-bc50-af0037e61c9a.gif)

<img width="598" alt="image" src="https://user-images.githubusercontent.com/25105806/181845973-4e02e479-23da-4334-b569-6bc5a7a58b7e.png">


Leetcode link: https://leetcode.com/problems/insertion-sort-list/

<br />

### Approach 1: insertionSortList()

The solution is very straight-forward, we just pick a node, find its inserting place using a loop and move it. However, we should NOT treat the linked list as a vector or standard list because the singly linked list does not allow visiting back, which means we will lose track of 'next node to be sorted' after we've moved the nodes back and forth right in the original `head` linked list. Instead, we create a new head and connect nodes to the new linked list. Since we will disconnect node from `head` and connect it to `newHead`, we did not use any new space except for the dummy new head. 


The steps are:
1. Create a new head `sentinel`
2. Pick a node from the beginning of original linked list
3. Find the inserting place of the node in the new head linked list
4. Disconnect the node from original linked list and connect it to new linked list
5. Repeat until all nodes are moved to new linked list


Full code:

```cpp
ListNode* insertionSortList(ListNode* head) {
    ListNode* sentinel = new ListNode(0);

    // we will move nodes from head list to newHead list
    ListNode* cur = head;
    ListNode* nxt = cur->next;
    ListNode* insert;
    ListNode* insertNext;
    while (cur) {
        nxt = cur->next; // mark next node to be sorted

        // find correct inserting place
        insert = sentinel;
        while (insert->next && cur->val >= insert->next->val) {
            insert = insert->next;
        }

        // move cur node to newHead list
        insertNext = insert->next;
        insert->next = cur; // insert cur in between insert and insertNext
        cur->next = insertNext;

        // sort next node
        cur = nxt;
    }

    return sentinel->next;
}
```

Time complexity is O(n^2) and space complexity is O(1):

<img width="654" alt="image" src="https://user-images.githubusercontent.com/25105806/181847134-4e001745-de51-42a4-942c-969592d35c6a.png">
