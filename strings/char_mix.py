print("Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string")

print()

def mix_char_up(a,b):
    new_a = b[:2] + a[2:]
    new_b = a[:2] + b[2:]

    return new_a + ' ' + new_b

print(mix_char_up('abc', 'xyz'))
print(mix_char_up('123', 'abcd'))


def chars_mix_up(a,b,c):
    x = c[2] + b[1] + a[0]

    y =  b[2] + c[0] + a[1]

    z = c[1] + a[2] + b[0]

    return x + " " + y + " " + z

print(chars_mix_up('abc', '123', 'xyz' ))