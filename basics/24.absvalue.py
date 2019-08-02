print("Write a Python program which will return true if the two given integer values are equal or their sum or difference is 5")

print()


def absvalue(x,y):
    if x == y or x-y ==5 or x+y ==5:
        return True
    else:
        return False


print(absvalue(7,2))
print(absvalue(2,2))
print(absvalue(3,2))
print(absvalue(23,8))
