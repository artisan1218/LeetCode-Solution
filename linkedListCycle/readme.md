# Linked List Cycle problem
<img width="852" alt="image" src="https://user-images.githubusercontent.com/25105806/173220866-68df99c7-9890-40ae-ba34-24ebf97049c5.png">


Leetcode link: https://leetcode.com/problems/linked-list-cycle/

<br />

### Approach 1: Cache with Set, hasCycleSet()

In this solution, we use a hash set to store all seen nodes so that we can quickly know when we encounter a seen node in the cycle.

```cpp
bool hasCycleSet(ListNode* head) {
    unordered_set<ListNode*> set;
    while (head != nullptr) {
        if (set.count(head)) {
            return true;
        } else {
            set.insert(head);
            head = head->next;
        }
    }
    return false;
}
```

Time complexity is O(n) and space complexity is O(n):\
<img width="668" alt="image" src="https://user-images.githubusercontent.com/25105806/173220929-97fb3360-844e-4adf-ac0d-76cb40c5e745.png">


<br />

### Approach 2: Constant Space, hasCycleConstantSpace()

Credits to: https://leetcode.com/problems/linked-list-cycle/discuss/44489/O(1)-Space-Solution

The idea can be explained by an example:\
Imagine two runners are running around a cycle palyground and they start at same position same time, but one of the runner is faster than the other runner. Then we know that at some point at the playground, the faster runner is bound to outrun the slower runner the whole cycle. 


We can apply the idea to this problem by setting up two pointers, one `fast` and one `slow`. They will start at the same node (both point to `head`) and we will use a loop to simulate the running process. The `slow` pointer will only move one node further in each iteration but the `fast` pointer will move two nodes further. We can consider the difference in steps as their speed. If there is a cycle in the given linkedlist then they are bound to meet at some point. 

In fact the speed of the `fast` pointer does not matter as long as it moves faster then the `slow` pointer. 


```cpp
bool hasCycleConstantSpace(ListNode* head) {
    ListNode* slow = head;
    ListNode* fast = head;
    while (fast != NULL && fast->next != NULL) {
        slow = slow->next;
        // it does not matter how fast pointer move, as long as it moves
        // faster than slow pointer, they are guaranteed to meet at some
        // point if the cycle exists
        // we can also move three nodes once instead of two nodes, which will be
        // fast->next->next->next, but also need to update while condition
        fast = fast->next->next;
        if (slow == fast) {
            return true;
        }
    }
    return false;
}
```


Time complexity is O(n) and space complexity is O(1):\
<img width="631" alt="image" src="https://user-images.githubusercontent.com/25105806/173221218-91343472-12de-4cd0-bf7f-6da5f0bd6a92.png">

