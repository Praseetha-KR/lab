class Solution:
    # Time Complexity: O(jewels.length + stones.length))
    # Space Complexity: O(jewels.length)

    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewel_set = set(jewels)
        return sum(s in jewel_set for s in stones)
