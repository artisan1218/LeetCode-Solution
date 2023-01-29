#include <iostream>
#include <string>
#include <unordered_map>
#include <vector>
using namespace std;

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
