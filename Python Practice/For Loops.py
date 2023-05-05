'''
For Loops.py
Jackson Daw

Notes:
Sequence is a controlled loop, it needs key words followed by a sequence
for num in 1,2,3,4,5,6:
    print(num)
    
range is a function, it creates a sequence
for num in range(100):
    print(num)

'''
# a function, which is a lump of code, can be referenced by calling main elsewhere
def main():
# prints the range in columns, known as a nested loop
    for dot in range 
    for num in range(10, 100, 5):
        for num1 in range(num, num+5):
            print(num, end="\t")
    else:
        print()
# counts down from 100 to 0 by increments of 5
    for num in range(100, 0, -5):
        print(num)
    else:
        print()
# prints the numbers in the loop   
    for num in 1, 5, 3, 57, 42:
        print(num)
    else:
        print()
# prints numbers in range excluding 100
    for num in range(100):
        print(num)
    else:
        print()
# # prints numbers in the range of 1-10
    for num in range(1,10):
        print(num)
    else:
        print()
# # prints numbers from 10 to 0 in increments of 2
    for num in range(10,0,-2):
        print(num)
    else:
        print()
        
if __name__ == "__main__":
    main()