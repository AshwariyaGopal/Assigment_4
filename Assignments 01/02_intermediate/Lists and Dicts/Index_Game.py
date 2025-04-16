def access_element(lst,index):
    if 0 <= index < len(lst):
        return lst[index]
    else:
        return "Index out of range!"
    
def modify_element(lst,index,new_value):
    if 0 <= index < len(lst):
        lst[index] = new_value
        return "Element modified successfully."
    else:
        return "Index out of range!"
    
def slice_list(lst, start, end):
    if start < 0 or end > len(lst):
        return "Start on end index is out of range!"
    return lst[start:end]

def main():
    my_list = ['apple','banana','cherry','grape','mango']

    while True:
        print("\n--- List Index Game ---")
        print("Current list:", my_list)
        print("Choose an operation:")
        print("1. Access an element")
        print("2. Modify an element")
        print("3. Slice the list")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            index = int(input("Enter the index to access: "))
            result = access_element(my_list, index)
            print("Result:", result)

        elif choice == '2':
            index = int(input("Enter the index to modify: "))
            new_value = input("Enter the new value: ")
            message = modify_element(my_list, index, new_value)
            print(message)

        elif choice == '3':
            start = int(input("Enter start index: "))
            end = int(input("Enter end index: "))
            result = slice_list(my_list, start, end)
            print("Sliced list:", result)

        elif choice == '4':
            print("Goodbye!")
            break

        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()

