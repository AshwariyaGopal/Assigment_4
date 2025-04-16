def main():
    numbers: list[int] = [1,2,3,4]

    # Method 1: Using a for loop
    doubled_numbers = []
    for num in numbers:
        doubled_numbers.append(num * 2)
    print(f"Original list: {numbers}")
    print(f"Doubled list: {doubled_numbers}")

# Method 2: Using list comprehension (more Pythonic way)
    doubled_numbers_2 = [num * 2 for num in numbers]
    print(f"Original list: {numbers}")
    print(f"Doubled list:, {doubled_numbers_2}" )

# Method 3: Using map function
    doubled_numbers_3 = list(map(lambda x: x * 2, numbers))
    print(f"Original list: {numbers}")
    print(f"Doubled list: {doubled_numbers_3}")

   


if __name__ == "__main__":
    main()
   