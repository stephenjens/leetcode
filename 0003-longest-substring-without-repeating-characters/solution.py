# 08/23/2022 11:18	Accepted	1169 ms	13.9 MB	python3
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if len(s) == 0:
            return 0
        
        i = 0
        current = ''
        max_size = -1
        while i < len(s):
            for j in range(i, len(s)):
                char = s[j]
                repeated_pos = current.find(char)
                #print("char: {} pos: {} i: {} j: {} max: {}, current: '{}' ".
                #      format(char, repeated_pos, i, j, max_size, current))
                if repeated_pos == -1:
                    current += char
                else:
                    if len(current) > max_size:
                        max_size = len(current)
                    current = ''
                    i += repeated_pos + 1
                    break
            
            
        return max_size
            
