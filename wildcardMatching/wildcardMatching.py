
class Solution:
    # TLE
    def isMatchBacktracking(self, s: str, p: str) -> bool:
        if len(p)!=0 and all([c=='*' for c in p]):
            return True
        else:
            return self.backtrack(s, p, 0, 0)
        
    def backtrack(self, s: str, p: str, strStart: int, patternStart: int):
        if strStart == len(s) and patternStart==len(p):
            return True
        elif strStart == len(s) and all([c=='*' for c in p[patternStart:]]):
            return True
        else:
            for i in range(len(s[strStart:])):
                for j in range(len(p[patternStart:])):
                    if p[j+patternStart] == '*':
                        # try all number of chars that can be matched with *
                        for numMatched in range(len(s)-strStart+1):
                            if self.backtrack(s, p, strStart+numMatched, patternStart+1):
                                return True
                        return False
                    elif p[j+patternStart] == '?':
                        return self.backtrack(s, p, strStart+1, patternStart+1)
                    else:
                        if p[j+patternStart] == s[i+strStart]:
                            return self.backtrack(s, p, strStart+1, patternStart+1)
                        else:
                            return False
            return False
        
    def isMatchDP(self, s: str, p: str) -> bool:
        
        # initialize 2d dp array, the size of array is one more than size of p and s
        # because the first element will be ''
        dp = [[False for _ in range(len(p)+1)] for _ in range(len(s)+1)]
        # '' always matches ''
        dp[0][0] = True
        
        # change all slot to True if read a * until the first non * char is met
        # this addresses the pair where p='***' and s=''
        for i in range(len(p)):
            if p[i]=='*':
                dp[0][i+1] = True
            else:
                break
        
        # real DP part
        # traverse all substring of s
        for i in range(1, len(dp)):
            # traverse all sub-pattern of p
            for j in range(1, len(dp[i])):
                '''
                read a ?
                if the ? is valid, then the result of this slot only depends on the previous substring of s
                and previous substring of p, which means we can 'remove' this pattern p and the current 
                char s by looking at dp[i-1][j-1]. If dp[i-1][j-1] is valid, then this is valid.
                '''
                if p[j-1]=='?':
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1]=='*':
                    '''
                    read a *
                    the * can match empty string or one/more string
                    If it matches empty string, which is equivalent to 'remove' the current * by looking at dp[i][j-1]
                    if it matches more string, which is equivalent to 'remove' the current char s by looking at dp[i-1][j]
                    '''
                    dp[i][j] = dp[i-1][j] or dp[i][j-1]
                # read a char
                else:
                    '''
                    if this char matches the pattern char, again we can 'remove' this pattern p and the current 
                    char s by looking at dp[i-1][j-1]
                    '''
                    if p[j-1] == s[i-1]:
                        dp[i][j] = dp[i-1][j-1]
                    else:
                        # the current char does not match with pattern, simply put False there
                        dp[i][j] = False
        
        return dp[-1][-1]

if __name__ == "__main__":
    solver = Solution()
    s = "abcdf"
    p = "a?*d?"
    print(solver.isMatchDP(s, p))



