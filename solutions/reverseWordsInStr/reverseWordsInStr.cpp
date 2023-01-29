#include <algorithm>
#include <iostream>
#include <string>

using namespace std;

class Solution {
   public:
    string reverseWords(string s) {
        // reverse the entire string
        reverse(s.begin(), s.end());

        int slow = 0, fast = 0, end = 0;
        while (fast < s.size()) {
            // skip all spaces and find the starting index of the non-space word
            while (fast < s.size() && s[fast] == ' ') {
                fast++;
            }

            // fill the string s with words and only one space between words
            int start = slow;
            while (fast < s.size() && s[fast] != ' ') {
                s[slow++] = s[fast++];
                end = slow;
            }

            // reverse the word
            reverse(s.begin() + start, s.begin() + slow);
            // add a space after each word
            if (slow < s.size()) {
                s[slow++] = ' ';
            }
        }

        // truncate the remaining char on the right
        s.resize(end);
        return s;
    }
};

int main() {
    Solution solver;
    string s = " the sky is blue ";
    auto result = solver.reverseWords(s);
    cout << result << endl;
    return 0;
}