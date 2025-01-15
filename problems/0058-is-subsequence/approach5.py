class Solution:
    # DP
    # Time Complexity: O(∣S∣⋅∣T∣)
    # Space Complexity: O(∣S∣⋅∣T∣)
    def isSubsequence(self, s: str, t: str) -> bool:
        s_len, t_len = len(s), len(t)
        if s_len == 0:
            return True

        dp = [[0] * (t_len + 1) for _ in range(s_len + 1)]
        for col in range(1, t_len + 1):
            for row in range(1, s_len + 1):
                if s[row - 1] == t[col - 1]:
                    dp[row][col] = dp[row - 1][col - 1] + 1
                else:
                    dp[row][col] = max(dp[row][col - 1], dp[row - 1][col])
            if dp[s_len][col] == s_len:
                return True
        return False
