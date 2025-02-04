'''
Write a function to convert a given number n into words.

The idea is to break down the number into International Number System, i.e., smaller groups of three digits (hundreds, tens, and ones), and convert each group into words.

Examples :

Input: n = 0
Output: "Zero"
Input: n = 123
Output: "One Hundred Twenty Three"
Input: n = 10245
Output: "Ten Thousand Two Hundred Forty Five"
Input: n = 2147483647
Output: "Two Billion One Hundred Forty Seven Million Four Hundred Eighty Three Thousand Six Hundred Forty Seven"
Constraints:
0 <= n <= 231-1
'''
def numberToWords(n):
    if n == 0:
        return "Zero"

    def one(num):
        switcher = {
            1: 'One',
            2: 'Two',
            3: 'Three',
            4: 'Four',
            5: 'Five',
            6: 'Six',
            7: 'Seven',
            8: 'Eight',
            9: 'Nine'
        }
        return switcher.get(num)

    def two_less_20(num):
        switcher = {
            10: 'Ten',
            11: 'Eleven',
            12: 'Twelve',
            13: 'Thirteen',
            14: 'Fourteen',
            15: 'Fifteen',
            16: 'Sixteen',
            17: 'Seventeen',
            18: 'Eighteen',
            19: 'Nineteen'
        }
        return switcher.get(num)

    def ten(num):
        switcher = {
            2: 'Twenty',
            3: 'Thirty',
            4: 'Forty',
            5: 'Fifty',
            6: 'Sixty',
            7: 'Seventy',
            8: 'Eighty',
            9: 'Ninety'
        }
        return switcher.get(num)

    def two(num):
        if not num:
            return ''
        elif num < 10:
            return one(num)
        elif num < 20:
            return two_less_20(num)
        else:
            tenner = num // 10
            rest = num - tenner * 10
            return ten(tenner) + ' ' + one(rest) if rest else ten(tenner)

    def three(num):
        hundred = num // 100
        rest = num - hundred * 100
        if hundred and rest:
            return one(hundred) + ' Hundred ' + two(rest)
        elif not hundred and rest:
            return two(rest)
        elif hundred and not rest:
            return one(hundred) + ' Hundred'

    billion = n // 1000000000
    million = (n - billion * 1000000000) // 1000000
    thousand = (n - billion * 1000000000 - million * 1000000) // 1000
    rest = n - billion * 1000000000 - million * 1000000 - thousand * 1000

    result = ''
    if billion:
        result += three(billion) + ' Billion'
    if million:
        result += ' ' if result else ''
        result += three(million) + ' Million'
    if thousand:
        result += ' ' if result else ''
        result += three(thousand) + ' Thousand'
    if rest:
        result += ' ' if result else ''
        result += three(rest)
    return result

# Example usage
n = 123
print(numberToWords(n))  # Output: "One Hundred Twenty Three"

n = 10245
print(numberToWords(n))  # Output: "Ten Thousand Two Hundred Forty Five"

n = 2147483647
print(numberToWords(n))  # Output: "Two Billion One Hundred Forty Seven Million Four Hundred Eighty Three Thousand Six Hundred Forty Seven"
