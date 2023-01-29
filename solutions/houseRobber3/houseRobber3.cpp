#include <iostream>
#include <unordered_map>
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
    int robDFS(TreeNode* root) {
        unordered_map<TreeNode*, int> cache;
        return helper(root, cache);
    }

    int helper(TreeNode* root, unordered_map<TreeNode*, int>& cache) {
        if (root == nullptr) {
            return 0;
        } else {
            if (cache.find(root) != cache.end()) {
                return cache[root];
            } else {
                int robRoot = root->val; // rob root
                int skipRoot = 0;        // skip root and rob children

                if (root->left) {
                    robRoot += helper(root->left->left, cache) + helper(root->left->right, cache); // rob grandchildren
                    skipRoot += helper(root->left, cache);                                         // rob children
                }
                if (root->right) {
                    robRoot += helper(root->right->left, cache) + helper(root->right->right, cache); // rob grandchildren
                    skipRoot += helper(root->right, cache);                                          // rob children
                }

                cache[root] = max(robRoot, skipRoot);
                return cache[root];
            }
        }
    }

    // https://www.youtube.com/watch?v=nHR8ytpzz7c
    int robOptimal(TreeNode* root) {
        auto [includeRoot, excludeRoot] = helper(root);
        return max(includeRoot, excludeRoot);
    }

    pair<int, int> helper(TreeNode* root) {
        if (!root) {
            return {0, 0};
        } else {
            auto left = helper(root->left);
            auto right = helper(root->right);

            // if we include the current root, then we should add the 'exclude root' value of next level
            int includeRoot = root->val + left.second + right.second;

            // if we exclude the current root, then simply choose the max value
            int excludeRoot = max(left.first, left.second) + max(right.first, right.second);

            return {includeRoot, excludeRoot};
        }
    }
};

int main() {
    Solution solver;
    TreeNode* root = new TreeNode(3);
    root->left = new TreeNode(4);
    root->right = new TreeNode(5);
    root->left->left = new TreeNode(1);
    root->left->right = new TreeNode(3);
    root->right->right = new TreeNode(1);

    cout << solver.robOptimal(root) << endl;
    return 0;
}