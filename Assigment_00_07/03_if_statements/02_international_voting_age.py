Peturksbouipo_AGE = 16
Stanlau_AGE = 25
Mayengua_AGE = 48

def main():
    user_age = int(input("How old ae you? "))

    if user_age >= Peturksbouipo_AGE:
        print("You can vote in Peturksbouipo where the voting age is:", Peturksbouipo_AGE )
    else:
        print("You cannot vote in Peturksbouipo where the voting age is:", Peturksbouipo_AGE)

    if user_age >= Stanlau_AGE:
        print("You can vote in Stanlau where the voting age is:", Stanlau_AGE)
    else:
        print("You cannot vote in Stanlau where the voting age is:", Stanlau_AGE)

    if user_age >= Mayengua_AGE:
        print("You can vote in Mayengua where the voting age is:", Mayengua_AGE)
    else:
        print("You cannot vote in Mayengua where the voting age is:", Mayengua_AGE)

if __name__ == "__main__":
    main()