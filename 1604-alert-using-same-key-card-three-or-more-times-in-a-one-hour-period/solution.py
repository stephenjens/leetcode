# 09/11/2022 11:14	Accepted	1696 ms	38.4 MB	python3

class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        by_person = {}
        for person, timestamp in zip(keyName, keyTime):
            if person not in by_person:
                by_person[person] = []
            h, m = timestamp.split(':')
            timestamp_m = (60 * int(h)) + int(m)
            by_person[person].append(timestamp_m)
        
        alerts = []
        for person in by_person:
            times = by_person[person]
            times.sort()
            
            start_ix = 0
            pos = 1
            while pos < len(times):
                if times[pos] - times[start_ix] <= 60:
                    pos += 1
                    if pos - start_ix >= 3:
                        break
                else:
                    while start_ix < pos and times[pos] - times[start_ix] > 60:
                        start_ix += 1
            if pos - start_ix >= 3:
                alerts.append(person)
        alerts.sort()
        return alerts
