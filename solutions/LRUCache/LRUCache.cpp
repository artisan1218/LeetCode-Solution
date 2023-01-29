#include <algorithm> // for find()
#include <deque>
#include <iostream>
#include <unordered_map>
#include <vector>
using namespace std;

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

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */
int main() {
    LRUCache* lRUCache = new LRUCache(2);
    lRUCache->put(1, 1);            // cache is {1=1}
    lRUCache->put(2, 2);            // cache is {1=1, 2=2}
    int result1 = lRUCache->get(1); // return 1
    cout << "Expect 1, " << result1 << endl;
    lRUCache->put(3, 3);            // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
    int result2 = lRUCache->get(2); // returns -1 (not found)
    cout << "Expect -1, " << result2 << endl;
    lRUCache->put(4, 4);            // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
    int result3 = lRUCache->get(1); // return -1 (not found)
    cout << "Expect -1, " << result3 << endl;
    int result4 = lRUCache->get(3); // return 3
    cout << "Expect 3, " << result4 << endl;
    int result5 = lRUCache->get(4); // return 4
    cout << "Expect 4, " << result5 << endl;
    return 0;
}