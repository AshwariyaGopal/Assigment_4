import random
N_Num: int = 10
MIN_VALUE: int = 1
MAX_VALUE: int = 100

def main():
     for i in range(N_Num):
          number = random.randint(MIN_VALUE,MAX_VALUE)
          print(f"Random number {i+1}: {number}")

if __name__ == "__main__":
     main()