# 09/10/2022 14:44	Accepted	230 ms	14.6 MB	python3
class Solution:
    
    def count(word: str) -> dict:
        counts = {}
        for c in word:
            if c not in counts:
                counts[c] = 0
            counts[c] += 1
        return counts
    
    def countCharacters(self, words: List[str], chars: str) -> int:
        char_counts = Solution.count(chars)

        total_length = 0
        for word in words:
            word_counts = Solution.count(word)

            good = True
            for c in word_counts:
                if c not in char_counts or word_counts[c] > char_counts[c]:
                    good = False
                    break
            if good:
                total_length += len(word)
        
        return total_length
