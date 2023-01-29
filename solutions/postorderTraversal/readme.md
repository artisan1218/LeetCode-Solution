# Binary Tree Postorder Traversal problem

![image](https://user-images.githubusercontent.com/25105806/176316021-2cc98e60-5cd1-483b-a65c-4b521de2a220.png)


Leetcode link: https://leetcode.com/problems/binary-tree-postorder-traversal/

<br />

### Approach 1: Recursion, postorderTraversalRecursion()

This is the traditinal standard way of doing pre-order traversal. We will visit `left` and `right` first, then add `root value` to the result.

```cpp
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
```

Time complexity is O(n) and space complexity is also O(n), which is the callstack:
![image](https://user-images.githubusercontent.com/25105806/176316307-59f8995a-17eb-4a01-81b3-d514f117b72a.png)


<br />

### Approach 2: Stack, postorderTraversalStack()
The point of using recursion is that we can come back(previous callstack) when we've visited all nodes in current subtree because the callstack will 'remember' the position of previous level subtree. Instead of using recursion, we can also use stack to 'remember' the position so that we can come back to the previous subtree.

```cpp
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
```

Time complexity is O(n) and space complexity is O(n):
![image](https://user-images.githubusercontent.com/25105806/176316868-f9934700-85e8-4474-a04f-cc97ccd40b1b.png)


<br />

### Approach 2: Stack, postorderTraversalStack2()

There is even a simpler version. We can think of post-order traversal as the reverse of the 'right->left->root'-order traverasl. This way, we can perform the 'right->left->root'-order traversal by just fliping the order of push of pre-order traversal then reverse the final result.

```cpp
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
```

Time complexity is O(n) and space complexity is O(n):
![image](https://user-images.githubusercontent.com/25105806/176317167-bdae198b-2324-42d3-b2ad-8506b01230e7.png)

