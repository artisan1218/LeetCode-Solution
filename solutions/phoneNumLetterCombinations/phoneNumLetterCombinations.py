from typing import List

def letterCombinations(digits: str) -> List[str]:
    if len(digits)==0:
        return []
    else:
        mapping = {'2': 'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        prev_list = ['']
        for d in digits:
            letters = mapping[d]
            result_list = [prefix+letter for prefix in prev_list for letter in letters]
            prev_list = result_list
        return result_list

if __name__ == "__main__":
 
    print(letterCombinations('23'))




