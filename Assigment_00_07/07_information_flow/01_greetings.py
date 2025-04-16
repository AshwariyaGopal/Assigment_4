bold_italics = "\033[1m\033[3m"  # Bold + Italics
reset = "\033[0m"  # Reset to default style

def main():
    name: str = input(f"{bold_italics}What's your name? {reset}")
    print(greet(name))

def greet(name):
    return f"{bold_italics}Greeting {name}!{reset}"

if __name__ == "__main__":
    main()