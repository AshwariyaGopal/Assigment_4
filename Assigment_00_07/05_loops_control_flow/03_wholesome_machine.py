def main():

    correct_affirmation = "I am capable of doing anything I put my mind to."

    print("Please type the following affirmation:", correct_affirmation)

    user_input = input()

    while user_input !=  correct_affirmation:
        print("Hmm That was not the affirmation.")
        print("Please type the following affirmation:", correct_affirmation)

        user_input = input()

    print("That's right! :)")

if __name__ == "__main__":
    main()