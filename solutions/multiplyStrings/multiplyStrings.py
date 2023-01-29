
class Solution:
    '''
    123 * 456 can be splited into 100*400 + 100*50 + 100*6 + 20*400 + 20*50 + 20*6 + 3*400 + 3*50 + 3*6
    this is really the very definition of multiplication
    we simply use two for-loop to do this, outer loop is to iterate through each digit of the longer number
    inner loop is to iterate through each digit of the shorter number, then we multiply them together
    '''
    def multiply(self, num1: str, num2: str) -> str:
        
        result = 0
        if len(num1)<len(num2):
            num1, num2 = num2, num1
        
        num1Base = 10**(len(num1)-1)  
        for digit1Str in num1:
            digit1 = int(digit1Str)
            
            num2Base = 10**(len(num2)-1)
            for digit2Str in num2:
                digit2 = int(digit2Str)
                result += digit1 * digit2 * num1Base * num2Base
                num2Base = num2Base//10
            num1Base = num1Base//10
        
        return str(result)
    
if __name__ == "__main__":
    solver = Solution()
    num1 = "123"
    num2 = "456"
    print(solver.multiply(num1, num2))





