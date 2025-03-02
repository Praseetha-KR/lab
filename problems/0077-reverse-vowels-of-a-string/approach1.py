class Solution:
    VOWELS = set(["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"])

    def reverseVowels(self, s: str) -> str:
        i = 0
        j = len(s) - 1
        chars = list(s)
        while i < j:
            if chars[i] not in self.VOWELS:
                i += 1
                continue
            if chars[j] not in self.VOWELS:
                j -= 1
                continue
            temp = chars[i]
            chars[i] = chars[j]
            chars[j] = temp
            i += 1
            j -= 1
        return "".join(chars)
