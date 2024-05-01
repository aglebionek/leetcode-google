class Solution:
    def intToRoman(self, num: int) -> str:
        result = ''
        num_str = str(num)
        number_of_digits = len(num_str)
        symbols = ["I", "V", "X",  "L", "C", "D", "M"]
        numbers = [1, 5, 10, 50, 100, 500, 1000]
        values = dict(zip(numbers, symbols))
        number_of_symbols = len(symbols)
        preceeding_symbols = ["I", "X", "C"]

        def find_nearest_symbol(x: int, first_digit: str):
            if first_digit != '4' and first_digit != '9':
                for i in range(0, number_of_symbols):
                    if x - numbers[i] >= 0: continue

                    return symbols[i-1], numbers[i-1]

                return symbols[-1], numbers[-1]
            
            number_to_append = int('1'+'0'*number_of_digits)
            return preceeding_symbols[number_of_digits]+values[x+number_to_append],9999

        for digit in num_str:
            number_of_digits -= 1
            if digit == '0': continue
            current_number_as_str = digit + '0'*number_of_digits
            current_number_as_int = int(current_number_as_str)
            while True:
                nearest_number_in_roman, nearest_number_in_arabic = find_nearest_symbol(current_number_as_int, digit)
                result += nearest_number_in_roman
                current_number_as_int -= nearest_number_in_arabic
                if current_number_as_int <= 0: break

        return result