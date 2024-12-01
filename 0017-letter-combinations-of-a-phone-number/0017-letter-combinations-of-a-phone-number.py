class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        if digits =='':
            return []

        phone = {'2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'}   

        results = ['']

        for digit in digits:
            letters = phone[digit]
            results = [prefix+letter for prefix in results for letter in letters]

        return results             