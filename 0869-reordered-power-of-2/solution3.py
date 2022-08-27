# 08/26/2022 19:58	Accepted	48 ms	13.8 MB	python3
class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        digits = sorted(str(n))
        p = 0
        while True:
            p2_digits = sorted(str(2**p))
            if len(p2_digits) > len(digits):
                break
            elif digits == p2_digits:
                return True
            p += 1
            
        return False
