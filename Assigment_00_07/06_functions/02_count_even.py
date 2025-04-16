def get_integers_from_users():
    numbers = []
    while True:
        user_input = input("Enter an integer or press enter to stop: ")
        if user_input == "":
            break
        
        number = int(user_input)  # assuming valid integer
        numbers.append(number)
    return numbers 
def count_even(lst):
    event_count = 0
    for num in lst:
        if num % 2 == 0:
            event_count += 1
    return event_count

def main():
    nums = get_integers_from_users()
    result = count_even(nums)
    print("Number of even numbers:", result)

if __name__ == "__main__":
    main()



