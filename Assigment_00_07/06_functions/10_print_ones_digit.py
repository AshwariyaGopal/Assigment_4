def print_ones_digit(num):
    ones = num % 10
    print(f"The ones digit is {ones}")

def main():
    num = int(input("Enter a number "))
    print_ones_digit(num)

if __name__ == "__main__":
    main()