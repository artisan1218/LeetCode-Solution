#include <iostream>
#include <unordered_set>

using namespace std;

// Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode* next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
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
};

int main() {
    ListNode* head = new ListNode(3);
    head->next = new ListNode(2);
    head->next->next = new ListNode(0);
    head->next->next->next = new ListNode(-4);
    head->next->next->next->next = head; // cycle
    Solution solver;
    cout << solver.detectCycleConstantSpace(head) << '\n';
    return 0;
}