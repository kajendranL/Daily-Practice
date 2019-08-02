def LCM(x, y):
    if x > y :
        z = x
    else:
        z = y

    while True:
        if ((z % x == 0) and z % y == 0):
            lcm =z
            break

        z+=1


    return lcm

print(LCM(12,30))

