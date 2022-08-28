class Solution:
    def romanToInt(self, s: str) -> int:
        value = 0
        tokens = collections.deque(s)
        current = ''
        while len(tokens) > 0:
            current = tokens.popleft()
            nextToken = tokens[0] if len(tokens) > 0 else None
            #print("current: {}".format(current))
            if current == 'I':
                if nextToken == 'V':
                    tokens.popleft()
                    value += 4
                elif nextToken == 'X':
                    tokens.popleft()
                    value += 9
                else:
                    value += 1
                    
            elif current == 'V':
                value += 5
            elif current == 'X':
                if nextToken == 'L':
                    value += 40
                    tokens.popleft()
                elif nextToken == 'C':
                    value += 90
                    tokens.popleft()
                else:
                    value += 10
            elif current == 'L':
                value += 50
            elif current == 'C':
                if nextToken == 'D':
                    value += 400
                    tokens.popleft()
                elif nextToken == 'M':
                    value += 900
                    tokens.popleft()
                else:
                    value += 100
            elif current == 'D':
                value += 500
            elif current == 'M':
                value += 1000
        return value
