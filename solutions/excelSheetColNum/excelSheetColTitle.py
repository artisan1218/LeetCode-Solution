# %%
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = ''
        while columnNumber > 26:
            r = columnNumber % 26
            if r==0:
                result += 'Z'
                columnNumber = (columnNumber // 26) - 1 
            else:
                result += chr(r + 64)
                columnNumber = columnNumber // 26
        result += chr(columnNumber + 64)
        return result[::-1]
    
    #  https://leetcode.com/problems/excel-sheet-column-title/solutions/441430/detailed-explanation-here-s-why-we-need-n-at-first-of-every-loop-java-python-c/?orderBy=most_votes
    def convertToTitle2(self, columnNumber: int) -> str:
        result = ''
        while columnNumber > 0:
            columnNumber -= 1
            r = columnNumber % 26
            result += chr(r + 65)
            columnNumber = columnNumber // 26
        return result[::-1]

solver = Solution()
columnNumber = 52
print(solver.convertToTitle2(columnNumber))

# %%



