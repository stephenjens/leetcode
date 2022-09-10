# 09/10/2022 14:20	Accepted	121 ms	13.8 MB	python3
# using a hashmap
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        counts = {}
        for cpdomain in cpdomains:
            count, domain = cpdomain.split(" ")
            count = int(count)
            
            parts = domain.split(".")
            for i in range(0, len(parts)):
                key = ".".join(parts[i:len(parts)])
                if key not in counts:
                    counts[key] = 0
                counts[key] += count
        return [f'{counts[key]} {key}' for key in counts]
