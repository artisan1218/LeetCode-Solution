# Linked List Cycle II problem
![image](https://user-images.githubusercontent.com/25105806/174423541-71ba9736-96b5-4ae2-8bbb-d557021ddd5b.png)


Leetcode link: https://leetcode.com/problems/linked-list-cycle-ii/

<br />

### Approach 1: HashSet, detectCycleSet()

This solution is to use a hash set to store all seen nodes so that we can know immediately if an new node has been seen before and therefore return the node.

```cpp
ListNode* detectCycleSet(ListNode* head) {
    auto ptr = head;
    unordered_set<ListNode*> set;
    while (ptr != nullptr) {
        if (set.find(ptr) != set.end()) {
            return ptr;
        }
        set.insert(ptr);
        ptr = ptr->next;
    }
    return NULL;
}
```

Time complexity is O(n) and space complexity is O(n):\
![image](https://user-images.githubusercontent.com/25105806/174423581-e57bf3ec-16ef-4514-b77c-a9277c4c3973.png)

<br />

### Approach 2: Constant Space Using Pointers, detectCycleConstantSpace()
Credits to: https://leetcode.com/problems/linked-list-cycle-ii/discuss/44781/Concise-O(n)-solution-by-using-C%2B%2B-with-Detailed-Alogrithm-Description

The solution is based on [linkedListCycle](https://github.com/artisan1218/LeetCode-Solution/tree/main/linkedListCycle) problem where we only need to detect the existence of cycle. After we've found out that there is a cycle in the linked list, our `fast` and `slow` pointers will meet at a same node inside the cycle. 

For example, the image below shows the state after `slow` and `fast` meet at node `M`
![1655529151381](https://user-images.githubusercontent.com/25105806/174423816-670abf48-3e46-4863-98ee-4941647ac821.png)

From this point, the trick begins:
We can denote the path that `slow` pointer traveled as `Dslow` and the path that `fast` pointer traveled as `Dfast`. Notice that every time `slow` pointer moves one step forward, `fast` pointer will move two steps forward. So the length of `Dfast`, at any given point, is always twice as the length of `Dslow`. If we assume `Dslow = x`, then `Dfast = 2x`. 

We also noticed that at node `M`, `slow` pointer traveled exact `x` steps and `fast` pointer traveled exact `2x` steps, which means if `slow` keeps traveling along the linked list for another `x` steps, `slow` will end up at the node `M` again. So if we set up another pointer called `entry` that starts at `head` and let `slow` and `entry` walks along the linked list simultaneously, they will end up meeting at one node and that's the entry node of the cycle. 

The path that `entry` walked would be red + yellow and the path that `slow` walked would be blue + yellow. Since we know both paths are of length `x` and they share a same part of the path (yellow), we know red = blue, so they are guranteed to meet and the first time they meet is the entry node to the cycle.


```cpp
ListNode* detectCycleConstantSpace(ListNode* head) {
    auto slow = head;
    auto fast = head;
    auto entry = head;
    while (fast != nullptr && fast->next != nullptr) {
        slow = slow->next;
        fast = fast->next->next;
        if (slow == fast) {
            while (slow != entry) {
                slow = slow->next;
                entry = entry->next;
            }
            return entry;
        }
    }
    return NULL;
}
```

Time complexity is O(n) and space complexity is O(1):\
![image](https://user-images.githubusercontent.com/25105806/174424144-08c81736-bda4-473c-890f-b4bfb7b37a43.png)

