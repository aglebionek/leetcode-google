class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False

        x_str = str(x)
        x_str_len = len(x_str)
        halved_index = x_str_len >> 1
        j = -1
        for i in range(0, halved_index):
            if x_str[i] != x_str[j]: return False
            j -= 1

        return True