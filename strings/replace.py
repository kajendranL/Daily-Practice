print("Get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself")

print()

def replace_str(str1):
    char = str1[0]
    str1 = str1.replace(char, '@')
    str1 = char + str1[1:]

    return str1

print(replace_str('restart'))
print(replace_str('return'))
print(replace_str('that'))
print(replace_str('since'))

print()


def replace_char(str1):
    idx = str1[1]

    str1 = str1.replace(idx, '@')

    str1 = str1 [0] + idx + str1[2:]

    return str1

print(replace_char('Malayalam'))
print(replace_char("Rajapalayam"))
print(replace_char("book"))
