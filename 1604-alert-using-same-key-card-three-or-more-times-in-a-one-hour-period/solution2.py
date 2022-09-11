# 09/11/2022 11:19	Accepted	1625 ms	35 MB	python3

# less janky sliding window copied from discussion
# slightly cleaner use of map(int, ...) to turn hours and minutes into ints
# cleaner iteration over by_person using .items()
class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        by_person = {}
        for person, timestamp in zip(keyName, keyTime):
            if person not in by_person:
                by_person[person] = []
            h, m = map(int, timestamp.split(':'))
            timestamp_m = 60 * h + m
            by_person[person].append(timestamp_m)
        
        alerts = []
        
        for person, times in by_person.items():
            times.sort()
            for i in range(2, len(times)):
                if i >= 2 and times[i] - times[i - 2] <= 60:
                    alerts.append(person)
                    break

        alerts.sort()
        return alerts
