def main():
    import sys
    x = int(sys.argv [1])
    test = input("Type an int: ")
    print(test)

    if x > 0 and x < 25 or x > 75 and x < 100:
        print(str(x) + "_ is between 0 and 25 or 75 and 100 ")
    else:
        print("oops")
    main()