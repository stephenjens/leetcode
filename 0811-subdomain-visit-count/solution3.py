# 09/10/2022 14:29	Accepted	111 ms	13.9 MB	python3
# hashamp with str.find() instead of splitting domain by '.'
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        counts = {}
        for cpdomain in cpdomains:
            count, domain = cpdomain.split(" ")
            count = int(count)
            
            c = 0
            pos = -1
            while True:
                key = domain[(pos+1):]
                if key not in counts:
                    counts[key] = 0
                counts[key] += count
                pos = domain.find('.', pos + 1)
                if pos == -1:
                    break

        return [f'{counts[key]} {key}' for key in counts]
                
