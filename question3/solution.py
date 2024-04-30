class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_longest_substring_len = 0
        current_substring = ""
        current_substring_len = 0
        for char in s:
            if char not in current_substring:
                current_substring += char
                current_substring_len += 1
                if current_substring_len > last_longest_substring_len:
                    last_longest_substring_len = current_substring_len
                continue
            current_substring += char
            char_index = current_substring.find(char) + 1
            current_substring = current_substring[char_index:]
            current_substring_len = current_substring_len - char_index + 1

        return last_longest_substring_len
            