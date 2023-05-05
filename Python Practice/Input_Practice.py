''' input.py
    Jackson Daw
    demonstrate input()'''
# reee
def main():
    name = input("What is your name? ")
    print("Hello,", name)
    try:
        age = int(input("How old are you? "))
    except:
        print("Error: please type an integer,")
        exit()
    print("You will be", age+1, "on your next birthday")
    money = float(input("How much money do you have? "))
    print(f"Please loan me {money/2:,.2f}.")
    
    
    
if __name__ == "__main__":
        main()