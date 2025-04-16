def get_numbers():

    users_numbers = []
    # print("Enter numbers (press enter twice to stop):")
    while True:
        number = input("Enter a number : ")
        if number == "":
            break
        users_numbers.append(int(number))
    return users_numbers

def count_numbers(numbers):
    counts = {}

    for number in numbers:
        counts[number] = counts.get(number, 0) + 1
    return counts

def show_result(counts):
    for number in sorted(counts):
        print(f"{number} appears {counts[number]} times.")

def main():
    numbers = get_numbers()
    counts = count_numbers(numbers)
    show_result(counts)


if __name__ == "__main__":
    main()