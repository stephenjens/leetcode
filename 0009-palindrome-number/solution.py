# 08/22/2022 14:02	Accepted	83 ms	13.9 MB	python3
class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = list(str(x))
        r = [c for c in reversed(s)]
        
        return s == r
