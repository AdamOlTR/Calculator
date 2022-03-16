# -*- coding: iso-8859-1 -*-
num1 = input("Enter the first number:")
oper = input("Which arithmetic operation should be performed? (+,-,/.,*): ")
num2 = input("Enter the second number: ")

num1 = int(num1)
num2 = int(num2)

if (oper == "+"):
    print("Your calculation is:", num1, " + ", num2)
    print("Result:", num1 + num2)

elif (oper == "-"):
    print("Your calculation is:", num1, " - ", num2)
    print("Result:", num1 - num2)

elif (oper == "/"):
    print("Your calculation is:", num1, " / ", num2)
    print("Result:", num1 / num2)

elif (oper == "*"):
    print("Your calculation is:", num1, " * ", num2)
    print("Result:", num1 * num2)
else:
    print("Your entries are not valid")