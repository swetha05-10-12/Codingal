class RomanConverter:
    def __init__(self, number):
        self.number = number

    def to_roman(self):
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4, 1
        ]
        rom = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV", "I"
        ]
        roman_num = ""
        num = self.number
        for i in range(len(val)):
            count = num // val[i]
            roman_num += rom[i] * count
            num -= val[i] * count
        return roman_num


user_input = int(input("Enter an integer: "))
converter = RomanConverter(user_input)
print("Roman Numeral:", converter.to_roman())