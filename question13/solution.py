class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        s_len = len(s) - 1
        values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000 }

        last_int = 0
        for i in range(s_len, -1, -1):
            itp = values[s[i]]
            if itp >= last_int:
                result += itp
                last_int = itp
                continue
            result -= itp
            last_int = itp

        return result