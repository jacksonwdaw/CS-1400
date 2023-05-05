def main():
    name = input("What is your name? ")
    print("Hello,", name)
    while True:
        try:
            age = int(input("How old are you? "))
        except:
            print("Error: please type an integer,")
            continue
        else:
            break
    print("You will be", age+1, "on your next birthday")
    money = float(input("How much money do you have? "))
    print(f"Please loan me {money/2:,.2f}.")
    
    
    
if __name__ == "__main__":
    main()