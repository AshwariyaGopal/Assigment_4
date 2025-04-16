# Milestone #1: Generate the random numbers
import random

NUM_ROUNDS = 5

def main():
    print("Welcome to the High-Low Game!")
    print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _")

   
    # Show both numbers for testing
    # print(f"The computer's number is {computer_number}")
    # print(f"Your number is {user_number}")
    score = 0

    for round_num in range(1,NUM_ROUNDS + 1):
        print(f"Round {round_num}")
        # Generate random numbers
        computer_number = random.randint(1,100)
        user_number = random.randint(1,100)

        print(f"Your number is {user_number}")  # Show user's number only

    
     
    
    # Milestone #2
        guess = input("Do you think you number is higher or lower than the computer's?: ").lower()

        while guess != "higher" and guess != "lower":
           guess = input("Please enter either 'higher' or 'lower': ").lower()

    # Milestone #3
        if user_number > computer_number and guess == "higher":
           print(f"You were right! The computer's number was {computer_number}")
           score += 1
        elif user_number < computer_number and guess == "lower":
           print(f"You were right! The computer's number was {computer_number}")
           score += 1
        else:
          print(f"Aww, that's incorrect. The computer number was {computer_number}")

          print(f"Your score is now {score}")
          print()
          # Extension 2: Conditional ending messages based on performance
    print("Your final score is", score)

    print("Thanks for playing")
    if score == NUM_ROUNDS:
        print("Wow!, You played perfectly!")
    elif score >= NUM_ROUNDS // 2:
        print("Good job! You played really well")
    else:
        print("Best of luck for next time!")



if __name__ == "__main__":
    main()