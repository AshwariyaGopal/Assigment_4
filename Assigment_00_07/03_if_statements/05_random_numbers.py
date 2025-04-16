import random

RANDOM_NUMBERS = 10
MIN_NUMBERS = 1
MAX_NUMBERS = 100

def main():


    # Generate random numbers
    for i in range(RANDOM_NUMBERS):
        number = random.randint(MIN_NUMBERS, MAX_NUMBERS)
        print(f"Random number {i+1}: {number}")

if __name__ == "__main__":
    main()