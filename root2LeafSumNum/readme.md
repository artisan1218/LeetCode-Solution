# Sum Root to Leaf Numbers problem
![image](https://user-images.githubusercontent.com/25105806/160010961-fe350e36-7c85-48d7-9f87-6b3f704dbe20.png)

Leetcode link: https://leetcode.com/problems/sum-root-to-leaf-numbers/

<br />

### Approach 1: DFS, sumNumbers()
The idea is fairly straight-forward, we simply traverse the entire tree using DFS, because we need to keep track of the path from root to leaf. The path from root to leaf is exactly what DFS does. Then for each new node value we meet, we multiply the old number by 10 and add the new value to form the new number until we've reached the leaf.

Python3 implementation:
```python3
def sumNumbers(self, root: Optional[TreeNode]) -> int:
    self.result = 0
    def dfs(root, numSoFar):
        #nonlocal result
        numSoFar = numSoFar * 10 + root.val
        if root.left is not None:
            dfs(root.left, numSoFar)
        if root.right is not None:
            dfs(root.right, numSoFar)

        if root.left is None and root.right is None:
            self.result += numSoFar
    dfs(root, 0)
    return self.result
```

C++ implementation:
```cpp
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
```

Time complexity is O(n):\
![aaea0f32fa8c0364485447b896bf2b4](https://user-images.githubusercontent.com/25105806/160011388-7ae7086e-3bcb-427f-a451-cebe096917f7.png)
![image](https://user-images.githubusercontent.com/25105806/160226413-faeef38f-c5be-4c08-a073-a033938b6333.png)

