def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    if b!=0:
        return a/b
    else:
        return "Error: Division by zero"
while True:
    print("Select operation:")
    print("1.addition")
    print("2.subtraction")
    print("3.multiplication")
    print("4.division")
    print("5.exit")
    choice = input("Enter choice(1/2/3/4):")
    if choice in ('1','2','3','4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if choice == '1':
            print(num1,"+",num2,"=", add(num1,num2))
        elif choice == '2':
            print(num1,"-",num2,"=", sub(num1,num2))
        elif choice == '3':
            print(num1,"*",num2,"=", mul(num1,num2))
        elif choice == '4':
            print(num1,"/",num2,"=", div(num1,num2))
        elif choice == '5':
            break
    else:
        print("Invalid Input")
