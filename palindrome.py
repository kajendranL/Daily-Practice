'''Ask the user for a string and print out whether this string is a palindrome or not.
(A palindrome is a string that reads the same forwards and backwards.)'''

word = input("Enter a word: ").strip()
reverse = word[::-1]

if word == reverse:
    print("This word", word, " is a palindrome")
else:
    print("This word", word, "is not a palindrome")



