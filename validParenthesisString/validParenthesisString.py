# %%
class Solution:
    def checkValidStringDFS(self, s: str) -> bool:
        cache = [[None for _ in range(len(s))] for _ in range(len(s))]
        def dfs(s, i, left):
            if left<0:
                return False
            else:
                if i==len(s):
                    return left==0
                else:
                    if cache[i][left] != None:
                        return cache[i][left]
                    else:
                        if s[i]=='(':
                            cache[i][left] = dfs(s, i+1, left+1)
                            return cache[i][left]
                        elif s[i]==')':
                            cache[i][left] = dfs(s, i+1, left-1)
                            return cache[i][left]
                        else: # wildcard *
                            cache[i][left] = dfs(s, i+1, left+1) or dfs(s, i+1, left-1) or dfs(s, i+1, left)
                            return cache[i][left]
        return dfs(s, 0, 0)


    # https://leetcode.com/problems/valid-parenthesis-string/discuss/107581/O(n)-time-O(1)-space-no-Recursion-just-scan-from-left-and-then-scan-from-right
    def checkValidStringTwoPass(self, s: str) -> bool:
        def scan(dir, s):
            open, close, star = 0, 0, 0
            # we will need to reverse the string when scanning from right
            if dir=='right':
                s = s[::-1]
    
            for c in s:
                if c=='(':
                    open+=1
                elif c==')':
                    close+=1
                else:
                    star+=1
                
                # when scanning from right, we should treat ) as open parenthesis, but we don't
                # need to rewrite the code block, simply swap the open and close when comparing them
                if (dir=='left' and close > (open + star)) or (dir=='right' and open > (close + star)):
                    return False 
            return True
        
        return scan('left', s) and scan('right', s)


    # https://www.youtube.com/watch?v=QhPdNS143Qg
    def checkValidStringOnePass(self, s: str) -> bool:
        leftMin, leftMax = 0, 0
        for c in s:
            if c=='(': 
                # if (, then the left open parenthesis is counted one more, which means we need one more closing parenthesis to validate the string
                leftMin+=1 
                leftMax+=1
            elif c==')':
                # if ), then the left open parenthesis is counted one less, which means we need one less closing parenthesis to validate the string
                leftMin-=1
                leftMax-=1
            else:
                # if *, then we can have one more open OR one less open parenthesis OR nothing. 
                # leftMin and leftMax marks the boundary of number of open parenthesis we can have based on different choices of wildcard character
                leftMin-=1
                leftMax+=1
            leftMin = max(0, leftMin) # leftMin cannot be negative, reset it 0 once it drops below 0
            if leftMax < 0:
                # if leftMax is below 0, which means we have more closing parenthesis than open parenthesis. 
                # We will never recover from this state, so it's immediately invalid. consider ))(())
                return False 
        return leftMin==0

    

if __name__ == '__main__':
    solver = Solution()
    s = "**))(("
    print(solver.checkValidStringTwoPass(s))

# %%



