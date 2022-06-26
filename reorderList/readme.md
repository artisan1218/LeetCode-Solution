# Reorder List problem
![image](https://user-images.githubusercontent.com/25105806/175793639-9e89ebcd-799c-4a7d-85c7-01ad49c450e6.png)


Leetcode link: https://leetcode.com/problems/reorder-list/

<br />

### Approach 1: Vector, reorderListVector()
The idea is to store all pointers to each node to a linear container(vector) and reconnect them to the correct node. This way we will have access to each node by the index.

```cpp
void reorderListVector(ListNode* head) {
    vector<ListNode*> vec;
    int length = 0;
    ListNode* cur = head;
    while (cur != nullptr) {
        vec.push_back(cur);
        cur = cur->next;
        length++;
    }

    int left = 0;
    int right = length - 1;
    for (int i = 0; i < length / 2; i++) {
        vec.at(left)->next = vec.at(right);
        left++;
        vec.at(right)->next = vec.at(left);
        right--;
    }
    vec.at(left)->next = nullptr;
}
```
Time complexity is O(n) and space complexity is O(n):
![image](https://user-images.githubusercontent.com/25105806/175793699-b277dd6e-e796-41a5-8c2a-04c0538e3913.png)

<br />

### Approach 2: Stack, reorderListStack()
Credits to: https://leetcode.com/problems/reorder-list/discuss/802119/C%2B%2B-really-simple-solution-using-stack-with-explanations

This is similar to approach #1, instead of using vector, we can use stack. We first add all nodes to the stack and pop them so that the node will be in reverse order. The stack will reverse the rigth half of the linked list for us, so we only need to connect them.

```cpp
void reorderListStack(ListNode* head) {
    stack<ListNode*> s;
    auto* cur = head;
    int size = 0;
    while (cur != nullptr) {
        size++;
        s.push(cur);
        cur = cur->next;
    }

    cur = head;
    auto* curNext = head;
    for (int i = 0; i < size / 2; i++) {
        curNext = cur->next;
        cur->next = s.top();
        s.pop();
        cur = cur->next;
        cur->next = curNext;
        cur = cur->next;
    }
    cur->next = nullptr;
}
```

Time complexity is O(n) and space complexity is O(n):
![image](https://user-images.githubusercontent.com/25105806/175793965-a6fa45aa-a801-4b10-954c-9c85c34dcd82.png)


<br />

### Approach 3: Constant Space, reorderListConstantSpace()
The idea is based on the second approach. We noticed that the final linked list is formed by three steps:
1. Find the middle point of the linked list and disconnect left and right part.

    To find the middle point of the linked list, we can use two pointers(`fast` and `slow`). The `fast` pointer will always travel twice as fast as the `slow` pointer, so by the time `fast` reaches the end of linked list, `slow` is guaranteed to be at the middle point.

2. Reverse the right part.

    We can do this in O(1) space. We need to keep two pointers `pre` and `next` where `pre` is used to mark the previous node of the current node, so that we can reverse the pointer and `next` is to mark the next node of the current node, so that we don't lose access to the remaining linked list after reversing current node.

3. Connect left and right part alternatively. For example if left part is `1->2->3` and right part is `6->5->4`, the result will be `1->6->2->5->3->4`.


Full code:
```cpp
void reorderListConstantSpace(ListNode* head) {
    // find the middle point
    auto* left = head;
    auto* slow = head;
    auto* fast = head;
    while (fast->next != nullptr && fast->next->next != nullptr) {
        slow = slow->next;
        fast = fast->next->next;
    }
    auto* right = slow->next;
    slow->next = nullptr; // disconnect the left and right part

    // reverse the right part
    auto* cur = right;
    auto* curNext = right;
    ListNode* pre = nullptr;
    while (cur != nullptr) {
        curNext = cur->next;
        cur->next = pre;
        pre = cur;
        cur = curNext;
    }
    right = pre;

    // reconnect both parts alternatively
    cur = head;
    while (left != nullptr && right != nullptr) {
        left = left->next;
        cur->next = right;
        cur = cur->next;
        right = right->next;
        cur->next = left;
        cur = cur->next;
    }
}
```

Time complexity is O(n) and space complexity is O(1):
![image](https://user-images.githubusercontent.com/25105806/175793977-6552021c-01e0-4d92-ba67-adbf37ffded3.png)


<br />

### Approach 4: Recursion, reorderListRecursion()
Credits to: 
1. https://leetcode.cn/problems/reorder-list/solution/xiang-xi-tong-su-de-si-lu-fen-xi-duo-jie-fa-by-34/ 
2. https://leetcode.com/problems/reorder-list/discuss/45113/Share-a-consise-recursive-solution-in-C%2B%2B

This solution is a little bit tricky compared to previous solutions. Steps:

1. Connect the head node with tail node. This is equivalent to `i -> n`
2. Then connect tail node with 'subHead' node, which is the next node of head node, so this is equivalent to `n -> i+1`
3. Repeat the process recursively on the inner nodes (`i+1` to `n-1`)

Note that the resursion function needs to return the `tail->next` node to previous callstack, so that we can get the pointer to it and then connect it with head node. 

We will control the recursive call by using the length of linked list. Every time we will move head pointer to next and minus length by 2. So that we will end up at the middle point of the linked list.
There two two bases cases:
1. If the length of the linked list is even, then we will have a linked list with length of 2 at them middle point. Therefore we need to set `head->next->next` to `null`.
2. If the length of the linked list is odd, then we will have a linked list with length of 1 (a single node) at them middle point. Therefore we need to set `head->next` to `null`.

Full code:
```cpp
void reorderListRecursion(ListNode* head) {
    // get length
    auto* cur = head;
    int length = 0;
    while (cur != nullptr) {
        length++;
        cur = cur->next;
    }
    helper(head, length);
}

ListNode* helper(ListNode* head, int length) {
    if (length == 1) { // base case
        ListNode* outTail = head->next;
        head->next = nullptr;
        return outTail;
    } else if (length == 2) { // base case
        ListNode* outTail = head->next->next;
        head->next->next = nullptr;
        return outTail;
    } else {
        auto* tail = helper(head->next, length - 2); // -2 per stack is to find the middle node
        auto* subHead = head->next;
        head->next = tail; // connect i node and n-i node
        auto* outTail = tail->next;
        tail->next = subHead; // connect n-i node and i+1 node
        return outTail;
    }
}
```

Time complexity is O(n) and space complexity is O(n^2), which is the memory size for the entire call stack:
```
Callstack1: 1 2 3 4 5 6 7
Callstack2:   2 3 4 5 6
Callstack3:     3 4 5
Callstack4:       4
```

![image](https://user-images.githubusercontent.com/25105806/175794281-07273941-d606-4044-8952-b031ad68a8e0.png)
