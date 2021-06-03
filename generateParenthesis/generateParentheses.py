from typing import List

class Solution:
    
    def generateParenthesis(self, n: int) -> List[str]:
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


if __name__ == "__main__":
    solver = Solution()
    n = 3
    print(solver.generateParenthesis2(n))




