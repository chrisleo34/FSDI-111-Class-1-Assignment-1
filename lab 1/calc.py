"""
Author: Christian Astarita
Title: Symple Python
"""

# global vars

# functions


def print_separator():
    print('_' * 30)


def print_menu():
    print_separator()

    print('Python Calc')
    print_separator()

    print("[1] Sum")
    print("[2] Subtract")
    print("[3] Multiply")
    print("[4] Divide")
    print("[x] Exit")

    print_separator()


def clear():
    # HomeWork clear screen python script
    lst1 = [[1], [2], [3], [4]]
    lst2 = lst1
    del lst1[:]


print("\n\n\n")

# direct instrunctions


opc = ''
while(opc != 'x'):

    print_menu()
    # input creates a pause, until you press enter( reads as a string)
    opc = input('Please choose an option: ')

    # print(opc) use this code to check if the code is working
    if(opc == 'x'):
        break

    num1 = float(input('Provide num 1: '))
    num2 = float(input('Provide num 2: '))

    if(opc == '1'):
        print(num1 + num2)
    elif(opc == '2'):
        print(num1 - num2)

    elif(opc == '3'):
        print(num1 * num2)

    elif(opc == '4'):
        if(num2 == 0):
            print("error, zero divison not allowed")
        else:
            print(num1 / num2)

    else:
        print("Please choose a valid option")

    input("Press Enter to continue...")
    clear()

print('Good Bye!!')
