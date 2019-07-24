print("Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return instead of the empty string")

print()

def replace_Str(str):
    if len(str)<2:
        return (str)
    return str[0:2] + str[-2:]

print(replace_Str('return'))
print(replace_Str('genesis'))
print(replace_Str('w3'))