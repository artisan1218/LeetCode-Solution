# LRU Cache problem
<img width="963" alt="image" src="https://user-images.githubusercontent.com/25105806/165434139-e52f2b54-df4f-4987-bbcf-f0340ccba08c.png">

Leetcode link: https://leetcode.com/problems/lru-cache/

<br/>

### Approach 1: Naive, LRUCacheNaive
The first thing we need to make clear of is the concept of LRU, it stands for the least recently used item, not the least used(count). To put another word, every `.get()` and `.put()` transaction will use an item by key, we want the item with least used record in terms of transactions.

To achieve this, we can use an map to store the `key, value` pair and a `deque` to store the LRU logic. Everytime we access an item, we will move that item in the `deque` to the back, which means the most recently used item, so item on the left will be LRU item.

```cpp
class LRUCacheNaive {
public:
    int cap;
    unordered_map<int, int> map;
    deque<int> dq;

    LRUCacheNaive(int capacity) {
        cap = capacity;
    }

    int get(int key) {
        if (map.find(key) != map.end()) {
            // update vec, move key to right
            dq.erase(find(dq.begin(), dq.end(), key));
            dq.push_back(key);
            return map[key];
        } else {
            return -1;
        }
    }

    void put(int key, int value) {
        if (map.find(key) != map.end()) {
            map[key] = value;
            dq.erase(find(dq.begin(), dq.end(), key));
            dq.push_back(key);
        } else {
            map[key] = value;
            dq.push_back(key);
        }

        if (map.size() > cap) {
            map.erase(dq.front());
            dq.pop_front();
        }
    }
};
```

Time complexity for `.put()` and `.get()` will be O(n) because `.erase()` is O(n). This will lead to TLE.

<br />

### Approach 1: Optimal Solution, LRUCache
Credits to: https://www.youtube.com/watch?v=7ABFKPK2hD4

The idea is to use a hashmap to store the `key, Node` pair, and instead of using `deque` to store the LRU logic, we'll use a doubly linked list. 

We will first contruct a class called `Node`, it will be the unit in a doubly linked list. At the begining, we will have two dummy nodes on the left and right of linked list, where left node is called `LRU_dummy` and it always points to LRU item, and the right node is called `MRU_dummy` and it always points to MRU item. 

We will update the linked list by removing old nodes and inserting new nodes on the right end to make sure these two pointers always point to the correct node. 

```cpp
class LRUCache {
public:
    struct Node {
    public:
        int key;
        int val;
        Node* prev;
        Node* next;

        Node(int _key, int _val) {
            key = _key;
            val = _val;
            prev = nullptr;
            next = nullptr;
        }
    };
    int cap;
    unordered_map<int, Node*> map;
    Node* LRU_dummy;
    Node* MRU_dummy;

    LRUCache(int capacity) {
        cap = capacity;
        LRU_dummy = new Node(0, 0); // dummy, least recently used
        MRU_dummy = new Node(0, 0); // dummy, most recently used

        // connect left and right dummy
        LRU_dummy->next = MRU_dummy;
        MRU_dummy->prev = LRU_dummy;
    }

    // remove from the linked list
    void remove(Node* node) {
        Node* prev = node->prev;
        Node* next = node->next;

        prev->next = next;
        next->prev = prev;
    }

    // insert new node to the right of the linked list, which means MRU
    void insert(Node* node) {
        Node* prev = MRU_dummy->prev;

        prev->next = node;
        MRU_dummy->prev = node;

        node->next = MRU_dummy;
        node->prev = prev;
    }

    int get(int key) {
        if (map.find(key) != map.end()) {
            // mark key as MRU, equivalent to move key to the right
            remove(map[key]);
            insert(map[key]);
            return map[key]->val;
        } else {
            return -1;
        }
    }

    void put(int key, int value) {
        if (map.find(key) != map.end()) {
            remove(map[key]); // remove the old node
        }
        map[key] = new Node(key, value); // add new node
        insert(map[key]);                // add a new node to the doubly linked list and move it to the right, MRU

        if (map.size() > cap) {
            // remove LRU from linkedlist and erase LRU from map
            Node* lru = LRU_dummy->next;
            remove(lru);
            map.erase(lru->key);
        }
    }
};
```


Time complexity for `.put()` and `.get()` is O(1) because we can always get the node by a hashmap, which will return the node given key in O(1), and updating the linked list is simply some operations on the pointers, which will also take only O(1):
<img width="626" alt="image" src="https://user-images.githubusercontent.com/25105806/165435517-d31a7a88-abc9-4bfd-9a84-c96524c3e935.png">
