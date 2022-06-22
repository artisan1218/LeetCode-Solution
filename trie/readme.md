# Implement Trie (Prefix Tree) problem
![image](https://user-images.githubusercontent.com/25105806/174951066-f496f30c-7049-4a40-be39-7b36c9f3217f.png)


Leetcode link: https://leetcode.com/problems/implement-trie-prefix-tree/

<br />

Reference: 
1. https://stackoverflow.com/questions/72674344/how-should-i-write-destructor-for-this-class-in-c
2. https://www.youtube.com/watch?v=oobqoCJlHA0

### Approach 1: No Extra Class, Trie

The basic structure of the Trie tree is to store each char of the word at a node. Words that share same prefix will also share the same path of the tree. 
For example the word 'apple' and 'application' will use the same path 'a->p->p', then split two paths for 'le' and 'lication'. We can include a hashmap and a boolean variable at each node. The hashmap is used to store the connection between two characters, so that we know the next node to take when searching and inserting. The boolean variable `isEnd` is used to store if current node is the ending character of a word. So that we can know when to stop searching when searching for a word. 

In this solution we build the class with no extra `TrieNode` class, instead, having a hashmap to store the `Trie` class itself as a pointer. When implementing this in C++, we need to also implement a destructor function. 

Since we designed the class using hashmap, we do not need to delete the pointers recursively:
1. Instances `a` of `Trie` class are owned by another instance of `Trie` class (lets call it owner) where `&a` appears in `owner.map`.
2. Whenever an instance owner becomes destroyed, it has to free all instances it (directly) owns:
3. Which means we only need to free the owner once, and it will automatically free all instances it owns.



```cpp
class Trie {
public:
    Trie() {
    }

    void insert(string word) {
        Trie* node = this;
        for (int i = 0; i < word.length(); i++) {
            if (node->map.find(word.at(i)) == node->map.end()) {
                node->map[word.at(i)] = new Trie();
            }
            node = node->map[word.at(i)];
        }
        node->isEnd = true;
    }

    bool search(string word) {
        Trie* node = this;
        for (int i = 0; i < word.length(); i++) {
            if (node->map.find(word.at(i)) == node->map.end()) {
                return false;
            } else {
                node = node->map[word.at(i)];
            }
        }
        return node->isEnd;
    }

    bool startsWith(string prefix) {
        Trie* node = this;
        for (int i = 0; i < prefix.length(); i++) {
            if (node->map.find(prefix.at(i)) == node->map.end()) {
                return false;
            } else {
                node = node->map[prefix.at(i)];
            }
        }
        return true;
    }

    ~Trie() {
        for (auto& pair : map) {
            delete pair.second;
        }
    }

private:
    unordered_map<char, Trie*> map = {};
    bool isEnd = false;
};
```

Time complexity of `insert()`, `search()` and `startsWith()` is O(n): 
![image](https://user-images.githubusercontent.com/25105806/174953834-0599166f-d724-45f8-9130-5a5ac7efd7f3.png)

<br />


### Approach 2: Separating TrieNode() Class, Trie2

The basic structure is the same as approach #1 but this time we use a separate `TrieNode()` class to represent a node. We can therefore reduce the memory useage because each node is now only a small class with two variables. Also it's more readable. 

When writing the destructor of this class, we have to delete every instances recursively because we're now deleting the pointer of `TrieNode()` class, which is different from a hashmap.

```cpp
struct TrieNode {
public:
    unordered_map<char, TrieNode*> map = {};
    bool isEnd = false;
};

class Trie {
public:
    Trie() {
        root = new TrieNode();
    }

    void insert(string word) {
        auto* node = root;
        for (int i = 0; i < word.length(); i++) {
            if (node->map.find(word.at(i)) == node->map.end()) {
                node->map[word.at(i)] = new TrieNode();
            }
            node = node->map[word.at(i)];
        }
        node->isEnd = true;
    }

    bool search(string word) {
        auto* node = root;
        for (int i = 0; i < word.length(); i++) {
            if (node->map.find(word.at(i)) == node->map.end()) {
                return false;
            } else {
                node = node->map[word.at(i)];
            }
        }
        return node->isEnd;
    }

    bool startsWith(string prefix) {
        auto* node = root;
        for (int i = 0; i < prefix.length(); i++) {
            if (node->map.find(prefix.at(i)) == node->map.end()) {
                return false;
            } else {
                node = node->map[prefix.at(i)];
            }
        }
        return true;
    }

    ~Trie() {
        clear(root);
    }

    void clear(TrieNode* root) {
        for (auto& pair : root->map) {
            if (pair.second != nullptr) {
                clear(pair.second);
            }
        }
        delete root;
    }

private:
    TrieNode* root;
};
```

Time complexity is still the same:
![image](https://user-images.githubusercontent.com/25105806/174954857-44bb6a01-03ef-4a9d-83a3-11270b7f4504.png)
