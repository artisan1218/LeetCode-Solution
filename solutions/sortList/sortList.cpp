#include <iostream>

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
    ListNode* sortList(ListNode* head) {
        if (head && head->next) {
            auto* mid = split(head);
            auto* left = sortList(head); // sort the left part
            auto* right = sortList(mid); // sort the right part
            return merge(left, right);
        }
        return head;
    }

    ListNode* merge(ListNode* l1, ListNode* l2) {
        ListNode* sentinel = new ListNode(-1);
        ListNode* cur = sentinel;

        while (l1 && l2) {
            if (l1->val > l2->val) {
                cur->next = l2;
                l2 = l2->next;
            } else {
                cur->next = l1;
                l1 = l1->next;
            }
            cur = cur->next;
        }
        cur->next = l1 ? l1 : l2;
        return sentinel->next;
    }

    ListNode* split(ListNode* head) {
        ListNode* midPrev = nullptr;
        ListNode* fast = head;
        while (fast != nullptr && fast->next != nullptr) {
            fast = fast->next->next;
            if (midPrev == nullptr) {
                midPrev = head; // midPrev is one iteration slower, so it will point to the previous node of middle node
            } else {
                midPrev = midPrev->next;
            }
        }
        auto* mid = midPrev->next;
        midPrev->next = nullptr; // disconnect the left and right part of the linkedlist
        return mid;
    }
};

int main() {
    ListNode* head = new ListNode(-1);
    head->next = new ListNode(5);
    head->next->next = new ListNode(3);
    head->next->next->next = new ListNode(4);
    head->next->next->next->next = new ListNode(0);

    Solution solver;
    ListNode* result = solver.sortList(head);
    while (result != nullptr) {
        std::cout << result->val << " ";
        result = result->next;
    }
    std::cout << std::endl;

    return 0;
}
