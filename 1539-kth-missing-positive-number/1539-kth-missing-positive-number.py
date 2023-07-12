class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        
        arr_set = set(arr)
        counter = 0
        for num in range(1, arr[-1]+k+1):
            
            if num not in arr_set:
                counter += 1
                
            if counter == k:
                return num