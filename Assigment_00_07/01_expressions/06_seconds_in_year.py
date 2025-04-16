DAYS_IN_YEAR = 365
HOURS_IN_DAYS = 24
MIN_PER_HOUR = 60
SEC_PER_MIN = 60

def main():
    total_Second = DAYS_IN_YEAR * HOURS_IN_DAYS * MIN_PER_HOUR * SEC_PER_MIN

    print(f"There are {total_Second} seconds in a year")

if __name__ == "__main__":
    main()