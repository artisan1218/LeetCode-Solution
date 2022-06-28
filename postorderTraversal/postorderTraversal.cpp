#include <algorithm>
#include <iostream>
#include <stack>
#include <vector>
using namespace std;

// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode* left, TreeNode* right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    vector<int> postorderTraversalRecursion(TreeNode* root) {
        vector<int> result;
        helper(root, result);
        return result;
    }

    void helper(TreeNode* root, vector<int>& result) {
        if (root == nullptr) {
            return;
        } else {
            helper(root->left, result);
            helper(root->right, result);
            result.push_back(root->val);
        }
    }

    vector<int> postorderTraversalStack(TreeNode* root) {
        stack<TreeNode*> s;
        vector<int> result;
        TreeNode* last = nullptr;
        while (root || !s.empty()) {
            if (root) {
                s.push(root);
                root = root->left;
            } else {
                auto* node = s.top();
                if (node->right && node->right != last) {
                    root = node->right; // keep searching for the left node
                } else {
                    result.push_back(node->val);
                    s.pop();
                    last = node;
                }
            }
        }
        return result;
    }

    vector<int> postorderTraversalStack2(TreeNode* root) {
        stack<TreeNode*> s;
        s.push(root);
        vector<int> result;

        while (!s.empty()) {
            auto* node = s.top();
            s.pop();
            if (node != nullptr) {
                result.push_back(node->val);
                // right and left might be nullptr, and being pushed into the stack
                // but we will not store it's val in result because we made sure node!=nullptr
                s.push(node->left);
                s.push(node->right);
            }
        }
        reverse(result.begin(), result.end());
        return result;
    }
};

int main() {
    TreeNode* root = new TreeNode(1);
    root->left = new TreeNode(2);
    root->right = new TreeNode(3);
    root->left->left = new TreeNode(4);
    root->left->right = new TreeNode(5);

    Solution solver;
    auto result = solver.postorderTraversalStack(root);
    for (auto e : result) {
        cout << e << " ";
    }
    cout << "\n";
}