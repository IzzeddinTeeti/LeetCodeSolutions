class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if len(s) ==1:
            return 1
        elif len(s) ==0:
            return 0
        
        char_set = set()  # To store unique characters in the current window
        left = 0          # Left pointer of the sliding window
        max_length = 0    # Variable to store the maximum length

        for right in range(len(s)):  # Right pointer of the sliding window
            # If a character is repeated, shrink the window from the left
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            # Add the current character to the set and update max_length
            char_set.add(s[right])
            max_length = max(max_length, right - left + 1)

        return max_length
                
            
            
            
        