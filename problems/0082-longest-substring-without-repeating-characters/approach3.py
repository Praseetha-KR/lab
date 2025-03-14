class Solution:
    # Time complexity : O(n)
    # Space complexity : O(n)

    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlen = 0
        i = 0
        char_to_next_index = {}
        for j in range(len(s)):
            if s[j] in char_to_next_index:
                i = max(char_to_next_index[s[j]], i)
            maxlen = max(maxlen, j + 1 - i)
            char_to_next_index[s[j]] = j + 1
        return maxlen
