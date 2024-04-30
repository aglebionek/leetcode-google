class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s
        array = []
        for _ in range(0, numRows):
            array.append("")

        move_down = True
        row_index = 1
        max_index = numRows - 1
        array[0] += s[0]
        for i in range(1, len(s)):
            letter = s[i]
            array[row_index] += letter
            if row_index % max_index == 0:
                move_down = not move_down
            if move_down:
                row_index += 1
                continue
            row_index -= 1

        return ''.join(array)