class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        return self.kmp_search(s + s, goal)

    def kmp_search(self, text: str, pattern: str) -> bool:
        lps = self.compute_longest_prefix_suffix(pattern)
        txt_idx = pat_idx = 0
        txt_len = len(text)
        pat_len = len(pattern)
        while txt_idx < txt_len:
            if text[txt_idx] == pattern[pat_idx]:
                txt_idx += 1
                pat_idx += 1
                if pat_idx == pat_len:
                    return True
            elif pat_idx > 0:
                pat_idx = lps[pat_idx - 1]
            else:
                txt_idx += 1
        return False

    def compute_longest_prefix_suffix(self, pattern: str) -> list:
        pat_len = len(pattern)
        lps = [0] * pat_len
        length = 0
        i = 1

        while i < pat_len:
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            elif length > 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
        return lps
