# 08/22/2022 09:29	Accepted	62 ms	13.9 MB	python3
import math

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        else:
            return math.log2(math.fabs(n)) % 2 == 0.0
        
