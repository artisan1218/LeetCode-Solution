
class Solution:
    def longestValidParenthesesTwoStacks(self, s: str) -> int:
        stack = []
        idxList = []
        
        # use a stack to keep track of unpaired parenthesis
        # use a list to store the indices of unpaired parentheses
        for i in range(len(s)):
            char = s[i]
            if len(stack)>0 and s[i]==")" and stack[-1]=="(":
                stack.pop()
                idxList.pop()
            else:
                stack.append(char)
                idxList.append(i)
        
        # compute the longest distance
        if len(idxList)==0:
            return len(s)
        else:
            if idxList[-1] != len(s)-1:
                idxList.append(len(s))
            longest = 0
            prev = -1
            for idx in idxList:
                current = idx - prev -1
                longest = max(longest, current)
                prev = idx

        return longest
    
    def longestValidParenthesesDP(self, s: str) -> int:
        
        dp = []
        for idx in range(len(s)):
            char = s[idx]
            if char=='(': 
                dp.append(0)
            else:
                if idx>0:
                    if s[idx-1] == '(':  # case ()
                        if idx>=2:
                            dp.append(dp[idx-2] + 2)
                        else:
                            dp.append(2)
                    elif s[idx-1] == ')': # case ))
                        validSubstrBeginningIdx = idx - dp[idx-1] - 1
                        if validSubstrBeginningIdx >=0 and s[validSubstrBeginningIdx] == '(':
                            # there might be valid substring before this substring
                            if validSubstrBeginningIdx >= 2:
                                # case ()(()), connecting two valid substrings
                                dp.append(dp[idx-1] + dp[validSubstrBeginningIdx-1] + 2) 
                            else:
                                dp.append(dp[idx-1] + 2)
                        else:
                            dp.append(0)
                else:
                    dp.append(0)

        return 0 if len(dp)==0 else max(dp)
    
if __name__ == "__main__":
    solver = Solution()
    s = "(()))())("
    print(solver.longestValidParenthesesDP(s))




