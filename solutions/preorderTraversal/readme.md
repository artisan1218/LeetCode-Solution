# Binary Tree Preorder Traversal problem
![image](https://user-images.githubusercontent.com/25105806/176317253-642e17fd-7a51-4d9e-a557-c63508d62f0f.png)

Leetcode link: https://leetcode.com/problems/binary-tree-preorder-traversal/

<br />

### Approach 1: Recursion, preorderTraversalRecursion()

Standard way of doing pre-order traversal. By adjusting the order of recursive call, we can achieve pre-order, in-order or post-order traversal.

```cpp
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
```

Time complexity is O(n) and space complexity is O(n), which is the callstack:
![image](https://user-images.githubusercontent.com/25105806/176317458-a20dc590-f95d-4cb8-93ff-6779a0c95d0b.png)

<br />

### Approach 2: Stack, preorderTraversalStack()

The point of using recursion is that we can come back(previous callstack) when we've visited all nodes in current subtree because the callstack will 'remember' the position of previous level subtree. Instead of using recursion, we can also use stack to 'remember' the position so that we can come back to the previous subtree.

Notice that we will always push and store the root's value first, then push its right subtree and left subtree. So when popping them, left subtree will be popped out first. Then we will push its right and left subtree(This is similar to the recursive call, we just use stack to simulate the callstack).

```cpp
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
```

Time complexity is O(n) and space complexity is O(n):
![image](https://user-images.githubusercontent.com/25105806/176317647-b94c37b7-1d7e-4913-b089-f4b2ad9a00cc.png)

<br />

### Approach 3: Morris Traversal, preorderTraversalMorris()

Credits to: 
1. https://www.youtube.com/watch?v=wGXB9OWhPTg
2. https://leetcode.com/problems/binary-tree-preorder-traversal/discuss/45466/C%2B%2B-Iterative-Recursive-and-Morris-Traversal

The previous two solutions both uses O(n) space, the reason is that we have to be able to come back to previous(parent) subtree after we've visited all nodes in current subtree. If we look at the structure of the binary tree, there is no way to come back from lower level to higher level. So if we can build connections from lower subtree to higher subtree, then we can 'come back', which means we can save the O(n) space by just using O(1) space.

The path we will build is from the `predecessor` of a root to `root`. The `predecessor` is the right-most node in the left subtree of a root:
```cpp
auto* pre = root->left;
while (pre->right != nullptr && pre->right != root) {
    pre = pre->right;
}
```

For example, the image below shows the path we built in red dash line:

<img src="https://user-images.githubusercontent.com/25105806/176319034-4429bb00-fa4d-4855-a878-649a51320d94.jpg" width="40%" height="40%">


`pre` is the predecessor of tree `root` and `pre'` is the predecessor of tree `root'`. With the paths, we can come back from a subtree to root, then simply remove the connection to restore its original structure.

Full code:
```cpp
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
```

Time complexity is O(n) and space complexity is O(1):
![image](https://user-images.githubusercontent.com/25105806/176319413-11a207dd-4fd1-48c1-96ce-eb5327b0ee87.png)
