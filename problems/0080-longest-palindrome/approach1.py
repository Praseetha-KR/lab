from collections import Counter


class Solution:
    # Greedy Way (Hash Table)
    # Time complexity: O(n)
    # Space complexity: O(1)

    def longestPalindrome(self, s: str) -> int:
        counter = Counter(s)
        palindrome_len = odd_count = 0
        for ch in counter:
            count = counter[ch]
            palindrome_len += (count // 2) * 2
            odd_count += count % 2

        if odd_count > 0:
            palindrome_len += 1
        return palindrome_len
