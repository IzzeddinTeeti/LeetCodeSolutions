import collections

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        count = collections.Counter(words)
        
        sorted_count = sorted(count.keys(), key=lambda word: (-count[word], word))
        
        return sorted_count[:k]
        print(count)
        
        
        