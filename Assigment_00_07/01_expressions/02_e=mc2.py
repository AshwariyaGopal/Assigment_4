LIGHT_VALUE: int = 299792458  

def main():
    mass_input = input(f"\033[1;3m Enter Kilos of mass:\033[0m")
    mass = float(mass_input)
    
    energy = mass * (LIGHT_VALUE ** 2)
    
    print("\ne = m * C^2...")
    print(f"m = {mass} kg")
    print(f"C = {LIGHT_VALUE} m/s")
    print(f"{energy} joules of energy!")

if __name__ == "__main__":
    main()