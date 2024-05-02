class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ''
        i = 0
        one_string = strs.pop()
        while True:
            try:
                current_letter = one_string[i]
                for string in strs:
                    if string[i] != current_letter: raise Exception()
                result += current_letter
                i += 1
            except:
                break
        return result
        