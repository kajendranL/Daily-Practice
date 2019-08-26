# Write a Python program to convert an integer to a roman numeral

class Py_solution:
    def Arab_to_Roman(self, num):
        Arab = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
            ]
        Roman = [
            'M', 'CM', 'D', 'CD'
            'C', 'XC', 'L', 'XL'
            'X', 'IX', 'V', 'IV'
            'I'
            ]

        roman_num = ''
        i = 0
        while num > 0:
            for j in range(num // Arab[i]):
                roman_num += Roman[i]
                num -= Arab[i]

            i += 1
        return roman_num
print(Py_solution().Arab_to_Roman(1))
print(Py_solution().Arab_to_Roman(4000))

