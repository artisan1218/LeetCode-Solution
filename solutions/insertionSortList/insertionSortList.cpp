#include <iostream>
using namespace std;

// Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode* next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode* next) : val(x), next(next) {}
};

class Solution {
public:
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
};

int main() {
    Solution solver;

    ListNode* head = new ListNode(4);
    head->next = new ListNode(2);
    head->next->next = new ListNode(1);
    head->next->next->next = new ListNode(3);

    auto* result = solver.insertionSortList(head);
    auto* it = result;
    while (it != nullptr) {
        cout << it->val << " ";
        it = it->next;
    }
    cout << endl;

    return 0;
}