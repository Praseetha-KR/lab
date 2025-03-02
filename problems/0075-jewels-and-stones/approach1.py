from collections import Counter


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        stone_counter = Counter(stones)
        jewel_count = 0
        for j in jewels:
            jewel_count += stone_counter[j]
        return jewel_count
