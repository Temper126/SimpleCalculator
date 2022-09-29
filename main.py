# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')








# ****** Learning to build a Simple Calculator ******

# 1. ADD
# 2. SUBTRACT
# 3. MULTIPLY
# 4. DIVIDE


print("Select an operation to perform: ")
print("1. ADD")
print("2. SUBTRACT")
print("3. MULTIPLY")
print("4. DIVIDE")

operation = input()

if operation == "1":
    num1 = input("Enter first number:")
    num2 = input("Enter second number:")
    print("The Sum is:" + str(int(num1) + int(num2)))
elif operation == "2":
    num1 = input("Enter first number:")
    num2 = input("Enter second number:")
    print("The difference is:" + str(int(num1) - int(num2)))
elif operation == "3":
    num1 = input("Enter first number:")
    num2 = input("Enter second number:")
    print("The product is:" + str(int(num1) * int(num2)))
elif operation == "4":
    num1 = input("Enter first number:")
    num2 = input("Enter second number:")
    print("The result is:" + str(float(num1) / float(num2)))
else:
    print("Invalid Entry!")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
