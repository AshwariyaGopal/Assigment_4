def main():
    year = int(input("Please input a year: "))

    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("Thats's a leap year!")
            else:
                print("That's not a leap year!")
        else:
            print("That's a leap year!")
    else:
        print("That's not a leap year!")

if __name__ == "__main__":
    main()

# So we have multiple print statements because:
# One for years not divisible by 4
# One for years divisible by 4 but not by 100
# One for years divisible by 4, 100, and 400
# One for years divisible by 4 and 100 but not by 400
# This follows the Gregorian calendar rules for leap years:
# Must be divisible by 4
# If divisible by 100, must also be divisible by 400
# Otherwise, it's not a leap year