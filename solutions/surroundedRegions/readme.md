# Surrounded Regions problem
<img width="856" alt="image" src="https://user-images.githubusercontent.com/25105806/161416881-ae3e1867-fabc-4ae0-ac94-ebeed2832a87.png">

Leetcode link: https://leetcode.com/problems/surrounded-regions/

<br/>

### Approach 1: DFS, solve(), captureUnsurrounded()

Reference: https://www.youtube.com/watch?v=9z2BunfoZ5Y

The solution is based on a key observation that if a block is connected to any block on the border of the `board`, then it is not surrounded. We can iterate through all blocks on the board, then use dfs to find any connected blocks and mark them as 'not surrounded'. Then simply go over the entire board and flip those blocks which are not marked as 'not surrounded'. In this solution, 'not surrounded' blocks are marked as 'T'.

```cpp
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
```

Time complexity is O(n):\
<img width="665" alt="image" src="https://user-images.githubusercontent.com/25105806/161417174-087ebd67-8aa7-4fd1-90db-ed554d029658.png">
