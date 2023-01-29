#include <iostream>
#include <unordered_map>
#include <unordered_set>
#include <vector>

using namespace std;

// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> neighbors;
    Node() {
        val = 0;
        neighbors = vector<Node*>();
    }
    Node(int _val) {
        val = _val;
        neighbors = vector<Node*>();
    }
    Node(int _val, vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};

class Solution {
public:
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

    // reference: https://www.youtube.com/watch?v=mQeF6bN8hMk
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
};

int main() {
    Solution solver;

    Node node1(1);
    Node node2(2);
    Node node3(3);
    Node node4(4);
    node1.neighbors.push_back(&node2);
    node1.neighbors.push_back(&node4);
    node2.neighbors.push_back(&node1);
    node2.neighbors.push_back(&node3);
    node3.neighbors.push_back(&node2);
    node3.neighbors.push_back(&node4);
    node4.neighbors.push_back(&node1);
    node4.neighbors.push_back(&node3);

    Node* result = solver.cloneGraph(&node1);
}