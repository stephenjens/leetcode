# 08/26/2022 14:29	Accepted	4315 ms	13.8 MB	python3
# heckin slow solution that actually does all the permutations (copied from solutions tab)
class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        return any(cand[0] != '0' and bin(int("".join(cand))).count('1') == 1
                   for cand in itertools.permutations(str(n)))
