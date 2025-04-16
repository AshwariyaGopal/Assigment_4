def get_user_data():
    first_name: str = input("Enter your first name?: ")
    last_name: str = input("Enter your last name?: ")
    email_address: str = input("What is your email address?: ")

    return first_name , last_name , email_address

def main():
    user_data = get_user_data()
    print("Received the following user data:", user_data)

if __name__ == "__main__":
    main() 