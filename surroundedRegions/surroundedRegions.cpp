#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    void solve(vector<vector<char>> &board) {
        for (int r = 0; r < board.size(); r++) {
            for (int c = 0; c < board[r].size(); c++) {
                // if r, c is on the boarder of board
                if (board[r][c] == 'O' && (r == 0 || r == board.size() - 1 || c == 0 or c == board[r].size() - 1)) {
                    captureUnsurrounded(board, r, c);
                }
            }
        }
        for (int r = 0; r < board.size(); r++) {
            for (int c = 0; c < board[r].size(); c++) {
                if (board[r][c] == 'O') {
                    board[r][c] = 'X';
                } else if (board[r][c] == 'T') {
                    board[r][c] = 'O';
                }
            }
        }
    }

    void captureUnsurrounded(vector<vector<char>> &board, int r, int c) {
        if (r < 0 || c < 0 || r >= board.size() || c >= board[0].size() || board[r][c] != 'O') {
            return;
        } else {
            // 'T' marks any spot that will not be flipped to 'X'
            board[r][c] = 'T';
            captureUnsurrounded(board, r + 1, c);
            captureUnsurrounded(board, r - 1, c);
            captureUnsurrounded(board, r, c + 1);
            captureUnsurrounded(board, r, c - 1);
        }
    }
};

int main() {

    vector<vector<char>> board{
        {'X', 'X', 'X', 'X'},
        {'X', 'O', 'O', 'X'},
        {'X', 'X', 'O', 'X'},
        {'X', 'O', 'X', 'X'}};
    cout << "The board is set to: " << endl;
    for (auto vec : board) {
        for (auto c : vec) {
            cout << c << ' ';
        }
        cout << endl;
    }
    cout << endl;

    Solution solver;
    solver.solve(board);

    cout << "After the modification: " << endl;
    for (auto vec : board) {
        for (auto c : vec) {
            cout << c << ' ';
        }
        cout << endl;
    }
}