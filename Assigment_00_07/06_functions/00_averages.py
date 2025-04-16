def average(a: float, b: float):
    sum = a + b
    return sum / 2

def main():
    print("🔢 First set of numbers:")
    num1 = float(input("Enter your first number: "))
    num2 = float(input("Enter your second number: "))

    average_1 = average(num1, num2)

    print("\n🔢 Second set of numbers:")
    num_3 = float(input("Enter you third number: "))
    num_4 = float(input("Enter your fourth number: "))
    average_2 = average(num_3,num_4)
    
    final = average(average_1, average_2)
    print("\n✅ Results:")
    # in simple
    # print("Average 1: ", average_1)
    # print("Average_2: ", average_2)
    # print("Final Average of Both: ", final)
    # with some more improved
    print(f"📍 Average of {num1} and {num2} = {average_1}")
    print(f"📍 Average of {num_3} and {num_4} = {average_2}")
    print(f"🎯 Final average of both = {final}")

if __name__ == "__main__":
    main()