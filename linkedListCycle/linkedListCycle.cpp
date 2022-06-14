#include <exception>
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
};

int main() {
    ListNode* head = new ListNode(3);
    head->next = new ListNode(2);
    head->next->next = new ListNode(0);
    head->next->next->next = new ListNode(-4);
    head->next->next->next->next = head; // cycle
    Solution solver;
    cout << solver.hasCycleConstantSpace(head) << '\n';
    return 0;
}