from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        visited = {}
        
        for word in strs:
            
            ordered = str(sorted(word))
            
            if ordered in visited.keys():
                visited[ordered].append(word)
            else:
                visited[ordered] = [word]
            
        return list(visited.values())