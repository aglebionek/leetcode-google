class Solution:
    def longestPalindrome(self, s: str) -> str:
        string_len = len(s)

        if string_len == 1: return s

        def is_palindrome(potential_palindrome: str) -> bool:
            potential_palindrome_len = len(potential_palindrome) >> 1
            j = -1
            for i in range(0, potential_palindrome_len):
                if potential_palindrome[i] != potential_palindrome[j]: return False
                j -= 1
            return True
        
        if is_palindrome(s): return s
        
        potential_palindromes = []
        for i in range(0, string_len):
            for j in range(string_len-1, i, -1):
                if s[i] == s[j]:
                    potential_palindrome = s[i:j+1]
                    if is_palindrome(potential_palindrome): 
                        potential_palindromes.append(potential_palindrome)
                        break

        if len(potential_palindromes) == 0: return s[0]
        potential_palindromes = sorted(potential_palindromes, key=len)

        return potential_palindromes[-1]