# Cracking the Safe problem
![image](https://user-images.githubusercontent.com/25105806/179154083-3c55d53d-5612-4d11-b5e6-579c695ba20c.png)

Leetcode link: https://leetcode.com/problems/cracking-the-safe/

<br />

### Approach 1: Backtracking, backtrack()

The idea is to use backtrack to explore all possible ways of appending new characters. However, we need to make sure we don't add duplicate passwords in our path, so we have to maintain a hashset of seen passwords. When certain path does not contain all passwords, we backtrack.

The stopping condition for the recursion function is when the size of seen hashset contains `pow(k, n)` number of unique passwords.

```cpp
string crackSafeBacktrack(int n, int k) {
    string result(n, '0');
    set<string> seen = {result};
    bakctrack(n, k, result, seen);
    return result;
}

bool bakctrack(int n, int k, string& cur, set<string>& seen) {
    if (seen.size() == pow(k, n)) {
        return true;
    }

    for (int i = 0; i < k; i++) {
        cur.append(to_string(i));                          // append the new char
        string password = cur.substr(cur.length() - n, n); // get the newly formed password
        if (seen.count(password) == 0) {
            // newly formed password is not seen before, we can add it to the set and append next one recursively
            seen.insert(password);
            if (bakctrack(n, k, cur, seen)) {
                return true;
            }
            cur.pop_back();       // backtrack
            seen.erase(password); // backtrack
        } else {
            // the newly formed password is seen, we should try appending another char
            cur.pop_back();
        }
    }
    return false;
}
```

Time complexity is O(k^n) because we will explore every possible way and space complexity is also O(k^n), which is the callstack:
![image](https://user-images.githubusercontent.com/25105806/179309249-90e9a4d7-299d-4186-b3a9-d3462c039749.png)


<br />

### Approach 2: Hierholzer Algorithm, hierholzer()

Credits to: https://leetcode.cn/problems/cracking-the-safe/solution/zhuan-hua-wei-ou-la-hui-lu-wen-ti-hierholzer-suan-/

If we consider the passwords as a graph, each node represents the shared portion between passwords, which has length of `n-1` and each edge represents the new character we add to our next passwords, then the valid solution is simply an Eulerian cycle. We can use Hierholzer algorithm to find the Eulerian cycle.

We can assume the solution exists and start at the 'all-zero node' and choose next edge to go based on edge index, everytime we choose an edge to go, we have to delete it from our graph representation to avoid duplicate visiting. If at an certain edge we don't find any available edges to go, which means we've reached a dead end, we can now put the previous edge we choose to our result, because dead end must be visited at the end, that's why we enter the recursion function first, then store the result. Then simply explore the next possible edge and add it to our result backwards(equivalent to popping from callstack).

In actual coding, we use a vector of 0/1 to represent the visited status of each edge. We use

1. `currNode = edgeIdx % nodeNum` to convert edge index to node index
2. `edgeIdx = currNode * k + outboundIdx` to convert node index to edge index


For example, `n=2, k=2`

The graph can look like this:

<img src="https://user-images.githubusercontent.com/25105806/179312017-59704b88-89bf-41e2-9da6-f15c446f4d94.jpg" height="20%" width="20%">

We can see that the graph has two nodes of value 0 and 1 and 4 edges of 0 and 1. We will form a password by one node and one edge.

The Hierholzer algorithm will explore the graph starting at node `0` and in this order:
![ec8484714b0b4c4f16991337981bd5b](https://user-images.githubusercontent.com/25105806/179312387-1a1dd232-0e13-404a-9ab3-1bee9c22eaa0.jpg)


From left to right, every time we've visited an edge, we will remove it from the graph and add the edge to the callstack down below. When we hit the third callstack, we found that we've reached a dead end at node 0 because node 0 has no more outbounds, so we start adding previous edge to our result (pop from callstack). Next, we can visit the last edge at node 1 and add it to callstack. After this, all edges have been visited and all we need to do is simply get the edge value from callstack to our `result` variable.

Note that the final result after the algorithm is `0110`, which is the reverse of the actual Eulerian cycle, but the order of the solution does not matter in the context of this problem, so we don't need to flip it. 

Finally, we have to append the value of initial node to our result to form the final answer because we start at the initial 'all-zeros node' and its value should be included in the solution.

```cpp
string crackSafeHierholzer(int n, int k) {
    int nodeNum = pow(k, n - 1);      // not pow(k, n) because each node represent the shared portion between passwords, which has length of n-1, so total number of nodes will be k^n-1 not k^n
    vector<int> side(nodeNum * k, 0); // each node has k out-degrees, so total of node*k edges
    string result;
    hierholzer(side, k, 0, result, nodeNum);
    result += string(n - 1, '0'); // append the starting string
    return result;
}

void hierholzer(vector<int>& side, int k, int edgeIdx, string& res, int nodeNum) {
    int currNode = edgeIdx % nodeNum;                           // convert edge index to node index
    for (int outboundIdx = 0; outboundIdx < k; outboundIdx++) { // iterate over all outdegree edges of each node
        int edgeIdx = currNode * k + outboundIdx;               // convert node idx and outdegree idx to edge idx
        if (side[edgeIdx] == 0) {                               // we haven't explored this edge yet
            side[edgeIdx]++;
            hierholzer(side, k, edgeIdx, res, nodeNum);
            res += to_string(outboundIdx);
        }
    }
}
```

Time complexity is O(k^n) which is the number of edges we explored, space complexity is also O(k^n), which is the callstack:
![image](https://user-images.githubusercontent.com/25105806/179313754-48c1753e-aa18-49e1-9987-4a3d04f4eb0a.png)
