class Solution:
    def bitwiseComplement(self, n: int) -> int:
        
        if n==0:
            return 1
        binary = []
        
        ans = n
        reminder = 0
        
        while ans:
            binary.append(ans % 2)
            ans = ans // 2
        
        binary = list(reversed(binary))
        inv_binary = [0 if i==1 else 1 for i in binary]
        
        ans = 0
        for ind, i in enumerate(reversed(inv_binary)):
            ans += i * 2**ind
        # print(binary)   
        return ans
        