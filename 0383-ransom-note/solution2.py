# 08/25/2022 11:39	Accepted	86 ms	14.3 MB	python3
# solution found in forum that's basically the same as mine but uses
# collections.Counter() and doesn't bother with missing letters

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomCounts = collections.Counter(ransomNote)
        magazineCounts = collections.Counter(magazine)

        for rnLetter, rnCount in ransomCounts.items():
            if rnLetter not in magazineCounts or magazineCounts[rnLetter] < rnCount:
                return False
        return True
