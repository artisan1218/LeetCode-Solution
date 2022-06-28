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
    vector<int> preorderTraversalRecursion(TreeNode* root) {
        vector<int> result;
        helper(root, result);
        return result;
    }

    void helper(TreeNode* root, vector<int>& result) {
        if (root == nullptr) {
            return;
        } else {
            result.push_back(root->val);
            helper(root->left, result);
            helper(root->right, result);
        }
    }

    vector<int> preorderTraversalStack(TreeNode* root) {
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
                s.push(node->right);
                s.push(node->left);
            }
        }
        return result;
    }

    vector<int> preorderTraversalMorris(TreeNode* root) {
        vector<int> result;
        while (root) {
            if (root->left) {
                // find the predecessor of the root so that we can come back after visiting all left subtree
                auto* pre = root->left;
                while (pre->right != nullptr && pre->right != root) {
                    pre = pre->right;
                }

                if (pre->right == nullptr) {     // build connection between root and pre
                    pre->right = root;           // connection
                    result.push_back(root->val); // visit root
                    root = root->left;           // visit left
                } else {
                    pre->right = nullptr; // restore the original tree by removing the connection we've built
                    root = root->right;   // visit right
                }
            } else {
                result.push_back(root->val); // left is null, we can visit root node
                root = root->right;          // then go to the right / back to root if right is null originally
            }
        }

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
    auto result = solver.preorderTraversalMorris(root);
    for (auto e : result) {
        cout << e << " ";
    }
    cout << "\n";
}