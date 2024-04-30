class Solution:
    def reverse(self, x: int) -> int:
        upper_limit = 0x80000000
        lower_limit = -0x80000000

        sign = ''
        x_str = str(x)
        if x_str[0] == '-':
            sign = '-'
            x_str = x_str[1:]

        result = int(sign + x_str[::-1])

        if result >= upper_limit: return 0
        if result < lower_limit: return 0
        return result