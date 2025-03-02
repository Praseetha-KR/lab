class Solution:
    # Time Complexity: O(jewels.length ∗ stones.length))
    # Space Complexity: O(1)

    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return sum(s in jewels for s in stones)
