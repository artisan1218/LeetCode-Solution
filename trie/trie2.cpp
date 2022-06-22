#include <iostream>
#include <string>
#include <unordered_map>
using namespace std;

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

int main() {

    // Your Trie object will be instantiated and called as such:
    string word = "hello";
    string prefix = "hel";

    Trie* obj = new Trie();
    obj->insert(word);
    bool param_2 = obj->search(word);
    bool param_3 = obj->startsWith(prefix);

    cout << param_2 << "\n";

    delete obj;

    return 0;
}
