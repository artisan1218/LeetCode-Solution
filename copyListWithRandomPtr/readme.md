# Convert Sorted List to Binary Search Tree problem
![image](https://user-images.githubusercontent.com/25105806/170204331-331637cb-a3b7-4159-b7d7-c263e38bbd18.png)

Leetcode link: [https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/](https://leetcode.com/problems/copy-list-with-random-pointer/)

<br />

### Approach 1: Map, copyRandomListMap()
This is the naive solution where we simply read the original linked list, create a copy of the original linked list with 'next' pointer then use a map to store the projection relation from the original node to copied node, which will be used to reconstruct the 'random' pointer. We use map to store the relation because when we go through the original linked list, we may encounter the case that the random pointer of the current node points to a node that we haven't met yet. In this case, there is no way connect the random pointer of the copied node. 

```cpp
Node* copyRandomListMap(Node* head) {
    unordered_map<Node*, Node*> map;
    Node* copyHead = new Node(-1);
    Node* copyCur = copyHead;

    Node* oriCur = head;
    while (oriCur != NULL) {
        copyCur->next = new Node(oriCur->val);
        copyCur = copyCur->next;
        map[oriCur] = copyCur;
        oriCur = oriCur->next;
    }

    oriCur = head;
    Node* copyRandom = copyHead;
    while (oriCur != NULL) {
        if (oriCur->random != NULL) {
            copyRandom->next->random = map[oriCur->random];
        } else {
            copyRandom->next->random = nullptr;
        }
        copyRandom = copyRandom->next;
        oriCur = oriCur->next;
    }

    return copyHead->next;
}
```

Time complexity is O(n) and space complexity is O(n):\
![image](https://user-images.githubusercontent.com/25105806/170205205-f92aa80d-1826-491f-bfbe-2e7fe0401066.png)

<br />


### Approach 2: Modify Original Linked List, copyRandomListModifyOri()
Credits to: https://leetcode.com/problems/copy-list-with-random-pointer/discuss/43491/A-solution-with-constant-space-complexity-O(1)-and-linear-time-complexity-O(N)

Regardless of how to approach this question, we have to find a way to store the relationship between the original node to copied node because of the unordered 'random' pointer.

The ides of this solution is to modify the original linked list, insert the copied node right after the original node. This way, we are guaranteed that the corresponding random node is right after the original node. Then simply connect them one by one and finally disconnect the copied linked list from original linked list.

<img src="https://user-images.githubusercontent.com/25105806/170206163-42672a34-cedb-4327-b91a-fcb69890f4e3.jpg" heigth="70%" width="70%">


In this solution, we store the relation between original node and copied node by inserting the copied node right in the original linked list in a certain order. Therefore, we can get rid of the map (also reduce the space complexity down to O(1))

```cpp
Node* copyRandomListModifyOri(Node* head) {
    if (head == NULL) {
        return head;
    } else {
        // step 1: create new nodes and append new node right after original node
        Node* oriCur = head;
        Node* oriNext = head;
        while (oriCur != NULL) {
            oriNext = oriCur->next;               // mark the connecting node for the new node
            oriCur->next = new Node(oriCur->val); // connect original node to new node
            oriCur = oriCur->next;
            oriCur->next = oriNext; // connect new node to the original linked list
            oriCur = oriNext;
        }

        // step 2: connect 'random' pointer
        oriCur = head;
        while (oriCur != NULL) {
            if (oriCur->random != NULL) {
                oriCur->next->random = oriCur->random->next;
            }
            oriCur = oriCur->next->next;
        }

        // step 3: disconnect copied linked list from original linked list
        oriCur = head;
        Node* copyCur = head->next;
        Node* result = head->next; // return this
        while (copyCur->next != NULL) {
            // connect current original node to next original node
            oriCur->next = copyCur->next;
            oriCur = oriCur->next;
            // connect current copied node to next copied node
            copyCur->next = oriCur->next;
            copyCur = copyCur->next;
        }
        oriCur->next = nullptr; // disconnect the last pair of original/copy node

        return result;
    }
}
```

Time complexity is O(n) and space complexity is O(1):\
![image](https://user-images.githubusercontent.com/25105806/170207128-0d47d507-d70f-4306-8bfb-a00c6aa20912.png)
  
<br />

### Approach 3: Map, copyRandomListMap2()
Credits to: https://leetcode.com/problems/copy-list-with-random-pointer/discuss/811151/Extremely-simple-solution-using-C%2B%2B

Another way of using map is to directly use the copied node stored in map without creating a new linked list. The idea is that the newly created nodes are already in the map, we can directly modify the nodes in the map by accessing them with `map[originalNode]`.

```cpp
Node* copyRandomListMap2(Node* head) {
    unordered_map<Node*, Node*> map;
    Node* cur = head;
    // create the "original node to copied node" relation and store it in map
    while (cur != NULL) {
        map[cur] = new Node(cur->val);
        cur = cur->next;
    }

    cur = head;
    while (cur) {
        // use the map to find corresponding nodes
        map[cur]->next = map[cur->next];
        map[cur]->random = map[cur->random];
        cur = cur->next;
    }
    return map[head];
}
```

Time complexity is O(n) and space complexity is O(1):\
![image](https://user-images.githubusercontent.com/25105806/170207842-929ed9c6-bb12-485b-a451-6856fde1f966.png)
