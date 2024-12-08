from Test1 import *
from Test2 import *
from Test3 import *
from Test4 import *

def myFun():
    cre_tab()
    cre_trans()
    cre_bud()

    while True:
        print("\n1. Register\n2. Login\n3. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            username = input("Enter username: ")
            password = input("Enter password: ")
            register_user(username, password)
        elif choice == '2':
            username = input("Enter username: ")
            password = input("Enter password: ")
            if authenticate_user(username, password):
                print("Login successful!")
            else:
                print("Invalid credentials!")
        elif choice == '3':
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    myFun()
