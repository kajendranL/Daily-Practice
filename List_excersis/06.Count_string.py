print('''Write a Python program to count the number of strings where the string length is 2 
or more and the first and last character are same from a given list of strings''')

print()

def count_str(list):
    count = 0

    for s in list:
        if len(s)>1 and s[0] == s[-1]:
            count+=1

    return count

print(count_str(['abc','123','xyz','564','123']))
print(count_str(['abc','123','xyz','abc','123']))