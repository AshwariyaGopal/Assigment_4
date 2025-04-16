def main():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    quotient = num1 // num2
    remainder = num1 % num2
    
    # print(f"When {num1} is divided by {num2}:")
    # print(f"Quotient = {quotient}")
    # print(f"Remainder = {remainder}")
    print("The result of this division is " + str(quotient) + " with a remainder of " + str(remainder))

if __name__ == "__main__":
    main()
