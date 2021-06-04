

from typing import List

class Solution:
    
    def generateParenthesisDP1(self, n: int) -> List[str]:
        idx_result = [[0]]
        tmp_res = []
        for i in range(1, n):
            for prev in idx_result: # [0]
                # the new pos of the opening parenthesis can only be greater than the current right-most one
                # and smaller than the right-most closing parenthesis  
                for newPos in range(prev[-1]+1, 2*(i+1)-1):
                    # form new idx result by appending new position of the opening parenthesis to the 
                    # end of each previous result
                    tmp_res.append(prev + [newPos])
            idx_result = tmp_res
            tmp_res = []
            # we can simply replace the above two nested loop with the statement below
            #idx_result = [prev+[newPos] for prev in idx_result for newPos in range(prev[-1]+1, 2*(i+1)-1)]
        
        # turn idx_result in to actual string
        str_result = []
        for res in idx_result:
            # default char is closing parenthesis, we will replace ')' at given index with '('
            template = [')'] * 2 * n
            for pos in res:
                template[pos] = '('
            str_result.append(''.join(template))
        return str_result
    
    def generateParenthesisDP2(self, n: int) -> List[str]:
        dp = [[] for i in range(n + 1)]
        dp[0].append('')
        
        # increase n by 1 each time, solve sub-problems one by one
        for curr_n in range(n + 1):
            # for each of the result in previous n, which is the 'sub-problem'
            for prev in range(curr_n):
                # get all permutations of sub problem solutions and form new solution
                for x in dp[prev]:
                    for y in dp[curr_n - prev - 1]:
                        dp[curr_n] += ['(' + x + ')' + y ]
                # the above nested loop can be replaced with this statement
                #dp[i] += ['(' + x + ')' + y for x in dp[j] for y in dp[i - j - 1]]
        # dp contains of solutions to all sub-problems, we only want the solution for n
        return dp[-1]
    
    def generateParenthesisBacktrack(self, n: int) -> List[str]:
        result = []
        self.backtrack(result, '', 0, 0, n)
        return result
    
    def backtrack(self, result, string, openP, closeP, n):
        
        if len(string)==2*n:
            result.append(string)
            return  
        
        # if openning parenthesis is less than n, then we can add more openning parenthesis
        if openP < n:
            self.backtrack(result, string+'(', openP+1, closeP, n)
        
        # if closing parenthesis is less than opening parenthesis, then we can one more closing 
        # parenthesis to match up the openning parenthesis
        if closeP < openP:
            self.backtrack(result, string+')', openP, closeP+1, n)
        
       

if __name__ == "__main__":
    solver = Solution()
    n = 3
    print(solver.generateParenthesisBacktrack(n))





