# House Robber III problem

<img width="1035" alt="image" src="https://user-images.githubusercontent.com/25105806/181690151-246a41c8-c8fc-498f-bcc2-d2cba7c3b4ea.png">


Leetcode link: https://leetcode.com/problems/house-robber-iii/

<br />

### Approach 1: DFS with Memorization, robDFS()

The idea is to use DFS to explore all possible ways exhaustedly. At any node, we have two choice:
1. Rob the root node and jump to root's grandchildren nodes
2. Do not rob the root and jump to root's children nodes

at the end we simply return the max among these two choices. However, this way of calculation will visit many duplicate nodes and thus increase time complexity. To avoid revisiting, we use memorization technique, which is a map that stores the 'root-value' kv pair.

Full code:
```cpp
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
```

Time complexity is O(n):\
<img width="656" alt="image" src="https://user-images.githubusercontent.com/25105806/181691130-e865c85b-8f1f-4262-8c6c-f37580227fed.png">


<br />



### Approach 2: DFS, robOptimal()

Credits to: https://www.youtube.com/watch?v=nHR8ytpzz7c

We can consider this problem in this way: at any nodes, we can either rob the root or skip the root. We can denote the two choices using a pair, the first value means the value we get by robbing the root and following nodes, the second value means the value we get by not robbing the root and rob the following nodes. We can then calculate the pair node by node recursively.

```
pair<int, int> left = helper(root->left);
pair<int, int> right = helper(root->right);
```

`left` pair includes two values: max value we can get by robbing the `root->left` and max value we can get by not robbing `root->left`. Similar for `right` pair.

Next, we will simply return the paired value of robbing current `root` and not robbing:
```
// if we include the current root, then we should add the 'exclude root' value of next level
int includeRoot = root->val + left.second + right.second;

// if we exclude the current root, then simply choose the max value
int excludeRoot = max(left.first, left.second) + max(right.first, right.second);
```

Full code:
```cpp
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
```
