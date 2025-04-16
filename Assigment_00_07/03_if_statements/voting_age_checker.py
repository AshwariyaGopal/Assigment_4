def main():
    # Get user's age
    age = int(input("How old are you? "))
    
    # Voting ages for different countries
    PETURKSBOUIPO_AGE = 16
    STANLAU_AGE = 25
    MAYENGUA_AGE = 48
    
    # Check eligibility for Peturksbouipo
    if age >= PETURKSBOUIPO_AGE:
        print(f"You can vote in Peturksbouipo where the voting age is {PETURKSBOUIPO_AGE}.")
    else:
        print(f"You cannot vote in Peturksbouipo where the voting age is {PETURKSBOUIPO_AGE}.")
    
    # Check eligibility for Stanlau
    if age >= STANLAU_AGE:
        print(f"You can vote in Stanlau where the voting age is {STANLAU_AGE}.")
    else:
        print(f"You cannot vote in Stanlau where the voting age is {STANLAU_AGE}.")
    
    # Check eligibility for Mayengua
    if age >= MAYENGUA_AGE:
        print(f"You can vote in Mayengua where the voting age is {MAYENGUA_AGE}.")
    else:
        print(f"You cannot vote in Mayengua where the voting age is {MAYENGUA_AGE}.")

if __name__ == "__main__":
    main() 