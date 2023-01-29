#include <iostream>
#include <string>
#include <unordered_map>
#include <vector>
using namespace std;

class Solution {
public:
    bool wordPattern(string pattern, string s) {
        // split the string by space
        vector<string> strSplits;
        int start = 0;
        int end = 0;
        while (end < s.length()) {
            if (s[end] == ' ') {
                strSplits.push_back(s.substr(start, end - start));
                start = end + 1;
            }
            end++;
        }
        strSplits.push_back(s.substr(start, end - start + 1));

        if (strSplits.size() == pattern.length()) {
            unordered_map<char, string> char2Str;
            unordered_map<string, char> str2Char;

            for (int i = 0; i < strSplits.size(); i++) {
                char p = pattern.at(i);
                string str = strSplits.at(i);

                if (char2Str.find(p) != char2Str.end()) {
                    if (char2Str[p] != str) {
                        return false;
                    }
                } else {
                    char2Str[p] = str;
                }

                if (str2Char.find(str) != str2Char.end()) {
                    if (str2Char[str] != p) {
                        return false;
                    }
                } else {
                    str2Char[str] = p;
                }
            }
            return true;
        } else {
            return false;
        }
    }
};

int main() {
    Solution solver;

    string pattern = "abba";
    string s = "dog cat cat dog";
    bool result = solver.wordPattern(pattern, s);
    cout << result << endl;

    return 0;
}