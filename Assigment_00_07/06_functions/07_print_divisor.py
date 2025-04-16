def print_divisors(num):
     # ANSI escape codes for blue text
    blue_text = "\033[94m"
    reset_text = "\033[0m"
    print(f"Here are the divisors of {blue_text}{num}{reset_text}")
    for i in range(num):
        curr_divisor = i + 1
        if num % curr_divisor == 0:
            print(curr_divisor)

def main():
    num = int(input("Enter a number: "))
     
    print_divisors(num)

if __name__ == "__main__":
    main()

