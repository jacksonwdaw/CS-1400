''' Loops.py
    Jacskon Daw
    Demonstrate Loops
    
    Notes:
    A control vairable is an important part of a while loop it needs 3 things:
    1. it needs to intialize the loop
    2. it needs to test it
    3. it needs to be modified to complete the loop

# counting loop
def play_game():
    print("You win!")
    
def main():
    play_again = "y"
    while play_again == "y":
        play_game()
        play_again = input("do you want to play again? ")
        
if __name__ == "__main__":
    main()
    
'''
# sentinel loop
def play_game():
    print("You win!")
    
def input_num():
    num = int(input("Enter a number, 0 to quit: "))
    return num
    
def main():
    total = 0
    number = input_num()
    while number != 0:
        total += number
        num = input_num()
    print(f"The total is: {total}")
        
        
if __name__ == "__main__":
    main()
    

    
    