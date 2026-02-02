def add(num1,num2):
    return num1 + num2



while True:
    num1 = int(input("Enter first number: "))
    operation = input("Enter operator: ")
    num2 = int(input("Enter the second number: "))

    match operation:
        case "+":
            sum = num1 + num2
            print(f"{num1} + {num2} = {sum}")
