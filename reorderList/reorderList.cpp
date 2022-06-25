#include <iostream>
#include <stack>
#include <unordered_map>
#include <vector>
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
};

int main() {
    ListNode* head = new ListNode(1);
    head->next = new ListNode(2);
    head->next->next = new ListNode(3);
    head->next->next->next = new ListNode(4);
    head->next->next->next->next = new ListNode(5);

    Solution solver;
    solver.reorderListRecursion(head);

    while (head != nullptr) {
        cout << head->val << " ";
        head = head->next;
    }
    cout << endl;

    return 0;
}