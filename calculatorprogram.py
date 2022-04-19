def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

print("Select Operation")
print("1.Addition")
print("2.Subtraction")
print("3.Mulptiplication")
print("4. Division")

while True:

    choice = input("Enter Choice (1/2/3/4):")

    if choice in ('1','2','3','4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1,num2))

        if choice == '2':
            print(num1, "-", num2, "=", subtract(num1,num2))

        if choice == '3':
            print(num1, "*", num2, "=", multiply(num1,num2))
        
        if choice == '4':
            print(num1, "/", num2, "=", divide(num1,num2))

        next_calculation = input("Would you like to continue?(yes/no): ")
        if next_calculation == "no":
            break
    else:
        print("Invalid Input")
