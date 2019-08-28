
complete = False

user = { "Amala" : 123456,
         "Yazhini": 256431,
         "Epifano": 564789,
        }
while not complete:
    username = input("Enter user name: ")
    password = input("Enter password: ")

    if username == username and password == password:
        continue

    elif username not in user:
        print("This is invalid name, please re enter")
        continue
    elif password != user[username]:
        print("User name or password is not right")
        continue

    elif password == user[username]:
        print("Welcome", username)
        print("Thankyou for logging in")
        complete =  True

print("User name and Password validated by python")

