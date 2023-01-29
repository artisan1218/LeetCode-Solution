# Sort List problem
![image](https://user-images.githubusercontent.com/25105806/192935105-81db4bc2-d738-4f40-a840-abd42bb17162.png)

Leetcode link: https://leetcode.com/problems/sort-list/

<br />

### Approach 1: Merge Sort, Divide and Conquer, sortList(), merge(), split()
Credit to: https://leetcode.com/problems/sort-list/solution/

The algorithm is a standard divide and conquer logic. If we treat the linked list as a list, we can split the list in halves recursively: left and right, and when we cannot split the sub-list anymore, we merge them back. The actual sorting happens in the `merge` function where we put smaller node at the front. Since every merged sub-list is sorted, when we merge two sub-lists, we only need to compare the front two nodes. 

```cpp
ListNode* sortList(ListNode* head) {
    if (head && head->next) {
        auto* mid = split(head);
        auto* left = sortList(head); // sort the left part
        auto* right = sortList(mid); // sort the right part
        return merge(left, right);
    }
    return head;
}

ListNode* merge(ListNode* l1, ListNode* l2) {
    ListNode* sentinel = new ListNode(-1);
    ListNode* cur = sentinel;

    while (l1 && l2) {
        if (l1->val > l2->val) {
            cur->next = l2;
            l2 = l2->next;
        } else {
            cur->next = l1;
            l1 = l1->next;
        }
        cur = cur->next;
    }
    cur->next = l1 ? l1 : l2;
    return sentinel->next;
}

ListNode* split(ListNode* head) {
    ListNode* midPrev = nullptr;
    ListNode* fast = head;
    while (fast != nullptr && fast->next != nullptr) {
        fast = fast->next->next;
        if (midPrev == nullptr) {
            midPrev = head; // midPrev is one iteration slower, so it will point to the previous node of middle node
        } else {
            midPrev = midPrev->next;
        }
    }
    auto* mid = midPrev->next;
    midPrev->next = nullptr; // disconnect the left and right part of the linkedlist
    return mid;
}
```

Time complexity is O(nlogn) and space complexity is O(nlogn):

![image](https://user-images.githubusercontent.com/25105806/192936355-8d0f6532-ca84-4483-85e9-6934ee03723f.png)
