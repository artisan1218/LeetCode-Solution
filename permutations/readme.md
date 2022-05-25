# Permutations problem
* Given an array `nums` of distinct integers, return all the possible permutations. You can return the answer in any order.

Leetcode link: https://leetcode.com/problems/permutations/

<br />

### Approach 1: DFS, permute(), Python3
The idea is simple, we will see the problem as a tree structure. We solve this using recursion:

```
dfs(nums = [1, 2, 3] , path = [] , result = [] )
|____ dfs(nums = [2, 3] , path = [1] , result = [] )
|      |___dfs(nums = [3] , path = [1, 2] , result = [] )
|      |    |___dfs(nums = [] , path = [1, 2, 3] , result = [[1, 2, 3]] ) # added a new permutation to the result
|      |___dfs(nums = [2] , path = [1, 3] , result = [[1, 2, 3]] )
|           |___dfs(nums = [] , path = [1, 3, 2] , result = [[1, 2, 3], [1, 3, 2]] ) # added a new permutation to the result
|____ dfs(nums = [1, 3] , path = [2] , result = [[1, 2, 3], [1, 3, 2]] )
|      |___dfs(nums = [3] , path = [2, 1] , result = [[1, 2, 3], [1, 3, 2]] )
|      |    |___dfs(nums = [] , path = [2, 1, 3] , result = [[1, 2, 3], [1, 3, 2], [2, 1, 3]] ) # added a new permutation to the result
|      |___dfs(nums = [1] , path = [2, 3] , result = [[1, 2, 3], [1, 3, 2], [2, 1, 3]] )
|           |___dfs(nums = [] , path = [2, 3, 1] , result = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1]] ) # added a new permutation to the result
|____ dfs(nums = [1, 2] , path = [3] , result = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1]] )
       |___dfs(nums = [2] , path = [3, 1] , result = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1]] )
       |    |___dfs(nums = [] , path = [3, 1, 2] , result = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2]] ) # added a new permutation to the result
       |___dfs(nums = [1] , path = [3, 2] , result = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2]] )
            |___dfs(nums = [] , path = [3, 2, 1] , result = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]] ) # added a new permutation to the result
```

```python3
def permute(self, nums: List[int]) -> List[List[int]]:
    result = []
    self.dfs(nums, [], result)
    return result

def dfs(self, nums, path, result):

    if len(nums)==0:
        result.append(path)
    else:
        for i in range(len(nums)):
            self.dfs(nums[:i]+nums[i+1:], path+[nums[i]], result)

```

Actual running time:\
![image](https://user-images.githubusercontent.com/25105806/125020993-a8338c00-e02e-11eb-99e5-903145ffbd94.png)

<br />

### Approach 2: Iteration, permute(), CPP
We can also use iterative approach to solve this. The iterative solution can handle larger size of input because we don't need to worry about recursion running out of stack size. 

The idea is to iteratively add `num` from `nums` to the list. Each new `num` can be add at different indices of previous permutations and we just need to store them.

```cpp
vector<vector<int>> permute(vector<int>& nums) {
    vector<vector<int>> pre, cur;
    for (const auto& num : nums) {
        if (pre.size() == 0) {
            pre.push_back({num});
        } else {
            for (auto permutation : pre) {
                int size = permutation.size();
                for (int i = 0; i <= size; i++) {
                    permutation.insert(permutation.begin() + i, num);
                    cur.push_back(permutation);
                    permutation.erase(permutation.begin() + i);
                }
            }
            pre = cur;
            cur.clear();
        }
    }
    return pre;
}
```

Time complexity is O():\
<img width="637" alt="image" src="https://user-images.githubusercontent.com/25105806/170169743-14ace4bb-8f44-4f73-9961-f59b221124e7.png">
