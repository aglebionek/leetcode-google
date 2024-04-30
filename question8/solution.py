class Solution:
    def myAtoi(self, s: str) -> int:
        upper_limit = 0x80000000 - 1
        lower_limit = -0x80000000

        s = s.strip()
        result = ''
        sign = ''
        for x in s:
            if x == '-' or x == '+':
                if sign != '' or result != '': break
                sign = x
                continue
            if not x.isdigit():
                break
            result += x
        
        if len(result) == 0: result = '0'
        result = int(sign + result)
        
        if result > upper_limit: return upper_limit
        if result < lower_limit: return lower_limit
        return result
