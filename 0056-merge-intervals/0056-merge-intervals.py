class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals = sorted(intervals)
        left = intervals[0][0]
        right = intervals[0][1]
        ans = []
        
        intervals = intervals[1:]
        
        for interval in intervals:
            if interval[0] <= right:
                right = interval[1] if interval[1] > right else right
            else:
                ans.append([left, right])
                left, right = interval[0], interval[1]
        
        ans.append([left, right])
        return ans