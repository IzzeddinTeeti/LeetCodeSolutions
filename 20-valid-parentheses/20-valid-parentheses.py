class Solution:
    def isValid(self, s: str) -> bool:
        match = {'(': ')', 
                 '[': ']', 
                 '{': '}'}
           
        if len(s) < 2:
            return False
        
        stack = []
        
        for ch in s:
            if ch in match.keys():
                stack.append(ch)
            elif len(stack) > 0 and match[stack[-1]] == ch:
                stack.pop()
            else:
                return False
                
        return len(stack) == 0
                
        