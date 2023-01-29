#include <iostream>
#include <unordered_map>

using namespace std;

// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;

    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};

class Solution {
public:
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

    // https://leetcode.com/problems/copy-list-with-random-pointer/discuss/43491/A-solution-with-constant-space-complexity-O(1)-and-linear-time-complexity-O(N)
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

    // https://leetcode.com/problems/copy-list-with-random-pointer/discuss/811151/Extremely-simple-solution-using-C%2B%2B
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
};

int main() {
    int nextAry[] = {7, 13, 11, 10, 1};
    int randomAry[] = {-1, 0, 4, 2, 0};

    unordered_map<int, Node*> map;
    Node* oriHead = new Node(-1);
    Node* oriCur = oriHead;

    // construct the linked list - 'next' field
    for (int i = 0; i < sizeof(nextAry) / sizeof(nextAry[0]); i++) {
        oriCur->next = new Node(nextAry[i]);
        oriCur = oriCur->next;
        map[i] = oriCur;
    }

    // construct the linked list - 'random' field
    Node* oriRandom;
    for (int i = 0; i < sizeof(randomAry) / sizeof(randomAry[0]); i++) {
        oriRandom = map[i];
        if (randomAry[i] != -1) {
            oriRandom->random = map[randomAry[i]];
        } else {
            oriRandom->random = nullptr;
        }
    }

    // test the constructed linked list
    Node* test = oriHead->next;
    while (test != nullptr) {
        cout << test->val << " ";
        test = test->next;
    }
    cout << endl;

    test = oriHead->next;
    while (test != nullptr) {
        if (test->random == nullptr) {
            cout << "NULL ";
        } else {
            cout << test->random->val << " ";
        }
        test = test->next;
    }
    cout << endl;

    // solution
    Solution solver;
    Node* copy = solver.copyRandomListMap2(oriHead->next);
    return 0;
}