import bisect
from collections import defaultdict


class Solution:
    # Time Complexity: O(∣T∣+∣S∣⋅log∣T∣)
    # Space Complexity: O(∣T∣)
    def isSubsequence(self, s: str, t: str) -> bool:
        m = defaultdict(list)
        for i, c in enumerate(t):
            m[c].append(i)

        current_match_index = -1
        for c in s:
            if c not in m:
                return False
            char_positions = m[c]
            match_index = bisect.bisect_right(char_positions, current_match_index)
            # Note: Python bisect is faster than linear search or binary search
            if match_index == len(char_positions):
                return False
            current_match_index = char_positions[match_index]
        return True
