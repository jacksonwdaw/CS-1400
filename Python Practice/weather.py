""" weather.py
    Jackson Daw
    demonstrate if statements
everything indented after the if statement is controlled by it.
the 'else' condition cannot exist by itself, it has to be with another statement
'elif' stands for 'else if', and shares similarity to else since it can't be by itself.
'elif' makes its statement the opposite of the previous statement.
'and' requires that all statements must be true.
'or' requires that at least one be true.
"""
def main():
    temp = int(input("What is the temperature? "))
    snow = input("Is it snowing? ")
    rain = input("Is it raining? ")
    if temp < 32 and (snow == "yes" or rain == "yes"):
        print("Better wear a coat.")
    elif temp < 45:
        print("Wear a sweater")
    elif temp < 85:
        print("You can wear shorts.")
    else:
        print("Better wear sunscreen")
        
if __name__ == "__main__":
    main()