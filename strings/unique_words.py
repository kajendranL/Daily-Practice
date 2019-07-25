print('''Prints the unique words in sorted 
form from a comma separated sequence of words''')

print()

def unique_word(words):
    for n in words:
        print(','.join(sorted(list(set(n)))))

item = input("Enter the words: ").split()
print(unique_word(item))


print()

items = input("Input comma separated sequence of words")
words = [word for word in items.split(",")]
print(",".join(sorted(list(set(words)))))