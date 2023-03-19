#include <iostream>
#include <math.h>
#include <string>
#include <vector>

class Solution {
public:
    int titleToNumber(std::string columnTitle) {
        int n = columnTitle.length();
        int result = 0;
        for (char c : columnTitle) {
            result += (int(c) - 64) * pow(26, n - 1);
            n--;
        }
        return result;
    }
};

int main() {
    Solution solver;
    std::cout << solver.titleToNumber("ZY") << std::endl;
    return 0;
}
