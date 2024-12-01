class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        lengths = [len(word) for word in strs]
        print(lengths)

        min_length = min(lengths)
        shortest_str_idx = lengths.index(min_length)
        shortest_str = strs[shortest_str_idx]
        # print(min_length, shortest_str)

        ans = ''
        chars = ''

        for char in shortest_str:
            chars += char

            x = [word.startswith(chars) for word in strs]
            if all(x):
                ans = chars
            # print(chars, x, ans)
        return ans
        