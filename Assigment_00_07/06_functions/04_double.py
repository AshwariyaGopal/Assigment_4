def double_num(num:int):
    return num * 2

def main():
    user_input = int(input("Enter a number: "))
    result = double_num(user_input)
   
    

      # Applying bold and italics to user input
    
    print(f"Double that is: \033[1m\033[3m{result}\033[0m")
if __name__ == "__main__":
    main()