def in_range(n,low,high):
    if n >= low and n <= high:
        return True
    return False

def main():
    n = int(input("Enter a number (n): "))
    low = int(input("Enter the lower bound (low): "))
    high = int(input("Enter the upper bound (high): "))

    # Check if the number is in range and print result
    if in_range(n, low, high):
        print(f"{n} is in the range [{low}, {high}]")
    else:
        print(f"{n} is NOT in the range [{low}, {high}]")

# Call main if this script is being run
if __name__ == "__main__":
    main()