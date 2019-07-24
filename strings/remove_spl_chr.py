def remove_spl_char(str,n):
    first = str[:n]
    second = str[3+1:]
    return first + second

print(remove_spl_char('python', 0))
print(remove_spl_char('python', 3))
print(remove_spl_char('python', 2))


print()

def remove_2(list1, n):
    return list1[:n] + list1[3+1:]

print(remove_2('python',3))

