class Solution:
    def maxArea(self, heights: List[int]) -> int:

        left = 0
        right = len(heights) -1
        max_area = 0
        repeated = False
        # print(max_area)

        while right > left and not repeated:
            area = min(heights[right],heights[left]) * (right - left)

            max_area = area if area > max_area else max_area

            if heights[right] <= heights[left]:
                right -= 1
            else:
                left += 1
            # print(left, right, max_area)
            
        return max_area




        # for ind, hight in enumerate(heights):
        for ind in range(2, len(heights)):

            if (ind-left)*min(heights[ind],heights[left]) >= max_area:
                max_area = (ind-left)*min(heights[ind],heights[left])
                right = ind
                
            if min(heights[ind],heights[ind-1]) >= max_area and heights[ind-1] > heights[left]:
                max_area = min(heights[ind-1],heights[left])
                left = ind-1
            print(ind, left, right, max_area)
        
        return max_area
            


        