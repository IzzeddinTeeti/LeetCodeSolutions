class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        
        factors = set()
        
        max_search_limit = int(n **(1/2)) + 1
        
        for i in range(1, max_search_limit):
            
            if n % i ==0:
                factors.add(i)
                factors.add(n//i)
        
        
        if k > len(factors):
            return -1
        else:
            factors = sorted(list(factors))
            return factors[k-1]