class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:

        counter = 0

        for num in range(1, arr[-1]+k+1):
            if num not in arr:
                counter +=1

            if counter == k:
                return num