'''Given a string of odd length greater 7, return a string
made of the middle three chars of a given String'''


def midchar(strings):
    midindex = int(len(strings) / 2)
    print("The original string is: ", strings)
    midthree = strings[midindex - 1:midindex + 2]
    print("The middle three chars are: ", midthree)


midchar("JhonDipPeta")
midchar("Jasonay")
midchar("Kajendran")