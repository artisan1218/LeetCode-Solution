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
            
    def strStrKMP(self, haystack: str, needle: str) -> int:
        # generate 'nextList' array, need O(k) time
        i = 1
        j = 0
        strLen = len(haystack)
        ndlLen = len(needle)
        nextList = [0] * ndlLen # nextList stores the jumping index when a bad match happens
        while i < ndlLen:
            # first index in nextList is always 0, which means 0 itself is a common prefix/suffix
            if needle[i] == needle[j]:
                nextList[i] = j + 1
                j += 1
                i += 1
            else:
                if j!=0:
                    j = nextList[j-1]
                else:
                    nextList[i] = 0
                    i+=1

        #the actual checking starts here, need O(n) time
        strPtr = ndlPtr = 0
        while strPtr < strLen and ndlPtr < ndlLen:
            # if the char matches, check the next one
            if haystack[strPtr] == needle[ndlPtr]:
                strPtr += 1
                ndlPtr += 1
            # bad check happend, find the next position needle pointer needs to go according to nextList
            else:
                if ndlPtr != 0:
                    # go the char before common prefix/suffix so that we can avoid checking already checked chars
                    ndlPtr = nextList[ndlPtr-1]
                else:
                    # needle pointer is still at first index, move string pointer to next
                    strPtr += 1
        # the entire needle has been matched
        if ndlPtr == ndlLen:
            return strPtr-ndlPtr
        else:
            return -1

if __name__ == "__main__":
    haystack = "hello"
    needle = "llo"
    solver = Solution()
    print(solver.strStrKMP(haystack, needle))




