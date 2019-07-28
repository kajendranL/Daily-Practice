print('''Write a Python program to find the 
list of words that are longer than n from a given list of words''')

print()


def long_words(n, str1):
    word_len = []

    txt = str1.split()

    for i in txt:
        if len(i) > n:
            word_len.append(i)
    return word_len


print(long_words(3, "The quick brown fox jumps over the lazy dog"))

####################OR OR OR OR OR OR OR #####################

print()


def lon_words(n, lst):
    return ([x for x in str.split('') if len(x) > n])


print(long_words(3, "The quick brown fox jumps over the lazy dog."))
