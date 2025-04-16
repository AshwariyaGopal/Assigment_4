MERCURY_GRAVITY = 0.376 
VENUS_GRAVITY = 0.889 
MARS_GRAVITY = 0.378 
JUPITER_GRAVITY = 2.36 
SATURN_GRAVITY = 1.081 
URANUS_GRAVITY = 0.815 
NEPTUNE_GRAVITY = 1.14 
EARTH_GRAVITY = 1.0

def main():
    earth_weight = float(input("Enter a weight on Earth: "))
    planet = input("Enter a Planet: ").capitalize()

    if planet == "Mercury":
        factor = MERCURY_GRAVITY
    elif planet == "Venus":
        factor = VENUS_GRAVITY
    elif planet == "Mars":
        factor = MARS_GRAVITY
    elif planet == "Jupiter":
        factor = JUPITER_GRAVITY
    elif planet == "Saturn":
        factor = SATURN_GRAVITY
    elif planet == "Uranus":
        factor = URANUS_GRAVITY
    else:
       factor = NEPTUNE_GRAVITY
    
    # planet_weight = earth_weight * MARS_MULTIPLE
    planet_weight = earth_weight * factor
    round_planetary_Weight = round(planet_weight, 2)

    print(f"The equivalent weight on {planet}: {planet_weight} " )

if __name__ == "__main__":
    main()

