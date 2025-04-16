def main():
    fruit: str = input("Enter a fruit: ")
    stock = num_in_stock(fruit)
    if stock == 0:
        print("This fruit is not in stock.")
    else:
        print("This fruit is in stock! Here's how many: ")
        print(stock)

def num_in_stock(fruit):
    if fruit == 'apple':
        return 2
    elif fruit == 'durian':
        return 4
    elif fruit == 'pear':
        return 1000
    elif fruit == "banana":
        return 300
    elif fruit == "mango":
        return 40
    elif fruit == "orange":
        return 30
    elif fruit == "grapes":
        return 80
    else:
        return 0
    
if __name__ == "__main__":
    main()
