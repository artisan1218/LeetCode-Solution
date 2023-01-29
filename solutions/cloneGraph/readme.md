# Clone Graph problem
<img width="728" alt="image" src="https://user-images.githubusercontent.com/25105806/164999391-8b40ad88-5a8c-4830-9b37-bad11bc0ba40.png">


Leetcode link: https://leetcode.com/problems/clone-graph/

<br />

### Approach 1: Map, cloneGraph()
The key idea of this solution is to store the projection relationship between original node value and cloned node using a map `map`, this way we can keep track of all created nodes by using the original node value as we traverse the original graph.

```cpp
Node* cloneGraph(Node* node) {
    if (node != nullptr) {
        unordered_set<int> seenNodes;
        unordered_map<int, Node*> map;
        Node* clone = new Node();
        helper(node, clone, seenNodes, map);
        return clone;
    } else {
        return nullptr;
    }
}

void helper(Node* node, Node* clone, unordered_set<int>& seenNodes, unordered_map<int, Node*>& map) {
    clone->val = node->val;
    seenNodes.insert(node->val);
    map[clone->val] = clone;

    for (auto n : node->neighbors) {
        int nVal = n->val;
        if (map.find(nVal) == map.end()) {
            map[nVal] = new Node(nVal);
        }
        clone->neighbors.push_back(map[nVal]);
        if (seenNodes.find(nVal) == seenNodes.end()) {
            helper(n, map[nVal], seenNodes, map);
        }
    }
}
```

Time complexity is O(n) because we only traverse all nodes once:\
<img width="621" alt="image" src="https://user-images.githubusercontent.com/25105806/164999504-53bea53a-64e4-42ec-bd32-df0a38b166cc.png">


<br />

### Approach 2: DFS, cloneGraph2()

Credits to: https://www.youtube.com/watch?v=mQeF6bN8hMk

The idea is to use DFS to traverse the graph. We still need a map to store the projection relation between old node and cloned node. We'll use recursion to add all adjacent nodes to `neighbors` list.

```cpp
Node* cloneGraph2(Node* node) {
    if (node != nullptr) {
        unordered_map<Node*, Node*> oldToNew;
        return helper2(node, oldToNew);
    } else {
        return nullptr;
    }
}

Node* helper2(Node* node, unordered_map<Node*, Node*>& oldToNew) {
    if (oldToNew.find(node) != oldToNew.end()) {
        return oldToNew[node];
    } else {
        Node* copy = new Node(node->val);
        oldToNew[node] = copy;
        for (auto n : node->neighbors) {
            Node* toBeConnected = helper2(n, oldToNew);
            copy->neighbors.push_back(toBeConnected);
        }
        return copy;
    }
}
```

Time complexity is O(n):\
<img width="613" alt="image" src="https://user-images.githubusercontent.com/25105806/164999643-3c1cd9cd-5487-4d0c-8b77-036f59caeb2a.png">

```
