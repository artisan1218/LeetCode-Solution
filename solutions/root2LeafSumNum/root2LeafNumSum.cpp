#include <iostream>
using namespace std;

// Definition for a binary tree node.
struct TreeNode{
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution{
    int result = 0; 
public:
    int sumNumbers(TreeNode *root){
        dfs(root, 0);
        return result;
    }

    void dfs(TreeNode *root, int numSoFar){
        if (root != NULL){
            numSoFar = numSoFar * 10 + root->val;
            if (root->left == NULL && root->right == NULL){
                result += numSoFar;
            }
            dfs(root->left, numSoFar);
            dfs(root->right, numSoFar);
        }
    }
};

int main(){
    TreeNode *root = new TreeNode(4);
    root->left = new TreeNode(9);
    root->right = new TreeNode(5);
    root->left->left = new TreeNode(1);

    Solution solver;
    int result = solver.sumNumbers(root);
    cout << result;
    return 0;
}