class Solution:
    # Greedy Way (Optimized)
    # Time complexity: O(n)
    # Space complexity: O(1)

    def longestPalindrome(self, s: str) -> int:
        freq_map = {}
        odd_freq_count = 0
        for c in s:
            freq_map[c] = freq_map.get(c, 0) + 1
            if freq_map[c] % 2 == 1:
                odd_freq_count += 1
            else:
                odd_freq_count -= 1
        if odd_freq_count > 0:
            return len(s) - odd_freq_count + 1
        return len(s)
