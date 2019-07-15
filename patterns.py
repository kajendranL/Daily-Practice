

print("____________________________________________________________")
print("Pattern 1")
print()


n=6
for i in range(1, n+1):
    print("*"*n)   
    
print("____________________________________________________________")

print("Pattern 2")
print()
n=6
for i in range(1,n+1):
    for j in range (1, n+1):
        print(i, end='') # i printed
    print()
    
print()


print("____________________________________________________________")
print("Pattern 3")
print()

n=6
for i in range(1, n+1):
    for j in range(1,n+1):
        print(j, end='') # printed
    print()

print("____________________________________________________________")
print("Pattern 4")
print()

n=6
for i in range(1,n+1):
    for j in range (1,n+1):
        print(chr(64+i),end='')
    print()
print("____________________________________________________________")
print("Pattern 5")
print()

n=6
for i in range(1,n+1):
    for j in range(1, n+1):
        print(chr(64+j), end='')
    print()
    
print()
print("Pattern 5 Modified")
print()

n=6
for i in range(1,n+1):
    for j in range(1, n+1):
        print(chr(64+1), end='')
    print()
print("____________________________________________________________")

print("Pattern 6")
print()

n=6
for i in range(1,n+1):
    for j in range(1, n+1):
        print(n+1-i, end="")
    print()

print("____________________________________________________________")
print("Pattern 7")
print()

n=6
for i in range(1,n+1):
    for j in range(1,n+1):
        print(n+1-j, end='')
    print()
print("____________________________________________________________")
print("Pattern 8")
print()

n=8
for i in range(1, n+1):
    for j in range(1,n+1):
        print(chr(65+n-i),end='')
    print()

print("____________________________________________________________")
print("Pattern 9")
print()

n=8
for i in range(1,n+1):
    for j in range (1,n+1):
        print(chr(65+n-j),end='')
    print()

print("____________________________________________________________")
print("Pattern 10")
print()

n=8
for i in range(1,n+1):
    for j in range(1, i+1):
        print(i, end='')
    print()
    
    
print()
print("Pattern 10 Modified ")
print()

n=8
for i in range(1,n+1):
    for j in range(1, i+1):
        print("*", end='')
    print()
print("____________________________________________________________")
print("Pattern 10 similar to pattern 1's code")
print()


n=8
for i in range(1, n+1):
    print("*"*i)
print("____________________________________________________________")
print("Pattern 13")

print()
n=8
for i in range(1,n+1):
    for j in range(1, i+1):
        print(chr(64+j),end='')
    print()
print("____________________________________________________________")
print("Pattern 14")

print()
n=8

for i in range(1, n+1):
    for j in range(1,n+2 -i):
        print("*", end='')
    print()
print("____________________________________________________________")


print("Pattern 13 +14 Combined")
n=10
for i in range(1,n+1):
    for j in range(1, i+1):
        print("*",end='')
    print()
for i in range(1, n+1):
    for j in range(1,n+2 -i):
        print("*", end='')
    print()
print("____________________________________________________________")

print("Pattern 13 +14 Combined II")
n=10
for i in range(1,n+1):
    for j in range(1, i+1):
        print(i,end='')
    print()
for i in range(1, n+1):
    for j in range(1,n+2 -i):
        print(i, end='')
    print()
print("____________________________________________________________")




