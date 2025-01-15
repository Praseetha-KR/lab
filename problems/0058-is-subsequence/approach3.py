class Solution:
    # Greedy
    # Time Complexity: O(∣T∣)
    # Space Complexity: O(|T|)
    def isSubsequence(self, s: str, t: str) -> bool:
        LEFT_BOUND = len(s)
        RIGHT_BOUND = len(t)

        def is_subseq(s_index: int, t_index: int) -> bool:
            if s_index == LEFT_BOUND:
                return True
            if t_index == RIGHT_BOUND:
                return False
            if s[s_index] == t[t_index]:
                s_index += 1
            t_index += 1
            return is_subseq(s_index, t_index)

        return is_subseq(0, 0)
