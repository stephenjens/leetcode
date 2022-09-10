# 09/10/2022 14:49	Accepted	415 ms	14.5 MB	python3
# more python-esque solution
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        char_counts = collections.Counter(chars)
        total_length = 0

        for word in words:
            word_counts = collections.Counter(word)
            if all(word_counts[c] <= char_counts[c] for c in word_counts):
                total_length += len(word)
        
        return total_length
