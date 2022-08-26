# 08/25/2022 11:32	Accepted	101 ms	14.2 MB	python3
import string

class Solution:
    def countLetters(s: str) -> dict:
        counts = {letter: 0 for letter in list(string.ascii_lowercase)}
        for letter in s:
            counts[letter] += 1
        return counts
    
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomCount = Solution.countLetters(ransomNote)
        magazineCount = Solution.countLetters(magazine)
        for letter in list(string.ascii_lowercase):
            if magazineCount[letter] < ransomCount[letter]:
                return False
        
        return True
