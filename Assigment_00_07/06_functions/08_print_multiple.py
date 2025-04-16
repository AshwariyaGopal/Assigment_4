 # ANSI escape codes for blue text
blue_text = "\033[94m"
reset_text = "\033[0m"


def print_multiple(message,repeats):
    for i in range(repeats):
        print(message)

def main():
    message = input("Please type a message: ")
    print(f"{blue_text}{message}{reset_text}")
    repeat = int(input("Enter a number of times to repeat your message: "))
    print(f"{blue_text}{repeat}{reset_text}")

    print_multiple(message,repeat)

if __name__ == "__main__":
    main()


