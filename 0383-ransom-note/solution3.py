# 08/25/2022 11:43	Accepted	79 ms	14.1 MB	python3
# another one from the forum that's a bit faster and uses less memory than
# solution1.py and solution2.py. I also tried pre-sorting the strings, and the
# time and memory both jumped. Storing magazine in a counter and decrementing
# it only had a marginal speedup over this solution, and it took a bit more
# memory.

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for c in ransomNote:
            if c not in magazine:
                return False
            magazine = magazine.replace(c, '', 1)
        return True
