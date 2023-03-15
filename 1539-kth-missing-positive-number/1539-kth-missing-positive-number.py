class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:

        counter = 0

        for num in range(1, arr[-1]+k+1):
            if num not in arr:
                counter +=1

            if counter == k:
                return num
            
            
            
# https://leetcode.com/problems/kth-missing-positive-number/discuss/3262163/C%2B%2B-Java-Python3-1-line-O(logn)
    
# https://leetcode.com/problems/kth-missing-positive-number/discuss/3262072/Python3-oror-44-ms-faster-than-96.22-of-Python3