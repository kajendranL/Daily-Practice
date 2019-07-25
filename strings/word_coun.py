print("""Write a Python program to remove the characters 
which have odd index values of a given string""")

print()

def word_count(str):
    counts = dict()
    word = str.split()

    for n in word:
        if n in counts:
            counts[n] += 1

        else:
            counts[n] = 1

    return counts

print(word_count('the quick brown fox jumps over the lazy dog.'))
