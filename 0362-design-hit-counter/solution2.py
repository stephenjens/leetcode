# 08/26/2022 18:32	Accepted	34 ms	13.8 MB	python3
# same as solution.py but uses a collections.deque() instead of a
# list. popleft() is O(1) for a deque while pop(0) is O(n) for a list.
class HitCounter:
    def __init__(self):
        self.hits = collections.deque()  

    def _prune(self, prune_at=None):
          if len(self.hits) > 0:
            prune_at = self.hits[len(self.hits) - 1] if prune_at is None else prune_at
              while len(self.hits) > 0 and prune_at - self.hits[0] >= 300:
                pruned = self.hits.popleft()
          
    def hit(self, timestamp: int) -> None:
        self.hits.append(timestamp)
        self._prune()
        
    def getHits(self, timestamp: int) -> int:
        self._prune(timestamp)
          
        return len(self.hits)
