# 08/27/2022 18:23	Accepted	50 ms	13.9 MB	python3
class Solution:
    def intToRoman(self, num: int) -> str:
        roman = ''
        h = { 
            100: ['M', 'D', 'C'],
            10:  ['C', 'L', 'X'],
            1:   ['X', 'V', 'I']
        }
        seen = 0
        for div, digits in h.items():
            x = int((num - seen) / div)
            #print("div={} x={} seen={} roman={}".format(div, x, seen, roman))
            if x > 0:

                while x >= 10:
                    roman += digits[0] # 'M' 'C' 'X'
                    x -= 10
                    seen += 10 * div
                if x == 9:
                    roman += digits[2] + digits[0] #'CM' 'XC' 'IX' 
                    x -= 9
                    seen += 9 * div
                elif x >= 5:
                    roman += digits[1] # 'D' 'L' 'V'
                    x -= 5
                    seen += 5 * div
                elif x >= 4:
                    roman += digits[2] + digits[1] # 'CD' 'XL', 'IV'
                    x -= 4
                    seen += 4 * div
                while x > 0: 
                    roman += digits[2] # 'X' 'I'
                    x -= 1
                    seen += div
            
        return roman
