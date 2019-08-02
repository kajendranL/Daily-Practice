print(
    "Get a new string from a given string where 'Is' has been added to the front. If the given string already begins with 'Is' then return the string unchanged")

print()


def new_string(str):
    if len(str) >= 2 and len(str[:2]) == 'Is':
        return str

    else:
        return "Is" + str


print(new_string('Array'))
print(new_string('Isnumber'))
