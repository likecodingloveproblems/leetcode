class Solution:
    def intToRoman(self, num: int) -> str:
        decimal_roman_map = {
            1000: "M",
            900: "CM",
            500: "D",
            400: "CD",
            100: "C",
            90: "XC",
            50: "L",
            40: "XL",
            10: "X",
            9: "IX",
            5: "V",
            4: "IV",
            1: "I",
        }
        result = ""
        for decimal, roman in decimal_roman_map.items():
            if num // decimal:
                result += roman * (num // decimal)
                num -= decimal * (num // decimal)
        return result


n = 3
n = 58
n = 1994
print(Solution().intToRoman(n))
