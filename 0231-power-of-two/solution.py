# 08/22/2022 09:47	Accepted	63 ms	13.8 MB	python3
from math import log2, fabs
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 1:
            return False
        
        x = log2(n)
        if x == 0.0:
            return True
        elif x >= 1:
            return float(int(x)) == x
        else:
            return False
