class Solution:
    def strStrSlidingWindow(self, haystack: str, needle: str) -> int:
        left = 0
        right = len(needle)
        while right <= len(haystack):
            if haystack[left:right] == needle:
                return left
            else:
                left+=1
                right+=1
        return -1
        
    def strStrImprovedSlidingWindow(self, haystack: str, needle: str) -> int:
        if needle == '':
            return 0
        else:
            for idx in range(len(haystack)):
                if haystack[idx] == needle[0]:
                    if needle[1:] == haystack[idx+1: idx+len(needle)]:
                        return idx
            return -1
    
    def strStrTwoPointers(self, haystack: str, needle: str) -> int:
        if len(haystack) < len(needle): # early termination
            return -1
        elif needle == '':
            return 0
        else:
            strPtr = 0
            ndlPtr = 0
            while ndlPtr < len(needle) and strPtr < len(haystack): 
                # if they are not equal, check the next char in haystack and reset needle pointer
                if haystack[strPtr] != needle[ndlPtr]:
                    # strPtr is not simply +=1 because maybe we're not checking the first char of needle
                    strPtr = strPtr - ndlPtr + 1
                    ndlPtr = 0
                else: 
                    strPtr += 1
                    ndlPtr += 1
            
            # the entire needle has been matched
            if ndlPtr == len(needle):
                return strPtr-ndlPtr
            else:
                return -1


if __name__ == "__main__":
    haystack = "hello"
    needle = "ll"
    solver = Solution()
    print(solver.strStrTwoPointers(haystack, needle))





