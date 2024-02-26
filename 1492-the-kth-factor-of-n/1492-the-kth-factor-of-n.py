class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        
        max_loop = int(sqrt(n))
        counter = 0
        for i in range(1, n+1):
            if n % i == 0:
                counter += 1
            
            if counter == k:
                return i
            
        return -1
            
        