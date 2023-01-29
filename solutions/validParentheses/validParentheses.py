
class Solution:
    def isValid(self, s: str) -> bool:
        checkList = list()

        for char in s:
            if len(checkList)>0 and self.isValidPair(checkList[-1], char):
                checkList.pop(-1)
            else:
                checkList.append(char)
        return len(checkList)==0
    
    def isValidPair(self, left, right):
        return left=='(' and right==')' or left=='[' and right ==']' or left=='{' and right=='}'


if __name__ == "__main__":
    solver = Solution()
    print(solver.isValid("({[)"))







