# 08/26/2022 14:25	Accepted	50 ms	13.7 MB	python3
class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        digits = sorted(str(n))
        for p in range(34):
            p2_digits = sorted(str(2**p))
            if digits == p2_digits:
                return True
        return False
