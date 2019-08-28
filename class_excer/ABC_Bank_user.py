
data = {'alpha': {'password': [1234],
                  'balance': [2000]
                  },
        'beta': {'password': [4321],
                 'balance': [2000]
                 },
        'gamma': {'password': [9876],
                  'balance': [5000]
                  },
        }

chance = 3


class Customer_details():


    def __init__(self, name):
        self.name   = name

    def pin(self):
        for i in data:
            if i == 'passwprd':
                continue




print("Welcome to ABC Bank, \n Please Enter your name to procee")

name = input("Enter your name:  ")





