# 08/26/2022 15:13	Accepted	41 ms	14 MB	python3
class HitCounter:

    def __init__(self):
        self.hits = []       

    def _prune(self, prune_at=None):
        #print("{}".format(self.hits))
        if len(self.hits) > 0:
            prune_at = self.hits[len(self.hits) - 1] if prune_at is None else prune_at
            #print("prune_at {}".format(prune_at))
            while len(self.hits) > 0 and prune_at - self.hits[0] >= 300:
                pruned = self.hits.pop(0)
                #print("pruned {}".format(pruned))
        
    def hit(self, timestamp: int) -> None:
        self.hits.append(timestamp)
        self._prune()
        
    def getHits(self, timestamp: int) -> int:
        self._prune(timestamp)
        #print("getHits @ {}: {}".format(timestamp, len(self.hits)))
        
        return len(self.hits)

