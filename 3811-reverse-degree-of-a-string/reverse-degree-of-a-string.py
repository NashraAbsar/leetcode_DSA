class Solution:
    def reverseDegree(self, s: str) -> int:
        total_deg = 0
        for i, char in enumerate(s):
            rev_alpha_pos = 26 - (ord(char) - ord('a'))
            string_pos = i + 1
            total_deg += rev_alpha_pos * string_pos
        return total_deg
