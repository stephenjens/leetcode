# 08/22/2022 09:54	Accepted	225 ms	13.9 MB	python3
from math import log, fabs
class Solution:

    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        while n % 3 == 0:
            n = n / 3
        if n == 1:
            return True
        else:
            return False
