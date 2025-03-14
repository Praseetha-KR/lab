from collections import Counter


class Solution:
    # Time complexity : O(2n) == O(n)
    # Space complexity : O(min(m,n))

    def lengthOfLongestSubstring(self, s: str) -> int:
        window_counter = Counter()
        maxlen = 0
        i = 0
        j = 0
        while j < len(s):
            window_counter[s[j]] += 1
            while window_counter[s[j]] > 1:
                window_counter[s[i]] -= 1
                i += 1
            maxlen = max(maxlen, j + 1 - i)
            j += 1
        return maxlen
