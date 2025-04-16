# ADULT_AGE: int = 18


# def is_adult_age(age:int):
#     if age >= ADULT_AGE:
#         return True
    
#     return False

# def main():
#     age = int(input("How old is this person?: "))
    

#     if is_adult_age(age):
#         print("(Entered age is an adult age)")

#     else:
#         print("(Entered age is not an adult age)")
#     print(is_adult_age(age))

# if __name__ == "__main__":
#     main()


ADULT_AGE: int = 18

bold_italics = "\033[1m\033[3m"  # Bold + Italics
reset = "\033[0m"  # Reset to default style

def is_adult_age(age: int):
    if age >= ADULT_AGE:
        return True
    return False

def main():
    # Ask for age input on the same line
    print("How old is this person?: ", end="")  # Keeps input on the same line
    age_input = input()  # Raw input as string
    print(f"{bold_italics}{age_input}{reset}")  # Print input in bold italics
    
    age = int(age_input)  # Convert to int after showing it

    if is_adult_age(age):
        print("(Entered age is an adult age)")
    else:
        print("(Entered age is not an adult age)")
    
    print(is_adult_age(age))

if __name__ == "__main__":
    main()
